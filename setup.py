from distutils.core import setup
setup(
  name = 'fortune.py',
  packages = ['fortune'],
  package_data = {'fortune': ['cookiesets/*.txt']},
  scripts = ["fortune/fortune.py"],
  version = '0.1',
  description = 'Fortune cookie teller for your shell',
  author = u'Håkan Waara',
  author_email = u'hwaara@gmail.com',
  url = 'https://github.com/hakanw/fortune.py', 
  keywords = ['fortune', 'fate', 'cookie'], 
  classifiers = [],
)
