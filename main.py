import eel

mypage = {
  'scheme': 'http',
  'host': 'localhost',
  'port': 4200,
  'page': 'index.html'
}

eel.init('public')
eel.start({'port': 4200}, options={
  'port': 8000,
  'host': 'localhost',
  'chromeFlags': ['--auto-open-devtools-for-tabs']
})