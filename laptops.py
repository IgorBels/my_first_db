import sqlite3


con = sqlite3.connect('db.sqlite')
cur = con.cursor()

titles_data = [
        (1, 'Vivobook'), #ASUS
        (2, 'Magicbook'), #Honor
        (3, 'ROG Flow'), #ASUS
        (4, 'Aspire 7') #Acer
]

types_data = [
        (1, 'Ультрабук'),
        (2, 'Игровой'),
        (3, 'Трансформер')
]

colors_data = [
        (1, 'Black'),
        (2, 'Silver'),
        (3, 'White')
]

producers_data = [
        (1, 'ASUS'),
        (2, 'Honor'),
        (3, 'Acer')
]

laptots_data = [
        (1, 1, 1, 2, 1),
        (2, 2, 1, 3, 2),
        (3, 3, 3, 1, 1),
        (4, 4, 2, 3, 3)
]

cur.executescript('''
CREATE TABLE IF NOT EXISTS titles(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS types(
    id INTEGER PIMARY KEY,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS colors(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL    
);


CREATE TABLE IF NOT EXISTS producers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS laptops(
    id INTEGER NOT NULL,
    title_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    color_id INTEGER NOT NULL,
    producer_id INTEGER NOT NULL,
    PRIMARY KEY(id, title_id, type_id, color_id, producer_id),
    FOREIGN KEY(title_id) REFERENCES titles(id),
    FOREIGN KEY(type_id) REFERENCES types(id),
    FOREIGN KEY(color_id) REFERENCES colors(id),
    FOREIGN KEY(producer_id) REFERENCES producers(id)
);
''')

cur.executemany('INSERT INTO titles(id, title) VALUES (?, ?)', titles_data)
cur.executemany('INSERT INTO types(id, type) VALUES (?, ?)', types_data)
cur.executemany('INSERT INTO colors(id, name) VALUES (?, ?)', colors_data)
cur.executemany('INSERT INTO producers(id, name) VALUES (?, ?)', producers_data)
cur.executemany('INSERT INTO laptops(id, title_id, type_id, color_id, producer_id) VALUES (?, ?, ?, ?, ?)', laptots_data)

cur.execute('''
SELECT 
    titles.title,
    types.type,
    colors.name,
    producers.name
FROM laptops
JOIN titles ON laptops.title_id = titles.id
JOIN types ON laptops.type_id = types.id
JOIN colors ON laptops.color_id = colors.id
JOIN producers ON laptops.producer_id = producers.id
GROUP BY types.type;
''')

con.commit()
con.close()