"""basic loadtest scenario(s) for shavar server
$ curl -k  --data "mozstd-track-digest256;a:1" https://shavar.stage.mozaws.net/downloads # noqa"""
import os
from molotov.fmwk import scenario

DEBUG = True
URL_SERVER = os.getenv('URL_SERVER',
                       'https://shavar.stage.mozaws.net')
_LINE = '------------------------------------------------------------'
_LISTS = [
    "base-track-digest256",
    "baseeff-track-digest256",
    "basew3c-track-digest256",
    "content-track-digest256",
    "contenteff-track-digest256",
    "contentw3c-track-digest256",
    "mozfull-track-digest256",
    "mozfullstaging-track-digest256",
    "mozplugin-block-digest256",
    "mozplugin2-block-digest256",
    "mozstd-track-digest256",
    "mozstd-trackwhite-digest256",
    "mozstdstaging-track-digest256",
    "mozstdstaging-trackwhite-digest256",
    "moztestpub-track-digest256",
    "moztestpub-trackwhite-digest256"
]


def log_header(msg):
    print('\n\n{0}\n{1}\n{0}'.format(_LINE, msg))


@scenario(100)
async def get_all_lists(session):
    for list in _LISTS:
        """Get TP lists from shavar server"""

        data = '{0};a:1'.format(list)
        url = URL_SERVER + '/downloads'
        async with session.post(url, data=data) as resp:
            if DEBUG:
                log_header(list)
                body = await resp.content.read()
                resp = str(body, 'utf8')
                print(resp)
