# QwikCash - Marketplace API

This is a Django-based API for a marketplace application. It provides endpoints for managing various types of listings, including items, vehicles, and properties.

## Features

- User authentication using JWT (JSON Web Tokens)
- CRUD operations for item listings
- Endpoints for vehicle and property listings
- Image handling for listings and user profiles
- Customizable user model with phone number validation

## Main Components

1. User Management
   - Custom user model with email as the unique identifier
   - Phone number validation
   - Profile picture handling with automatic resizing

2. Listings
   - Base listing model with common fields
   - Specialized models for items, vehicles, and properties
   - Support for multiple photos per listing

3. Authentication
   - JWT-based authentication
   - Custom token views for obtaining, refreshing, and verifying tokens
   - Secure cookie handling for tokens

4. API Views
   - List views for items, vehicles, and properties
   - Detailed CRUD operations for item listings

## Setup and Installation

[TO BE SHARED SOON!]

## API Endpoints

- `/api/token/`: Obtain JWT tokens
- `/api/token/refresh/`: Refresh JWT tokens
- `/api/token/verify/`: Verify JWT tokens
- `/api/logout/`: Logout and clear token cookies

- `/api/items/`: List all item listings (GET) or create a new item listing (POST)
- `/api/items/<pk>/`: Retrieve, update, or delete a specific item listing

- `/api/vehicles/`: List all vehicle listings
- `/api/properties/`: List all property listings

[Add more endpoints as needed]

## Authentication

This API uses JWT for authentication. To access protected endpoints, include the JWT token in the Authorization header of your requests: