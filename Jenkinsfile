pipeline {
    agent any

        stages {
            stage("test file exists") {
                steps {
                    script {
                        if (fileExists('/Users/sbevc/foo')) {
                            sh "echo ~/foo exists!!!"
                        } else {
                            sh "echo ~/foo does not exist!"
                        }
                        sh "exit 1"
                    }
                }

            }

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
                curl http://127.0.0.1:8000/builds/api/jenkins-builds/ \
                -F project_name=jenkins-test \
                -F repo_url=${GIT_URL} \
                -F git_branch=${GIT_BRANCH} \
                -F jenkins_url=${JENKINS_URL} \
                -F job_name=${JOB_NAME} \
                -F build_number=${BUILD_NUMBER} \
                -F tests_output=@/Users/sbevc/tests-output/pytest_output.xml -F tests_runner=pytest \
                -F tests_output=@/Users/sbevc/tests-output/npm_output.xml -F tests_runner=npm \
                -F docker_image=jenkins-tests::\$(docker inspect -f {{.Id}} jenkins-tests)
                """
        }
    }
}
