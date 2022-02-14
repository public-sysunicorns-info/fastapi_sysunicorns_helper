import setuptools
import subprocess


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

_result = subprocess.run("src/fastapi_sysunicorns/version.py", encoding="utf-8", stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True, shell=True)
version = _result.stdout

setuptools.setup(
    name="fastapi-sysunicorns-helper",
    version=version,
    description="Utility Package for FastApi Python Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/public-sysunicorns-info/fastapi_sysunicorns_helper",
    project_urls={
        "Bug Tracker": "https://github.com/public-sysunicorns-info/fastapi_sysunicorns_helper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)