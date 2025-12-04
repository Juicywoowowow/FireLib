# Implementation Plan

- [x] 1. Project Setup and Build Infrastructure
  - [x] 1.1 Initialize npm project and install dependencies
    - Create package.json with webpack, terser-webpack-plugin, express, typescript
    - Configure tsconfig.json for ES modules output
    - _Requirements: 5.1, 5.2, 5.3, 5.4_

  - [x] 1.2 Configure Webpack build pipeline
    - Create webpack.config.js with Terser plugin for minification
    - Configure tree-shaking and ES module output
    - Set up source map generation
    - Configure output to dist/ folder
    - _Requirements: 5.1, 5.2, 5.3, 5.5_

  - [x] 1.3 Create Express development server
    - Create server.js with Express on port 4596
    - Serve dist/ folder for compiled library and WASM
    - Serve public/ folder for test HTML files
    - _Requirements: 5.1_

  - [x] 1.4 Set up Emscripten/WASM build configuration
    - Create C source directory structure (src/wasm/)
    - Create Makefile or build script for Emscripten compilation
    - Configure WASM output to dist/ folder
    - _Requirements: 4.1, 4.2, 4.3_

- [x] 2. WASM Core Math Module
  - [x] 2.1 Implement C math library for vectors and matrices
    - Write vec2, vec3, vec4 operations in C
    - Write mat4 operations (multiply, inverse, transpose, transforms)
    - Write quaternion operations
    - Compile to WASM with Emscripten
    - _Requirements: 4.1, 4.2, 4.3, 4.5_

  - [x] 2.2 Create WASM memory manager in C
    - Implement custom allocator for typed memory pools
    - Create functions for alloc, free, and memory views
    - Export memory management API to JavaScript
    - _Requirements: 4.2, 4.3_

  - [x] 2.3 Create JavaScript WASM Bridge
    - Implement WASMBridge class to load and instantiate WASM modules
    - Create typed array views into WASM memory
    - Implement copyToWASM/copyFromWASM utilities
    - Add JS fallback detection for browsers without WASM
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5_

  - [x] 2.4 Create JavaScript math wrappers
    - Implement Vector2, Vector3, Matrix4, Quaternion classes
    - Classes delegate calculations to WASM by default
    - Fall back to pure JS if WASM unavailable
    - _Requirements: 4.4_

- [x] 3. Engine Core
  - [x] 3.1 Implement Engine class with initialization
    - Create LJSGL.init(config) entry point
    - Handle canvas setup and WebGL context creation
    - Initialize WASM modules on startup
    - Return engine instance with subsystem access
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

  - [x] 3.2 Implement game loop with timing
    - Create requestAnimationFrame-based loop
    - Calculate delta time for frame-independent updates
    - Implement fixed timestep update option
    - Add pause/resume on tab visibility change
    - Expose FPS and frame time metrics
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [ ] 4. WebGL Renderer
  - [x] 4.1 Implement base Renderer class
    - Create WebGL context wrapper
    - Implement setClearColor, setViewport, clear methods
    - Expose raw GL context via getContext()
    - _Requirements: 2.1, 2.2_

  - [x] 4.2 Implement ShaderProgram class
    - Create shader compilation with error reporting
    - Implement uniform setters for various types
    - Add attribute location caching
    - Report shader errors with line numbers
    - _Requirements: 2.4, 2.5_

  - [x] 4.3 Implement Mesh class
    - Create vertex/index buffer management
    - Implement attribute binding configuration
    - Use WASM memory for buffer data when available
    - _Requirements: 2.1, 4.2_

  - [x] 4.4 Implement Material class
    - Create texture and uniform binding
    - Link materials to shader programs
    - _Requirements: 2.1, 2.4_

  - [x] 4.5 Implement batch renderer
    - Create draw call batching system
    - Minimize WebGL state changes
    - Integrate with WASM for batch data preparation
    - _Requirements: 2.3_

- [ ] 5. Scene Management
  - [ ] 5.1 Implement Scene and SceneManager classes
    - Create scene creation and switching
    - Implement proper resource disposal on scene switch
    - _Requirements: 3.1, 3.4_

  - [ ] 5.2 Implement GameObject class
    - Create hierarchical parent/child relationships
    - Implement component system (add/get/remove)
    - Handle active state and lifecycle
    - _Requirements: 3.1, 3.2_

  - [ ] 5.3 Implement Transform component
    - Create position, rotation, scale properties
    - Implement local and world matrix calculation via WASM
    - Propagate transforms through hierarchy
    - _Requirements: 3.2_

  - [ ] 5.4 Implement scene queries
    - Add findByName, findByTag, findByLayer methods
    - Implement custom predicate queries
    - _Requirements: 3.5_

- [ ] 6. Input System
  - [ ] 6.1 Implement InputManager core
    - Create unified input state tracking
    - Implement action mapping system
    - Add event subscription (on/off)
    - _Requirements: 7.1, 7.2, 7.5_

  - [ ] 6.2 Implement KeyboardHandler
    - Track key down/pressed/released states
    - Handle keydown/keyup events
    - _Requirements: 7.1, 7.2_

  - [ ] 6.3 Implement MouseHandler
    - Track position and delta movement
    - Provide normalized canvas coordinates
    - Implement pointer lock support
    - _Requirements: 7.3_

  - [ ] 6.4 Implement GamepadHandler
    - Detect gamepad connection/disconnection
    - Read axis and button states
    - _Requirements: 7.4_

- [ ] 7. Asset Loading
  - [ ] 7.1 Implement AssetLoader and AssetCache
    - Create Promise-based loading API
    - Implement caching to prevent duplicate loads
    - Add progress callbacks for batch loading
    - _Requirements: 8.1, 8.2, 8.3_

  - [ ] 7.2 Implement texture loading
    - Load images and create WebGL textures
    - Handle load errors with retry option
    - _Requirements: 8.1, 8.4_

  - [ ] 7.3 Implement shader loading
    - Load vertex/fragment shader source files
    - Compile and return ShaderProgram
    - _Requirements: 8.1_

  - [ ] 7.4 Implement asset disposal
    - Release GPU memory on unload
    - Clear cache functionality
    - _Requirements: 8.5_

- [ ] 8. Error Handling
  - [ ] 8.1 Implement custom error classes
    - Create LJSGLError, WebGLError, ShaderError, WASMError, AssetError
    - Add error codes enum
    - _Requirements: 1.3, 2.5, 4.4, 8.4_

- [ ] 9. Testing and Demo
  - [ ] 9.1 Create public/index.html test page
    - Set up HTML with canvas element
    - Import compiled LJSGL from dist/
    - Initialize engine and create simple test scene
    - _Requirements: 1.1, 1.2_

  - [ ] 9.2 Implement simple demo game
    - Create rotating cube with texture
    - Add keyboard/mouse input handling
    - Display FPS counter
    - Verify WASM math is being used
    - _Requirements: 1.1, 2.1, 3.1, 6.5, 7.1_

  - [ ] 9.3 Write unit tests for math module
    - Test Vector2, Vector3, Matrix4, Quaternion operations
    - Verify WASM and JS fallback produce same results
    - _Requirements: 4.4_

  - [ ] 9.4 Write integration tests for engine
    - Test initialization with various configs
    - Test scene creation and object management
    - Test asset loading pipeline
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 3.1_
