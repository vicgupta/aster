# Pocketbase ORM

import os, uuid, json, re, datetime, requests, random
from pocketbase import PocketBase
from pocketbase.client import FileUpload

class PocketbaseORM():
    def __init__(self, pb_url, pb_useremail='', pb_userpassword='', pb_collection=''):
        self.pb = PocketBase(pb_url)
        self.userpassword = pb_userpassword
        self.useremail = pb_useremail
        self.auth = self.pb.collection("users").auth_with_password(self.useremail, self.userpassword)
        self.collection = pb_collection
    
    def update_item(self, record_id, item):
        try:
            result = self.pb.collection(self.collection).update(record_id, item)
        except:
            result = ""
        return result
    
    def add_item (self, input_json):
        try:
            # print (input_json)
            result = self.pb.collection(self.collection).create(input_json)
        except:
            result = "Error"
        return result

    def add_items (self, input_json):
        try:
            result = []
            # print (input_json)
            for item in input_json:
                # response = self.add_item(json.loads(item))
                response = self.pb.collection(self.collection).create(item)
                # response = self.pb.collection(self.collection).create(json.loads(item))
                result.append(response)
        except:
            result = ["Error"]
        return result

    def get_items(self, perPage=10, sort_by="-created"):
        try:
            rows = self.pb.collection(self.collection).get_list(
                1, f'{perPage}', {'sort': sort_by}
            )
        except:
            print ("error")
            rows = []
        return rows.items
    
    def get_items_with_filter_exact(self, column_name = "", column_value = "", perPage=10, sort_by="-created"):
        try:
            rows = self.pb.collection(self.collection).get_list(
                1, f'{perPage}',
                #{"filter": "article_keyword~'" + article_value + "'"}
                {
                    "filter": column_name + "='"+column_value+"'",
                    "sort": sort_by
                 }
            )
        except:
            rows = []
        return rows.items

    def get_items_with_filter(self, column_name = "", column_value= "", perPage=10, sort_by="-created"):
        try:
            rows = self.pb.collection(self.collection).get_list(
                1, f'{perPage}',
                #{"filter": "article_keyword~'" + article_value + "'"}
                {

                    "filter": column_name + "~'" + column_value + "'",
                    "sort": sort_by
                 }
            )
        except:
            rows = []
        return rows.items
    
    def add_featured_image(self, image_name):
        try:
            result = self.pb.collection(self.collection).create(
                {
                    # "status": "true",
                    # "featured_image": FileUpload(('', open(image_name, "rb"))),
                    "featured_image": FileUpload((str(image_name), open(image_name, "rb"))),
                })
        except:
            result = "Error"
        return result
    
    def update_featured_image(self, record_id, image_name):
        try:
            result = self.pb.collection(self.collection).update(record_id,
                {
                    "featured_image": FileUpload((str(image_name), open(image_name, "rb"))),
                })
        except:
            result = "Error"
        return result
    
    def delete_id (self, id):
        response = self.pb.collection(self.collection).delete(id)
        return response
        

#--------------------------------------------------------------------------------------------
# Example Usage 
# tblNews = pbfn.CleanTable('https://pb.company.com', 'xyz@company.com', 'password', 'news')
# results = tblNews.get_items(perPage=30)
# for result in results:
#     print (result.id, result.title)
#     tblNews.delete_id(result.id)


