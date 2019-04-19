pipeline {
  agent any
  stages {
    stage('Stage1') {
      parallel {
        stage('Step 1.1') {
          steps {
            echo '1234'
            sleep 1
            echo '321'
          }
        }
        stage('Step1.2') {
          steps {
            bat(script: 'cd d:\\', returnStdout: true, returnStatus: true)
          }
        }
      }
    }
  }
}