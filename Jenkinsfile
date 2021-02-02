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
                    -F project_name=jenkins-test \
                    -F repo_url=${GIT_URL} \
                    -F jenkins_url=http://host.docker.internal:8080 \
                    -F job_name=${JOB_NAME} \
                    -F build_number=${BUILD_NUMBER} \
                    -F tests_output=@/Users/sbevc/tests-output/pytest_output.xml \
                    -F git_branch=${GIT_BRANCH} 
                    -F docker_img=jenkins-tests::`docker inspect -f {{.Id}} jenkins-tests`
            """
        }
    }
}
