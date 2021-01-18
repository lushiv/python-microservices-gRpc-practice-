from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except IOError as e:
    print(e)

test_requirements = [
    'tox',
]

setup(
    name='bb_python_utils',
    version='0.0.1',
    description="BitsBeat Python Utils",
    long_description=readme + '\n',
    author="Subash Basnet",
    author_email='subash.basnet@bitsbeat.com',
    url='subashbasnet.com.np',
    packages=find_packages(),
    namespace_packages=['bb_python_utils'],
    package_dir={},
    package_data={
        # If any package contains *.ini
        "": ["*.ini"],
    },
    install_requires=requirements,
    license="",
    zip_safe=False,
    keywords='bitsbeat, python',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
