from setuptools import setup, find_packages

setup(
    name='edx_course_structure',
    version='1.0.0',
    description='EDX course structure',
    url='git@github.com/sarmientoSD/edx_course_structure.git',
    author='Fernando Sarmiento',
    author_email='fsarmientod@uni.pe',
    license='unlicense',
    package_dir={"": "lib"},
    packages=find_packages("lib"),
    zip_safe=False,
    install_requires=[
        "lxml",
    ]
)
