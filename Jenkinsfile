pipeline {
    agent any
    stages {
        stage('Migrate') {
            steps {
                sh 'python manage.py makemigrations --merge && python manage.py migrate'
            }
        }
    }
}