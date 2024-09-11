pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                containers:
                - name: docker
                  image: docker:latest
                  command:
                  - cat
                  tty: true
                  volumeMounts:
                  - mountPath: /var/run/docker.sock
                name: docker-sock
                volumes:
                - name: docker-sock
                    hostPath:
                    path: /var/run/docker.sock    
                '''
        }
    }


    options {
        timeout(time: 4, unit: 'MINUTES')
    }

    environment {
        ARTIFACT_ID = "luisito666/m2-api-rest:${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                container('docker') {
                    script {
                    dockerImage = docker.build("${env.ARTIFACT_ID}", "-f compose/production/django/Dockerfile .") 
                    }
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
                branch 'master'
            }
            steps {
                container('docker') {
                    script {
                        docker.withRegistry("", "DockerHubCredentials") {
                            dockerImage.push()
                        }
                    }
                }
            }
        }

        stage('Publish develop') {
            when {
                branch 'develop'
            }
            steps {
                container('docker') {
                    script {
                        docker.withRegistry("", "DockerHubCredentials") {
                            dockerImage.push()
                        }
                    }
                }
            }
        }
    }
}
