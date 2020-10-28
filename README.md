# Data-Scrapper

## Add names here (Alphabetically):

* Allen Leigh
* Hongyu Cheng
* Kanishkah Anwari
* SeGe Jung
* Tommy Wang
* Zahiduzzaman Biswas

## Deployment

### Testing locally

To test locally, please have Python3 and Docker installed.

Code below was tested on MacOS.

Start the web application without Docker:

```shell
pip install -r app/requirements.txt

python3 app/main.py
```

Start the web application with Docker:

```shell
# Clone repository
git clone https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper

# Move to Data-Scrapper directory
cd Data-Scrapper

# Build docker image
docker build --tag datascrapper:1.0 .

# Run image as container
docker run --publish 5000:5000 --detach --name ds  datascrapper:1.0

# Visit homepage
curl localhost:5000

# Stop and remove Docker container
docker stop ds
docker rm ds
```
