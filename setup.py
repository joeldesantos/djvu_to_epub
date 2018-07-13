from setuptools import setup

setup(name='djvu_to_epub',
      version='0.1',
      description='Converts DJVU files to EPUB books',
      long_description = read('README.md'),
      keywords=['djvu', 'epub', 'ebook', 'kindle'],
      url='http://github.com/joeldesantos/djvu_to_epub',
      author='Joel de Santos',
      author_email='joeldesantos@gmail.com',
      license='GNU Affero General Public License',
      packages=['djvu_to_epub', 'djvu_to_epub.formatters', 'djvu_to_epub.templates'],
      zip_safe=False,
      classifiers = [
        "Development Status :: 1 - Development",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      install_requires = [
        "lxml", "six"
      ]
    )