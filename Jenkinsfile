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
                   dockerImage = docker.build("${env.ARTIFACT_ID}", "-f compose/development/django/Dockerfile .")
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
