import boto3
from django.conf import settings
import os

class Bucket:


    """CDN Bucket manager


    init method creates connection
    """

    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name='s3',
            aws_access_key_id='216643bc-a5e2-432c-a5c3-df7815a3d60c',
            aws_secret_access_key='60850c20bf35fdc12193e7eb2a43380223df51e6ca412e63a8835f35cd7c0479',
            endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',

        )


    def get_objects(self):
        result = self.conn.list_objects_v2(Bucket='django-shop-erfan')
        if result['KeyCount']:
            return result['Contents']
        else:
            return None


    def delete_object(self , key): #this is not async but in the tasks.py we use async of celery
        self.conn.delete_object(Bucket='django-shop-erfan', Key=key)
        return True

    def download_object(self , key):
        file_path = os.path.join(settings.BASE_DIR, 'AWS', key)
        with open(file_path, 'wb') as f:
            self.conn.download_fileobj('django-shop-erfan',key,f)


bucket = Bucket()