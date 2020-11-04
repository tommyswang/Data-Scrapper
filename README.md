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

## Deployment

### Local development

**Pre-requisites**

* Python3
* Docker
* MySQL server


**NOTE: after pull from master branch, always install packages from `app/requirements.txt`**

### First time running setup

Create the database on local:

```
mysql -u root -e "create database data_scrapper"
```

#### Run server without docker

```shell
# update packages
pip3 install -r app/requirements.txt
mkdir -p app/files

# run server
python3 app/main.py
```

To switch environment, use `ENV=<env name> python3 app/main.py`. Available environments are:

* `dev_local` (default)
* `dev_remote`
* `production`


#### Run server With docker (TODO)

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

### Deploy to HDAP

Any update to the `deploy` branch will automatically trigger a deployment to HDAP.
