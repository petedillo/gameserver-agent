@Library('jenkins-shared-library@main') _

singleImageBuild(
    repo: 'https://github.com/petedillo/gameserver-agent',
    registry: 'diolab:5000',
    host: 'diolab',
    sshCreds: 'jenkins-petedillo',
    composePath: '/home/pete/services/gameserver-agent/compose.yaml',
    imageName: 'gameserver-agent',
    branch: 'dev',
    buildArgs: [],
    contextPath: '.',
    platform: 'linux/amd64',
    push: true
)
