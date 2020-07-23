from classes.connection import MyDb

#items table- data insert, data retrieval, data change, findout data, delete data


class Item:
    def __init__(self):
        self.my_db = MyDb()

    def add_item(self, name, types, rate):
        if name == '' or type == '' or rate == '':
            return False
        elif str(name).isalpha()!=True :
            return False
        elif str(type).isalpha()!=True:
            return False
        elif not rate.isdigit():
            return False
        else:
            qry = "INSERT INTO items (name, type, price) VALUES (%s,%s,%s)"
            values = (name, types, rate)
            return self.my_db.iud(qry, values)

    def show_item(self):
        all_items = []
        try:
            qry = "SELECT * FROM items"
            return self.my_db.show_data(qry)

        except Exception as abc:
            print(abc)
            return all_items

    def search_item(self, key):
        all_items = []
        try:
            if key=="":
                return False
            else:
                qry = "SELECT * FROM items WHERE name LIKE '" + key + "%'"
                all_items = self.my_db.show_data(qry)
                return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def update_item(self, row, name, types, rate):
        try:
            if row == "":
                return False
            else:
                qry = "UPDATE items SET name = %s, type = %s, price = %s WHERE id = %s"
                values = (name, types, rate, row)
                self.my_db.iud(qry, values)
                return True
        except Exception as abc:
            print(abc)
            return False

    def delete_item(self,row):
        try:
            if row == "":
                return False
            else:
                qry = "DELETE FROM items WHERE id = %s"
                values = (row)
                self.my_db.iud(qry, values)
                return True
        except Exception as abc:
            print(abc)
            return False
