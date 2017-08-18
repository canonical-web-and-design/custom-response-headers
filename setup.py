from setuptools import setup

setup(
    name='canonicalwebteam.custom-response-headers',
    version='0.2.0',
    author='Canonical Webteam',
    url='https://github.com/canonical-webteam/custom-response-headers',
    packages=[
        'canonicalwebteam',
        'canonicalwebteam.custom_response_headers'
    ],
    description=(
        'Django middleware for setting custom HTTP haders'
        'to be included in every HTTP response.'
    ),
    longdescription=open('README.md').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)

