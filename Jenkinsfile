pipeline {
    agent any

    stages {
        stage("build") {
            steps {
                sh 'echo building test image...'
                sh 'docker build -t jenkins-tests .'
            }
        }

        stage("test") {
            steps {
                sh 'echo running tests in docker'
                sh 'docker run jenkins-tests'
            }
        }

    }

    post {
        always {
            sh """
            echo post-always stage
            docker build -t send-script -f send.Dockerfile .
            docker run send-script --jenkins-url=${env.JENKINS_URL} --job-name=${env.JOB_NAME} --build-number=${env.BUILD_NUMBER}
            """
        }
    }
}
