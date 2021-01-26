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
                export URL=export URL=http://127.0.0.1:8000/deploys/api/jenkins-builds/
                curl $URL \
                    -F project_name=jenkins-test \
                    -F repo_url=https://github.com/sbevc/jenkins-test.git 
                    -F jenkins_url=http://host.docker.internal:8080 
                    -F job_name=test/master 
                    -F build_number=22 
                    -F tests_output=@~/tests-output/pytest_output.xml 
            """
        }
    }
}
