# Email Management Web App using Django

This repository contains a web application built with Django that allows users to manage email recipient groups and send emails to those groups.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Email Sending](#email-sending)
  - [Recipient Group Management](#recipient-group-management)
- [Usage](#usage)
- [Code Explanation](#code-explanation)

## Introduction

The "Email Management Web App using Django" project showcases the development of a web application where users can manage recipient groups and send emails to those groups.

## Features

### Email Sending

Users can compose and send emails to recipient groups. They can choose to send emails to specific recipient groups or individual email addresses.

### Recipient Group Management

Users can create, edit, and delete recipient groups. Each group can contain multiple email addresses that the user can manage.

## Usage

1. Ensure that you have the required dependencies installed in your Django environment.
2. Open the terminal and navigate to the project directory.
3. Run the development server using the command: `python manage.py runserver`.
4. Access the web application at `http://localhost:8000`.

## Code Explanation

The provided Django views code demonstrates the functionality of the Email Management Web App. Key aspects include:

- **Email Sending**: Users can send emails to selected recipient groups or individual email addresses. The application uses the Django `send_mail` function to send emails.

- **Recipient Group Management**: Users can create new recipient groups, add email addresses to them, and manage the group's content. The app allows for deleting groups and individual email addresses.

- **User Authentication**: The app checks if the user is authenticated before allowing access to certain views. If the user is not authenticated, they are redirected to the home page.

- **Templates**: The app uses Django templates to render HTML pages and display relevant data to the user.

