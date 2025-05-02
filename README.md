# portfolio.old

This is my first (and failed) attempt at creating a portfolio website back in 2023 - 2nd year of university.  
Started to idealize this project in the Fall of 2022 - 1st year of university - but only got around to artboarding and coding in the Spring of 2023.  
However, it took me till the Spring of 2025 to actualize/implement a proper working portfolio website.

You can actually run this code through the following steps. [Comprehensive guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
1. Create a Python virtual environment (venv). <https://docs.python.org/3/library/venv.html>
```
python -m venv .venv
```
2. Activate the venv.
```
source .venv/bin/activate
```
3. Using pip, install the dependencies listed in the requirements.txt.
```
pip install -r requirements.txt
```
4. Using Django commands, migrate the Django models to the database.
```
python manage.py makemigrations  
python manage.py migrate
```
5. Run the Django webserver.
```
python manage.py runserver
```

Portfolio website (current): <https://joshualiew.com/home/>

The homepage of my portfolio prototype __(old, failed attempt!)__ :  
![Prototype homepage image!](/artboards/10_prototype_home.png)

To view the old artboards, look in this the [artboards](https://github.com/joshua-liew/portfolio.old-failed/tree/master/artboards) directory.  
![Old home page artboard!](/artboards/01_desktop_home.png)