from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
# 3dE*.cd5sYw8bnh
setup(
    name='DjangoViz',
    version='1.0.0',
    author='Prathmesh Nandurkar',
    author_email='prathmeshnandurkar123@gmail.com',
    url='https://github.com/prathmesh2048/commandline-tool',
    description='CLI tool that can visualize the database schema of Django applications using the Atlas Cloud Playground.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
    py_modules = ['action', 'djangoviz'],
    license='MIT',
    packages=find_packages(),
    install_requires=[requirements],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        djangoviz=action:cli
    '''
)
