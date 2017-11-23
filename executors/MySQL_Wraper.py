import pymysql.cursors

from set import config_db

def wraper_read(sql):
    ''' wraper  read mysql  '''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    finally:
        connection.close()


def wraper_write(sql):
    '''wraper write mysql'''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            cursor.execute(sql)

        connection.commit()
    finally:
        connection.close()



def read_mysql():
    pass


def write_mysql():
    pass
