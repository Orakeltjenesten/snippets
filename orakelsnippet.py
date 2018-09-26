# encoding: utf-8

import sys
import argparse
from workflow import Workflow, ICON_WEB, ICON_INFO, ICON_WARNING, web, PasswordNotFound
from workflow.background import run_in_background, is_running


API_KEY = 'your-api-key'

def search_key_for_snippet(snippet):
    """Generate a string search key for a snippet"""
    elements = []
    elements.append(snippet['title'])  # title of snippet
    elements.append(snippet['description'])  # snippet description
    elements.append(snippet['search_keywords'])  # snippet tags
    return u' '.join(elements)

def main(wf):
    parser = argparse.ArgumentParser()
    
    # add apikey if --setkey given
    parser.add_argument('--setkey', dest='apikey', nargs='?', default=None)
    # add an optional query and save it to 'query'
    parser.add_argument('query', nargs='?', default=None)
    args = parser.parse_args(wf.args)


    if args.apikey:  # Script was passed an API key
        key = 'Token %s' % args.apikey
        wf.save_password('orakel_api_key', key)
        return 0

    try:
        api_key = wf.get_password('orakel_api_key')
    except PasswordNotFound:  # API key has not yet been set
        wf.add_item(u'Ingen API nøkkel satt.',
                    u'Bruk orakelapi for å sette API nøkkelen',
                    valid=False,
                    icon=ICON_WARNING)
        wf.send_feedback()
        return 0
    
    query = args.query
    # Get cache regardless of age with no call_back
    snippets = wf.cached_data('snippets', None, max_age=0)

    # Start update script if cached data are too old
    if not wf.cached_data_fresh('snippets', max_age=600):
        cmd = ['/usr/bin/python', wf.workflowfile('update.py')]
        run_in_background('update', cmd)

    # notify if update.py is running
    if is_running('update'):
        wf.add_item('Henter nyeste snippets fra Internsidene...',
                    valid=False,
                    icon=ICON_INFO)

    # filter snippets on query
    if query and snippets:
        snippets = wf.filter(query, snippets, key=search_key_for_snippet)
    
    if not snippets:
        wf.add_item('Ingen snippets ble funnet', icon=ICON_WARNING)
        wf.send_feedback()
        return 0
   
    # Add snippets to output list
    for snippet in snippets:
        wf.add_item(title=snippet['title'],
                    subtitle=snippet['description'],
                    arg=snippet['text'],
                    valid=True)

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow(update_settings={
    'github_slug': 'Orakeltjenesten/snippets',
    })
    sys.exit(wf.run(main))
