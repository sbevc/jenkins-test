pipeline {
    agent any

    stages {
        stage("test") {
            steps {
                sh """
                docker build -t jenkins-tests .
                docker run \
                    --rm \
                    -v ~/tests-output:/tests \
                    -e DOCKER_TESTS_VOLUME_PATH=/tests \
                    jenkins-tests
                """
            }
        }
    }

    post {
        always {
            sh """
                curl http://127.0.0.1:8000/deploys/api/jenkins-builds/ \
                    -H "Content-Type: application/json" \
                    -d "{"project_name": "foobar"}"
            """
        }
    }
}
