from app import appbuilder
from flask_appbuilder.api import BaseApi, expose
from flask import jsonify
import os
import json
import hashlib
import datetime
import base64
import hmac
from optparse import OptionParser

OSS_ACCESS_KEY_SECRET = os.getenv("OSS_ACCESS_KEY_SECRET")

def convert_base64(input):
    return base64.b64encode(input.encode("utf-8"))

def get_sign_policy(key, policy):
    hash_object = hmac.new(key.encode("utf-8"), policy, hashlib.sha1)
    hash_value = hash_object.digest()
    return str(base64.b64encode(hash_value))

class StorageAPI(BaseApi):

    resource_name = 'storage'

    @expose("signature")
    def signature(self):
        # TODO: generate key by file name
        now = datetime.datetime.now()
        key = "/usr/%s/%d/" % (now.strftime("%Y-%m-%d"), 1)
        expiration = now + datetime.timedelta(days=7)
        policy = {
            "expiration": expiration.strftime("%Y-%m-%dT%H:%M:%S%Z"),
            "conditions": [
                {
                    "bucket": os.getenv("OSS_BUCKET"),
                    "key": key
                },
                ["content-length-range", 0, 1048576],
            ]
        }

        base64policy = convert_base64(json.dumps(policy))
        signature = get_sign_policy(OSS_ACCESS_KEY_SECRET, base64policy)

        return jsonify({
            "signature": signature
        })

appbuilder.add_api(StorageAPI)