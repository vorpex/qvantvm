from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='qvantum',
    version='0.93',
    description='Python package for quantum computing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/vorpex/qvantum',
    author='Adam Sohonyai & Roland Sztaho',
    author_email='sohonyai.adam@gmail.com, rolandsztaho88@gmail.com',
    maintainer='Adam Sohonyai & Roland Sztaho',
    maintainer_email='sohonyai.adam@gmail.com, rolandsztaho88@gmail.com',
    license='MIT',
    keywords='python quantum computing',
    packages=find_packages(),
    # scripts=['bloch.py', 'check_bloch.py', 'check_circuit.py', 'check_gate.py', 'check_layer.py', \
    #     'check_qubit.py', 'check_register.py', 'circuit.py', 'gate.py', 'layer.py', 'qubit.py', \
    #     'register.py'],
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    zip_safe=False)
