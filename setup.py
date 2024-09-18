from setuptools import setup, Extension
from os import environ

if environ.get("NO_CYTHON"):
    setup(
        package_dir={"": "src"},
        packages=["elaina_triehard"],
        include_package_data=True,
        exclude_package_data={"": ["*.c"]},
    )
    exit()

setup(
    ext_modules=(
        [
            Extension("elaina_triehard.impl_c", ["src/elaina_triehard/impl_c.c"]),
        ]
    ),
    include_package_data=True,
    exclude_package_data={"": ["*.c"]},
)
