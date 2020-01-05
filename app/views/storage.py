from app import appbuilder
from flask_appbuilder.api import BaseApi, expose
from flask import jsonify, request
import os
import json
import hashlib
import datetime
import random
import base64
import hmac
from optparse import OptionParser

OSS_ACCESS_KEY_SECRET = os.getenv("OSS_ACCESS_KEY_SECRET")



class Signature:
    def __init__(self, key, access_key_secret):
        self.access_key_secret = access_key_secret
        self.key = key
        self._calculate()
        

    def asdict(self):
        return {
            "key": self.key,
            "policy": self.policy_base64.decode(),
            "signature": self.signature,
        }

    def _calculate(self):
        now = datetime.datetime.now()
        self.key = "usr/%s/%f-%s" % (now.strftime("%Y-%m-%d"), random.random(), self.key)
        expiration = now + datetime.timedelta(days=7)
        policy = {
            "expiration": expiration.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "conditions": [
                {
                    "bucket": os.getenv("OSS_BUCKET"),
                    "key": self.key,
                },
                ["content-length-range", 0, 1048576],
            ]
        }
        policy_string = json.dumps(policy)
        self.policy_base64 = self._convert_base64(policy_string)
        self.signature = self._get_sign_policy(self.policy_base64)

    def _convert_base64(self, input):
        return base64.b64encode(input.encode("utf-8"))

    def _get_sign_policy(self, policy):
        hash_object = hmac.new(self.access_key_secret.encode(), policy, hashlib.sha1)
        hash_value = hash_object.digest()
        return base64.b64encode(hash_value).decode("utf-8")

class StorageAPI(BaseApi):

    resource_name = 'storage'

    @expose("signature", methods=["POST"])
    def signature(self):
        keys = request.form.getlist("key[]")
        signatures = [(Signature(key, OSS_ACCESS_KEY_SECRET)).asdict() for key in keys]
        return jsonify(signatures)

appbuilder.add_api(StorageAPI)