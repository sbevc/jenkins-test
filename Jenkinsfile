/**
 * Check for files existence supporting unix globs 
 *
 * @param fileGlob filepath to check for, accepting "~", relative and absolute paths.
 */
def fileGlobExists(String fileGlob) {
    files = sh(returnStdout: true, script: """
        python -c 'import glob, os; print(glob.glob(os.path.expanduser("$fileGlob")))'
    """)
    notFound = "[]\n"
    return files != notFound
}


pipeline {
    agent any

        stages {

            stage("foo") {
                steps {
                    script {
                        println("Result is: ${currentBuild.result}")
                        try {
                            sh "exit 1"
                            println("NO ERROR")
                        } catch (error) {
                            println("ERROR")
                        }
                    }
                }
            }


            stage("test") {
                steps {
                    sh "echo testing..."
                }
            }
        }

    post {
        always {
            script {
                println("Result is: ${currentBuild.result}")
            }
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                script {
                    def files = [
                        "/Users/sbevc/fo*",
                        "./Dockerf*",
                        "~/fo*",
                        "~/nonexitent*"
                    ]
                    for (file in files) {
                        if (fileGlobExists(file)) {
                            println("$file found")
                        } else {
                            println("$file not found")
                        }
                    }
                }

            }
        }
    }
}
