pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-devops-app"
        CONTAINER_NAME = "flask-app"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Rithish24-cloud/end-to-end.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
            }
        }

        stage('Verify Running Container') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully. Application deployed.'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}