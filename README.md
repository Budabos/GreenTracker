## Table Of Content

## Title
## Learning Goals
## Description
## Requirements
## Features
## Project Setup
## Project Guidance
## Planning
## User Stories
    ## Example
## Models and Relationships
## Technologies
## Getting Started
## Prerequisites
## Installation
## Set up the database
## Usage
## Collaborators
## Deploying
## Contributing
## License


## Title
Full-Stack Project: GreenTracker App

## Learning Goals
Build a full-stack project with a React frontend and a Flask backend.
Apply skills learned throughout the program.
Build  a capstone project in Phase .
Develop a high-quality project for your portfolio.

## Description
🌿 Welcome to GreenTracker: Where Sustainability Meets Innovation! 🌱

At GreenTracker, we're not just a platform; we're a thriving community of environmental enthusiasts dedicated to sustainable living and eco-friendly practices. Our passion for sustainability drives us to explore innovative solutions and empower individuals to make a positive impact on the planet.

🌍 Our Mission:
We believe that small actions can lead to significant environmental impact. That's why we're committed to making sustainable living accessible and enjoyable for all. With GreenTracker, you're not just adopting a lifestyle; you're joining a movement towards a greener future.

🛠️ Features for Sustainable Development:

Carbon Footprint Calculations: Calculate your carbon footprint and track your progress towards reducing emissions.
Eco-friendly Product Discovery: Explore a diverse range of eco-friendly products, from household items to clothing and personal care products.
Community Forums: Connect with like-minded individuals, share tips, and inspire others to embrace sustainable practices.
Educational Resources: Access informative articles, guides, and tutorials on sustainable living and environmental conservation.
Green Initiatives: Participate in green initiatives and community projects aimed at creating positive environmental change.
💡 Empowering Eco-Conscious Choices:
We provide the tools and resources you need to make informed and eco-conscious decisions in your daily life. Whether it's choosing sustainable products, reducing waste, or adopting energy-efficient practices, GreenTracker is here to support you every step of the way.

🌱 Join Our Community:
Embark on a journey towards a greener future with GreenTracker. Every action you take counts towards creating a more sustainable world. Join our community today and be a part of the change!

Together, let's make sustainability the new norm and pave the way for a brighter, greener tomorrow. 🌿





## Requirements

Project Requirements
The listed requirements below are guidelines that should help you to determine what the complexity of your project should be. They are not hard and fast rules, and final project approval is up to your leads and SECs, who will be acting as project managers.

Backend
Your project must use a non-trivial Rails backend. Consult the following list for examples of things to include. You do not need to include all of these things, and the final decision of what must be included will be up to your project managers.

[ ] Auth
[ ] Tests
[ ] Multiple hasmanythrough relationships
[ ] Seeds from a complex data set
[ ] Custom routes
[ ] Custom controller/model methods
[ ] Basic database query optimizations
[ ] Background jobs for slow actions
[ ] Sockets or email integration
[ ] One significant refactor
[ ] Validation

Frontend
Your product must use a React based frontend. Consult the following list for examples of things to include. You do not need to include all of these things, and the final decision of what must be included will be up to your project manager (your instructor).

[ ] Auth
[ ] Tests
[ ] Interacting with a complex API
[ ] Redux
[ ] Custom CSS
[ ] One significant refactor


## Features
1. User Authentication: Allow users to create accounts, log in, and manage their profiles securely.
2. The Green Tracker app is designed to:

Calculate Carbon Footprint: It provides a robust carbon footprint calculator to assess users' environmental impact based on lifestyle choices.

Track Sustainable Habits: Users can set and monitor sustainable living goals, such as reducing waste and conserving resources.

Offer Eco-Friendly Shopping Guide: The app includes a comprehensive database of eco-friendly products across various categories to facilitate informed purchasing decisions.

Foster Community Engagement: Users can connect with local sustainability initiatives and events, fostering a sense of community and collaboration.

Provide Educational Resources: The app offers accessible and engaging educational materials on climate change and sustainable practices to empower users with knowledge.

Track Impact: Users can visualize and celebrate their collective impact on the environment, including tracking their carbon footprint and other sustainable actions.
3. 


## Project Setup
The project begin with using the structure described in the "Full-Stack Development" module. The client and server code are segregate.

## Project Guidance
Defining the primary purpose of your Green Tracker app. Break down user stories between MVP-required features and stretch goals.

