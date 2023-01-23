pipeline {
    agent any
    stages {
        stage('Migrate') {
            steps {
                sh 'python manage.py migrate'
            }
        }
        stage('Create Superuser') {
            steps {
                sh 'echo "from django.contrib.auth.models import User; User.objects.create_superuser(\'admin\',\'admin@example.com\',\'password\')" | python manage.py shell'
            }
        }
    }
}