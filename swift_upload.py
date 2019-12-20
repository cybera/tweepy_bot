from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient.client import Connection
from login import swift_me, swift_pass, swift_auth
import datetime as dt
def upload_file(container, input_file, output_file):
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

    with open(input_file, 'rb') as local:
        # print(local.readlines())
        print(local)
        swift_conn.put_object(
            container,
            output_file,
            contents=local,
            content_type='text/plain',
            chunk_size = 1024*100*1024
        )



