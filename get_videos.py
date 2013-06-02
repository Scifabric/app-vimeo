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


def get_videos_tag(per_page=20, page=1, tags='science'):
    """
    Gets videos for a given tag
    :arg string hashtag: Vimeo hashtag to get the videos
    :returns: A list of Videos.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.videos.getByTag', tag=tags, per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        # print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")


def get_videos_channel(per_page=20, page=1, channel_id='technolust'):
    """
    Gets videos for a given channel
    :arg string channel id: Vimeo channel id to get the videos
    :returns: A list of Videos.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.channels.getVideos', channel_id=channel_id, per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        # print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")


def get_videos_group(per_page=20, page=1, group_id='science'):
    """
    Gets videos for a given group
    :arg string channel id: Vimeo group id to get the videos
    :returns: A list of Videos.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.groups.getVideos', group_id=group_id, per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        # print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")

def get_videos_category(per_page=20, page=1, category='nature'):
    """
    Gets videos for a given group
    :arg string channel id: Vimeo group id to get the videos
    :returns: A list of Videos.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.categories.getRelatedVideos', category=category, per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        # print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")


def get_videos_user_tag(per_page=20, page=1, user_id='craigprotzel', tag='itp'):
    """
    Gets videos for a given user and tag
    :arg string channel id: Vimeo user and tag id to get the videos
    :returns: A list of Videos.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.videos.search', user_id=user_id, query=tag, per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        # print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")

def get_videos_album(per_page=20, page=1, album_id='1659487'):
    """
    Gets videos for a given album
    :arg string channel id: Vimeo group id to get the videos
    :returns: A list of Videos.
    :rtype: list
    """
    try:
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        results = v.get('vimeo.albums.getVideos', album_id=album_id, per_page=per_page,
                        page=page)
        results = json.loads(results)
        videos = results['videos']['video']
        oembeds = []
        for v in videos:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                oembeds.append(json.loads(res.text)['html'])
        # print oembeds
        return oembeds
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")