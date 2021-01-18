pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                sh 'echo hello'
                sh 'python3 script.py'
            }
        }
    }
    post {
        always {
            sh 'echo POST'
            sh 'python3 script.py'
        }
    }
}
