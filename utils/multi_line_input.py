import io

class multi_line_input():
    def __init__(self):
        self.shell = get_ipython()
        self.sio = io.StringIO('')
        self.shell.events.register('pre_run_cell', self.pre_run_cell)
        
    def __call__(self):
        return self.sio.readline().strip()
    
    def pre_run_cell(self, info):
        text = self.shell.user_ns['text_area'].value
        self.sio = io.StringIO(text)