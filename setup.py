import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_version():
    try:
        with open('VERSION', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "0.0.1-dev"

setuptools.setup(
    name = "mcoti_package",
    version = get_version().rstrip(),
    author = "mcoti",
    author_email = "mcoti@gmail.com",
    description = "A small example package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/pypa/sampleproject",
    project_urls = {
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src"),
    python_requires = ">=3.7",
)