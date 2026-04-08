pipeline {
    agent any
    environment {
        DOCKER_CREDS = credentials('dockerhub-creds')
        DOCKER_USER = 'ankit44881'
        CLUSTER_NAME = 'chai-politics-prod'
        REGION = 'us-east-1'
    }
    stages {
        stage('Build & Push') {
            steps {
                sh "docker build -t ${DOCKER_USER}/chai-app:${env.BUILD_ID} ."
                sh "echo ${DOCKER_CREDS_PSW} | docker login -u ${DOCKER_CREDS_USR} --password-stdin"
                sh "docker push ${DOCKER_USER}/chai-app:${env.BUILD_ID}"
            }
        }
        stage('Deploy to EKS') {
            steps {
                // Point Jenkins to the right cluster
                sh "aws eks update-kubeconfig --region ${REGION} --name ${CLUSTER_NAME}"
                
                // Deploy the LoadBalancer and Deployment
                sh "kubectl apply -f k8s.yaml"
                
                // Update the image to the one we JUST pushed (e.g., build #5)
                sh "kubectl set image deployment/chai-web nginx-container=${DOCKER_USER}/chai-app:${env.BUILD_ID}"
            }
        }
    }
}