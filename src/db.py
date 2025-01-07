import psycopg2 as pg

def connection(db): 
    # connection remains open 
    try:
        conn=pg.connect(dbname=db,
                        port="5432",
                        host="localhost",
                        password="5101",
                        user="portfolio")
        #print("connection created ")
        return conn
    except pg.Error as e:
        print(e)
#connection("project")          

def insert_text_data(db,title,description):
    conn=connection(db)
    try:
        l1=conn.cursor()
        query="""insert into projects(title,description)
              values(%s,%s)  """
        l1.execute(query,(title,description))
        conn.commit()
    except pg.Error as e:
        conn.rollback()
        print(e)
    finally:
        l1.close()
        conn.close()

                

def json_data(db):
    #return data as form of json
    conn=connection(db)
    try:
        table=conn.cursor()
        query=""" select json_build_object
        ('id',id,'title',title,'description',description) 
        from projects"""
        table.execute(query)
        l1=table.fetchall()
        l2=[]
        for index in range(len(l1)):
            l2.append(l1[index][0])

        return l2
    except pg.Error as e:
        print(e)
    finally:
        table.close()
        conn.close()   


def insert_image(db,file_path,i):
    conn=connection(db)
    try:
        file=open(file_path,"rb")
        image=file.read()
        #query1="""update image set pro_image=%s where id=%s"""
        #query="""insert into projects(id,image) values(%s,%s)"""
        table=conn.cursor()
        table.execute(query,(i,pg.Binary(image)))
        conn.commit()
    except pg.Error as e:
        print(e)
        conn.rollback()
    finally:
        table.close()
        conn.close()     

def image_data(db,i):
    conn=connection(db)
    try:
        
        query="""select image from projects where id=%s"""
        table=conn.cursor()
        table.execute(query,(i,))
        binary_image=table.fetchone()
        return binary_image[0]
    except pg.Error as e:
        print(e)
    finally:
        table.close()
        conn.close()        





