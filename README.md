# QPerformance API POC

## Install docker engine

**Cent OS**

1- Install required packages. yum-utils provides the yum-config-manager utility, and device-mapper-persistent-data and lvm2 are required by the devicemapper storage driver.
```
 sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```

2- Use the following command to set up the stable repository.
```
 sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

3- Install the latest version of Docker Engine - Community and containerd:
```
sudo yum install docker-ce docker-ce-cli containerd.io
```

**Ubuntu**

1- Update the apt package index:

```
sudo apt-get update
```

2- Install packages to allow apt to use a repository over HTTPS:
```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

3- Add Docker’s official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

4- Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

**Windows**

Download installer [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).

## Run

```
make deploy
```

## View logs
```
make logs
```

### Notes

To check everything is working correctly check the application logs:

```
make logs
```

The output should be something like this:

```
DATABASE_TYPE: mysql
DATABASE_HOST: betacode.tech
DATABASE_USER: betacode
DATABASE_PASSWD: Pocosi12!
DATABASE_NAME: qperformance
VERSION: 0.0.1
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 228-235-486
```

You can also check if everything is working by accessing the version endpoint ```http://<your-ip-or-host>:<port>/v1/version ```.  
The **localhost** endpoint should be [http://localhost:5000/v1/version](http://localhost:5000/v1/version)
 
### Configuration

In the root of the project there is ```.env``` file. This file can be altered in order to configure the application for a specific environment.
This file should have the following structure:

```
VERSION=0.0.2
PORT=5000
DATABASE_TYPE=mysql
DATABASE_HOST=betacode.tech
DATABASE_USER=betacode
DATABASE_PASSWD=Pocosi12!
DATABASE_NAME=qperformance
```

**VERSION:** Code version, should be incremented after each build.  
**PORT:** Port that the application will use when running, default is 5000  
**DATABASE_TYPE:** Database type. For default we use mysql  
**DATABASE_HOST:** Database ip or domain name.  
**DATABASE_USER:** Database user.  
**DATABASE_PASSWD:** Database password.  
**DATABASE_NAME:** Database schema name.  

### Production

For ubuntu or cent os use apache server to create a reverse proxy to the docker images currently running on your machine.

**Cent OS**

1- Enabling mod proxy. (if its already enabled just skip this step.)

```
sudo vim /etc/httpd/conf/httpd.conf
```

Add the following lines:

```
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
```

**Note:** To verify the current modules installed run ```httpd -M```.

2- Create virtual host

Create conf file:
```
vim your-domain-name.conf
```
Paste the following code:
```
<VirtualHost <your-domain-name>:*>

ProxyPreserveHost On

ProxyPass / http://127.0.0.1:5000/

ProxyPassReverse / http://127.0.0.1:5000/

</VirtualHost>


```

3- Restart apache

```
sudo systemctl restart httpd
```

4- Test

Use the virtual host defined url to access the api like this: ```http://<your-domain-name>/v1/version```



### Development

This project uses [pipenv](https://pipenv.pypa.io/en/latest/).
To run the app install dependencies:

```
pipenv install
```

And then run:

```
pipenv shell
pipenv start
```


### Documentation

API documentation can be checked [here](https://documenter.getpostman.com/view/2102316/SzS1SntA?version=latest).
