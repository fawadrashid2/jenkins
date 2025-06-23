pipeline {
    agent any

    environment {
        IMAGE_NAME = 'hello85'
        CONTAINER_NAME = 'hello85-container'
        PORT = '85'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/umarmir/jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove any previous container
                    sh "docker rm -f ${CONTAINER_NAME} || true"

                    // Run new container on specified port
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:${PORT} ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "App is live on port ${PORT}"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
