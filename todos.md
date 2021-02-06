# Todos

## Open
- [POKER-3] Add Basic server persistence
  - Pickles should be enough.
- [POKER-2] Make a list of stories available
  - At this point we want 
    - a proper persistence model
    - critically rethink the design decision of using flask 
- [POKER-66] Consider adding tests...
  
## Solved
- [POKER-4] Setup js-linter
  Currently almost disabled. Original setting did not allow
  console usage, which was annoying me to much.
- [POKER-5] Make session survive page reload
  Tough. JWT Token should not be stored in local storage. HTTPOnly Session
  does no survive port change between frontend and backend.
- [POKER-6] Add feature to remove users
- [POKER-7] Add nginx-setup.
  This might solve the session issues.