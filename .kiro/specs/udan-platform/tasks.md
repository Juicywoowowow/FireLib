# Implementation Plan

- [x] 1. Project Setup & Docker Infrastructure
  - [x] 1.1 Create project directory structure and initialize package.json files
    - Create root directory structure: `client/`, `server/`, `legacy/`, `docker/`, `database/`
    - Initialize `client/package.json` with Vue.js, TypeScript, Vite, Jest, @vue/vue3-jest dependencies
    - Initialize `server/package.json` with Next.js, Turbopack, TypeScript, Jest, ts-jest dependencies
    - Create `client/jest.config.js` and `server/jest.config.js` with proper configuration
    - _Requirements: 1.1, 1.2, 14.6_

  - [x] 1.2 Create Docker configuration files
    - Write `docker/Dockerfile` with Node.js, PHP, and PostgreSQL setup
    - Write `docker/docker-compose.yml` for container orchestration
    - Configure environment variables for database and API connections
    - _Requirements: 1.1, 1.2, 1.3_

  - [x] 1.3 Create Python3 setup script
    - Write `setup.py` to build and start Docker container
    - Implement options for restart, rebuild, and remove existing container
    - Display local URL on successful setup
    - _Requirements: 1.1, 1.3, 1.4_

  - [x] 1.4 Create database migration for initial schema
    - Write `database/migrations/001_initial_schema.sql` with tables: users, ai_models, conversations, messages, global_api_keys, user_api_keys
    - Include indexes for performance optimization
    - _Requirements: 11.1, 11.2_

- [x] 2. Backend Core Services
  - [x] 2.1 Set up Next.js project with Turbopack
    - Configure `server/next.config.js` with Turbopack
    - Set up TypeScript configuration in `server/tsconfig.json`
    - Create base `server/src/app/layout.tsx`
    - _Requirements: 1.2_

  - [x] 2.2 Implement database service with Jest tests
    - Create `server/src/services/database.service.ts` with PostgreSQL connection pool
    - Implement query helper methods with parameterized queries
    - Add connection error handling and retry logic
    - Create `server/src/services/__tests__/database.service.test.ts` with Jest tests
    - Test connection, query execution, and error handling
    - _Requirements: 11.2, 11.4, 14.1_

  - [x] 2.3 Implement encryption service with Jest tests
    - Create `server/src/services/encryption.service.ts` with AES-256 encryption
    - Implement `encrypt()`, `decrypt()`, and `mask()` methods
    - Create `server/src/services/__tests__/encryption.service.test.ts` with Jest tests
    - Test encrypt/decrypt roundtrip, masking format, edge cases
    - _Requirements: 7.2, 8.3, 14.5_

  - [x] 2.4 Create TypeScript models
    - Create `server/src/models/user.model.ts` with User interface and DB operations
    - Create `server/src/models/ai-model.model.ts` with AIModel interface and CRUD
    - Create `server/src/models/conversation.model.ts` with Conversation interface
    - Create `server/src/models/message.model.ts` with Message interface
    - _Requirements: 11.1_

- [x] 3. Authentication System
  - [x] 3.1 Implement auth service with Jest tests
    - Create `server/src/services/auth.service.ts`
    - Implement `verifyGoogleToken()` using Google OAuth library
    - Implement `createSession()`, `getSession()`, `destroySession()`
    - Implement `isFirstUser()` to check if any admin exists
    - Create `server/src/services/__tests__/auth.service.test.ts` with Jest tests
    - Test token validation, session lifecycle, first-user detection
    - _Requirements: 2.1, 2.2, 2.3, 3.4, 14.1_

  - [x] 3.2 Create auth API routes with Jest tests
    - Create `server/src/app/api/auth/google/route.ts` for OAuth callback
    - Create `server/src/app/api/auth/session/route.ts` for session management
    - Implement first-user admin detection and redirect logic
    - Create `server/src/app/api/__tests__/auth.routes.test.ts` with Jest integration tests
    - Test OAuth flow, session creation, admin redirect
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 14.2_

  - [x] 3.3 Create auth middleware
    - Create `server/src/middleware/auth.middleware.ts` for session validation
    - Create `server/src/middleware/admin.middleware.ts` for admin-only routes
    - _Requirements: 2.3, 4.1_

