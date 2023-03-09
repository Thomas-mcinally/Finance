from setuptools import setup, find_packages

setup(
    dependency_links=[],
    name="stockprice-cli",
    packages=find_packages(exclude=["tests"]),
    email="thomasmcinally@hotmail.com",
    author="Thomas Mcinally",
    url="https://github.com/Thomas-mcinally/stockprice",
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    install_requires=[
        "appdirs==1.4.4",
        "beautifulsoup4==4.11.2; python_full_version >= '3.6.0'",
        "certifi==2022.12.7; python_version >= '3.6'",
        "cffi==1.15.1",
        "charset-normalizer==3.1.0; python_full_version >= '3.7.0'",
        "cryptography==39.0.2; python_version >= '3.6'",
        "frozendict==2.3.5; python_version >= '3.6'",
        "html5lib==1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "idna==3.4; python_version >= '3.5'",
        "lxml==4.9.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "multitasking==0.0.11",
        "numpy==1.24.2",
        "pandas==1.5.3",
        "pycparser==2.21",
        "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pytz==2022.7.1",
        "requests==2.28.2; python_version >= '3.7' and python_version < '4'",
        "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "soupsieve==2.4; python_version >= '3.7'",
        "urllib3==1.26.14; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
        "webencodings==0.5.1",
        "yfinance==0.2.12",
    ],
    version="1.0.5",
    entry_points={"console_scripts": ["stockprice = stockprice.main:main"]},
)
