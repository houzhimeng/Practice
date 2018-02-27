# from src import commons
# commons.add()
#
# func_name = 'add'
#
# func = getattr(commons,func_name)
# func()

module = 'src.commons'
func_name = 'add'

import importlib
m = importlib.import_module(module)
func = getattr(m,func_name)
func()

