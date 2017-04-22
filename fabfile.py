from fabric.api import run


def build_n_serve():
    run('docker pull da5id2517/seven_tweets')
    run('docker run -p 80:5000 da5id2517/seven_tweets')