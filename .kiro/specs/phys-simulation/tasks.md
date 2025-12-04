# Implementation Plan

- [x] 1. Set up project structure and build configuration
  - [x] 1.1 Initialize project with package.json and dependencies
    - Create package.json with Electron, Webpack, Terser, and electron-builder dependencies
    - Configure npm scripts for dev, build, and package commands
    - _Requirements: 5.1, 5.2_

  - [x] 1.2 Create Webpack configuration for dual bundle output
    - Configure two entry points: engine and client
    - Set up Terser plugin for minification
    - Output `physengine.js` with UMD library format and `physclient.js`
    - _Requirements: 5.1, 5.2, 5.3, 5.4_

  - [x] 1.3 Set up Electron main process and configuration
    - Create `src/main.js` with BrowserWindow setup on port 7300
    - Create `src/preload.js` for secure context bridge
    - Create `electron-builder.yml` for packaging
    - _Requirements: 4.1, 4.2, 4.3, 4.4_

  - [x] 1.4 Create base HTML and CSS files
    - Create `src/renderer/index.html` with canvas and UI container structure
    - Create `src/renderer/styles.css` with base application styles
    - _Requirements: 6.1, 6.2, 6.3_

- [x] 2. Implement Phyeng core math and base classes
  - [x] 2.1 Implement Vector2 math utility class
    - Create `src/engine/math/Vector2.js` with all vector operations
    - Implement add, subtract, multiply, dot, magnitude, normalize, clone methods
    - Write unit tests for Vector2 operations
    - _Requirements: 1.1, 1.3_

  - [x] 2.2 Implement Body base class
    - Create `src/engine/Body.js` with physics properties
    - Implement position, velocity, acceleration, mass, friction, restitution properties
    - Implement applyForce and update methods
    - Write unit tests for Body physics calculations
    - _Requirements: 1.1, 1.3, 1.4, 1.5_

  - [x] 2.3 Implement Rectangle shape class
    - Create `src/engine/shapes/Rectangle.js` extending Body
    - Implement width, height properties and getVertices method
    - Implement getBounds for AABB collision detection
    - Write unit tests for Rectangle
    - _Requirements: 2.6_

  - [x] 2.4 Implement Circle shape class
    - Create `src/engine/shapes/Circle.js` extending Body
    - Implement radius property and getBounds method
    - Write unit tests for Circle
    - _Requirements: 2.6_

- [x] 3. Implement collision detection system
  - [x] 3.1 Implement AABB broad-phase collision detection
    - Create `src/engine/physics/Collision.js`
    - Implement detectAABB method for broad-phase filtering
    - Write unit tests for AABB detection
    - _Requirements: 1.2_

  - [x] 3.2 Implement narrow-phase collision detection
    - Implement detectCircleCircle for circle-circle collisions
    - Implement detectRectRect for rectangle-rectangle collisions
    - Implement detectCircleRect for circle-rectangle collisions
    - Return collision info with normal, depth, and contact point
    - Write unit tests for each collision type
    - _Requirements: 1.2_

- [ ] 4. Implement physics solver
  - [x] 4.1 Implement physics integration
    - Create `src/engine/physics/Solver.js`
    - Implement Velocity Verlet integration for position/velocity updates
    - Implement gravity application
    - Write unit tests for integration accuracy
    - _Requirements: 1.1, 1.3, 1.6_

  - [x] 4.2 Implement collision response
    - Create `src/engine/physics/Response.js`
    - Implement impulse-based collision resolution
    - Apply momentum conservation and restitution
    - Write unit tests for collision response
    - _Requirements: 1.2, 1.4_

  - [x] 4.3 Implement friction handling
    - Add friction force calculations to Solver
    - Apply friction during collision response
    - Write unit tests for friction behavior
    - _Requirements: 1.5_

