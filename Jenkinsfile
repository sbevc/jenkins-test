pipeline {
    agent any

    environment {
        TESTS_PATH = "/tests"
    }

    stages {
        stage("test") {
            steps {
                sh """
                docker build -t jenkins-tests .
                docker run \
                    --rm \
                    -v ${TESTS_PATH}:$TESTS_PATH \
                    -e TESTS_PATH=${TESTS_PATH} \
                    jenkins-tests
                """
                sh 'ls ${TESTS_PATH}'
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
                -v ${TESTS_PATH}:${TESTS_PATH} \
                -e JENKINS_URL=http://host.docker.internal:8080 \
                -e JOB_NAME=${env.JOB_NAME} \
                -e BUILD_NUMBER=${env.BUILD_NUMBER} \
                -e DOCKER_TESTS_VOLUME_PATH=${TESTS_PATH} \
                send-script
            docker volume rm ${TESTS_PATH}
            """
        }
    }
}
