from setuptools import setup

setup(
    name="git_demo_python",
    version="0.0.1",
    packages=["animals"],
    url="https://github.com/ChrisMcCarthyDev/git_demo_python",
    author="Chris McCarthy",
    description="A demo Python project to enable python training for my team",
    install_requires = [],
    extras_require={
        "dev": [
            "pytest"
        ]
    }
)
