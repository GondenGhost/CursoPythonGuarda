import sqlite3
conn = sqlite3.connect("heroes_dragons.db")
cursor = conn.curso()

cursor.execute('''CREATE TABLE IF NOT EXISTS heracs
                (in INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXTO,
                health INTEGER,
                attack INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS dragons
                (in INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXTO,
                health INTEGER,
                attack INTEGER)''')

conn.commit()
conn.close()

class caracter:
    def __init__(selfself,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack

class hero(character):
    def __str__(self):
        return f"hero:{self,name},health: {self.health}, attack: {self.attack}"

class dragon(character):
    def __str__(self):
        return f"dragon:{self.name},health:{self,health}, attack: {self.attack}"

def insert_hero(hero):
    conn = sqlite3.connect("heroes_dragons.db.py")
    cursor = conn.cursor()
    cursor.execute(INSERT INFO heroes (name,health,attack)VALUES(?,?,?)",
    (hero.name,hero.health,hero.attack))
    conn.commit()
    conn.close()

def insert_dragon(gragon):
    conn = sqlite3.connect("heroes_dragons.db.py")
    cursor = conn.cursor()
    cursor.execute("INSERT INFO dragons (name,health, attack) VALUES (?,?,?"),
                    (dragon.name,dragon.health,dragon.attack))

    conn.commit()
    conn.close()

def get_heroes():
    conn = sqlite3.connect("heroes_dragons.db.py")
    cursor = conn.cursor()
    cursor.execute("SELECT . FROM heroes")
    heroes_data = cursor.fetchall()
    conn.close()

    heroes = [hero(*data[1:])for data in heroes_data]
    return heroes

def get_dragons():
        conn = sqlite3.connect("heroes_dragons.db.py")
    cursor = conn.cursor()
    cursor.execute("SELECT . FROM dragons")
    heroes_data = cursor.fetchall()
    conn.close()

    dragon= [hero(*data[1:])for data in dragons_data]
    return dragons

def run_tournament():
    heroes = get_heroes()
    dragon = get_dragons()

    for hero in heroes
        for dragon in dragons:
            if hero.attack > dragon.attack:
                print(f"{hero.name}venceu {dragon.name}!")



