import setuptools

with open("README.md", "r") as fh:
	description = fh.read()


setuptools.setup(
	name = "pyfgc_decoders",
	version = "0.0.3",
	author = "Carlos Ghabrous Larrea",
	author_email = "carlos.ghabrous@cern.ch",
	description = description,
	url="https://gitlab.cern.ch/ccs/fgc/tree/master/sw/clients/python/pyfgc_decoders",
	python_requires=">=3.6",

	packages=setuptools.find_packages()
)
