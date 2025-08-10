-- Database schema for travel chatbot keyword filtering
-- File: travel_keywords.sql

-- Create database
CREATE DATABASE IF NOT EXISTS travel_chatbot;
USE travel_chatbot;

-- Table for allowed travel keywords
CREATE TABLE travel_keywords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    keyword VARCHAR(100) NOT NULL,
    language ENUM('en', 'vi') DEFAULT 'en',
    category VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for blocked non-travel keywords  
CREATE TABLE blocked_keywords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    keyword VARCHAR(100) NOT NULL,
    reason VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert travel keywords (English)
INSERT INTO travel_keywords (keyword, language, category) VALUES
-- General travel terms
('travel', 'en', 'general'),
('tourism', 'en', 'general'),
('tourist', 'en', 'general'),
('visit', 'en', 'general'),
('trip', 'en', 'general'),
('vacation', 'en', 'general'),
('holiday', 'en', 'general'),
('destination', 'en', 'general'),
('journey', 'en', 'general'),
('adventure', 'en', 'general'),

-- Accommodations
('hotel', 'en', 'accommodation'),
('hostel', 'en', 'accommodation'),
('resort', 'en', 'accommodation'),
('accommodation', 'en', 'accommodation'),
('booking', 'en', 'accommodation'),
('reservation', 'en', 'accommodation'),

-- Attractions & Places
('attraction', 'en', 'attraction'),
('landmark', 'en', 'attraction'),
('monument', 'en', 'attraction'),
('museum', 'en', 'attraction'),
('temple', 'en', 'attraction'),
('cathedral', 'en', 'attraction'),
('palace', 'en', 'attraction'),
('castle', 'en', 'attraction'),
('bridge', 'en', 'attraction'),
('park', 'en', 'attraction'),
('beach', 'en', 'attraction'),
('mountain', 'en', 'attraction'),
('lake', 'en', 'attraction'),
('river', 'en', 'attraction'),
('island', 'en', 'attraction'),

-- Transportation
('flight', 'en', 'transportation'),
('airport', 'en', 'transportation'),
('train', 'en', 'transportation'),
('bus', 'en', 'transportation'),
('taxi', 'en', 'transportation'),
('metro', 'en', 'transportation'),
('subway', 'en', 'transportation'),
('transportation', 'en', 'transportation'),

-- Activities
('sightseeing', 'en', 'activity'),
('explore', 'en', 'activity'),
('tour', 'en', 'activity'),
('guide', 'en', 'activity'),
('itinerary', 'en', 'activity'),
('shopping', 'en', 'activity'),
('market', 'en', 'activity'),
('nightlife', 'en', 'activity'),

-- Food & Culture
('restaurant', 'en', 'food_culture'),
('food', 'en', 'food_culture'),
('cuisine', 'en', 'food_culture'),
('local', 'en', 'food_culture'),
('culture', 'en', 'food_culture'),

-- Practical info
('visa', 'en', 'practical'),
('currency', 'en', 'practical'),
('budget', 'en', 'practical'),
('cost', 'en', 'practical'),
('price', 'en', 'practical'),
('weather', 'en', 'practical'),
('climate', 'en', 'practical');

-- Insert travel keywords (Vietnamese)
INSERT INTO travel_keywords (keyword, language, category) VALUES
('du lịch', 'vi', 'general'),
('du lich', 'vi', 'general'),
('khách sạn', 'vi', 'accommodation'),
('nhà hàng', 'vi', 'food_culture'),
('điểm đến', 'vi', 'general'),
('thăm quan', 'vi', 'activity'),
('tham quan', 'vi', 'activity'),
('ăn uống', 'vi', 'food_culture'),
('chùa', 'vi', 'attraction'),
('đền', 'vi', 'attraction'),
('bảo tàng', 'vi', 'attraction'),
('công viên', 'vi', 'attraction'),
('biển', 'vi', 'attraction'),
('núi', 'vi', 'attraction'),
('thành phố', 'vi', 'general'),
('văn hóa', 'vi', 'food_culture'),
('ẩm thực', 'vi', 'food_culture'),
('hướng dẫn', 'vi', 'activity'),
('tour', 'vi', 'activity'),
('lịch trình', 'vi', 'activity'),
('địa điểm', 'vi', 'general'),
('giao thông', 'vi', 'transportation'),
('chỗ ở', 'vi', 'accommodation'),
('chi phí', 'vi', 'practical'),
('giá cả', 'vi', 'practical'),
('visa', 'vi', 'practical');

-- Insert blocked keywords
INSERT INTO blocked_keywords (keyword, reason) VALUES
-- Entertainment
('movie', 'Entertainment - not travel related'),
('film', 'Entertainment - not travel related'),
('cinema', 'Entertainment - not travel related'),
('tv show', 'Entertainment - not travel related'),
('series', 'Entertainment - not travel related'),
('actor', 'Entertainment - not travel related'),
('actress', 'Entertainment - not travel related'),
('game', 'Gaming - not travel related'),
('gaming', 'Gaming - not travel related'),
('video game', 'Gaming - not travel related'),

-- Sports
('sport', 'Sports - not travel related'),
('football', 'Sports - not travel related'),
('basketball', 'Sports - not travel related'),
('soccer', 'Sports - not travel related'),

