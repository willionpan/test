pipeline {
  agent any
  stages {
    stage('Stage1') {
      parallel {
        stage('Step 1.1') {
          steps {
            echo '1234'
            sleep 10
            echo '321'
          }
        }
        stage('Step1.2') {
          steps {
            echo '12345'
            bat(script: 'cd d:\\', returnStdout: true, returnStatus: true)
            sleep 10
            echo '22345'
          }
        }
        stage('Step1.3') {
          agent any
          steps {
            echo '333333'
            sleep 10
            echo '34444'
          }
        }
      }
    }
  }
}