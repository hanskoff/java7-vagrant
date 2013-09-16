from fabric.api import task, settings
from fabtools.vagrant import vagrant
from fabtools import require, deb, oracle_jdk, python, tomcat

@task
def provision():
    require.file('.vimrc', source='vimrc')
    deb.update_index()
    # install java7
    require.oracle_jdk.installed()
    # install tomcat7
    require.tomcat.installed()
    # install mysql
    require.mysql.server(password='s3cr3t')
    with settings(mysql_user='root', mysql_password='s3cr3t'):
        require.mysql.user('dbuser', 'somerandomstring')
        require.mysql.database('myapp', owner='dbuser')
    # install other packages
    require.deb.packages([
        'build-essential',
        'python'
        ], update=True)
    deb.upgrade()
    

@task
def installMongo():
    require.deb.key('7F0CEB10', keyserver='keyserver.ubuntu.com')
    require.deb.source('mongodb', 'http://downloads-distro.mongodb.org/repo/ubuntu-upstart', 'dist', '10gen')
    # deb.update_index()
    require.deb.packages([
        'mongodb-10gen',
        ], update=True)

@task
def installTomcat():
    require.oracle_jdk.installed()
    # install tomcat
    require.tomcat.installed('6.0.36')
    # require.tomcat.installed()

@task
def startTomcat():
    tomcat.start_tomcat()

@task
def versionTom():
    print tomcat.version()
