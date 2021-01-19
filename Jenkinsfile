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
            echo $JENKINS_URL
            docker run \
                -e JENKINS_URL=${env.JENKINS_URL} \
                -e JOB_NAME=${env.JOB_NAME} \
                -e BUILD_NUMBER=${env.BUILD_NUMBER} \
                send-script
            """
        }
    }
}
