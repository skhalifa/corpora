# -*- coding: utf-8 -*-
import os

FILE_UPLOAD_PERMISSIONS = 0644

# So, we can get to a LB externally but not internally.
# This if for public access to the LB
# http://LB-corpora-production-deepspeech-1243053555.ap-southeast-2.elb.amazonaws.com/transcribe
# e.g. a local development server.
DEEPSPEECH_URL_PUBLIC = \
    "http://deep.koreromaori.io/transcribe"


# Internally we can't use application LBs, we have to use network ones
# Unfortunately we don't get the same statistics here.
DEEPSPEECH_URL_PRIVATE = \
    "http://LB-corpora-production-deep-tcp-4113e81f0772e13a.elb.ap-southeast-2.amazonaws.com/transcribe"


DEEPSPEECH_URL_BETA = \
    "http://172.31.10.32:5000/transcribe_with_metadata"

DEEPSPEECH_URL_BETA_PUBLIC = \
    "http://3.104.105.146:5000/transcribe_with_metadata"


if 'local' in os.environ['ENVIRONMENT_TYPE']:
    DEEPSPEECH_URL = DEEPSPEECH_URL_BETA_PUBLIC
elif 'staging' in os.environ['ENVIRONMENT_TYPE']:
    DEEPSPEECH_URL = DEEPSPEECH_URL_PRIVATE
else:
    DEEPSPEECH_URL = DEEPSPEECH_URL_PRIVATE

OLD_URL = "http://waha-tuhi-api-17.dragonfly.nz/transcribe"