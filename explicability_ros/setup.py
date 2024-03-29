
from setuptools import find_packages, setup

package_name = "explicability_ros"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages",
            ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="dsobh",
    maintainer_email="dsobh@unileon.es",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "explicability_node = explicability_ros.explicability_node:main",
            "explicability_client_node = explicability_ros.explicability_client_node:main",
            "vexp_node = explicability_ros.vexp_node:main"
        ],
    },
)
