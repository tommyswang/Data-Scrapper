# Application Manual - Data Scraper

**Team Name**: HZ-TASK Force 

**Team Members**: Allen Leigh, Hongyu Cheng, Kanishkah Anwari, SeGe Jung, Tommy Wang, Zahiduzzaman Biswas 

**Project Name**: Data Scraper 

**GitHub Link**: https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper 



# Data-Scrapper

(Connect to GaTech VPN before connecting to the sites below)

* Live site: https://apps.hdap.gatech.edu/data-scrapper-app/
* CI: https://drone.hdap.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper/ (Need to be on Ga Tech Network)
* Rancher: https://rancher.hdap.gatech.edu/ (Need to be on Ga Tech Network)


## Add names here (Alphabetically):

* Allen Leigh
* Hongyu Cheng
* Kanishkah Anwari
* SeGe Jung
* Tommy Wang
* Zahiduzzaman Biswas

## Local development

**Pre-requisites**

* Python3, pip3
* Docker
* MySQL server

**NOTE: after pull from master branch, always install packages from `app/requirements.txt`**

We use Makefile to make development and testing more convenient.

**NOTE: `make` command should be executed inside `app/` ONLY :**

* `make setup`: create local database etc,.
* `make update`: update database schema and Python packages.
* `make server`: start app server on local.
* `make test`: run test suite.
* `make clear`: clear all data

### First time Setup

Run command `make setup && make update`.

This does:

* Create local database
* Install Python packages

If you need to change database configuration, please update the `app/makefile` locally.

### Run server without Docker

NOTE: after pulling the latest master branch, run `make update`.

Run command `make server`.

To switch environment, execute `ENV=<env name> python3 app/main.py`. Available environments are:

* `dev_local` (default)
* `dev_remote`
* `production`


### Run server With docker (TODO)

(As we are using a separate container for MySQL, this method for development is not support)

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

## Deployment to HDAP

Any update to the `deploy` branch will automatically trigger a deployment to HDAP.
