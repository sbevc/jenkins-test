pipeline {
    agent any

    environment {
        PY_ENV = "/Users/sbevc/.local/share/virtualenvs/jenkins-7fb5-MYk/bin/python3"
    }

    stages {
        stage("test") {
            sh '$PY_ENV -m pytest'
        }

        stage("build") {
            steps {
                sh 'echo building...'
            }
        }
    }

    post {
        always {
            sh 'echo post-always'
            sh '$PY_ENV script.py'
        }
    }
}
