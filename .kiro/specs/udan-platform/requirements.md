# Requirements Document

## Introduction

Udan is an open-source, self-hosted AI agent deployment platform that runs locally via Docker. It allows users to deploy and interact with AI agents using their own API keys from any provider. The platform features a modern, slick UI built with Vue.js for the client-side and Next.js with Turbopack for the backend. It uses PostgreSQL for data persistence and supports Google OAuth for authentication. The system has two user roles: Admin (first registered user) and regular Users, each with distinct dashboards and capabilities.

## Tech Stack

- **Frontend**: Vue.js (.vue files), HTML, CSS, TypeScript
- **Backend**: Next.js with Turbopack, React, TypeScript
- **Legacy**: PHP for legacy parts
- **Database**: PostgreSQL
- **Authentication**: @react-oauth/google
- **Deployment**: Docker (Python3 setup script)
- **UI Font**: JetBrains Mono

---

## Requirements

### Requirement 1: Docker-Based Local Deployment

**User Story:** As a developer, I want to deploy Udan locally using Docker with a single Python3 script, so that I can quickly set up the platform without complex configuration.

#### Acceptance Criteria

1. WHEN the user runs the Python3 setup script THEN the system SHALL create a Docker container with all required dependencies installed.
2. WHEN the Docker container starts THEN the system SHALL initialize the PostgreSQL database with the required schema.
3. WHEN the setup completes THEN the system SHALL display the local URL where Udan is accessible.
4. IF the Docker container already exists THEN the system SHALL offer options to restart, rebuild, or remove it.

---

### Requirement 2: Google OAuth Authentication

**User Story:** As a user, I want to sign up and log in using my Google account, so that I can securely access the platform without creating a new password.

#### Acceptance Criteria

1. WHEN a user visits the login page THEN the system SHALL display a "Sign in with Google" button using @react-oauth/google.
2. WHEN a user clicks the Google sign-in button THEN the system SHALL redirect to Google's OAuth flow.
3. WHEN Google authentication succeeds THEN the system SHALL create or retrieve the user account and establish a session.
4. IF Google authentication fails THEN the system SHALL display an appropriate error message.

---

### Requirement 3: First User Admin Registration

**User Story:** As the first user to register, I want to be automatically designated as an admin, so that I can configure and manage the platform.

#### Acceptance Criteria

1. WHEN the first user completes Google OAuth THEN the system SHALL redirect them to an admin registration page.
2. WHEN the first user completes admin registration THEN the system SHALL assign them the "admin" role.
3. WHEN subsequent users register THEN the system SHALL assign them the "user" role by default.
4. IF no admin exists in the database THEN the system SHALL treat the next registering user as the first user.

---

### Requirement 4: Admin Dashboard & AI Model Management

**User Story:** As an admin, I want to manage AI models and their configurations, so that I can control which AI agents are available to users.

#### Acceptance Criteria

1. WHEN an admin logs in THEN the system SHALL display the admin dashboard with AI model management options.
2. WHEN an admin creates a new AI model THEN the system SHALL allow them to specify: name, provider, model ID, and system prompt.
3. WHEN an admin edits an AI model THEN the system SHALL allow modification of the model's name, prompt, and configuration.
4. WHEN an admin deletes an AI model THEN the system SHALL remove it and all associated conversations.
5. WHEN an admin renames an AI model THEN the system SHALL update the name across all references.
6. WHEN viewing the admin dashboard THEN the system SHALL display a list of all configured AI models with their status.

---

### Requirement 5: User Dashboard & Conversations

**User Story:** As a regular user, I want to view my conversations and settings, so that I can interact with AI agents and manage my account.

#### Acceptance Criteria

1. WHEN a user logs in THEN the system SHALL display the user dashboard with a conversations sidebar.
2. WHEN a user views the dashboard THEN the system SHALL show a list of their previous conversations.
3. WHEN a user clicks on a conversation THEN the system SHALL load and display the conversation history.
4. WHEN a user accesses settings THEN the system SHALL allow them to update their profile and preferences.

---

### Requirement 6: AI Agent Interaction

**User Story:** As a user, I want to chat with AI agents, so that I can get assistance and have conversations with configured AI models.

#### Acceptance Criteria

1. WHEN a user selects an AI agent THEN the system SHALL open a chat interface for that agent.
2. WHEN a user sends a message THEN the system SHALL forward it to the configured AI provider with the appropriate API key.
3. WHEN the AI responds THEN the system SHALL display the response in the chat interface.
4. WHEN a conversation occurs THEN the system SHALL persist all messages to the PostgreSQL database.
5. IF the API call fails THEN the system SHALL display an error message and allow retry.

---

### Requirement 7: API Key Management (Global & User Keys)

**User Story:** As an admin, I want to configure global API keys for AI providers, so that users can use the platform without their own keys.

#### Acceptance Criteria

1. WHEN an admin configures global API keys THEN the system SHALL support OpenAI, Anthropic, and Google Gemini providers.
2. WHEN storing API keys THEN the system SHALL encrypt them before saving to the database.
3. WHEN making API calls THEN the system SHALL decrypt and use the appropriate API key.
4. WHEN an admin views global API keys THEN the system SHALL display them in a masked format.
5. WHEN no user custom key exists THEN the system SHALL fall back to the global admin-configured key.

