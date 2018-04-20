"""
Recursively applies pems to a directory tree
"""
import os
from reactors.utils import Reactor, agaveutils


def main():

    r = Reactor()
    m = r.context.get('message_dict')  # shortcut to message_dict
    p = r.pemagent

    r.logger.debug("Message: {}".format(m))
    # Use JSONschema-based message validator
    # - In theory, this obviates some get() boilerplate
    if r.validate_message(m) is False:
        r.on_failure("Invalid message: {}".format(m))

    (syst, abspath, fname) = agaveutils.from_agave_uri(m.get('uri'))
    try:
        fullpath = os.path.join(abspath, fname)
        r.logger.debug('fullpath: {}'.format(fullpath))
        p.grant(syst, fullpath, m.get('username'), m.get('permission'))
    except Exception as e:
        r.on_failure(e)


if __name__ == '__main__':
    main()
