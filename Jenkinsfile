pipeline {
    agent any
    environment {
        EXAMPLE = 'test'
    }

    stages {
        stage('Build new image') {
            steps {
                echo "Building new docker image..."
                sh 'docker build -t fastapi_template .'
            }
        }
        stage('Stop old container') {
            steps {
                echo "Stopping old container..."
                sh 'docker stop fastapi_template || true'
            }
        }
        stage('Remove old container') {
            steps {
                echo "Removing old docker container..."
                sh 'docker rm fastapi_template || true'
            }
        }
        stage('Run new container') {
            steps {
                echo "Running new docker container..."
                sh 'docker run  --name=fastapi_template --workdir=/app -p 5000:5000 -d fastapi_template:latest '
            }
        }
    }
}