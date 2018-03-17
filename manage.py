from flask_script import Manager,Server
from main import app

manager=Manager(app)#将app传给Manager对象，以初始化flask_script

manager.add_command('server',Server())

#manager_shell_contecxt创建执行命令，在下一个函数执行
@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__=='__main__':
    manager.run()