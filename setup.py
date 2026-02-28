from setuptools import setup, find_packages

setup(
    name='crypto-tape-bot-Vector',
    version='0.1.0',
    author='douglasdott-crypto',
    author_email='your_email@example.com',  # Replace with your email
    description='A bot for managing crypto tapes.',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add your project's dependencies here
        # 'numpy',
        # 'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)