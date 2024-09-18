from setuptools import find_packages, setup, Extension
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

extensions = [
    Extension(
        "elaina_triehard",  # 模块名称（不包括 .pyx 后缀）
        sources=["src/elaina_triehard/*.pyx"],  # 源文件路径
        include_dirs=[os.path.join(os.getcwd(), "src")],  # include path
    )
]

setup(
    ext_modules=cythonize(extensions),  # 使用 cythonize 编译扩展
    include_package_data=True,  # 包含包内的数据
    #packages=find_packages("src"),  # 查找包
    #exclude_package_data={"": ["*.c"]},  # 排除 .c 文件
)