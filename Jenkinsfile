pipeline {
    agent {
        kubernetes {
            containerTemplate {
                   name 'docker'
                   image 'docker:latest'
                   ttyEnabled true
                   command 'cat'
            }
        }
    }


    options {
        timeout(time: 10, unit: 'MINUTES')
    }

    environment {
        ARTIFACT_ID = "luisito666/m2-api-rest:${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
        DOCKER_HOST = "172.16.1.25"
    }

    stages {
        stage('Build') {
            steps {
                script {
                   dockerImage = docker.build("${env.ARTIFACT_ID}", "-f compose/production/django/Dockerfile .")
                }
            }
        }

        // stage('Testing') {
        //     steps {
        //         sh "docker run ${dockerImage.id} python manage.py test"
        //     }
        // }

        stage('Publish master') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry("", "DockerHubCredentials") {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Publish develop') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    docker.withRegistry("", "DockerHubCredentials") {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
