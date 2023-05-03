from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="django-theme-academy",
    version="0.3.4",
    packages=find_packages(),
    include_package_data=True,
    package_data={'academy_theme': ["py.typed"]},
    install_requires=[
        "django-wildewidgets >= 0.13.49"
    ],
    author="Caltech IMSS ADS",
    author_email="imss-ads-staff@caltech.edu",
    url="https://github.com/caltechads/django-theme-academy",
    description="A Tabler-based, fixed left sidebar django theme.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Testing',
    ],
)
