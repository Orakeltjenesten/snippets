# encoding: utf-8
import sys

from workflow import PasswordNotFound, Workflow3, web


def get_recent_snippets(api_key):
    """Hent nyeste snippets fra internsidene

    Returner liste av snippetd

    """
    url = 'https://intern.orakel.ntnu.no/snippets/api/'
    params = dict(count=100, format='json')
    headers = dict(Authorization=api_key)
    r = web.get(url, params, headers)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by internsidene and extract the snippets
    snippets = r.json()
    return snippets


def main(wf):
    try:
        # Get API key from Keychain
        api_key = wf.get_password('orakel_api_key')

        def wrapper():
            return get_recent_snippets(api_key)

        snippets = wf.cached_data('snippets', wrapper, max_age=99)

        # Record our progress in the log file
        log.debug('%d snippets cached' % len(snippets))

    except PasswordNotFound:  # API key has not yet been set
        log.error('No API key saved')
        return 1

    return 0


if __name__ == '__main__':
    workflow = Workflow3()
    log = workflow.logger
    sys.exit(workflow.run(main))