- [x] 4. AI Provider System
  - [x] 4.1 Create base AI provider interface
    - Create `server/src/providers/base.provider.ts` with AIProvider interface
    - Define `chat()`, `validateApiKey()`, and model listing methods
    - _Requirements: 13.5_

  - [x] 4.2 Implement OpenAI provider with Jest tests
    - Create `server/src/providers/openai.provider.ts`
    - Implement chat completion API integration
    - Add model list (GPT-4, GPT-3.5, etc.)
    - Create `server/src/providers/__tests__/openai.provider.test.ts` with Jest tests
    - Test request formatting, response parsing, error handling
    - _Requirements: 13.1, 14.4_

  - [x] 4.3 Implement Anthropic provider with Jest tests
    - Create `server/src/providers/anthropic.provider.ts`
    - Implement Claude API integration
    - Add model list for Claude variants
    - Create `server/src/providers/__tests__/anthropic.provider.test.ts` with Jest tests
    - Test request formatting, response parsing, error handling
    - _Requirements: 13.2, 14.4_

  - [x] 4.4 Implement Google Gemini provider with Jest tests
    - Create `server/src/providers/gemini.provider.ts`
    - Implement Gemini API integration
    - Add model list for Gemini variants
    - Create `server/src/providers/__tests__/gemini.provider.test.ts` with Jest tests
    - Test request formatting, response parsing, error handling
    - _Requirements: 13.3, 14.4_

  - [x] 4.5 Implement AI service with Jest tests
    - Create `server/src/services/ai.service.ts`
    - Implement `resolveApiKey()` with user key → global key fallback
    - Implement `chat()` method that routes to correct provider
    - Implement `getProvider()` factory method
    - Create `server/src/services/__tests__/ai.service.test.ts` with Jest tests
    - Test key resolution logic, provider routing, error cases
    - _Requirements: 6.2, 7.5, 8.2, 14.1_

