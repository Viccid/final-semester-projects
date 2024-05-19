-- Create schema
CREATE SCHEMA IF NOT EXISTS NETFLIX_DATA;

-- create and populate tables
create table if not exists NETFLIX_DATA.NETFLIX
(
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    rating VARCHAR(10),
    ratingLevel VARCHAR(255),
    ratingDescription TEXT,
    release_year INT,
    user_rating_score DECIMAL(5,2),
    user_rating_size INT
);

COPY NETFLIX_DATA.NETFLIX (
    id,
    title,
    rating,
    ratingLevel,
    ratingDescription,
    release_year,
    user_rating_score,
    user_rating_size
    ) 

FROM '/data/netflix.csv' DELIMITER ',' CSV HEADER;