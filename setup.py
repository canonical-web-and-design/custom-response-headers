from setuptools import setup

setup(
    name="canonicalwebteam.custom-response-headers",
    version="0.2.0",
    author="Canonical Webteam",
    url="https://github.com/canonical-webteam/custom-response-headers",
    packages=["canonicalwebteam", "canonicalwebteam.custom_response_headers"],
    description=(
        "Django middleware for setting custom HTTP headers"
        "to be included in every HTTP response."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["Django >= 1.3"],
)
