# Project Setup

## Steps to Get the Project Up and Running

1) **Clone the repository**  
    - Clone the repo with `git clone`
    - Change into the directory with `cd`

2) **Build the project** with `docker-compose up --build -d`
    - This will start two services: 
        - `db`: PostgreSQL database with persistent volume
        - `web`: Django API exposed on `localhost:8080`
3) **Apply migrations** with `docker-compose exec web python manage.py migrate`

## Browsable API
- After running the project,  visit `http://localhost:8000/api/` to enter DRF's browsable API

## Example USE

### Create a device / server:
curl -X POST http://localhost:8000/api/devices/ \
     -H "Content-Type: application/json" \
     -d '{"name":"MyFirstDevice"}' 

curl -X POST http://localhost:8000/api/servers/ \
     -H "Content-Type: application/json" \
     -d '{"name":"MyFirstServer"}'

### List servers
curl -X GET http://localhost:8000/api/servers/

### List a specific server
curl -X GET http://localhost:8000/api/servers/<id>/

### List devices
curl -X GET http://localhost:8000/api/devices/

### Update Server status
To start a server:
curl -X PATCH http://localhost:8000/api/servers/<id>/ \
     -H "Content-Type: application/json" \
     -d '{"status":"starting"}'
The command above will return "status":"running" if an online device was found,
else will return "status":"error"

To stop a server:
curl -X PATCH http://localhost:8000/api/servers/<id>/ \
     -H "Content-Type: application/json" \
     -d '{"status":"stopped"}'


## Design choices
- A package named "api" was created, separate from the overall "server_manager" package.

- For ease of access and future-proofing, urls, serializers, and views are separated for Device and Server objects
    - Models are both stored in the same file as they are not very extensive, but in the future, they can be easily
        split into their own, separate model file
- For both Device and Server, I decided to utilize two separate views: one for creating and viewing objects (which inherits from `generics.ListCreateAPIView`), and one for PATCH calls (which inherits from `generics.RetrieveUpdateAPIView`)

- Since this code will not be deployed to prod, we can leave the `SECRET_KEY` and `DEBUG=TRUE` as they are in `settings.py`. In a prod situation,
`DEBUG` would be set to `FALSE`, and the `SECRET_KEY` would be added to something like a `.env` file which would not be publicly available.