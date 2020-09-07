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
    conn.commit()
conn.close()




conn = sqlite3.connect('assiment.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileName From tbl_file WHERE col_fileName = '.txt'")
    varList = cur.fetchall()
    for item in varList:
        List = "File type .txt: {}".format(item[0])

    print(List)
