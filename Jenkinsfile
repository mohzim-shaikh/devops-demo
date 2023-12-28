pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mohzim-shaikh/devops-demo.git']])
            }
        }
        stage('Lint') {
            steps {
                sh 'python3 -m flake8'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 app_testcases.py'
            }
        }
        stage('Docker Lint') {
            steps {
                sh 'hadolint --ignore DL3008 Dockerfile'
            }
        }
    }
}
