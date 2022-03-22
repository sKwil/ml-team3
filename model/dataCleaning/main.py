import dbSetup as db

# Install the database (ONLY CALL THIS ONCE)
db.install()

# Load the Cities data
db.loadCities()

# Load the weather data
db.loadWeatherData()

# Create views for easily accessing data
db.createViews()
