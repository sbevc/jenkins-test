pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                sh 'echo building...'
            }
        }
    }
    post {
        always {
            sh 'echo post-always'
            sh 'python3 script.py'
        }
    }
}
