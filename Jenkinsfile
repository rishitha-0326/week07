
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f registration-app || exit 0'
                bat 'docker run -d -p 5000:5000 --name registration-app registration-app'
            }
        }
    }
}
