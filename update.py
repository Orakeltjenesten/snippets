# encoding: utf-8
from workflow import web, Workflow, PasswordNotFound


def get_recent_snippets(api_key):
    """Hent nyeste snippets fra internsidene

    Returner liste av snippetd

    """
    url = 'https://s.ntnu.no/snippets/'
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

        # Retrieve snippets from cache if available and no more than 600
        # seconds old

        def wrapper():
            """`cached_data` can only take a bare callable (no args),
            so we need to wrap callables needing arguments in a function
            that needs none.
            """
            return get_recent_snippets(api_key)

        snippets = wf.cached_data('snippets', wrapper, max_age=1)
        # Record our progress in the log file
        log.debug('%d snippets cached' % len(snippets))
    except PasswordNotFound:  # API key has not yet been set
        # Nothing we can do about this, so just log it
        log.error('No API key saved')

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    wf.run(main)
