pipeline {
    agent any


    options {
        timeout(time: 2, unit: 'MINUTES')
    }

    environment {
        ARTIFACT_ID = "luisito666/m2-api-rest:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                script {
                   dockerImage = docker.build("default", "-f compose/development/django/Dockerfile .") "${env.ARTIFACT_ID}"
                }
            }
        }

        stage('Publish') {
            when {
                branch 'master'
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
