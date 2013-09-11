from django.utils.translation import ugettext as _

SERVICES = (
    # shortname, name, icon
    ('official', 'Infinity Forum', ''),
    ('datasphere', 'Datasphere', ''),
    ('flickr', 'Flickr', 'img/services/flickr.png'),
    ('twitter', 'Twitter', 'img/services/twitter.png'),
    ('facebook', 'Facebook', 'img/services/facebook.png'),
    ('googleplus', 'Google+', 'img/services/googleplus.png'),
)
SERVICES_DICT = dict([(r[0], r) for r in SERVICES])

IMPROVIDERS = (
    # shortname, name, icon
    ('aim', 'AIM', 'img/improviders/aim.png'),
    ('yim', 'Y!IM', 'img/improviders/yim.png'),
    ('gtalk', 'GTalk', 'img/improviders/gtalk.png'),
    ('msn', 'MSN', 'img/improviders/msn.png'),
    ('jabber', 'Jabber', 'img/improviders/jabber.png'),    
)
IMPROVIDERS_DICT = dict([(r[0], r) for r in IMPROVIDERS])

# Convenience mapping from fields to machinetag (namespace, predicate)
MACHINETAGS_FROM_FIELDS = dict(
    [('service_%s' % shortname, ('services', shortname))
     for shortname, name, icon in SERVICES] +
    [('im_%s' % shortname, ('im', shortname))
     for shortname, name, icon in IMPROVIDERS] + [
         ('privacy_search', ('privacy', 'search')),
         ('privacy_email', ('privacy', 'email')),
         ('privacy_im', ('privacy', 'im')),
         ('privacy_irctrack', ('privacy', 'irctrack')),
         ('blog', ('profile', 'blog')),
         ('looking_for_work', ('profile', 'looking_for_work')),
     ]
)
