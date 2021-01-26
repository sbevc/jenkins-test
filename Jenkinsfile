pipeline {
    agent any

    stages {
        stage("test") {
            steps {
                sh """
                docker build -t jenkins-tests .
                docker run \
                    --rm \
                    -v ~/tests-output:/tests
                    -e DOCKER_TESTS_VOLUME_PATH=/tests
                    jenkins-tests
                """
                sh """ls ~/tests-output"""
            }
        }

    }

    post {
        always {
            sh """
            echo post-always stage
            docker build -t send-script -f send.Dockerfile .
            docker run \
                --rm \
                -v ${DOCKER_TESTS_VOLUME}:${DOCKER_TESTS_VOLUME_PATH} \
                -e JENKINS_URL=http://host.docker.internal:8080 \
                -e JOB_NAME=${env.JOB_NAME} \
                -e BUILD_NUMBER=${env.BUILD_NUMBER} \
                -e DOCKER_TESTS_VOLUME_PATH=${DOCKER_TESTS_VOLUME_PATH} \
                send-script
            docker volume rm ${DOCKER_TESTS_VOLUME}
            """
        }
    }
}
