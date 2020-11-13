c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888

# (local) disable auth
c.NotebookApp.token = ''
c.NotebookApp.password = ''

# access to jupyter server by IDE
c.NotebookApp.disable_check_xsrf =True