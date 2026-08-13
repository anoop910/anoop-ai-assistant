# EnquiryManagement

## Project Summary

EnquiryManagement is a Spring Boot MVC web application designed to help educational institutions manage student enquiries from registration to admission. The application provides secure user authentication, enquiry management, dashboard reporting, course management, email notifications, and search functionality through a centralized web interface.

The application follows a layered architecture using Spring Boot, Spring MVC, Spring Data JPA, Thymeleaf, and MySQL. It separates presentation, business logic, and database access into dedicated layers to improve maintainability and scalability.

---

# EnquiryManagement Problem Statement

Educational institutions often manage student enquiries manually using spreadsheets or paper records, making it difficult to track enquiry status, follow up with students, and generate reports.

EnquiryManagement digitizes this process by providing a centralized system where authorized users can register, authenticate, manage student enquiries, update enquiry status, search records, and monitor overall enquiry statistics from a dashboard.

---

# EnquiryManagement Project Objectives

The primary objectives of EnquiryManagement are:

- Digitize the student enquiry management process.
- Reduce manual data management.
- Maintain centralized student records.
- Track enquiry status efficiently.
- Improve communication through email notifications.
- Provide dashboard-based reporting.
- Simplify administration using a web interface.

---

# EnquiryManagement My Responsibilities

## Backend

For the EnquiryManagement backend, I was responsible for:

- Designing the Spring Boot MVC architecture.
- Developing REST and MVC controllers.
- Implementing business logic using service classes.
- Creating JPA entities and repositories.
- Managing student enquiry records.
- Implementing user authentication.
- Integrating JavaMail for email notifications.
- Designing DTOs for request and response handling.
- Connecting the application with MySQL.
- Implementing form validation.

## Frontend

For the EnquiryManagement frontend, I was responsible for:

- Building server-side rendered pages using Thymeleaf.
- Creating enquiry management forms.
- Designing dashboard pages.
- Building login, signup, and account unlock pages.
- Displaying enquiry statistics.
- Implementing responsive user interfaces.

---

# EnquiryManagement Technology Stack

EnquiryManagement is built using the following technologies.

## Backend

- Java
- Spring Boot
- Spring MVC
- Spring Data JPA
- Hibernate
- Spring Validation
- JavaMail
- Maven

## Frontend

- Thymeleaf
- HTML
- CSS
- Bootstrap (if included by the project)

## Database

- MySQL

## Development Tools

- IntelliJ IDEA / VS Code
- Maven
- Git

---

# EnquiryManagement System Architecture

EnquiryManagement follows a layered MVC architecture.

User

↓

Thymeleaf Pages

↓

Spring MVC Controllers

↓

Service Layer

↓

Repository Layer

↓

MySQL Database

Each layer has a dedicated responsibility, making the application easier to maintain and extend.

---

# EnquiryManagement User Workflow

The primary workflow in EnquiryManagement is:

1. User registers an account.
2. Account activation email is sent.
3. User unlocks the account.
4. User logs into the application.
5. Dashboard displays enquiry statistics.
6. User creates student enquiries.
7. User edits or updates enquiry information.
8. User searches enquiries using filters.
9. Dashboard reflects updated information.

---

# EnquiryManagement Major Features

EnquiryManagement provides the following features:

- User Registration
- Account Unlock
- User Login
- Dashboard
- Student Enquiry Management
- Course Management
- Enquiry Status Tracking
- Search and Filter
- Email Notifications
- Form Validation
- CRUD Operations

---

# EnquiryManagement Database Design

The application manages multiple business entities, including:

- User Details
- Student Enquiries
- Courses
- Enquiry Status

Spring Data JPA repositories handle persistence while entities represent database tables.

---

# EnquiryManagement Authentication Workflow

EnquiryManagement authenticates users before allowing access to enquiry management features.

The authentication process includes:

- User registration
- Account activation
- Login validation
- Session management

This ensures only authorized users can access administrative functionality.

---

# EnquiryManagement Email Notification Workflow

EnquiryManagement integrates JavaMail to automate user communication.

Typical email operations include:

- Account activation
- Account unlock
- User notifications

Automating email communication reduces manual administrative work.

---

# EnquiryManagement Major Features Demonstrated

Developing EnquiryManagement demonstrates experience with:

- Spring Boot MVC
- Spring Data JPA
- Hibernate ORM
- Thymeleaf
- JavaMail Integration
- DTO Design
- Layered Architecture
- Repository Pattern
- Service Layer Pattern
- Form Validation
- Authentication
- CRUD Development

---

# EnquiryManagement Challenges Solved

While developing EnquiryManagement, I addressed several engineering challenges:

- Designing a clean layered architecture.
- Managing user authentication.
- Integrating automated email notifications.
- Organizing DTOs and entities.
- Maintaining entity relationships.
- Implementing reusable CRUD operations.
- Building dashboard reporting.
- Implementing enquiry search functionality.

---

# EnquiryManagement What I Learned

Developing EnquiryManagement improved my understanding of:

- Spring Boot MVC architecture.
- Spring Data JPA.
- Hibernate ORM.
- Thymeleaf template engine.
- JavaMail API.
- Repository Pattern.
- Service Layer Pattern.
- DTO-based application design.
- Form validation.
- Authentication workflow.
- CRUD application development.

---

# EnquiryManagement Future Improvements

The following improvements are planned for EnquiryManagement:

- JWT-based authentication.
- Role-based authorization.
- React frontend.
- REST API version.
- Docker deployment.
- Kubernetes deployment.
- Redis caching.
- Audit logging.
- Notification service.
- Cloud deployment.
- Analytics dashboard.

---