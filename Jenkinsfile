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
         'python --version'
      }
    }
    stage('hello') {
      steps {
        'python main.py'
      }
    
  }
  
}
}
