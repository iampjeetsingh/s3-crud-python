## Functional Requirements

- [x] API should validate a JWT token before allowing access to the caller.

- [x] The JSON files should be stored on an S3 bucket.

API Resources to be exposed -

- [x] Create file - To create a new JSON file on an S3  bucket. UUID should be used to name a new file.

- [x] Get file - To read the contents of an existing JSON file.

- [x] Update file - To update the content of an existing JSON file. 

- [x] Delete File  - To delete a JSON file from the s3 bucket.


## Non Functional requirements:

- [ ] Unit tests using moto or similar library to mock AWS services (`Provided postman collection for testing`)

- [ ] Lint and prettier configurations (`Didn't use`)

- [x] Dockerise the application

- [x] Readme file on how to deploy and run the service. 

- [x] Add a checklist of the above items on ReadMe and check all the items before submitting the assignment.


## How to deploy
- Clone the repo \
```git clone https://github.com/iampjeetsingh/s3-crud-python```

- Go to the directory \
```s3-crud-python```

- Install docker

- Create the Docker image \
```docker build -t myapp .```

- Create an ECR registry\
```aws ecr create-repository --repository-name myapp --region us-east-1```

- Give the Docker CLI permission to access your Amazon account\
```aws configure```\
```aws ecr get-login-password --region us-east-1```\
```aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin [your account number].dkr.ecr.us-east-1.amazonaws.com```\
\
Refer this [blog](https://towardsdatascience.com/deploying-a-docker-container-with-ecs-and-fargate-7b0cbc9cd608) for more info
- Upload your docker image to ECR\
```docker push 828253152264.dkr.ecr.us-east-1.amazonaws.com/myapp```