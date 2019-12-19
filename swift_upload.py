from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient.client import Connection
from login import swift_me, swift_pass, swift_auth
from swiftclient.service import SwiftUploadObject

auth = v3.Password(auth_url = swift_auth,
                   username = swift_me,
                   password = swift_pass,
                   user_domain_name='Default',
                   project_name='Data Science',
                   project_domain_name='Default')

# Create session
keystone_session = session.Session(auth=auth)

# Create swiftclient Connection
swift_conn = Connection(session=keystone_session)

container = 'alberta_twitter_data'

with open('alberta_tweets_2019', 'rb') as local:
    # print(local.readlines())
    print(local)
    swift_conn.put_object(
        container,
        'nov_2019_tweets_backup.txt',
        contents=local,
        content_type='text/plain',
        chunk_size = 1024*100
    )

