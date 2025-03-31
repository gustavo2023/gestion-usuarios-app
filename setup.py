from setuptools import setup, find_packages

setup(
    name="gestion_usuarios",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mysql-connector-python==8.1.0",
        "python-dotenv==1.0.0",
        "sqlalchemy==2.0.25",
        "rich==13.7.0",
        "pytest==8.0.0",
        "passlib==1.7.4",
        "bcrypt==4.0.1",
    ],
    entry_points={
        "console_scripts": [
            "gestion-usuarios=cli.main:show_menu",
        ],
    },
)