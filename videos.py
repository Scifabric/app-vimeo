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
import click

@click.command()
@click.option('--per-page', default=20, help='Number of videos per page')
@click.option('--page', default=1, help='Page to get videos from')
@click.option('--by-tags', help='Get videos with these tags', default=None)
@click.option('--by-channel', help='Get videos from a channel', default=None)
@click.option('--by-group', help='Get videos from a group', default=None)
@click.option('--by-category', help='Get videos from a category', default=None)
@click.option('--by-user', help='Get videos from a user ID', default=None)
@click.option('--tagged', help='To use in conjunction with --by-user', default=None)
@click.option('--by-album', help='Get videos from an album', default=None)
def cli(per_page, page, by_tags, by_channel, by_group, by_category, by_user,
        tagged, by_album):
    try:
        action = None
        filename = None
        query = dict(page=page, per_page=per_page)
        v = vimeo.Client(key=config.CONSUMER_KEY, secret=config.CONSUMER_SECRET)
        if by_tags:
            click.secho("Getting videos from tags: %s" % by_tags,
                        fg="yellow")
            action = 'vimeo.videos.getByTag'
            query['tag'] = by_tags
            filename = 'video_tasks_from_tags.json'
        elif by_channel:
            click.secho("Getting videos from channel: %s" % by_channel,
                        fg="yellow")
            action = 'vimeo.channels.getVideos'
            query['channel_id'] = by_channel
            filename = 'video_tasks_from_channel.json'
        elif by_group:
            click.secho("Getting videos from group: %s" % by_group,
                        fg="yellow")
            action = 'vimeo.groups.getVideos'
            query['group_id'] = by_group
            filename = 'video_tasks_from_group.json'
        elif by_category:
            click.secho("Getting videos from category: %s" % by_category,
                        fg="yellow")
            action = 'vimeo.categories.getRelatedVideos'
            query['category'] = by_category
            filename = 'video_tasks_from_category.json'
        elif by_user and tagged:
            click.secho("Getting videos tagged: %s from user: %s" %
                        (tagged, by_user))
            action = 'vimeo.videos.search'
            query['user_id'] = by_user
            query['query'] = tagged
            filename = 'video_tasks_from_user_tagged.json'
        elif by_album:
            click.secho("Getting videos from album: %s " % by_album)
            action = 'vimeo.albums.getVideos'
            query['album_id'] = by_album
            filename = 'video_tasks_from_album.json'
        else:
            raise click.UsageError("Please use --help to see the available options")
        results = v.get(action, **query)
        write_results_to_json_file(results, filename)
        click.secho("Done!", fg="green")
    except:
        raise
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")

def write_results_to_json_file(results, filename):
    results = json.loads(results)
    videos = results['videos']['video']
    oembeds = []
    with click.progressbar(videos, label="Processing videos") as bar:
        for v in bar:
            req = 'http://vimeo.com/%s' % v['id']
            url = 'http://vimeo.com/api/oembed.json?url=%s' % req
            payload = {'maxwidth': 512}
            res = requests.get(url, params=payload)
            if res.status_code == 200:
                tmp = dict()
                tmp['oembed'] = json.loads(res.text)['html']
                oembeds.append(tmp)
    file = open(filename, 'w')
    file.write(json.dumps(oembeds))
    file.close()


if __name__ == '__main__':
    cli()
