from executors.MySQL_Wraper import wraper_read, wraper_write


class POSTS:
    def __init__(self, search=None):
        self.search = search

        self.sql_post_read = "SELECT * FROM `dbo_post` ORDER BY `dbo_post`.`id` DESC;"
        self.sql_post_search = "SELECT * FROM `dbo_post` ORDER BY `dbo_post`.`id` DESC;"


    def get(self):
        return wraper_read(self.sql_post_read)

    def put(self):
        return wraper_write()

    def delete(self):
        return wraper_write()

    def search_text(self):
        print(self.search)
        return wraper_read(self.sql_post_search)