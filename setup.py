from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read() #force no build without readme

setup(
    name="KingdomsAndWarfare",
    version="0.1.0",
    description="Kingdoms, Units, Unit Traits all for MCDM's excellent expansion for D&D",
    packages=["Kingdoms", "Units", "Traits"],
    python_requires=">=3.11",
    project_urls={"Source": "https://github.com/bleehu/PyMCDMKingdomsAndWarfare"}
)