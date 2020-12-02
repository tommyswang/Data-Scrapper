# Special Instructions

**Team Name**: HZ-TASK Force 

**Team Members**: Allen Leigh, Hongyu Cheng, Kanishkah Anwari, SeGe Jung, Tommy Wang, Zahiduzzaman Biswas 

**Project Name**: Data Scraper 

**GitHub Link**: https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper 

Below is a complete instruction for setting up the application on local. The instruction is tested on Ubuntu.

Before running, please ensure some dependencies are installed:

* Python 3 with `pip3`
* Java 11 or above
* MySql server

On Debian based Linux system, you should be able to install them using:

```
sudo apt-get update && apt-get install -y software-properties-common && \
sudo add-apt-repository ppa:deadsnakes/ppa && \
sudo apt-get update && \
sudo apt-get install -y python3.8 python3-pip default-jre mysql-server && \
sudo service mysql start
```

After pulling the git repo, please navigate to the directory of the repo in terminal, and run the commands below..

```
cd app

# setup database 
make setup 

# install dependencies
make update

# run server on local in development mode
make server
```

You should be able to see the web server running.

### Troubleshooting on HDAP live site

If you encounter this error:

```
Bad gateway
Apache/2.4.18 (Ubuntu) Server at apps.hdap.gatech.edu Port 443
```

We suspect it is related to the configuration of HDAP Kubernetes node. Please compressor your uploading file and try again, typically less than 1MB.
