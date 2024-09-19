from setuptools import find_packages, setup, Extension
from os import environ
import os
from Cython.Build import cythonize


setup(
    ext_modules=cythonize(Extension(
        "elaina_triehard.impl_c",
        sources=["elaina_triehard/impl_c.pyx"],
    )),
    include_package_data=True,  # 包含包内的数据
    packages=find_packages(),  # 查找包
    exclude_package_data={"": ["*.c"]},  # 排除 .c 文件
)
