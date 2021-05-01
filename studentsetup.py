from cx_Freeze import *
#includefiles = ["mana.ico"]
includes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", # Dictionary
     "stumanage", #name
     "TARGETDIR", #component
     "[TARGETDIR]\Studentmanagementsystemapp.exe", # target
     None, # Arguments
     None,  # Discription
     None,  # hOTKEY
     None,  # ICON
     None,  # Iconindex
     None,  # showcmd
     "TARGETDIR", # wkdir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data':msi_data}
setup(
    version="0.1",
    description="student Management System developed by sejal agrawal",
    author="sejal agrawal",
    name="Student Management System",
    options={'build_exe':{} ,"bdist_msi":bdist_msi_options, },
    executables=[
        Executable(
            script="studentmanagementsystemapp.py",
            base=base,
            #icon='mana.ico',
        )
    ]
)