- [x] 5. API Key Management Routes with Jest Tests
  - [x] 5.1 Create global API key routes with Jest tests
    - Create `server/src/app/api/keys/global/route.ts`
    - Implement GET (masked keys) and POST (set key) for admin
    - Encrypt keys before storage, mask on retrieval
    - Create `server/src/app/api/__tests__/keys.global.routes.test.ts` with Jest tests
    - Test admin authorization, encryption, masking
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 14.2_

  - [x] 5.2 Create user API key routes with Jest tests
    - Create `server/src/app/api/keys/user/route.ts`
    - Implement GET (user's masked keys), POST (add key), DELETE (remove key)
    - Encrypt keys, associate with user only
    - Create `server/src/app/api/__tests__/keys.user.routes.test.ts` with Jest tests
    - Test user isolation, encryption, CRUD operations
    - _Requirements: 8.1, 8.3, 8.4, 8.5, 14.2_

  - [x] 5.3 Create admin user key oversight routes with Jest tests
    - Create `server/src/app/api/keys/user/overview/route.ts` for listing users with custom keys
    - Create `server/src/app/api/keys/user/[userId]/revoke/route.ts` for revoking access
    - Ensure admin cannot see actual key values
    - Create `server/src/app/api/__tests__/keys.oversight.routes.test.ts` with Jest tests
    - Test admin-only access, key hiding, revocation
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 14.2_

- [x] 6. AI Model & Conversation Routes
  - [x] 6.1 Create AI model CRUD routes
    - Create `server/src/app/api/models/route.ts` for list and create
    - Create `server/src/app/api/models/[id]/route.ts` for get, update, delete
    - Restrict create/update/delete to admin role
    - _Requirements: 4.2, 4.3, 4.4, 4.5, 4.6_

  - [x] 6.2 Create conversation routes
    - Create `server/src/app/api/conversations/route.ts` for list and create
    - Create `server/src/app/api/conversations/[id]/route.ts` for get and delete
    - Filter conversations by authenticated user
    - _Requirements: 5.2, 5.3, 6.4_

  - [x] 6.3 Create chat route
    - Create `server/src/app/api/chat/route.ts`
    - Accept message, resolve API key, call AI provider, store response
    - Handle provider errors gracefully
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [x] 7. Vue.js Frontend Setup
  - [x] 7.1 Initialize Vue.js project with Vite
    - Set up `client/vite.config.ts` with Vue plugin
    - Configure TypeScript in `client/tsconfig.json`
    - Create `client/src/main.ts` entry point
    - Create `client/src/App.vue` root component
    - _Requirements: 10.1_

  - [x] 7.2 Set up Vue Router
    - Create `client/src/router/index.ts` with routes for login, dashboard, chat, admin
    - Implement route guards for authentication
    - _Requirements: 10.3_

  - [x] 7.3 Set up Pinia stores
    - Create `client/src/stores/auth.ts` for user session state
    - Create `client/src/stores/conversations.ts` for conversation list
    - Create `client/src/stores/models.ts` for AI model list
    - _Requirements: 5.1, 5.2_

  - [x] 7.4 Create global styles with JetBrains Mono
    - Create `client/src/styles/main.css` with JetBrains Mono font import
    - Define CSS variables for color palette (dark mode)
    - Set up 8px grid spacing system
    - _Requirements: 10.1, 10.2_

- [ ] 8. Authentication UI Components
  - [ ] 8.1 Create Google login component
    - Create `client/src/components/auth/GoogleLogin.vue`
    - Integrate @react-oauth/google (or vue3-google-login equivalent)
    - Emit success/error events
    - _Requirements: 2.1, 2.2_

  - [ ] 8.2 Create login view
    - Create `client/src/views/LoginView.vue`
    - Display centered Google sign-in button
    - Handle OAuth callback and redirect
    - _Requirements: 2.1, 2.4_

  - [ ] 8.3 Create admin registration view
    - Create `client/src/views/AdminRegisterView.vue`
    - Display form for first-user admin setup
    - Redirect to admin dashboard on completion
    - _Requirements: 3.1, 3.2_

- [ ] 9. Dashboard UI Components
  - [ ] 9.1 Create conversation sidebar component
    - Create `client/src/components/dashboard/ConversationSidebar.vue`
    - Display list of conversations with titles
    - Emit select event on click
    - _Requirements: 5.1, 5.2_

  - [ ] 9.2 Create user dashboard view
    - Create `client/src/components/dashboard/UserDashboard.vue`
    - Include conversation sidebar and main content area
    - Display user settings access
    - _Requirements: 5.1, 5.4_

  - [ ] 9.3 Create admin dashboard view
    - Create `client/src/components/dashboard/AdminDashboard.vue`
    - Include tabs for model management, user key overview, global settings
    - _Requirements: 4.1, 4.6_

  - [ ] 9.4 Create dashboard view with role routing
    - Create `client/src/views/DashboardView.vue`
    - Route to UserDashboard or AdminDashboard based on user role
    - _Requirements: 4.1, 5.1_

- [ ] 10. Chat UI Components
  - [ ] 10.1 Create message list component
    - Create `client/src/components/chat/MessageList.vue`
    - Display messages with user/assistant styling
    - Auto-scroll to latest message
    - _Requirements: 6.3_

  - [ ] 10.2 Create message input component
    - Create `client/src/components/chat/MessageInput.vue`
    - Text input with send button
    - Emit send event, support disabled state
    - _Requirements: 6.1_

  - [ ] 10.3 Create chat window component
    - Create `client/src/components/chat/ChatWindow.vue`
    - Combine MessageList and MessageInput
    - Handle message sending and response display
    - _Requirements: 6.1, 6.3_

  - [ ] 10.4 Create chat view
    - Create `client/src/views/ChatView.vue`
    - Include model selector and ChatWindow
    - Load conversation history
    - _Requirements: 5.3, 6.1_

- [ ] 11. Admin Management Components
  - [ ] 11.1 Create model manager component
    - Create `client/src/components/admin/ModelManager.vue`
    - Display model list with create/edit/delete actions
    - Form for model name, provider, model ID, system prompt
    - _Requirements: 4.2, 4.3, 4.4, 4.5_

  - [ ] 11.2 Create user key overview component
    - Create `client/src/components/admin/UserKeyOverview.vue`
    - Display users with custom keys (provider list, no actual keys)
    - Revoke access button per user
    - _Requirements: 9.1, 9.2, 9.3, 9.5_

  - [ ] 11.3 Create global key settings component
    - Create `client/src/components/admin/GlobalKeySettings.vue`
    - Form for OpenAI, Anthropic, Gemini API keys
    - Display masked values, allow updates
    - _Requirements: 7.1, 7.4_

- [ ] 12. User Settings Components
  - [ ] 12.1 Create user settings component
    - Create `client/src/components/settings/UserSettings.vue`
    - Display and edit user profile (name, avatar)
    - _Requirements: 5.4_

  - [ ] 12.2 Create API key settings component
    - Create `client/src/components/settings/ApiKeySettings.vue`
    - Form for user to add/remove custom API keys
    - Display masked values for existing keys
    - _Requirements: 8.1, 8.4, 8.5_

- [ ] 13. PHP Legacy Support
  - [ ] 13.1 Create PHP legacy handler
    - Create `legacy/api/legacy-handler.php`
    - Set up basic routing for legacy endpoints
    - Connect to PostgreSQL database
    - _Requirements: 12.1, 12.2, 12.4_

  - [ ] 13.2 Configure Docker for PHP
    - Update Dockerfile to include PHP runtime
    - Configure nginx/apache to route legacy requests to PHP
    - _Requirements: 12.1, 12.2_

- [ ] 14. Integration & Polish
  - [ ] 14.1 Wire frontend to backend API
    - Create API client utility in `client/src/api/client.ts`
    - Connect all Vue components to corresponding API routes
    - Handle loading states and errors
    - _Requirements: 6.5, 10.3_

  - [ ] 14.2 Implement responsive design
    - Add mobile breakpoint styles (sidebar collapse < 768px)
    - Test tablet and desktop layouts
    - _Requirements: 10.4_

  - [ ] 14.3 Write integration tests
    - Test auth flow: Google OAuth → session → role assignment
    - Test chat flow: message → provider → storage
    - Test key resolution: user key → global fallback
    - _Requirements: 2.3, 6.2, 7.5, 8.2_

  - [ ] 14.4 Update README with setup instructions
    - Document Docker setup process
    - Document environment variables
    - Document admin setup flow
    - _Requirements: 1.3_
