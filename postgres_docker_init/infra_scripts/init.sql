-- Create schema
CREATE SCHEMA IF NOT EXISTS MOVIE_DATA;

-- create and populate tables
create table if not exists MOVIE_DATA.MOVIES
(
    index serial primary key,       
    budget bigint,                  
    genres text,                    
    id  integer unique,             
    keywords text,                  
    original_language varchar(10),  
    original_title varchar(255),    
    overview text,                  
    popularity float,               
    release_date date,              
    revenue bigint,                 
    runtime integer,        
    status varchar(50),          
    title varchar(255),             
    vote_count integer,             
    cast text,                     
    director varchar(255)      
);


COPY MOVIE_DATA.MOVIES (
    index, 
    budget, 
    genres,                    
    id,keywords,                  
    original_language,  
    original_title,    
    overview,                  
    popularity,               
    release_date,              
    revenue,                 
    runtime,        
    status,          
    title,             
    vote_count,             
    cast,                     
    director)
FROM '/data/movies.csv' DELIMITER ',' CSV HEADER;