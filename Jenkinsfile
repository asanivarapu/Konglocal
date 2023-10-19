pipeline {
  agent any
  stages {
    stage('Stage1') {
      steps {
        sh 'echo \'hello world.. deploying kong proxy service\''
      }
    }

   stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 main.py'
      }
    
  }
  environment {
    dev = 'dev'
  }
}
