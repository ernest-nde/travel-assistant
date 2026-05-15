from setuptools import setup, find_packages

setup(
    name="travel-assistant",
    version="0.1.0",
    description="Travel Assistant Chatbot - Assistant de voyage conversationnel",
    author="CCNB Student",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "black>=24.1.1",
            "flake8>=7.0.0",
        ]
    },
)