# Models and Relationships


## Technologies
1. Flask:
Description: Flask is a lightweight and flexible web application framework for Python. Role in Project: Used as the backend framework to create a RESTful API to handle server-side logic and communicate with the database.

2. React:
Description: React is a JavaScript library for building user interfaces, particularly for single-page applications where data can change over time. Role in Project: Used for building the frontend, allowing for the creation of dynamic and responsive user interfaces.

3. Tailwinds:
Description: Tailwind CSS is a utility-first CSS framework that provides a set of pre-built utility classes for rapidly designing and styling the frontend components of React applications. Role in Project: Utilized Tailwind CSS to design and style the frontend components of the Green Tracker app, ensuring a consistent and visually appealing user interface.

4. Figma:
Description: Figma is a collaborative design tool used for creating wireframes, prototypes, and UI designs. Role in Project: Employed for planning and creating wireframes to visualize the layout and design of the Green Tracker app's frontend.

5. Flask-SQLAlchemy:
Description: Flask extension that simplifies database integration with Flask applications using SQLAlchemy, an SQL toolkit and Object-Relational Mapping (ORM) library. Role in Project: Facilitates interaction between the Flask application and the relational database, managing models and relationships.

6. Thunder Client:
Description: Thunder Client is a REST API client extension for Visual Studio Code, simplifying the testing of API endpoints. Role in Project: Potentially used for testing and interacting with the Flask API during development.

7. React Router:
Description: React Router is a standard library for routing in React applications, enabling navigation between different views or components. Role in Project: Used to create and manage different client-side routes, enhancing user navigation within the React frontend.

7. Render:
Description: Render is a platform for deploying and scaling web applications and static websites. Role in Project: Used for deploying both the Flask backend and the React frontend, making the workout app accessible online.

8. Virtualenv:
Description: Virtualenv is a tool for creating isolated Python environments, ensuring dependencies for different projects don't interfere with each other. Role in Project: Used for managing Python dependencies and creating a virtual environment for the Flask application.

## Getting Started
## Prerequisites
## Installation
Clone the repositories: git clone https://github.com/yourusername/GreenTracker_Backend.git &  git clone https://github.com/yourusername/GreenTracker_Frontend.git

Navigate to the project directory: cd GreenTracker_Frontend & GreenTracker_Backend

Create and activate a virtual environment: virtualenv venv source venv/bin/activate # On Windows, use venv\Scripts\activate

## Set up the database
flask db init flask db migrate flask db upgrade

## Usage
Run the Flask application: flask run Open your browser and navigate to http://localhost:5555. Register a new account or log in if you already have one. Explore the app features

## Collaborators
Miriam Maina ("https://github.com/wahitum")
John Mbeba ("https://github.com/jmbeba")
Caroline Opiyo ("https://github.com/Budabos")
Ian Gichane ("https://github.com/IanGichane")
Ashley Rarieya ("https://github.com/ararieya")
Nelson Murithi ("https://github.com/NellieMK65")
Elijah Ngocho  ("https://github.com/ngocho24")


## Deploying

## Contributing
🌿 We welcome contributions from the open-source community to enhance and improve the GreenTracker App! 🌱

If you're passionate about environmental conservation and interested in making a positive impact, we invite you to join us. By contributing to GreenTracker, you'll play a vital role in creating a more sustainable future.

🛠️ How you can contribute:

Review our Contributing Guidelines: Familiarize yourself with our processes and standards to ensure smooth collaboration.
Adhere to our Code of Conduct: Respectful and inclusive interactions are essential to our community.
Check out our project repository: Explore our codebase, submit pull requests, or tackle open issues.
💡 Your contributions matter: Every line of code, documentation improvement, or bug fix helps make the GreenTracker App experience even more exceptional for users worldwide.

Join us in our mission to make a difference. Together, we can create a greener, healthier planet. 🌍


## License

## License (" MIT License")
GreenTracker is an open-source project licensed under the MIT License. This means that you can use, modify, and distribute the project while providing appropriate attribution and adhering to the license terms outlined in the LICENSE file.

At GreenTracker, we are passionate about environmental conservation and are committed to providing tools to track and monitor environmental data. We hope you enjoy your journey through our platform and discover new ways to contribute to a greener and more sustainable world. Thank you for joining us in our mission to protect our planet!























Single-database configuration for Flask.
