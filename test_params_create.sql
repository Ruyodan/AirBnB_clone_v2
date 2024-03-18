-- Step 1: Create new states
INSERT INTO State (name) VALUES ('California'), ('Arizona');

-- Step 2: Retrieve all states
SELECT * FROM State;

-- Step 3: Create a new place
INSERT INTO Place (city_id, user_id, name, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude)
VALUES ('0001', '0001', 'My_little_house', 4, 2, 10, 300, 37.773972, -122.431297);

-- Step 4: Retrieve all places
SELECT * FROM Place;
