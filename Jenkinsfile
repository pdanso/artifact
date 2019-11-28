<<<<<<< HEAD
// node {
//
//     try {
//         stage 'Checkout'
//             checkout scm
//
//             sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
//             def lastChanges = readFile('GIT_CHANGES')
// //             slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"
//
//         stage 'Test'
//             sh 'virtualenv corporate_env -p python3.7'
//             sh '. corporate_env/bin/activate'
//             sh 'corporate_env/bin/pip install -r requirements.txt'
//             sh 'corporate_env/bin/python3.7 manage.py runserver'
// //             sh 'env/bin/python3.7 manage.py test --testrunner=djtrump.tests.test_runners.NoDbTestRunner'
//
// //         stage 'Deploy'
// //             sh './deployment/deploy_prod.sh'
// //
// //         stage 'Publish results'
// //             slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
//     }
//
// //     catch (err) {
// //         slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
// //         throw err
// //     }
//
// }
//
// #!/usr/bin/groovy
//
// node {
//   // If you are having issues with your project not getting updated,
//   // try uncommenting the following lines.
//   //stage 'Checkout'
//   //checkout scm
//   //sh 'git submodule update --init --recursive'
//   stage 'Checkout'
//             checkout scm
//
//             sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
//
//   stage 'Update Python Modules'
//   // Create a virtualenv in this folder, and install or upgrade packages
//   // specified in requirements.txt; https://pip.readthedocs.io/en/1.1/requirements.html
//   sh 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements.txt'
//
//   stage 'Test'
//   // Invoke Django's tests
//   sh 'source env/bin/activate && python ./manage.py runtests'
// }
//
// pipeline {
//     agent { docker { image 'python:3.5.1' } }
//     stages {
//         stage('build') {
//             steps {
//                 sh 'python --version'
//             }
//         }
//     }
//     stages {
//         stage('Test') {
//             steps {
//                 sh 'python --version'
//             }
//         }
//     }
// }

pipeline {
         agent any
         stages {
              stage('One') {
                   steps {
                       echo 'Hi, this is Priscilla from Mesika'
                   }
              }
              stage('Two') {
                 steps {
                    input('Do you want to proceed?')
                 }
              }
              stage('Three') {
                 when {
                       not {
                            branch "master"
                       }
              }
                 steps {
                       echo "Hello"
                 }
                 }
              stage('Four') {
                    parallel {
                         stage('Unit Test') {
                           steps {
                                echo "Running the unit test..."
                           }
                         }
                         stage('Integration test') {
                              steps {
                                echo "Running the integration test..."
                              }
                         }
                   }
              }
         }
}
=======
node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'

        stage 'Test'
            sh 'virtualenv -q corporate_env'
            sh 'source ./corporate_env/bin/activate'
            sh 'python $WORKSPACE/corporate_banking_api/manage.py test'
            sh 'cd $WORKSPACE/corporate_banking_analysis'
    }

  catch{
  }

}

>>>>>>> e57f893beca38a3603c4a98e60bd5724b2a85a15
