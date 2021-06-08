import eel

# This is how I do it: https://github.com/robinloop/eel-angular-demo/blob/master/main.py
"""
----------------------------------------------------------------------------------
  'options' argument deprecated in v1.0.0, see https://github.com/ChrisKnott/Eel
  To suppress this error, add 'suppress_error=True' to start() call.
  This option will be removed in future versions
----------------------------------------------------------------------------------

WTF?!
"""

eel.init('public')
eel.start({'port': 4200},suppress_error=True, options={
  'chromeFlags': ['--auto-open-devtools-for-tabs']
})