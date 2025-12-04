# Requirements Document

## Introduction

Phys is a web-based physics simulation application built with Electron. It features a custom physics engine called "Phyeng" written in pure JavaScript from scratch. The application allows users to create, place, and simulate physics objects in a 2D environment. The codebase is compiled using Webpack with the Terser plugin, outputting two files: `physengine.js` (the core engine) and `physclient.js` (the application client). The app runs on port 7300 and is packaged using electron-builder.

## Requirements

### Requirement 1: Physics Engine Core (Phyeng)

**User Story:** As a user, I want a reliable physics engine that accurately simulates real-world physics, so that I can observe realistic object behavior.

#### Acceptance Criteria

1. WHEN the simulation is running THEN the engine SHALL calculate and apply gravity to all objects each frame
2. WHEN two objects collide THEN the engine SHALL detect the collision and calculate appropriate response forces
3. WHEN an object has velocity THEN the engine SHALL update the object's position based on velocity and delta time
4. WHEN objects collide THEN the engine SHALL apply momentum conservation principles
5. IF an object is at rest on a surface THEN the engine SHALL apply friction forces when external forces act on it
6. WHEN the simulation runs THEN the engine SHALL maintain a consistent physics timestep for deterministic behavior

### Requirement 2: Object Management

**User Story:** As a user, I want to place and manage various physics objects in the simulation, so that I can create different scenarios.

#### Acceptance Criteria

1. WHEN the user selects a block/object type THEN the system SHALL allow placement in the simulation area
2. WHEN the user clicks on the simulation area THEN the system SHALL create the selected object at that position
3. WHEN an object is placed THEN the system SHALL assign default physics properties (mass, friction, restitution)
4. WHEN the user selects an existing object THEN the system SHALL allow deletion of that object
5. IF the user drags an object THEN the system SHALL update the object's position in real-time
6. WHEN objects are placed THEN the system SHALL support at minimum: rectangles/blocks and circles

### Requirement 3: Simulation Controls

**User Story:** As a user, I want to control the simulation playback, so that I can start, stop, and observe physics interactions.

#### Acceptance Criteria

1. WHEN the user presses the play button THEN the simulation SHALL start running the physics calculations
2. WHEN the user presses the pause button THEN the simulation SHALL freeze all physics calculations while preserving state
3. WHEN the user presses the stop/reset button THEN the simulation SHALL return all objects to their initial positions
4. WHEN the simulation is paused THEN the user SHALL still be able to place and manipulate objects
5. IF the simulation is running THEN the play button SHALL visually indicate the active state

### Requirement 4: Electron Application Shell

**User Story:** As a user, I want a desktop application experience, so that I can run the simulation as a standalone app.

#### Acceptance Criteria

1. WHEN the application starts THEN Electron SHALL load the physics simulation interface
2. WHEN the application runs THEN it SHALL serve content on port 7300
3. WHEN the user closes the window THEN the application SHALL properly terminate all processes
4. WHEN packaged THEN electron-builder SHALL create distributable application bundles
5. IF the application window is resized THEN the simulation canvas SHALL adapt to the new dimensions

### Requirement 5: Build System

**User Story:** As a developer, I want a proper build system, so that the code is optimized and organized for production.

#### Acceptance Criteria

1. WHEN the build runs THEN Webpack SHALL compile the source into two separate files: `physengine.js` and `physclient.js`
2. WHEN building for production THEN the Terser plugin SHALL minify the output files
3. WHEN the engine code changes THEN only `physengine.js` SHALL need recompilation
4. WHEN the client code changes THEN only `physclient.js` SHALL need recompilation
5. IF source maps are enabled THEN Webpack SHALL generate corresponding map files for debugging

### Requirement 6: User Interface

**User Story:** As a user, I want an intuitive interface, so that I can easily interact with the simulation.

#### Acceptance Criteria

1. WHEN the application loads THEN the system SHALL display a canvas area for the simulation
2. WHEN the application loads THEN the system SHALL display a toolbar with object selection options
3. WHEN the application loads THEN the system SHALL display playback controls (play, pause, reset)
4. WHEN hovering over an object in the simulation THEN the system SHALL provide visual feedback
5. IF an object is selected THEN the system SHALL visually highlight the selected object
6. WHEN displaying icons THEN the system SHALL use custom SVG icons (no emojis or icon fonts)
7. WHEN the toolbar renders THEN all tool and control icons SHALL be inline SVG elements for crisp rendering