---

### Requirement 8: User Custom API Keys

**User Story:** As a user, I want to use my own API keys for AI providers, so that I can have independent usage and billing.

#### Acceptance Criteria

1. WHEN a user accesses their settings THEN the system SHALL allow them to add custom API keys for OpenAI, Anthropic, or Google Gemini.
2. WHEN a user has a custom API key configured THEN the system SHALL use that key instead of the global key for their requests.
3. WHEN storing user API keys THEN the system SHALL encrypt them and associate them only with that user.
4. WHEN a user views their own API keys THEN the system SHALL display them in a masked format.
5. IF a user removes their custom API key THEN the system SHALL revert to using the global key for that provider.

---

### Requirement 9: Admin User Key Oversight

**User Story:** As an admin, I want to see which users have custom API keys and revoke their access if needed, so that I can maintain platform security and privacy compliance.

#### Acceptance Criteria

1. WHEN an admin views the admin dashboard THEN the system SHALL display a list of users who have custom API keys configured.
2. WHEN viewing users with custom keys THEN the system SHALL NOT display the actual API key values (privacy protection).
3. WHEN an admin revokes a user's custom key access THEN the system SHALL delete the user's custom API keys.
4. WHEN a user's custom key access is revoked THEN the system SHALL notify the user and revert them to global keys.
5. WHEN displaying user key status THEN the system SHALL show which providers each user has custom keys for (without revealing the keys).

---

### Requirement 10: Modern UI/UX Design

**User Story:** As a user, I want a clean, modern interface similar to Next.js styling with JetBrains font, so that I have a pleasant user experience.

#### Acceptance Criteria

1. WHEN the application loads THEN the system SHALL apply JetBrains Mono font throughout the interface.
2. WHEN displaying the UI THEN the system SHALL use a clean, minimalist design consistent with Next.js aesthetics.
3. WHEN navigating the application THEN the system SHALL provide smooth transitions and responsive layouts.
4. WHEN viewing on different screen sizes THEN the system SHALL adapt the layout responsively.

---

### Requirement 11: Database Schema & Persistence

**User Story:** As a system administrator, I want data persisted in PostgreSQL, so that user data, conversations, and configurations are reliably stored.

#### Acceptance Criteria

1. WHEN the system initializes THEN the system SHALL create tables for users, conversations, messages, and AI models.
2. WHEN data is created or modified THEN the system SHALL persist changes to PostgreSQL immediately.
3. WHEN the Docker container restarts THEN the system SHALL retain all previously stored data.
4. WHEN querying data THEN the system SHALL use efficient indexed queries for performance.


---

### Requirement 12: PHP Legacy Compatibility

**User Story:** As a system maintainer, I want the platform to support legacy PHP components, so that existing integrations continue to work during migration.

#### Acceptance Criteria

1. WHEN the Docker container builds THEN the system SHALL include PHP runtime for legacy component support.
2. WHEN legacy PHP endpoints are called THEN the system SHALL route requests to the PHP handlers.
3. WHEN new features are developed THEN the system SHALL use the modern stack (Vue/Next.js/TypeScript) instead of PHP.
4. IF a legacy PHP component fails THEN the system SHALL log the error without affecting the main application.

---

### Requirement 13: Supported AI Providers

**User Story:** As a user, I want to use AI agents from multiple providers, so that I can choose the best model for my needs.

#### Acceptance Criteria

1. WHEN configuring an AI model THEN the system SHALL support OpenAI models (GPT-4, GPT-3.5, etc.).
2. WHEN configuring an AI model THEN the system SHALL support Anthropic models (Claude).
3. WHEN configuring an AI model THEN the system SHALL support Google Gemini models.
4. WHEN selecting a provider THEN the system SHALL display available models for that provider.
5. WHEN adding a new provider in the future THEN the system SHALL have an extensible architecture to accommodate it.

---

### Requirement 14: Mandatory Jest Testing

**User Story:** As a developer, I want all code to be covered by Jest tests, so that the codebase remains reliable and regressions are caught early.

#### Acceptance Criteria

1. WHEN any backend service is implemented THEN the system SHALL have corresponding Jest unit tests.
2. WHEN any API route is implemented THEN the system SHALL have Jest integration tests covering success and error cases.
3. WHEN any Vue component is implemented THEN the system SHALL have Jest component tests using Vue Test Utils.
4. WHEN any AI provider is implemented THEN the system SHALL have Jest tests for request formatting and response parsing.
5. WHEN the encryption service is implemented THEN the system SHALL have Jest tests for encrypt/decrypt roundtrip and masking.
6. WHEN running the test suite THEN the system SHALL use Jest as the test framework for both client and server.
7. WHEN code is committed THEN the system SHALL require all Jest tests to pass (enforced via CI/pre-commit hooks).
8. WHEN new features are added THEN the system SHALL require tests to be written before or alongside the implementation (TDD encouraged).
