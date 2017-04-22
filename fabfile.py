from fabric.api import run, local


def build_n_serve():
    local('docker build -t da5id2517/seven_tweets .')
    local('docker push da5id2517/seven_tweets')
    run('docker stop $(docker ps -q)')
    run('docker pull da5id2517/seven_tweets')
    run('docker run -p 80:5000 da5id2517/seven_tweets')