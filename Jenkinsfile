pipeline {
  agent any
  stages {
    stage('Stage1') {
      steps {
         'echo \'hello world.. deploying kong proxy service\''
      }
    }

   stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python main.py'
      }
    
  }
  
}
}
