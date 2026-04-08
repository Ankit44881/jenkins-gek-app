pipeline {
    agent any
    environment {
        // This ID must match exactly what you see in your screenshot
        DOCKER_CREDS = credentials('dockerhub-creds')
        DOCKER_USER = 'ankit44881'
    }
    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                sh "docker build -t ${DOCKER_USER}/chai-app:${env.BUILD_ID} ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // Jenkins automatically provides _USR and _PSW from the credentials call above
                sh "echo ${DOCKER_CREDS_PSW} | docker login -u ${DOCKER_CREDS_USR} --password-stdin"
                sh "docker push ${DOCKER_USER}/chai-app:${env.BUILD_ID}"
            }
        }
    }
}