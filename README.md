# Data-Scrapper

[![Build Status](https://drone.hdap.gatech.edu/api/badges/gt-cs6440-hit-fall2020/Data-Scrapper/status.svg?ref=refs/heads/deploy)](https://drone.hdap.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper)

(Connect to GaTech VPN before connecting to the sites below)

* Live site: https://apps.hdap.gatech.edu/data-scrapper-app/
* CI: https://drone.hdap.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper/
* Rancher: https://rancher.hdap.gatech.edu/


## Add names here (Alphabetically):

* Allen Leigh
* Hongyu Cheng
* Kanishkah Anwari
* SeGe Jung
* Tommy Wang
* Zahiduzzaman Biswas

## Deployment

### Testing locally

**Pre-requisites**

* Python3
* Docker

#### Without docker

```shell
pip install -r app/requirements.txt

python3 app/main.py
```

#### With docker

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

### Deploy to HDAP

Any update to the `deploy` branch will automatically trigger a deployment to HDAP.