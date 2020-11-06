import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "face-recognition-python-webcam",
    version = "0.0.1",
    author = "Kamlesh Singh",
    author_email = "kamaleshs48@gmail.com",
    description = ("An ."),
    license = "BSD",
    keywords = "face-recognition-python-webcam",
    url = "http://packages.python.org/face-recognition-python-webcam",
    packages=['face_recognition_python_webcam', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)