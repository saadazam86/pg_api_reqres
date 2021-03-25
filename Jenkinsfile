pipeline {
    environment {
        PYTHON_HOME= "C:/prjtools/python/ver_3.7.6_p4"
    }
    agent any
    options {
        disableConcurrentBuilds()
    }
    stages {
        stage ('Fetch User Data') {
            steps {
                script {
                    def status = bat script:"%PYTHON_HOME%\\python.exe -u fetch_userdata_reqres.py" , returnStatus:true
                    if (status != 0) {
                        currentBuild.result='FAILURE'
                    }
                    else {
                        currentBuild.result='SUCCESS'
                        archiveArtifacts artifacts: "user_data.xlsx", allowEmptyArchive: true
                    }
                }
            }
        }
    }
}

