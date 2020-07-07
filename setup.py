from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'tszhas',
  packages = ['tszhas'],
  version = '1.2.0',
  license='MIT',
  #long_description=long_description,
  #long_description_content_type='text/markdown',
  author = 'Anders Gill',
  author_email = 'gill@outlook.com',
  url = 'https://github.com/RaaLabs/TSIClient',
  #download_url = 'https://github.com/RaaLabs/TSIClient/archive/v_0.7.tar.gz',    # I explain this later on
  keywords = ['Time Series Insight', 'TSI', 'TSI SDK'],
  install_requires=[
          'requests',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)