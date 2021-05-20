pipeline {
  agent any
  stages {
    stage('Stage1') {
      parallel {
        stage('Step 1.1') {
          steps {
            echo '1234'
          }
        }

        stage('Step1.2') {
          steps {
            bat(script: 'd:\\run.bat', returnStdout: true, returnStatus: true)
          }
        }

      }
    }

  }
}