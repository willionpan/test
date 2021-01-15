pipeline {
  agent any
  stages {
    stage('Stage1') {
      parallel {
        stage('Step 1.1') {
          steps {
            echo '1234'
            sleep 20
            echo '321'
          }
        }

        stage('Step1.2') {
          steps {
            echo '12345'
            bat(script: 'cd d:\\', returnStdout: true, returnStatus: true)
            sleep 20
            echo '22345'
          }
        }

      }
    }

    stage('Stage2') {
      steps {
        sleep 1
      }
    }

  }
}