pipeline {
    agent any

    stages {
        stage("test") {
            steps {
                sh """
                    echo \\"\$(whoami)\\"
                    exit 1
                """
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
            whoami = sh (
                script: 'whoami',
                returnStdout: true
            )
            sh """
                curl http://127.0.0.1:8000/deploys/api/jenkins-builds/ \
                    -H "Content-Type: application/json" \
                    -d '{
                        "project_name": "test1234",
                        "repo_url": "https://github.com/sbevc/jenkins-test.git",
                        "jenkins_url": "http://host.docker.internal:8000",
                        "git_branch": "${GIT_BRANCH}",
                        "job_name": "${JOB_NAME}",
                        "build_number": "${BUILD_NUMBER}",
                        "tests_output": [
                            {"whoami": ${whoami}}
                        ]
                    }'
            """
        }
    }
}
