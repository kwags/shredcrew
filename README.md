# Shred Crew Website

**Shred Crew** is a custom mountain biking website built with Python and Django, featuring dynamic pages, a newsletter subscription system, database integration, and a Django admin interface for managing subscribers.

The project was developed from concept through implementation, including the website's logo, branding, UI/UX, front-end development, and Django back-end functionality.

<img width="1400" height="852" alt="sc-home" src="https://github.com/user-attachments/assets/855051e6-4c3e-4a31-8dea-1a6d00199990" />

## Features

* Dynamic mountain biking website
* Newsletter subscription system
* Subscriber data stored in a SQLite database
* Django admin interface for managing subscribers
* Form validation and signup success messaging
* Custom website navigation and page layouts
* Custom branding, typography, and visual styling
* Mountain biking-focused content and imagery

<img width="1000" height="536" alt="sc-eventsslider" src="https://github.com/user-attachments/assets/3dedfccc-36c1-489e-9a38-bbf1ef1a8773" />

## Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **JavaScript**

## Django Functionality

The website uses Django to handle the application's dynamic functionality and newsletter subscription system.

A custom `Subscriber` model stores subscriber email addresses and signup dates. A Django `ModelForm` handles newsletter registration and validation, while the Django admin interface provides tools to search, filter, sort, and manage subscriber records.

The newsletter signup flow connects the front-end form to the Django application, saves validated subscriber information to the SQLite database, and provides feedback to the user after a successful submission.

## Front-End Development

The front end was developed with HTML, CSS, and JavaScript and integrated with the Django application.

## Website Design

The website layout and UI/UX was designed in Figma. The logo was designed in Adobe Illustrator.
