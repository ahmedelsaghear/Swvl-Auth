Swvl_Auth


Prerequisites

    Ubuntu installed
    
Installing

    run scripts/get_dependencies.sh
    and to start the service run run.sh

Built With

    Flask the web framework used
    Sqlite for the database

about design

    there are 4 main models in the service:
    
    1- User
    2- Group is a collection of Users. A User can belong to zero or more Groups
    3- Resource is the target that a user is trying to access
    4- permission is a connection between a Group and a Resource that grants this Group (with
        its Users) the authorization to access that Resource

    design decisions
    1- make a many to many relationship between user and group tables
    2- make a many to many relationship between resource and group tables
    3- build the permission as association table to represent the relation bentween resource and group
