# InfiniStream

## Project Summary

InfiniStream is a full-stack video upload and streaming platform that stores video chunks in Telegram instead of traditional cloud storage. The backend is built with Spring Boot, while the frontend is developed using React. The system supports large file uploads, metadata management, authentication, and progressive video streaming.

---

#  InfiniStream Problem Statement

Large video storage can become expensive when using traditional cloud storage solutions. I wanted to build a system that separates metadata management from binary storage and explore Telegram as an alternative storage provider while maintaining a clean backend architecture.


---

# InfiniStream components and features

## Backend
In the InfiniStream backend, I was responsible for:
- Designed REST APIs using Spring Boot.
- Built chunk-based upload workflow.
- Integrated Telegram Bot API.
- Implemented JWT authentication.
- Managed metadata using SQLite.
- Built upload and streaming services.
- Designed queue-based processing.
- Implemented retry handling.
- Created session management.
- Developed streaming endpoints.

## Frontend
In the InfiniStream frontend, I was responsible for:
- Built the application using React.
- Designed upload interface.
- Implemented video player.
- Connected frontend with backend APIs.
- Managed authentication.
- Displayed upload progress.
- Implemented responsive UI.

---

# InfiniStream Technology Stack
InfiniStream is developed using the following technologies.
## Backend

- Java
- Spring Boot
- Spring Security
- Spring Data JPA
- REST APIs
- WebClient
- Maven

## Frontend

- React
- Axios
- React Router
- HTML
- CSS

## Database
- MySQL
- SQLite
- JPQL

## External Services

- Telegram Bot API

---

# InfiniStream System Architecture
InfiniStream follows a layered architecture where the React frontend communicates with the Spring Boot backend through REST APIs. The backend coordinates upload processing, metadata management, and Telegram integration.

Frontend (React)

↓

REST APIs

↓

Spring Boot Backend

↓

Upload Service

↓

Queue Processing

↓

Telegram Bot API

↓

Mysql Metadata

↓

Streaming Service

↓

Frontend Video Player

---

# InfiniStream Upload Workflow
The upload workflow in InfiniStream follows these steps:

1. User selects a video in the React application.
2. Frontend sends the upload request.
3. Backend creates an upload session.
4. Video is divided into chunks.
5. Chunks are uploaded to Telegram.
6. Telegram file identifiers are stored.
7. Metadata is saved in SQLite.
8. Upload status is returned to the frontend.

---

# InfiniStream Streaming Workflow
The streaming workflow in InfiniStream follows these steps:
1. User opens a video.
2. React requests video data.
3. Backend retrieves metadata.
4. Telegram chunks are downloaded.
5. Chunks are streamed to the client.
6. Video plays without requiring local file storage.

---

# InfiniStream Major Features
The major features implemented in InfiniStream include:
- Large video upload
- Chunk-based processing
- Telegram storage integration
- Video streaming
- Metadata management
- JWT authentication
- REST APIs
- Queue-based upload processing
- Session management
- Retry handling

---

# InfiniStream Challenges Solved
While developing InfiniStream, I solved several engineering challenges:
- Handling large file uploads.
- Managing upload failures.
- Integrating Telegram as storage.
- Tracking upload progress.
- Coordinating asynchronous processing.
- Maintaining metadata consistency.

---

#  What I Learned
Developing InfiniStream strengthened my understanding of:
- Spring Boot architecture
- REST API design
- React integration
- JWT authentication
- Queue-based processing
- External API integration
- Session management
- Backend optimization
- Full-stack application development

---

#  Future Improvements
The following enhancements are planned for InfiniStream to improve scalability, performance, and maintainability:

- Parallel chunk uploads
- Redis caching
- Docker deployment
- Kubernetes support
- AWS deployment
- Monitoring and metrics

---


# InfiniStream Interview Guide

## Project Introduction (30-Second Answer)

When introducing **InfiniStream** during an interview, I describe it as a full-stack video upload and streaming platform built using React and Spring Boot. Instead of storing videos in traditional cloud storage such as AWS S3, InfiniStream uploads video chunks to Telegram using the Telegram Bot API. The backend stores only metadata, including Telegram file identifiers and chunk information, in SQLite. During playback, InfiniStream retrieves the required chunks from Telegram and streams them back to the client.

---



# Why Did You Build InfiniStream?

I built **InfiniStream** to:

- Learn full-stack application development.
- Understand large file upload workflows.
- Work with third-party APIs.
- Improve Spring Boot architecture skills.
- Explore metadata-driven video streaming.
- Gain practical experience with React and backend integration.

---


# Technical Challenges

### Integrating Telegram as Storage

One of the biggest technical challenges in **InfiniStream** was integrating Telegram as the storage backend while keeping metadata synchronized in the local database.

---

### Large Video Uploads

InfiniStream required a reliable upload workflow capable of handling large video uploads efficiently instead of relying on a single HTTP request.

---

### Metadata Management

Since InfiniStream stores videos externally, accurate metadata management is essential to identify and reconstruct videos during streaming.

---

### Frontend and Backend Communication

The InfiniStream frontend and backend required well-defined REST APIs to support uploading, metadata retrieval, and video streaming.

---

# Design Decisions

## Why Spring Boot?

InfiniStream uses Spring Boot because it provides dependency injection, REST API support, modular architecture, and simplifies backend development.

## Why React?

InfiniStream uses React because it enables reusable UI components and efficient communication with backend REST APIs.


## Why Telegram?

InfiniStream uses Telegram as the external storage platform so that metadata management remains separate from binary file storage. the biggest advantage is that it allows for a free of cost alternative to traditional cloud storage while still providing reliable file storage and retrieval.

---



---

# Limitations

The current implementation of **InfiniStream** could be improved by adding:

- Cloud deployment
- Distributed storage
- Monitoring
- Advanced caching
- Load balancing
- Horizontal scalability

These are planned enhancements rather than implemented features.

---


# HR Interview Questions

## Tell me about InfiniStream project.

InfiniStream is a full-stack video upload and streaming application where React is used for the frontend and Spring Boot powers the backend. Instead of storing videos in traditional cloud storage, InfiniStream integrates with the Telegram Bot API for file storage while maintaining metadata in SQLite. The project gave me practical experience in backend engineering, external API integration, and full-stack application development.

---

## Why did you choose InfiniStream project?

I chose to build **InfiniStream** because I wanted a project involving backend architecture, external API integration, metadata management, and full-stack communication rather than a simple CRUD application.

---

# Which part did you enjoy the most?

While developing **InfiniStream**, I enjoyed designing the backend architecture and integrating Telegram because it required understanding how different components communicate and how metadata drives the overall workflow.

---

# What was the biggest challenge?

The biggest challenge in **InfiniStream** was designing a reliable upload workflow while keeping metadata synchronized with an external storage provider.

---

# What would you improve?

Future improvements for **InfiniStream** include Docker deployment, Kubernetes orchestration, Redis caching, monitoring, and cloud infrastructure to make the platform more production-ready.

---
