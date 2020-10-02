# Data-Scrapper

## Add names here:
SeGe Jung


## Deployment

### Testing locally

To test locally, please have Python3 and Docker installed.

Code below was tested on MacOS.

Start the web application without Docker:

```shell
python3 app/main.py
```

Start the web application with Docker:

```shell
# Start docker container
docker run -d --name data-scrapper -p 5000:5000 allenlsy/ds-data-scrapper

# Visit homepage
curl localhost:5000

# Stop and remove Docker container
docker stop data-scrapper
docker rm data-scrapper
```