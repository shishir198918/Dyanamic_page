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
        

def insert_data(db,title,description,image):
    conn=connection(db)
    try:
        l1=conn.cursor()
        query=f"""insert into projects
        (title,description,image)values('{title}','{description}',%s)  """
        l1.execute(query,(pg.Binary(image),))
        conn.commit()
    except pg.Error as e:
        conn.rollback()
        print(e)
    finally:
        l1.close()
        conn.close()

def image_data(db,key):
    conn=connection(db)
    try:
        
        query="""select image from projects where id=%s"""
        table=conn.cursor()
        table.execute(query,(key,))
        binary_image=table.fetchone()
        return binary_image[0]
    except pg.Error as e:
        print(e)
    finally:
        table.close()
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


def project_json(db,id):
    conn=connection(db)
    try:
        query="""select json_build_object
        ('title',title,'description','description')
          from projects where id=%s"""
        table=conn.cursor()
        table.execute(query,(id,))
        l1=table.fetchall()
        table.close()
        return l1[0]
    except pg.Error as e:
        print(e)
    finally:
        conn.close()





        





