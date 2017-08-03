import pypandoc
import os

f = open('README.txt', 'w+')
f.write(pypandoc.convert('README.md', 'rst'))
f.close()
os.system("python setup.py sdist bdist_wheel")
os.system("twine upload dist/*")
os.remove('README.txt')
