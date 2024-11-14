# API Design

## Forums and Activities Microservice

### Create Forum

* **Endpoint path:** /forums/
* **Endpoint URL:** `http://localhost:8001/api/forums_activities/forums/`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "title": "string",
      "description": "string"
    }
    ```
* **Response:** Created forum information
* **Response shape (JSON):**
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string"
    }
    ```

### Get Forums

* **Endpoint path:** /forums/
* **Endpoint URL:** `http://localhost:8001/api/forums_activities/forums/`
* **Endpoint method:** GET
* **Response:** List of forums
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "integer",
        "title": "string",
        "description": "string"
      }
    ]
    ```

### Create Activity

* **Endpoint path:** /activities/
* **Endpoint URL:** `http://localhost:8001/api/forums_activities/activities/`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "name": "string",
      "description": "string",
      "picture_url": "string"
    }
    ```
* **Response:** Created activity information
* **Response shape (JSON):**
    ```json
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "picture_url": "string"
    }
    ```

### Get Activities

* **Endpoint path:** /activities/
* **Endpoint URL:** `http://localhost:8001/api/forums_activities/activities/`
* **Endpoint method:** GET
* **Response:** List of activities
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "description": "string",
        "picture_url": "string"
      }
    ]
    ```

## Auth, Profile, and Admin Microservice

### Sign Up

* **Endpoint path:** /auth/signup
* **Endpoint URL:** `http://localhost:8002/auth/signup`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```
* **Response:** Created user information
* **Response shape (JSON):**
    ```json
    {
      "id": "string",
      "username": "string",
      "email": "string"
    }
    ```

### List Users

* **Endpoint path:** /auth/users
* **Endpoint URL:** `http://localhost:8002/auth/users`
* **Endpoint method:** GET
* **Response:** List of users
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "string",
        "username": "string",
        "email": "string"
      }
    ]
    ```

### Get Single User

* **Endpoint path:** /auth/users/{id}
* **Endpoint URL:** `http://localhost:8002/auth/users/{id}`
* **Endpoint method:** GET
* **Response:** Single user information
* **Response shape (JSON):**
    ```json
    {
      "id": "string",
      "username": "string",
      "email": "string"
    }
    ```

### Update User

* **Endpoint path:** /auth/users/{id}
* **Endpoint URL:** `http://localhost:8002/auth/users/{id}`
* **Endpoint method:** PUT
* **Request shape (JSON):**
    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```
* **Response:** Updated user information
* **Response shape (JSON):**
    ```json
    {
      "id": "string",
      "username": "string",
      "email": "string"
    }
    ```

### Delete User

* **Endpoint path:** /auth/users/{id}
* **Endpoint URL:** `http://localhost:8002/auth/users/{id}`
* **Endpoint method:** DELETE
* **Response:**
    ```json
    {
      "message": "User deleted successfully"
    }
    ```

### Create Profile

* **Endpoint path:** /profiles/
* **Endpoint URL:** `http://localhost:8002/profiles/`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "user_id": "string",
      "bio": "string"
    }
    ```
* **Response:** Created profile information
* **Response shape (JSON):**
    ```json
    {
      "id": "string",
      "user_id": "string",
      "bio": "string"
    }
    ```

### List Profiles

* **Endpoint path:** /profiles/
* **Endpoint URL:** `http://localhost:8002/profiles/`
* **Endpoint method:** GET
* **Response:** List of profiles
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "string",
        "user_id": "string",
        "bio": "string"
      }
    ]
    ```

### Get Single Profile

* **Endpoint path:** /profiles/{id}
* **Endpoint URL:** `http://localhost:8002/profiles/{id}`
* **Endpoint method:** GET
* **Response:** Single profile information
* **Response shape (JSON):**
    ```json
    {
      "id": "string",
      "user_id": "string",
      "bio": "string"
    }
    ```

### Update Profile

* **Endpoint path:** /profiles/{id}
* **Endpoint URL:** `http://localhost:8002/profiles/{id}`
* **Endpoint method:** PUT
* **Request shape (JSON):**
    ```json
    {
      "user_id": "string",
      "bio": "string"
    }
    ```
