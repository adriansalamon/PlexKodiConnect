#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

from .. import utils


def remove_trailing_slash(path):
    """
    Removes trailing slashes or backslashes from path [unicode], and is NOT
    dependent on os.path
    """
    if '/' in path:
        path = path[:-1] if path.endswith('/') else path
    else:
        path = path[:-1] if path.endswith('\\') else path
    return path


class Sync(object):
    def __init__(self, entrypoint=False):
        # Direct Paths (True) or Addon Paths (False)?
        self.direct_paths = None
        # Is synching of Plex music enabled?
        self.enable_music = None
        # Do we sync artwork from the PMS to Kodi?
        self.artwork = None
        # Path remapping mechanism (e.g. smb paths)
        # Do we replace \\myserver\path to smb://myserver/path?
        self.replace_smb_path = None
        # Do we generally remap?
        self.remap_path = None
        self.force_transcode_pix = None
        # Mappings for REMAP_PATH:
        self.remapSMBmovieOrg = None
        self.remapSMBmovieNew = None
        self.remapSMBtvOrg = None
        self.remapSMBtvNew = None
        self.remapSMBmusicOrg = None
        self.remapSMBmusicNew = None
        self.remapSMBphotoOrg = None
        self.remapSMBphotoNew = None
        # Escape path?
        self.escape_path = None
        # Shall we replace custom user ratings with the number of versions available?
        self.indicate_media_versions = None
        # Will sync movie trailer differently: either play trailer directly or show
        # all the Plex extras for the user to choose
        self.show_extras_instead_of_playing_trailer = None
        # Only sync specific Plex playlists to Kodi?
        self.sync_specific_plex_playlists = None
        # Only sync specific Kodi playlists to Plex?
        self.sync_specific_kodi_playlists = None
        # Shall we show Kodi dialogs when synching?
        self.sync_dialog = None

        # How often shall we sync?
        self.full_sync_intervall = None
        # Background Sync disabled?
        self.background_sync_disabled = None
        # How long shall we wait with synching a new item to make sure Plex got all
        # metadata?
        self.backgroundsync_saftymargin = None
        # How many threads to download Plex metadata on sync?
        self.sync_thread_number = None

        # Shall Kodi show dialogs for syncing/caching images? (e.g. images left
        # to sync)
        self.image_sync_notifications = None

        # Do we need to run a special library scan?
        self.run_lib_scan = None
        # Set if user decided to cancel sync
        self.stop_sync = False
        # Could we access the paths?
        self.path_verified = False

        self.load()

    def load(self):
        self.direct_paths = utils.settings('useDirectPaths') == '1'
        self.enable_music = utils.settings('enableMusic') == 'true'
        self.artwork = utils.settings('usePlexArtwork') == 'true'
        self.replace_smb_path = utils.settings('replaceSMB') == 'true'
        self.remap_path = utils.settings('remapSMB') == 'true'
        self.force_transcode_pix = utils.settings('force_transcode_pix') == 'true'
        self.remapSMBmovieOrg = remove_trailing_slash(utils.settings('remapSMBmovieOrg'))
        self.remapSMBmovieNew = remove_trailing_slash(utils.settings('remapSMBmovieNew'))
        self.remapSMBtvOrg = remove_trailing_slash(utils.settings('remapSMBtvOrg'))
        self.remapSMBtvNew = remove_trailing_slash(utils.settings('remapSMBtvNew'))
        self.remapSMBmusicOrg = remove_trailing_slash(utils.settings('remapSMBmusicOrg'))
        self.remapSMBmusicNew = remove_trailing_slash(utils.settings('remapSMBmusicNew'))
        self.remapSMBphotoOrg = remove_trailing_slash(utils.settings('remapSMBphotoOrg'))
        self.remapSMBphotoNew = remove_trailing_slash(utils.settings('remapSMBphotoNew'))
        self.escape_path = utils.settings('escapePath') == 'true'
        self.indicate_media_versions = utils.settings('indicate_media_versions') == "true"
        self.show_extras_instead_of_playing_trailer = utils.settings('showExtrasInsteadOfTrailer') == 'true'
        self.sync_specific_plex_playlists = utils.settings('syncSpecificPlexPlaylists') == 'true'
        self.sync_specific_kodi_playlists = utils.settings('syncSpecificKodiPlaylists') == 'true'
        self.sync_dialog = utils.settings('dbSyncIndicator') == 'true'

        self.full_sync_intervall = int(utils.settings('fullSyncInterval')) * 60
        self.background_sync_disabled = utils.settings('enableBackgroundSync') == 'false'
        self.backgroundsync_saftymargin = int(utils.settings('backgroundsync_saftyMargin'))
        self.sync_thread_number = int(utils.settings('syncThreadNumber'))

        self.image_sync_notifications = utils.settings('imageSyncNotifications') == 'true'
