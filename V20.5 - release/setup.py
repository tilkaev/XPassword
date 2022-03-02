import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

import sys
from distutils.core import setup
import cx_Freeze
import matplotlib

base = "Win32GUI"
#base = "Console"

executable = [cx_Freeze.Executable("passwordV20_5.pyw", targetName="XPassword.exe", base=base, icon='ico.ico')]

includes = ['tkinter', "webbrowser", "time", "os", "simpledialog", "idna.idnadata", "_cffi_backend", "pyautogui"]

excludes = ["numpy"]

zip_include_packages = ["tkinter","collections","encodings","importlib","tcl","simpledialog","asn1crypto",
                        "cryptography","ctypes",'email',"html","http","idna","logging",'pyAesCrypt','pydoc_data',
                        'unittest','urllib','xml','pyexpat',
                        'unicodedata','pyexpat']

build_exe_options = {"build_exe":
                    {"includes":includes,
                     "excludes":excludes,
                     "zip_include_packages":zip_include_packages,

                     'include_files':[
            'data',
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')],
                     'build_exe':"Password"}}

cx_Freeze.setup(
    name = "py",
    options = build_exe_options,
    version = "1.0",
    description = "standalone",
    executables = executable,
)
