# WhatToDad

## Overview

WhatToDad is a platform designed to celebrate fatherhood by providing a community for dads to share their experiences, seek advice, and engage in various events. The platform is built using FastAPI for the backend, React for the frontend, and MongoDB as the database. Docker and Docker Compose are used for containerization and orchestration of services.

![WhatToDad Home Page](screenshots/homepage.png)

## Features Overview

- **User Authentication**: Signup and login functionality with JWT-based token authentication.
- **Profile Management**: Users can update their profiles, add profile pictures, and update bio information.
- **Forums**: Users can create, edit, delete forums and add comments.
- **Activities**: Track and participate in activities like celebrations, events, and recent achievements.
- **Chat Rooms**: Users can create, join, and send messages in real-time chat rooms.

## Screenshots

### 1. User Login
![User Login](screenshots/login.png)

### 2. Profile Page
![Profile Page](screenshots/profile_page.png)

### 3. Forum List
![Forum List](screenshots/forum_list.png)

### 4. Chat Room
![Chat Room](screenshots/chat_room.png)

### 5. Celebrations Dashboard
![Celebrations](screenshots/celebrations.png)

## Project Structure

- **backend/**: Contains microservices for forums and activities, authentication and profile management, chat rooms, and celebrations of dadness.
- **frontend/**: Contains the React frontend for the application.
- **docker-compose.yml**: Orchestrates the services using Docker Compose.

## Services and Endpoints

### Forums and Activities Microservice

- **Create Forum**: `POST /forums/`
- **Get Forums**: `GET /forums/`
- **Get Single Forum**: `GET /forums/{id}`
- **Update Forum**: `PUT /forums/{id}`
- **Delete Forum**: `DELETE /forums/{id}`
- **Add Comment to Forum**: `POST /forums/{id}/comments`
- **Create Activity**: `POST /activities/`
- **Get Activities**: `GET /activities/`
- **Get Single Activity**: `GET /activities/{id}`
- **Update Activity**: `PUT /activities/{id}`
- **Delete Activity**: `DELETE /activities/{id}`

### Auth Profile and Admin Microservice

- **Sign Up**: `POST /auth/signup`
- **List Users**: `GET /auth/users`
- **Get Single User**: `GET /auth/users/{id}`
- **Update User**: `PUT /auth/users/{id}`
- **Delete User**: `DELETE /auth/users/{id}`
- **Get Current User**: `GET /auth/users/me`
- **Validate Token**: `GET /auth/validate`
- **Create Profile**: `POST /profiles/`
- **List Profiles**: `GET /profiles/`
- **Get Current User's Profile**: `GET /profiles/me`
- **Update Profile**: `PUT /profiles/me`
- **Update Profile Picture**: `PUT /profiles/me/picture`
- **Delete Profile Picture**: `DELETE /profiles/me/picture`
- **Get Single Profile**: `GET /profiles/{id}`
- **Delete Profile**: `DELETE /profiles/{id}`
- **Get Profile Picture by File ID**: `GET /profiles/me/picture/{file_id}`
- **Admin: Get All Users**: `GET /admin/users`

### Chat Rooms Microservice

- **Create Chat Room**: `POST /chats/`
- **Get All Chat Rooms**: `GET /chats/`
- **Get Single Chat Room**: `GET /chats/{chatroom_id}`
- **Get User's Chat Rooms**: `GET /chats/user/{user_id}`
- **Update Chat Room**: `PUT /chats/{chatroom_id}`
- **Delete Chat Room**: `DELETE /chats/{chatroom_id}`

### Messages Microservice

- **Create Message**: `POST /chats/messages/`
- **Get Single Message**: `GET /chats/messages/{message_id}`
- **Update Message**: `PUT /chats/messages/{message_id}`
- **Delete Message**: `DELETE /chats/messages/{message_id}`
- **Get Messages by Chat Room**: `GET /chats/messages/chatroom/{chatroom_id}`

### Celebrations of Dadness Microservice

- **Create Celebration**: `POST /celebrations/`
- **Get Celebrations**: `GET /celebrations/`
- **Get Recent Achievements**: `GET /celebrations/RecentAchievements/`
- **Create Recent Achievement**: `POST /celebrations/RecentAchievements/`
- **Get Single Recent Achievement**: `GET /celebrations/RecentAchievements/{id}`
- **Update Recent Achievement**: `PUT /celebrations/RecentAchievements/{id}`
- **Delete Recent Achievement**: `DELETE /celebrations/RecentAchievements/{id}`
- **Get Upcoming Events**: `GET /celebrations/UpcomingEvents/`
- **Create Upcoming Event**: `POST /celebrations/UpcomingEvents/`
- **Get Single Upcoming Event**: `GET /celebrations/UpcomingEvents/{id}`
- **Update Upcoming Event**: `PUT /celebrations/UpcomingEvents/{id}`
- **Delete Upcoming Event**: `DELETE /celebrations/UpcomingEvents/{id}`
- **Get Spotlight Dads**: `GET /celebrations/SpotlightDads/`
- **Create Spotlight Dad**: `POST /celebrations/SpotlightDads/`
- **Get Single Spotlight Dad**: `GET /celebrations/SpotlightDads/{id}`
- **Update Spotlight Dad**: `PUT /celebrations/SpotlightDads/{id}`
- **Delete Spotlight Dad**: `DELETE /celebrations/SpotlightDads/{id}`

## Running the Project

1. Ensure Docker is installed on your system.
2. Clone the repository.
3. Build and start all services using Docker Compose:

   ```bash
   docker-compose up --build

### Create the `.env` File

Copy the `.env.template` file to `.env`:

```bash
cp .env.template .env

## Team Members

- **Vincent Joe**: Responsible for the Celebrations of Dadness microservice.
- **Pablo Rivera**: Responsible for the Forums and Activities microservice.
- **Franklin Simpson**: Responsible for the Chat Rooms microservice.
- **Pablo Rivera**: Responsible for the Auth Profile and Admin microservice.
