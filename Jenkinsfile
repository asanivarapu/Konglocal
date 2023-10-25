pipeline {
  agent any
  stages {
    stage('mainconfigs') {
      parallel {
        stage('mainconfigs') {
          steps {
            echo 'hello.. loading main configs'
            git(url: 'parentrepourl', branch: 'main')
          }
        }

        stage('checkout api config') {
          steps {
            echo 'in checkout api config'
            git(url: 'repourl', branch: 'main')
            echo 'checkout $repourl complete'
          }
        }

        stage('checkout python scripts') {
          steps {
            echo 'in checkout of python scripts'
            git(url: '$scripts', branch: 'main')
          }
        }

        stage('Execute scripts') {
          steps {
            dir(path: 'scripts') {
              bat(script: 'main.py', returnStatus: true, returnStdout: true)
            }

          }
        }

      }
    }

  }
  environment {
    parentrepourl = 'https://github.com/asanivarapu/Konglocal.git'
    env = 'dev'
    branch = 'main'
    repourl = 'https://github.com/asanivarapu/Konglocal.git'
  }
}