* **Response:** Updated profile information
* **Response shape (JSON):**
    ```json
    {
      "id": "string",
      "user_id": "string",
      "bio": "string"
    }
    ```

### Delete Profile

* **Endpoint path:** /profiles/{id}
* **Endpoint URL:** `http://localhost:8002/profiles/{id}`
* **Endpoint method:** DELETE
* **Response:**
    ```json
    {
      "message": "Profile deleted successfully"
    }
    ```

### Get All Users (Admin)

* **Endpoint path:** /admin/users
* **Endpoint URL:** `http://localhost:8002/admin/users`
* **Endpoint method:** GET
* **Response:** List of all users
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "string",
        "username": "string",
        "email": "string"
      }
    ]
    ```

## Chat Rooms Microservice

### Create Chat Room

* **Endpoint path:** /chats/chatroom
* **Endpoint URL:** `http://localhost:8003/api/chat_rooms/chats/chatroom`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "name": "string",
      "description": "string"
    }
    ```
* **Response:** Created chat room information
* **Response shape (JSON):**
    ```json
    {
      "id": "integer",
      "name": "string",
      "description": "string"
    }
    ```

### Get Chat Rooms

* **Endpoint path:** /chats/chatrooms
* **Endpoint URL:** `http://localhost:8003/api/chat_rooms/chats/chatrooms`
* **Endpoint method:** GET
* **Response:** List of chat rooms
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "description": "string"
      }
    ]
    ```

### Create Message

* **Endpoint path:** /chats/message
* **Endpoint URL:** `http://localhost:8003/api/chat_rooms/chats/message`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "content": "string",
      "chatroom_id": "integer",
      "profile_picture_url": "string"
    }
    ```
* **Response:** Created message information
* **Response shape (JSON):**
    ```json
    {
      "id": "integer",
      "content": "string",
      "chatroom_id": "integer",
      "profile_picture_url": "string"
    }
    ```

### Get Messages

* **Endpoint path:** /chats/messages
* **Endpoint URL:** `http://localhost:8003/api/chat_rooms/chats/messages`
* **Endpoint method:** GET
* **Query parameters:**
  * chatroom_id: The ID of the chat room
* **Response:** List of messages in a chat room
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "integer",
        "content": "string",
        "chatroom_id": "integer",
        "profile_picture_url": "string"
      }
    ]
    ```

## Celebrations of Dadness Microservice

### Create Celebration

* **Endpoint path:** /celebrations/
* **Endpoint URL:** `http://localhost:8004/api/celebrations_dadness/celebrations/`
* **Endpoint method:** POST
* **Request shape (JSON):**
    ```json
    {
      "title": "string",
      "description": "string",
      "date": "string",
      "picture_url": "string"
    }
    ```
* **Response:** Created celebration information
* **Response shape (JSON):**
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "date": "string",
      "picture_url": "string"
    }
    ```

### Get Celebrations

* **Endpoint path:** /celebrations/
* **Endpoint URL:** `http://localhost:8004/api/celebrations_dadness/celebrations/`
* **Endpoint method:** GET
* **Response:** List of celebrations
* **Response shape (JSON):**
    ```json
    [
      {
        "id": "integer",
        "title": "string",
        "description": "string",
        "date": "string",
        "picture_url": "string"
      }
    ]
    ```

## Authentication Endpoints

### Log In

* **Endpoint path:** /token
* **Endpoint URL:** `http://localhost:8002/api/auth_profile_admin/token`
* **Endpoint method:** POST
* **Request shape (form):**
  * username: string
  * password: string
* **Response:** Account information and a token
* **Response shape (JSON):**
    ```json
    {
      "account": {
        "id": "integer",
        "username": "string",
        "email": "string"
      },
      "token": "string"
    }
    ```

### Log Out

* **Endpoint path:** /token
* **Endpoint URL:** `http://localhost:8002/api/auth_profile_admin/token`
* **Endpoint method:** DELETE
* **Headers:**
  * Authorization: Bearer token
* **Response:** Always true
* **Response shape (JSON):**
    ```json
    true
    ```
