# Set up Hasura-Graphql Engine

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

## How to run

Following env variables needs to be set accordingly in the `docker-compose.yml`,

```
# primary database that you want to connect
HASURA_GRAPHQL_DATABASE_URL

# database for storing the hasura metadata (can be same as primary db)
HASURA_GRAPHQL_METADATA_DATABASE_URL
```

Execute the below command from the workspace directory,

```
docker compose up
```

If the build is successful, hasura service runs at http://localhost:8888/

Once the hasura is up & running, you can connect to additional databases.
Click on `data` tab -> `Manage` database -> `Connect Database`. Enter the database uri string or env variable to connect.

Note: To skip the manual steps of connecting to additional db's (like application_store & account_store), there is a pre-built metadata json in the dir `metadata` that you can directly import from the settings.
![Alt text](metadata\metadata_import.PNG?raw=true "Title")

## Running Graphql queries in Python

### Install dependencies in your virtual env

```
python -m pip install --upgrade -r requirements.txt
```

### Run the example

```
python example\graphql_demo.py
```
