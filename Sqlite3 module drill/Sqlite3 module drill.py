
import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('db_txtfiles.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtfile TEXT \
        )")
    for fileName in fileList:
        if fileName.endswith('.txt'):
            cur.execute("INSERT INTO tbl_txtfiles(col_txtfile) VALUES (?)", \
                        (fileName,))
    cur.execute("SELECT col_txtfile FROM tbl_txtfiles")
    varFiles = cur.fetchall()
    print(varFiles)
    

        


