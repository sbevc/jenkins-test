pipeline {
    agent any

    environment {
        DOCKER_TESTS_VOLUME = "TestsVolume"
        DOCKER_TESTS_VOLUME_PATH = "/tests"
    }

    stages {
        stage("test") {
            steps {
                sh """
                docker build -t jenkins-tests .
                docker run \
                    --rm \
                    -v ${DOCKER_TESTS_VOLUME}:${DOCKER_TESTS_VOLUME_PATH} \
                    -e DOCKER_TESTS_VOLUME_PATH=${DOCKER_TESTS_VOLUME_PATH} \
                    jenkins-tests
                """
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
            """
        }
    }
}
