# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import vimeo
import json
import config
import requests


def get_videos(per_page=20, page=1):
    """
    Gets tweets for a given hashtag
    :arg string hashtag: Twitter hashtag to get the tweets
    :returns: A list of Tweets.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.videos.getByTag', tag='science', per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            res = requests.get(url)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")
