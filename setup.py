#just type this in cmd after going to this location --- python setup.py build
#or
#python setup.py bdist_msi
import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable(script = "chesszero.py",icon='pieces/icon.ico')]

cx_Freeze.setup(
	name ="CHESSZERO v0.1",
	options ={"build_exe":{"packages":["pygame","time",'copy','chess','random'],
							"include_files":[ os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
           					 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
           					 'pieces/','instructions image/','background.png','pieces/stockfish.exe']
 							}
 			},
	executables = executables,
	version="0.1"
	)