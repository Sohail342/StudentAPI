
# Django StudentAPI (DRF) with Docker

This is a simple Django REST Framework (DRF) API for managing student data. The project is containerized using Docker to provide a consistent development environment.

## Prerequisites
Make sure you have the following installed:

- Docker (including Docker Compose)
- Docker Hub account (optional, for pushing images)

## Installation
## Step 1:
Clone the repository:

```bash
  git clone https://github.com/Sohail342/StudentAPI.git

  cd studentAPI
```


## Running the Project:
You can run the project using Docker Compose, which will set up the necessary containers for both the Django application and the required dependencies.


## Step 1:
Build and start the Docker containers:

```bash
docker-compose up --build

```

## Step 2:
Open your browser and visit http://localhost:8000 to access the API.

## Step 3:
To stop the project, run:

```bash
  docker-compose down

```
## Other Commands:
Run Django migrations:

```bash
  docker-compose run web python manage.py migrate

```
Create a Django superuser:

```bash
  docker-compose run web python manage.py createsuperuser


```


## Contact
If you have any questions or feedback, feel free to reach out:
<p align="left">
<a href="https://wa.me/+923431285354" target="blank"><img align="center" src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/sohail_ahmad342" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="sohail_ahmad342" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/sohailahmad3428041928/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sohail-ahmad342" height="30" width="40" /></a>
<a href="https://instagram.com/sohail_ahmed113" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sohail_ahmed113" height="30" width="40" /></a>
<a href="mailto:sohailahmed34280@gmail.com" target="blank"><img align="center" src="https://img.icons8.com/ios-filled/50/000000/email-open.png" alt="Email" height="30" width="40" /></a>
</p>


