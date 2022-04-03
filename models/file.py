from lib import s3
import time
import json

BUCKET = 'json-files'


def get_key(file_id):
    return f'/files/{file_id}.json'


def get_temp_file(file_id):
    return f'/tmp/{file_id}.json'


class File:
    cache = None

    def __init__(self, file_id):
        self.file_id = file_id

    def sync(self):
        filename = get_temp_file(self.file_id)
        key = get_key(self.file_id)
        s3.download_file(file_name=filename, bucket=BUCKET, key=key)
        with open(filename, 'r') as f:
            self.cache = json.loads(f.read())

    def get_data(self):
        if self.cache is None:
            self.sync()
        if self.cache is None:
            return None
        return self.cache

    def update_data(self, data, user_id):
        if self.cache is None:
            try:
                self.sync()
            except:
                pass
        now = time.time()
        file = self.cache
        if file is None:
            file = {
                'created_by': user_id,
                'created_at': now,
                'uuid': self.file_id,
                'body': data
            }
        file['body'] = data
        file['modified_by'] = user_id
        file['modified_at'] = now
        self.cache = file
        # Write to temporary file
        filename = get_temp_file(self.file_id)
        key = get_key(self.file_id)
        with open(filename, 'w') as f:
            f.write(json.dumps(file))
            f.close()
        # upload that file
        s3.upload_file(file_name=filename, bucket=BUCKET, key=key)

    def delete(self):
        key = get_key(self.file_id)
        s3.delete_file(bucket=BUCKET, key=key)
