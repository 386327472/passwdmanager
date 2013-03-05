from distutils.core import setup
import glob
import py2exe

setup(windows=[{"script":"pwmanager","icon_resources":[(1,"icons/pm.ico")]}], 
      data_files=[("data",glob.glob("data/*.*")),
                  ("icons",glob.glob("icons/*.png")),
                  ("conf",glob.glob("conf/*.*")),
                  ("backup",glob.glob("backup/*.*")),
                  ] 
      )
