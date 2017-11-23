from executors.MySQL_Wraper import wraper_read, wraper_write


class POST:
    def __init__(self):
       self.sql_post_read="SELECT * FROM `dbo_post` ORDER BY `dbo_post`.`id` DESC;"

    def get(self):
        return wraper_read(self.sql_post_read)

    def put(self):
        return wraper_write()

    def delete(self):
        return wraper_write()
