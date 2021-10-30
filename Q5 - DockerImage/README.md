# Usage

## Prerequisite

Create an account on Docker Hub. Use the link to create an account: https://hub.docker.com/

## To Create the Docker Image follow the below steps:

### Step 1:
`FROM` - This Keyword specifies the underlying OS architecture that you gonna use to build the image.

### Step 2:
`RUN` - It alllows you to install the required application and packages needed for the Docker Image.

### Step 3:
`COPY` - It helps to copy the specific files and folders in the Docker image.

### Step 4:
`CMD` - The CMD command​ specifies the instruction that is to be executed when a Docker container starts. The main purpose of the CMD command is to launch the software required in a container.

### Step 5:
`EXPOSE`: The EXPOSE instruction exposes a particular port with a specified protocol inside a Docker Container. It does not map ports on the host machine.

### Step 6: 
To build the Docker Image use the following command:

```
docker build -t <docker_id>/<image_name>:<tagname> .
```

### Step 7:
To run the container with this image on the port 8080 use the below command:

```
docker run -dit --name <container_name> -p 8080:80 <image_name>
```

## To Publish Docker Image to  docker repository follow the below steps:

### Step 1:
Use the below command to login to your docker repository via command line

```
docker login
```

Enter your Username and password and you will be logged in.

### Step 2:
Use the command to push you image to your Docker Repository

```
docker push <docker_id>/<image_name>:<tagname>
```
Your image has been pushed to Repository.