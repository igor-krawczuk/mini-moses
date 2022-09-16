from setuptools import setup, find_packages


setup(name='mini_moses',
      version='1.0',
      python_requires='>=3.5.0',
      packages=find_packages() + ['mini_moses/metrics/SA_Score',
                                  'mini_moses/metrics/NP_Score',
                                  'mini_moses/dataset/data'],
      install_requires=[
          'tqdm>=4.26.0',
          'matplotlib>=3.0.0',
          'numpy>=1.15',
          'pandas>=0.25',
          'scipy>=1.1.0',
          'torch>=1.1.0',
          'fcd_torch>=1.0.5',
          'seaborn>=0.9.0',
      ],
      description=('Stripped down version of https://github.com/molecularsets/moses containing only data for easier installation'),
      author='Igor Krawczuk, original author:Insilico Medicine',
      author_email='contact-gh@krawczuk.eu',
      license='MIT',
      package_data={
          '': ['*.csv', '*.h5', '*.gz', '*.csv.gz', '*.npz'],
      }
      )
