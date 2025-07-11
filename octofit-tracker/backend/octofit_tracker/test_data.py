# Datos de prueba para Octofit (basado en MonaFit)
# Este archivo contiene datos de ejemplo para poblar la base de datos octofit_db

TEST_USERS = [
    {
        "username": "alice",
        "email": "alice@octofit.com",
        "first_name": "Alice",
        "last_name": "Smith",
        "team": "Red Rockets"
    },
    {
        "username": "bob",
        "email": "bob@octofit.com",
        "first_name": "Bob",
        "last_name": "Johnson",
        "team": "Blue Blazers"
    },
    {
        "username": "carol",
        "email": "carol@octofit.com",
        "first_name": "Carol",
        "last_name": "Williams",
        "team": "Green Giants"
    }
]

TEST_TEAMS = [
    {"name": "Red Rockets", "members": ["alice"]},
    {"name": "Blue Blazers", "members": ["bob"]},
    {"name": "Green Giants", "members": ["carol"]}
]

TEST_ACTIVITIES = [
    {"name": "Running", "description": "Run outdoors or on a treadmill."},
    {"name": "Cycling", "description": "Ride a bike outdoors or stationary."},
    {"name": "Swimming", "description": "Swim laps in the pool."}
]

TEST_WORKOUTS = [
    {"user": "alice", "activity": "Running", "duration": 30, "distance": 5},
    {"user": "bob", "activity": "Cycling", "duration": 45, "distance": 15},
    {"user": "carol", "activity": "Swimming", "duration": 20, "distance": 1}
]

TEST_LEADERBOARD = [
    {"team": "Red Rockets", "points": 100},
    {"team": "Blue Blazers", "points": 80},
    {"team": "Green Giants", "points": 90}
]
