pipeline {
    agent any

    environment {
        DOCKER_TESTS_VOLUME = "TestsVolume"
        DOCKER_TESTS_VOLUME_PATH = "/tests"

        SAF_ENDPOINT = "http://127.0.0.1:8000/deploys/api/jenkins-builds/"
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
            curl ${SAF_ENDPOINT} \
                -F project_name=jenkins-test \
                -F repo_url=https://github.com/sbevc/jenkins-test.git \
                -F jenkins_url=http://host.docker.internal:8000 \
                -F job_name=test/master \
                -F build_number=22 \
                -F tests_output=@${DOCKER_TESTS_VOLUME_PATH}/pytest_output.xml
            """
        }
    }
}
