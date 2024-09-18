from setuptools import setup, Extension
from os import environ
import os
from Cython.Build import cythonize

if environ.get("NO_CYTHON"):
    setup(
        package_dir={"": "src"},
        packages=["elaina_triehard"],
        include_package_data=True,
        exclude_package_data={"": ["*.c"]},
    )
    exit()


setup(
    ext_modules=cythonize("src/elaina_triehard/impl_c.pyx"),  # 使用 cythonize 编译扩展
    include_package_data=True,  # 包含包内的数据
    #packages=find_packages("src"),  # 查找包
    #exclude_package_data={"": ["*.c"]},  # 排除 .c 文件
)