import psycopg2 as pg

def connection(db): 
    # connection remains open 
    try:
        conn=pg.connect(dbname=db,
                        port="5432",
                        host="localhost",
                        password="5101",
                        user="postgres")
        #print("connection created ")
        return conn
    except pg.Error as e:
        print(e)
#connection("project")          

def insert_text_data(db,p_id,title,description):
    conn=connection(db)
    try:
        l1=conn.cursor()
        query="""insert into text_data
              values(%s,%s,%s)  """
        l1.execute(query,(p_id,title,description,))
        conn.commit()
    except pg.Error as e:
        conn.rollback()
        print(e)
    finally:
        l1.close()
        conn.close()
#insert_text_data("project","4","title-4","description4 for anything ")
                

def json_data(db):
    #return data as form of json
    conn=connection(db)
    try:
        table=conn.cursor()
        query=""" select json_build_object
        ('id',p_id,'title',title,'description',description) 
        from text_data"""
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
        query1="""update image set pro_image=%s where id=%s"""
        #query="""insert into image values(%s,%s)"""
        table=conn.cursor()
        table.execute(query1,(pg.Binary(image),i,))
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
        
        query="""select pro_image from image where id=%s"""
        table=conn.cursor()
        table.execute(query,(i,))
        binary_image=table.fetchone()
        return binary_image[0]
    except pg.Error as e:
        print(e)
    finally:
        table.close()
        conn.close()        

print(type(image_data('project',2)))
#insert_image("project","test_image/image3.jpg",3)



