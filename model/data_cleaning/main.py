import db_setup as db

# Install the database (ONLY CALL THIS ONCE)
db.install()

# Load the Cities data
db.load_cities()

# Load the weather data
db.load_weather_data()

# Create views for easily accessing data
db.create_views()
