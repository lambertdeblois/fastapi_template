pipeline {
    agent any
    environment {
        EXAMPLE = 'test'
    }

    stages {
        stage('Build image') {
            steps {
                echo "Building docker image..."
                sh 'docker build -t fastapi_template .'
            }
        }
        stage('Run image') {
            steps {
                echo "Running docker container..."
                sh 'docker run  --workdir=/app -p 5000:5000 -d fastapi-template:latest'
            }
        }
    }
}