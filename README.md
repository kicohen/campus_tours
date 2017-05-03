# CMU Self-Guided Tours
## Office of Undergraduate Admissions
### 67-340 Mobile Web Design and Development
#### Bernard, AJ, Ritika, Kenny

# Overview
This project is a mobile web app that is meant to provide perspective families with a way to view the CMU campus when the Office of Admissions is not offering tours.

### Server: https://35.166.188.191/
Deployed on Amazon EC2

### Versions:
* Python = 3.5.1
* Django = 1.10.4
* Database = sqlite3

### Client Side Libraries:
* Bootstrap 3
* Google Maps API
* JQuery

### Server and Deployment Info
Deployed an Ubuntu instance of Amazon EC2 running Apache 2.4.18. To properly function the server must have an SSL Certificate. Geolocation on modern browsers requires SSL connections. Currently because of the small size of the database, sqlite3 is a sufficient database, however, if you wish to scale the system you might want to switch to a larger database paradigm such as Postgres or mySQL. It is also recommended that you deploy within a python virtual environment. The only additional library to django that you need to install is django-bootstrap-forms.

### Sources:
* https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html
* https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/modwsgi/
* https://docs.djangoproject.com/en/1.10/ref/contrib/auth/
* https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
* https://docs.djangoproject.com/en/1.10/ref/models/fields/#integerfield
* https://tutorial.djangogirls.org/en/
