# Todos

## Open
- [POKER-2] Make a list of stories available
- [POKER-11] Critically rethink the design decision of using flask
    - Does it actually solve more problems than it creates? Websockets are a constant pain to use.
- [POKER-13] Use user roles. 
   - First user becomes admin. Only admin can clear votes and change story. 
- [POKER-12] Provide CVS export for estimated story
- [POKER-9] Configure proper logger class in python  
- [POKER-66] Consider adding tests...
- [POKER-10] New major version of npm available! 6.14.4 → 7.5.3
  
  "Changelog: https://github.com/npm/cli/releases/tag/v7.5.3"
  "Run npm install -g npm to update!"

- [POKER-100] Upgrade to vue.js 3.
  
  _Quote:_ "If you are planning to migrate a non-trivial Vue 2 app, we strongly recommend waiting for the Migration Build for a 
  smoother experience." 2021-07-01
  https://v3.vuejs.org/guide/migration/introduction.html#quickstart  

## Solved
- [POKER-3] Add Basic server persistence
  - A sqlite file stored in the container should be enough. I call the lack of permanent storage a feature. 
- [POKER-4] Setup js-linter
  Currently almost disabled. Original setting did not allow
  console usage, which was annoying me to much.
- [POKER-5] Make session survive page reload
  Tough. JWT Token should not be stored in local storage. HTTPOnly Session
  does no survive port change between frontend and backend.
- [POKER-6] Add feature to remove users
- [POKER-7] Add nginx-setup.
  This might solve the session issues.
- [POKER-8] Setup Logging properly in Docker container
  - Not sure where the server output goes to currently.
  