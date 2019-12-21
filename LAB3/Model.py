import PostgreSQL_backend


class ModelPostgreSQL(object):
    def __init__(self):
        self._connection = PostgreSQL_backend.connect_to_db()
        self._orm_session = PostgreSQL_backend.connect_to_db_orm()
        self._present_table_type = ''
        self._cursor = self.connection.cursor()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    @property
    def orm_session(self):
        return self._orm_session

    @property
    def present_table_type(self):
        return self._present_table_type

    @present_table_type.setter
    def present_table_type(self,new_present_table_type):
        self._present_table_type = new_present_table_type

    def create_item(self,cortage):
        if self.present_table_type == "Film":
            PostgreSQL_backend.insert_one_orm(self.orm_session,cortage)
        else:
            PostgreSQL_backend.insert_one(self.cursor,self.present_table_type,cortage)

    def read_items(self):
        if self.present_table_type == "Film":
            return PostgreSQL_backend.select_all_orm(self.orm_session)
        else:
            return PostgreSQL_backend.select_all(self.cursor,self.present_table_type)

    def update_item(self, list):
        if self.present_table_type == "Film":
            return PostgreSQL_backend.update_item_orm(self.orm_session,list)
        else:
            return PostgreSQL_backend.update_item(self.cursor, self.present_table_type, list)

    def delete_item(self,pr_key):
        if self.present_table_type == "Film":
            return PostgreSQL_backend.delete_one_orm(self.orm_session,pr_key)
        else:
            return PostgreSQL_backend.delete_one(self.cursor,self.present_table_type,pr_key)

    def delete_all(self):
        if self.present_table_type == "Film":
            return PostgreSQL_backend.delete_all_orm(self.orm_session)
        return PostgreSQL_backend.delete_all(self.cursor,self.present_table_type)

    def disconnect_from_db(self):
        PostgreSQL_backend.disconnect_from_db(self.connection,self.cursor)

