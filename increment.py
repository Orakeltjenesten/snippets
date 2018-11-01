# encoding: utf-8
import sys
from httplib import HTTPSConnection

from workflow import PasswordNotFound, Workflow3


def register_snippet(api_key, snippet_id):
    """Registerer bruk av snippets"""
    url = 'intern.orakel.ntnu.no'
    path = 'snippets/api/%s/' % snippet_id
    body = '{}'
    header = {'Authorization': api_key}
    conn = HTTPSConnection(url, 443)
    conn.request('PUT', path, body, header)
    response = conn.getresponse()
    print response.status
    print response.reason


def main(wf):
    # Get query from Alfred
    if len(wf.args):
        snippet_id = wf.args[0]
    else:
        return 0
    try:
        # Get API key from Keychain
        api_key = wf.get_password('orakel_api_key')

        register_snippet(api_key, snippet_id)

        log.debug('snippet %s registered with Internsidene' % snippet_id)

    except PasswordNotFound:  # API key has not yet been set
        log.error('No API key saved')
        return 0

    return 0


if __name__ == '__main__':
    workflow = Workflow3()
    log = workflow.logger
    sys.exit(workflow.run(main))