- [x] 5. Implement World simulation container
  - [x] 5.1 Create World class with body management
    - Create `src/engine/World.js`
    - Implement addBody, removeBody, clear methods
    - Implement getBodyAt for hit testing
    - _Requirements: 2.1, 2.4_

  - [x] 5.2 Implement simulation step loop
    - Implement step method with fixed timestep
    - Integrate physics solver and collision detection
    - Handle static vs dynamic body interactions
    - Write integration tests for World simulation
    - _Requirements: 1.6, 3.1, 3.2_

  - [x] 5.3 Create engine entry point and exports
    - Create `src/engine/index.js`
    - Export Phyeng namespace with World, Body, Rectangle, Circle, Vector2
    - Verify Webpack builds physengine.js correctly
    - _Requirements: 5.1, 5.3_

- [x] 6. Implement canvas renderer
  - [x] 6.1 Create Renderer class
    - Create `src/client/Renderer.js`
    - Implement canvas context setup and clear method
    - Implement resize handling for responsive canvas
    - _Requirements: 6.1, 4.5_

  - [x] 6.2 Implement body rendering
    - Implement drawBody method for rectangles and circles
    - Implement drawSelection for highlighted objects
    - Add hover visual feedback rendering
    - _Requirements: 6.4, 6.5_

- [x] 7. Implement SVG icons
  - [x] 7.1 Create SVG icon definitions
    - Create `src/client/icons/icons.js`
    - Implement playIcon, pauseIcon, resetIcon SVG strings
    - Implement selectIcon, rectangleIcon, circleIcon SVG strings
    - Implement deleteIcon SVG string
    - _Requirements: 6.6, 6.7_

- [x] 8. Implement UI components
  - [x] 8.1 Create Toolbar component
    - Create `src/client/ui/Toolbar.js`
    - Render tool buttons with SVG icons (select, rectangle, circle)
    - Implement tool selection state and callbacks
    - _Requirements: 6.2, 6.6, 6.7_

  - [x] 8.2 Create Controls component
    - Create `src/client/ui/Controls.js`
    - Render play, pause, reset buttons with SVG icons
    - Implement play state visual indication
    - _Requirements: 6.3, 3.5, 6.6, 6.7_

- [x] 9. Implement input handling
  - [x] 9.1 Create InputHandler class
    - Create `src/client/InputHandler.js`
    - Implement screen-to-world coordinate conversion
    - Track selected tool and selected body state
    - _Requirements: 2.1, 2.2_

  - [x] 9.2 Implement object placement
    - Handle mouse click for object creation at position
    - Create objects with default physics properties
    - _Requirements: 2.2, 2.3_

  - [x] 9.3 Implement object selection and dragging
    - Implement click-to-select using World.getBodyAt
    - Implement drag-to-move for selected objects
    - Implement object deletion
    - _Requirements: 2.4, 2.5_

- [x] 10. Implement main application controller
  - [x] 10.1 Create App class
    - Create `src/client/App.js`
    - Initialize World, Renderer, InputHandler, Toolbar, Controls
    - Wire up component callbacks
    - _Requirements: 3.1, 3.2, 3.3_

  - [x] 10.2 Implement simulation loop and controls
    - Implement play method to start requestAnimationFrame loop
    - Implement pause method to stop loop while preserving state
    - Implement reset method to restore initial body positions
    - _Requirements: 3.1, 3.2, 3.3, 3.4_

  - [x] 10.3 Create client entry point
    - Create `src/client/index.js`
    - Initialize App on DOM ready
    - Verify Webpack builds physclient.js correctly
    - _Requirements: 5.1, 5.4_

- [ ] 11. Integration and final wiring
  - [x] 11.1 Integrate engine with client
    - Import Phyeng in client and verify communication
    - Test object creation, simulation, and rendering end-to-end
    - _Requirements: 1.1, 1.2, 2.1, 3.1_

  - [ ] 11.2 Configure Electron for production
    - Verify port 7300 serving works correctly
    - Test window close and process termination
    - Test window resize and canvas adaptation
    - _Requirements: 4.1, 4.2, 4.3, 4.5_

  - [ ] 11.3 Test electron-builder packaging
    - Run electron-builder and verify output
    - Test packaged application launches correctly
    - _Requirements: 4.4_
