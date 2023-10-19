pipeline {
  agent any
  stages {
    stage('Stage1') {
      steps {
        sh 'echo \'hello world.. deploying kong proxy service\''
      }
    }

    stage('') {
      steps {
        git(url: 'https://github.com/asanivarapu/Konglocal.git', branch: 'main')
      }
    }

  }
  environment {
    dev = 'dev'
  }
}