workid = input('请输入作品id:')
print(__import__('requests').post('https://hackmao.pickfish.repl.co/',data=workid).content+'\n');
input('按下回车退出......')
