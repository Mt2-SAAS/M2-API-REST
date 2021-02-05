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
                   dockerImage = docker.build("${env.ARTIFACT_ID}", "-f compose/production/django/Dockerfile .") 
                }
            }
        }

        stage('Testing') {
            steps {
                sh "docker run ${dockerImage.id} python manage.py test"
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
