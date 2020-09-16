import sqlite3

fileList = ('information.dox','Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt', 'Data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('assiment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName VARCHAR(50) \
        )")
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute('INSERT INTO tbl_file(col_fileName) VALUES (?)',(file,))
            print(file)
        

    
    
    conn.commit()
conn.close()




