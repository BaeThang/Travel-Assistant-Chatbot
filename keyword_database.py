import sqlite3
import os
from pathlib import Path

class KeywordDatabase:
    def __init__(self, db_path="travel_keywords.db"):
        self.db_path = Path(__file__).parent / db_path
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database with travel keywords"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS travel_keywords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL,
            language TEXT DEFAULT 'en',
            category TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS blocked_keywords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL,
            reason TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS destinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT NOT NULL,
            continent TEXT NOT NULL,
            type TEXT DEFAULT 'city'
        )
        ''')
        
        # Check if data already exists
        cursor.execute("SELECT COUNT(*) FROM travel_keywords")
        if cursor.fetchone()[0] == 0:
            self.populate_initial_data(cursor)
        
        conn.commit()
        conn.close()
    
    def populate_initial_data(self, cursor):
        """Populate database with initial keyword data"""
        
        # Travel keywords (English)
        travel_keywords_en = [
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
            ('hotel', 'en', 'accommodation'),
            ('hostel', 'en', 'accommodation'),
            ('resort', 'en', 'accommodation'),
            ('accommodation', 'en', 'accommodation'),
            ('booking', 'en', 'accommodation'),
            ('attraction', 'en', 'attraction'),
            ('landmark', 'en', 'attraction'),
            ('monument', 'en', 'attraction'),
            ('museum', 'en', 'attraction'),
            ('temple', 'en', 'attraction'),
            ('cathedral', 'en', 'attraction'),
            ('palace', 'en', 'attraction'),
            ('castle', 'en', 'attraction'),
            ('park', 'en', 'attraction'),
            ('beach', 'en', 'attraction'),
            ('mountain', 'en', 'attraction'),
            ('flight', 'en', 'transportation'),
            ('airport', 'en', 'transportation'),
            ('train', 'en', 'transportation'),
            ('bus', 'en', 'transportation'),
            ('taxi', 'en', 'transportation'),
            ('transportation', 'en', 'transportation'),
            ('sightseeing', 'en', 'activity'),
            ('explore', 'en', 'activity'),
            ('tour', 'en', 'activity'),
            ('guide', 'en', 'activity'),
            ('itinerary', 'en', 'activity'),
            ('restaurant', 'en', 'food_culture'),
            ('food', 'en', 'food_culture'),
            ('cuisine', 'en', 'food_culture'),
            ('culture', 'en', 'food_culture'),
            ('visa', 'en', 'practical'),
            ('currency', 'en', 'practical'),
            ('budget', 'en', 'practical'),
            ('weather', 'en', 'practical')
        ]
        
        # Travel keywords (Vietnamese)
        travel_keywords_vi = [
            ('du lịch', 'vi', 'general'),
            ('du lich', 'vi', 'general'),
            ('khách sạn', 'vi', 'accommodation'),
            ('nhà hàng', 'vi', 'food_culture'),
            ('điểm đến', 'vi', 'general'),
            ('thăm quan', 'vi', 'activity'),
            ('tham quan', 'vi', 'activity'),
            ('chùa', 'vi', 'attraction'),
            ('bảo tàng', 'vi', 'attraction'),
            ('biển', 'vi', 'attraction'),
            ('núi', 'vi', 'attraction'),
            ('văn hóa', 'vi', 'food_culture'),
            ('ẩm thực', 'vi', 'food_culture'),
            ('tour', 'vi', 'activity'),
            ('giao thông', 'vi', 'transportation'),
            ('chỗ ở', 'vi', 'accommodation')
        ]
        
        # Blocked keywords
        blocked_keywords = [
            ('movie', 'Entertainment - not travel related'),
            ('film', 'Entertainment - not travel related'),
            ('game', 'Gaming - not travel related'),
            ('sport', 'Sports - not travel related'),
            ('math', 'Education - not travel related'),
            ('science', 'Education - not travel related'),
            ('health', 'Medical - not travel related'),
            ('computer', 'Technology - not travel related'),
            ('business', 'Business - not travel related'),
            ('politics', 'Politics - not travel related'),
            ('recipe', 'Cooking - not travel related'),
            ('music', 'Music - not travel related'),
            ('homework', 'Education - not travel related'),
            ('doctor', 'Medical - not travel related'),
            ('programming', 'Technology - not travel related')
        ]
        
        # Destinations
        destinations = [
            ('Paris', 'France', 'Europe', 'city'),
            ('London', 'United Kingdom', 'Europe', 'city'),
            ('Tokyo', 'Japan', 'Asia', 'city'),
            ('New York', 'United States', 'North America', 'city'),
            ('Bangkok', 'Thailand', 'Asia', 'city'),
            ('Rome', 'Italy', 'Europe', 'city'),
            ('Hanoi', 'Vietnam', 'Asia', 'city'),
            ('Ho Chi Minh City', 'Vietnam', 'Asia', 'city'),
            ('Da Nang', 'Vietnam', 'Asia', 'city'),
            ('Phu Quoc', 'Vietnam', 'Asia', 'city'),
            ('Vietnam', 'Vietnam', 'Asia', 'country'),
            ('Thailand', 'Thailand', 'Asia', 'country'),
            ('Japan', 'Japan', 'Asia', 'country'),
            ('France', 'France', 'Europe', 'country'),
            ('Italy', 'Italy', 'Europe', 'country')
        ]
        
        # Insert data
        cursor.executemany("INSERT INTO travel_keywords (keyword, language, category) VALUES (?, ?, ?)", 
                          travel_keywords_en + travel_keywords_vi)
        cursor.executemany("INSERT INTO blocked_keywords (keyword, reason) VALUES (?, ?)", 
                          blocked_keywords)
        cursor.executemany("INSERT INTO destinations (name, country, continent, type) VALUES (?, ?, ?, ?)", 
                          destinations)
    
    def get_travel_keywords(self):
        """Get all travel keywords"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT keyword FROM travel_keywords")
        keywords = [row[0] for row in cursor.fetchall()]
        conn.close()
        return keywords
    
    def get_blocked_keywords(self):
        """Get all blocked keywords"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT keyword FROM blocked_keywords")
        keywords = [row[0] for row in cursor.fetchall()]
        conn.close()
        return keywords
    
    def get_destinations(self):
        """Get all destination names"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM destinations")
        destinations = [row[0] for row in cursor.fetchall()]
        conn.close()
        return destinations
    
    def add_travel_keyword(self, keyword, language='en', category='general'):
        """Add new travel keyword"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO travel_keywords (keyword, language, category) VALUES (?, ?, ?)",
                      (keyword, language, category))
        conn.commit()
        conn.close()
    
    def add_blocked_keyword(self, keyword, reason=''):
        """Add new blocked keyword"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO blocked_keywords (keyword, reason) VALUES (?, ?)",
                      (keyword, reason))
        conn.commit()
        conn.close()
    
    def remove_keyword(self, keyword, table='travel_keywords'):
        """Remove keyword from specified table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE keyword = ?", (keyword,))
        conn.commit()
        conn.close()
