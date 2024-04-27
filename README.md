# canteen_management_app

## Overview
The Canteen Management App is a web-based application designed to streamline the management of canteen operations in various settings, such as schools, offices, and institutions. It provides a user-friendly interface for managing menu items, processing orders, handling payments, and generating reports.

## Features
- **User Authentication:** Secure login system for administrators and users.
- **Menu Management:** Easy management of menu items, including adding, editing, and deleting items.
- **Order Processing:** Efficient processing of customer orders, with real-time updates on order status.
- **Payment Integration:** Seamless integration with payment gateways to facilitate online transactions.

## Technologies Used
- **Backend:** Python with Django framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (for development), PostgreSQL (for production)
- **Payment Integration:** Razorpay API
- **Version Control:** Git
- **Deployment:** Heroku

## Installation
1. Clone the repository: `git clone https://github.com/your-username/canteen-management-app.git`
2. Navigate to the project directory: `cd canteen-management-app`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Usage
1. Access the admin dashboard by navigating to `/admin` and logging in with admin credentials.
2. Manage menu items, view orders, and generate reports from the admin dashboard.
3. Users can place orders by selecting items from the menu and completing the checkout process.


## Authors
- Prajakta Chorge
- Tanishka Kasliwal

## Acknowledgments
- Special thanks to [Razorpay](https://razorpay.com) for their payment integration API.
- Inspired by similar projects such as [FooCafeteria](https://github.com/example/foo-cafeteria) and [BarCanteen](https://github.com/example/bar-canteen).
