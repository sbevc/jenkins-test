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
                sh 'running tests in docker'
                sh 'docker run jenkins-tests'
            }
        }

    }

    //post {
        //always {
            //sh 'echo post-always'
            //sh '$PY_ENV script.py'
        //}
    //}
}
