import eel

# This is how I do it: https://github.com/robinloop/eel-angular-demo/blob/master/main.py

eel.init('public')
eel.start({'port': 4200},suppress_error=True, options={
    'port': 8000,
    'host': 'localhost',
})