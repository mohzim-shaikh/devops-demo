pipeline {
    agent any

    stages {
        stage('Commit') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mohzim-shaikh/devops-demo.git']])
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'                
                sh 'pip3 install -r app/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate'                
                sh 'python3 app_testcases.py'
            }
        }
        
    }
}