-- Music
('music', 'Music - not travel related unless concert/festival'),
('song', 'Music - not travel related'),
('album', 'Music - not travel related'),
('band', 'Music - not travel related'),
('singer', 'Music - not travel related'),

-- Education & Science
('math', 'Education - not travel related'),
('mathematics', 'Education - not travel related'),
('calculation', 'Education - not travel related'),
('equation', 'Education - not travel related'),
('formula', 'Education - not travel related'),
('science', 'Education - not travel related'),
('physics', 'Education - not travel related'),
('chemistry', 'Education - not travel related'),
('biology', 'Education - not travel related'),
('homework', 'Education - not travel related'),
('study', 'Education - not travel related unless study abroad'),

-- Health & Medicine
('health', 'Medical - not travel related'),
('disease', 'Medical - not travel related'),
('doctor', 'Medical - not travel related'),
('hospital', 'Medical - not travel related'),
('treatment', 'Medical - not travel related'),
('medicine', 'Medical - not travel related'),

-- Technology
('computer', 'Technology - not travel related'),
('software', 'Technology - not travel related'),
('programming', 'Technology - not travel related'),
('coding', 'Technology - not travel related'),
('technology', 'Technology - not travel related'),

-- Business & Finance
('business', 'Business - not travel related'),
('stock', 'Finance - not travel related'),
('investment', 'Finance - not travel related'),
('finance', 'Finance - not travel related'),

-- Politics & News
('politics', 'Politics - not travel related'),
('government', 'Politics - not travel related'),
('election', 'Politics - not travel related'),
('president', 'Politics - not travel related'),
('news', 'News - not travel related unless travel news'),

-- Cooking (non-travel context)
('recipe', 'Cooking - not travel related unless local cuisine'),
('cooking', 'Cooking - not travel related unless local cuisine'),
('baking', 'Cooking - not travel related unless local cuisine');

-- Insert famous travel destinations
CREATE TABLE destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    continent VARCHAR(50) NOT NULL,
    type ENUM('city', 'country', 'region', 'landmark') DEFAULT 'city'
);

INSERT INTO destinations (name, country, continent, type) VALUES
-- Major cities
('Paris', 'France', 'Europe', 'city'),
('London', 'United Kingdom', 'Europe', 'city'),
('Tokyo', 'Japan', 'Asia', 'city'),
('New York', 'United States', 'North America', 'city'),
('Bangkok', 'Thailand', 'Asia', 'city'),
('Singapore', 'Singapore', 'Asia', 'city'),
('Rome', 'Italy', 'Europe', 'city'),
('Berlin', 'Germany', 'Europe', 'city'),
('Sydney', 'Australia', 'Oceania', 'city'),
('Dubai', 'United Arab Emirates', 'Asia', 'city'),
('Barcelona', 'Spain', 'Europe', 'city'),
('Amsterdam', 'Netherlands', 'Europe', 'city'),
('Vienna', 'Austria', 'Europe', 'city'),
('Prague', 'Czech Republic', 'Europe', 'city'),
('Budapest', 'Hungary', 'Europe', 'city'),
('Istanbul', 'Turkey', 'Asia', 'city'),
('Moscow', 'Russia', 'Europe', 'city'),
('Beijing', 'China', 'Asia', 'city'),
('Seoul', 'South Korea', 'Asia', 'city'),

-- Vietnam destinations
('Hanoi', 'Vietnam', 'Asia', 'city'),
('Ho Chi Minh City', 'Vietnam', 'Asia', 'city'),
('Da Nang', 'Vietnam', 'Asia', 'city'),
('Phu Quoc', 'Vietnam', 'Asia', 'city'),
('Dalat', 'Vietnam', 'Asia', 'city'),
('Nha Trang', 'Vietnam', 'Asia', 'city'),
('Hoi An', 'Vietnam', 'Asia', 'city'),
('Hue', 'Vietnam', 'Asia', 'city'),
('Sapa', 'Vietnam', 'Asia', 'city'),

-- Countries
('Vietnam', 'Vietnam', 'Asia', 'country'),
('Thailand', 'Thailand', 'Asia', 'country'),
('Japan', 'Japan', 'Asia', 'country'),
('France', 'France', 'Europe', 'country'),
('Italy', 'Italy', 'Europe', 'country'),
('Spain', 'Spain', 'Europe', 'country'),
('Greece', 'Greece', 'Europe', 'country'),
('Turkey', 'Turkey', 'Asia', 'country'),
('Egypt', 'Egypt', 'Africa', 'country'),
('India', 'India', 'Asia', 'country'),
('China', 'China', 'Asia', 'country'),
('South Korea', 'South Korea', 'Asia', 'country'),
('Malaysia', 'Malaysia', 'Asia', 'country'),
('Indonesia', 'Indonesia', 'Asia', 'country'),
('Philippines', 'Philippines', 'Asia', 'country'),
('Cambodia', 'Cambodia', 'Asia', 'country');

-- Create indexes for better performance
CREATE INDEX idx_travel_keywords_keyword ON travel_keywords(keyword);
CREATE INDEX idx_blocked_keywords_keyword ON blocked_keywords(keyword);
CREATE INDEX idx_destinations_name ON destinations(name);

-- Views for easy querying
CREATE VIEW all_travel_terms AS
SELECT keyword FROM travel_keywords
UNION
SELECT name FROM destinations;

CREATE VIEW blocked_terms AS
SELECT keyword FROM blocked_keywords;
