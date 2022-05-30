# Copyright (C) 2021 GanstaKingofSA (Hanaka)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# The main code behind the music room. Pardon any mess within this PY file.


init -1 python:
    import random
    import re
    import os
    import json
    import pygame_sdl2
    from renpy.text.text import Text
    from renpy.display.im import image
    import renpy.audio.music as music
    import renpy.display.behavior as displayBehavior
  
  
    ###################################################################
    ######  Set up important variables for the music room engine  #####
    ###################################################################
    
    # Creation of Music Room and Code Setup
    version = 1.7
    
    # BDGR directory
    gamedir = None

    # Lists for holding media types
    BdgrAutoDefineList = []
    BdgrManualDefineList = []
    BdgrSoundtracks = []
    # Only ogg format tested
    bdgr_file_types = (".ogg",)

    # Stores soundtrack in progress
    bdgr_game_soundtrack = False

    # Stores positions of track/volume/default priority
    bdgr_time_position = 0.0
    bdgr_time_duration = 3.0
    bdgr_old_volume = 0.0
    BdgrPriorityScan = 2
    BdgrScale = 1.0

    # Stores paused track/player controls
    bdgr_game_soundtrack_pause = False
    BdgrPrevTrack = False
    BdgrRandomSong = False
    BdgrLoopSong = False
    BdgrOrganizeAZ = False
    BdgrOrganizePriority = True
    BdgrPausedstate = False

    random.seed()
    
    ###################################################################

    
    def bdgr_get_gamedir_path():
        """
        Get full BDGR (mode) gamedir path
        """
        return os.path.dirname(os.path.abspath(renpy.loader.transfn("bdgr_define_path_file.txt"))).replace("\\", "/")

                            
    def bdgr_set_ost_config():
        """
        Set the BDGR game dir path
        """
        global gamedir
        
        if renpy.windows:
            gamedir = bdgr_get_gamedir_path()
        elif renpy.android:
            try:
                os.mkdir(os.path.join(os.environ["ANDROID_PUBLIC"], "game"))
            except:
                pass
            gamedir = os.path.join(os.environ["ANDROID_PUBLIC"], "game")
        else:
            gamedir = bdgr_get_gamedir_path()
    

    class BdgrSoundtrack:
        """
        Class responsible to define songs to the music player.
        """

        def __init__(
            self,
            name="",
            path="",
            priority=2,
            author="",
            byteTime=False,
            description="",
            cover_art=False,
            unlocked=True,
        ):
            self.name = name
            self.path = path
            self.priority = priority
            self.author = author
            if byteTime:
                self.byteTime = byteTime
            else:
                self.byteTime = bdgr_get_duration(path)
            self.description = description
            if not cover_art:
                self.cover_art = "images/misc/none.png"
            else:
                self.cover_art = cover_art
            self.unlocked = unlocked


    @renpy.exports.pure
    class BdgrAdjustableAudioPositionValue(renpy.ui.BarValue):
        """
        Class that replicates a music progress bar in Ren'Py.
        """

        def __init__(self, channel="bdgr_music_room", update_interval=0.0):
            self.channel = channel
            self.update_interval = update_interval
            self.adjustment = None
            self._hovered = False

        def get_pos_duration(self):
            if not music.is_playing(self.channel):
                pos = bdgr_time_position
            else:
                pos = music.get_pos(self.channel) or 0.0

            duration = bdgr_time_duration

            return pos, duration

        def get_song_options_status(self):
            return BdgrLoopSong, BdgrRandomSong

        def get_adjustment(self):
            pos, duration = self.get_pos_duration()
            self.adjustment = renpy.ui.adjustment(
                value=pos, range=duration, changed=self.set_pos, adjustable=True
            )

            return self.adjustment

        def hovered(self):
            self._hovered = True

        def unhovered(self):
            self._hovered = False

        def set_pos(self, value):
            loopThis = self.get_song_options_status()
            if self._hovered and pygame_sdl2.mouse.get_pressed()[0]:
                global BdgrPausedstate
                BdgrPausedstate = False
                music.play("<from {}>".format(value) + bdgr_game_soundtrack.path, self.channel)
                if loopThis:
                    music.queue(bdgr_game_soundtrack.path, self.channel, loop=True)

        def periodic(self, st):

            pos, duration = self.get_pos_duration()
            loopThis, doRandom = self.get_song_options_status()

            if pos and pos <= duration:
                self.adjustment.set_range(duration)
                self.adjustment.change(pos)

            if pos > duration - 0.20:

                if loopThis:
                    music.play(bdgr_game_soundtrack.path, self.channel, loop=True)
                elif doRandom:
                    bdgr_random_song()
                else:
                    bdgr_next_track()

            return self.update_interval

    def bdgr_set_ost_scale():
        """
        Need to be run
        """
        global BdgrScale
        
        if renpy.config.screen_width != 1280:
            BdgrScale = renpy.config.screen_width / 1280.0
        else:
            BdgrScale = 1.0


    def bdgr_music_pos(style_name, st, at):
        """
        Returns the track position to Ren'Py.
        """

        global bdgr_time_position

        if music.get_pos(channel="bdgr_music_room") is not None:
            bdgr_time_position = music.get_pos(channel="bdgr_music_room")

        readableTime = bdgr_convert_time(bdgr_time_position)
        d = Text(readableTime, style=style_name)
        return d, 0.20


    def bdgr_get_duration(songPath=None):
        if bdgr_game_soundtrack and bdgr_game_soundtrack.byteTime and not songPath:
            return bdgr_game_soundtrack.byteTime
        else:
            try:
                if songPath:
                    pathToSong = songPath
                else:
                    pathToSong = bdgr_game_soundtrack.path

                tags = BdgrTinyTag.get_renpy(pathToSong, image=False)

                if tags.duration:
                    return tags.duration
                else:
                    if not songPath:
                        return music.get_duration(channel="bdgr_music_room") or bdgr_time_duration
            except:
                if not songPath:
                    return music.get_duration(channel="bdgr_music_room") or bdgr_time_duration


    def bdgr_music_dur(style_name, st, at):
        """
        Returns the track duration to Ren'Py.
        """

        global bdgr_time_duration

        bdgr_time_duration = bdgr_get_duration()

        readableDuration = bdgr_convert_time(bdgr_time_duration)
        d = Text(readableDuration, style=style_name)
        return d, 0.20


    def bdgr_dynamic_title_text(st, at):
        """
        Returns a resized song title text to Ren'Py.
        """

        title = len(bdgr_game_soundtrack.name)

        d = Text(bdgr_game_soundtrack.name,
                 style='st_song_name',
                 substitute=False
                 )

        return d, 0.20


    def bdgr_dynamic_author_text(st, at):
        """
        Returns a resized song artist text to Ren'Py.
        """

        author = len(bdgr_game_soundtrack.author)

        d = Text(bdgr_game_soundtrack.author,
                 style='st_song_author',
                 substitute=False
                 )

        return d, 0.20


    def bdgr_refresh_cover_data(st, at):
        """
        Returns the song cover art to Ren'Py.
        """

        d = image(bdgr_game_soundtrack.cover_art)
        return d, 0.20


    def bdgr_dynamic_description_text(st, at):
        """
        Returns a resized song album/comment to Ren'Py.
        """

        desc = len(bdgr_game_soundtrack.description)

        d = Text(bdgr_game_soundtrack.description,
                 style='st_song_description',
                 substitute=False,
                 )
        return d, 0.20


    def bdgr_auto_play_pause_button(st, at):
        """
        Returns either a play/pause button to Ren'Py based off song play status.
        """

        if music.is_playing(channel="bdgr_music_room"):
            if BdgrPausedstate:
                d = displayBehavior.ImageButton(bdgr_music_room_gui_path + "pause_black_idle.png")
            else:
                d = displayBehavior.ImageButton(
                    bdgr_music_room_gui_path + "pause_black_hover.png", action=bdgr_current_music_pause
                )
        else:
            d = displayBehavior.ImageButton(
                bdgr_music_room_gui_path + "play_black_hover.png", action=bdgr_current_music_play
            )
        return d, 0.20


    def bdgr_convert_time(x):
        """
        Converts track position and duration to human-readable time.
        """

        hour = ""

        if int(x / 3600) > 0:
            hour = str(int(x / 3600))

        if hour != "":
            if int((x % 3600) / 60) < 10:
                minute = ":0" + str(int((x % 3600) / 60))
            else:
                minute = ":" + str(int((x % 3600) / 60))
        else:
            minute = "" + str(int(x / 60))

        if int(x % 60) < 10:
            second = ":0" + str(int(x % 60))
        else:
            second = ":" + str(int(x % 60))

        return hour + minute + second


    def bdgr_current_music_pause():
        """
        Pauses the current song playing.
        """

        global bdgr_game_soundtrack_pause, BdgrPausedstate
        BdgrPausedstate = True

        if not music.is_playing(channel="bdgr_music_room"):
            return
        else:
            soundtrack_position = music.get_pos(channel="bdgr_music_room") + 1.6

        if soundtrack_position is not None:
            bdgr_game_soundtrack_pause = (
                "<from " + str(soundtrack_position) + ">" + bdgr_game_soundtrack.path
            )

        music.stop(channel="bdgr_music_room", fadeout=.5)


    def bdgr_current_music_play():
        """
        Plays either the paused state of the current song or a new song to the
        player.
        """

        global BdgrPausedstate
        BdgrPausedstate = False

        if not bdgr_game_soundtrack_pause:
            music.play(bdgr_game_soundtrack.path, channel="bdgr_music_room", fadein=.5)
        else:
            music.play(bdgr_game_soundtrack_pause, channel="bdgr_music_room", fadein=.5)


    def bdgr_current_music_forward():
        """
        Fast-forwards the song by 5 seconds or advances to the next song.
        """

        global bdgr_game_soundtrack_pause

        if music.get_pos(channel="bdgr_music_room") is None:
            soundtrack_position = bdgr_time_position + 5
        else:
            soundtrack_position = music.get_pos(channel="bdgr_music_room") + 5

        if soundtrack_position >= bdgr_time_duration:
            bdgr_game_soundtrack_pause = False
            if BdgrRandomSong:
                bdgr_random_song()
            else:
                bdgr_next_track()
        else:
            bdgr_game_soundtrack_pause = (
                "<from " + str(soundtrack_position) + ">" + bdgr_game_soundtrack.path
            )

            music.play(bdgr_game_soundtrack_pause, channel="bdgr_music_room")


    def bdgr_current_music_backward():
        """
        Rewinds the song by 5 seconds or advances to the next song behind it.
        """

        global bdgr_game_soundtrack_pause

        if music.get_pos(channel="bdgr_music_room") is None:
            soundtrack_position = bdgr_time_position - 5
        else:
            soundtrack_position = music.get_pos(channel="bdgr_music_room") - 5

        if soundtrack_position <= 0.0:
            bdgr_game_soundtrack_pause = False
            bdgr_next_track(True)
        else:
            bdgr_game_soundtrack_pause = (
                "<from " + str(soundtrack_position) + ">" + bdgr_game_soundtrack.path
            )

            music.play(bdgr_game_soundtrack_pause, channel="bdgr_music_room")


    def bdgr_next_track(back=False):
        """
        Advances to the next song ahead or behind to the player or the start/end.
        """

        global bdgr_game_soundtrack, BdgrPausedstate

        for index, item in enumerate(BdgrSoundtracks):
            if (
                bdgr_game_soundtrack.description == item.description
                and bdgr_game_soundtrack.name == item.name
            ):
                try:
                    if back:
                        bdgr_game_soundtrack = BdgrSoundtracks[index - 1]
                    else:
                        bdgr_game_soundtrack = BdgrSoundtracks[index + 1]
                except:
                    if back:
                        bdgr_game_soundtrack = BdgrSoundtracks[-1]
                    else:
                        bdgr_game_soundtrack = BdgrSoundtracks[0]
                break

        if bdgr_game_soundtrack != False:
            BdgrPausedstate = False
            music.play(bdgr_game_soundtrack.path, channel="bdgr_music_room", loop=BdgrLoopSong)


    def bdgr_random_song():
        """
        Advances to the next song with pure randomness.
        """

        global bdgr_game_soundtrack, BdgrPausedstate

        unique = 1
        if BdgrSoundtracks[-1].path == bdgr_game_soundtrack.path:
            pass
        else:
            while unique != 0:
                a = random.randrange(0, len(BdgrSoundtracks) - 1)
                if bdgr_game_soundtrack != BdgrSoundtracks[a]:
                    unique = 0
                    bdgr_game_soundtrack = BdgrSoundtracks[a]

        if bdgr_game_soundtrack != False:
            BdgrPausedstate = False
            music.play(bdgr_game_soundtrack.path, channel="bdgr_music_room", loop=BdgrLoopSong)


    def bdgr_mute_player():
        """
        Mutes the music player.
        """

        global bdgr_old_volume

        if renpy.game.preferences.get_volume("bdgr_music_room_mixer") != 0.0:
            bdgr_old_volume = renpy.game.preferences.get_volume("bdgr_music_room_mixer")
            renpy.game.preferences.set_volume("bdgr_music_room_mixer", 0.0)
        else:
            if bdgr_old_volume == 0.0:
                renpy.game.preferences.set_volume("bdgr_music_room_mixer", 0.5)
            else:
                renpy.game.preferences.set_volume("bdgr_music_room_mixer", bdgr_old_volume)


    def bdgr_refresh_list():
        """
        Refreshes the song list.
        """

        bdgr_scan_song()
        bdgr_resort()


    def bdgr_resort():
        """
        Adds songs to the song list and resorts them by priority or A-Z.
        """

        global BdgrSoundtracks
        BdgrSoundtracks = []
        
        for obj in BdgrAutoDefineList:
            if obj.unlocked:
                BdgrSoundtracks.append(obj)
        for obj in BdgrManualDefineList:
            if obj.unlocked:
                BdgrSoundtracks.append(obj)

        if BdgrOrganizeAZ:
            BdgrSoundtracks = sorted(BdgrSoundtracks, key=lambda soundtracks: soundtracks.name)
        if BdgrOrganizePriority:
            BdgrSoundtracks = sorted(BdgrSoundtracks, key=lambda soundtracks: soundtracks.priority)


    def bdgr_get_info(path, tags):
        """
        Gets the info of the tracks in the track info for defining.
        """

        sec = tags.duration
        try:
            image_data = tags.get_image()

            with renpy.exports.file("python-packages/binaries.txt") as a:
                lines = a.readlines()

            jpgbytes = bytes("\\xff\\xd8\\xff")
            utfbytes = bytes("o\\x00v\\x00e\\x00r\\x00\\x00\\x00\\x89PNG\\r\\n")

            jpgmatch = re.search(jpgbytes, image_data)
            utfmatch = re.search(utfbytes, image_data)

            if jpgmatch:
                cover_formats = ".jpg"
            else:
                cover_formats = ".png"

                if utfmatch:  # addresses itunes cover descriptor fixes
                    image_data = re.sub(utfbytes, lines[2], image_data)

            coverAlbum = re.sub(r"\[|\]|/|:|\?", "", tags.album)

            with open(
                os.path.join(gamedir, bdgr_track_cover_directory, coverAlbum + cover_formats), "wb"
            ) as f:
                f.write(image_data)

            art = bdgr_track_cover_directory + "/" + coverAlbum + cover_formats
            return tags.title, tags.artist, sec, art, tags.album, tags.comment
        except TypeError:
            return tags.title, tags.artist, sec, None, tags.album, tags.comment


    def bdgr_scan_song():
        """
        Scans the track folder for songs and defines them to the player.
        """

        global BdgrAutoDefineList

        exists = []
        for x in BdgrAutoDefineList[:]:
            try:
                renpy.exports.file(x.path)
                exists.append(x.path)
            except:
                BdgrAutoDefineList.remove(x)

        for x in os.listdir(gamedir + "/" + bdgr_track_directory):
            if x.endswith((bdgr_file_types)) and bdgr_track_directory + x not in exists:
                path = bdgr_track_directory + x
                tags = BdgrTinyTag.get(gamedir + "/" + path, image=True)
                title, artist, sec, altAlbum, album, comment = bdgr_get_info(path, tags)
                bdgr_def_song(
                    title, artist, path, BdgrPriorityScan, sec, altAlbum, album, comment, True
                )
                exists.append(path)
        
        rpa_file_list = []

        if renpy.android:
            rpa_file_list = [
                x for x in renpy.list_files() if x.endswith((bdgr_file_types))
            ]
        else:
            for archive in bdgr_archive_list:
                rpa_file = BdgrRenPyArchive(
                    os.path.join(gamedir, archive).replace("\\", "/"), padlength=0, key=0xDEADBEEF, version=2
                )
                rpa_file_list += [
                    x for x in rpa_file.list() if x.endswith((bdgr_file_types))
                ]

        for x in rpa_file_list:
            if x not in exists:
                if renpy.android:
                    tags = BdgrTinyTag.get_renpy(x, image=True, apk=True)
                else:
                    tags = BdgrTinyTag.get_renpy(x, image=True)
                title, artist, sec, altAlbum, album, comment = bdgr_get_info(x, tags)
                bdgr_def_song(
                    title, artist, x, BdgrPriorityScan, sec, altAlbum, album, comment, True
                )


    def bdgr_def_song(
        title, artist, path, priority, sec, altAlbum, album, comment, unlocked=True
    ):
        """
        Defines the song to the music player list.
        """

        if not title:
            title = str(path.replace(bdgr_track_directory, "")).capitalize()
        if not artist:
            artist = "Unknown Artist"
        if not altAlbum:
            altAlbum = "images/misc/none.png"
        else:
            try:
                renpy.exports.image_size(altAlbum)
            except:
                altAlbum = "images/misc/none.png"
        if not album:
            description = "Non-Metadata Song"
        else:
            description = album
        if comment:
            description += "\n" + comment

        class_name = re.sub(r"-|'| ", "_", title)

        class_name = BdgrSoundtrack(
            name=title,
            author=artist,
            path=path,
            byteTime=sec,
            priority=priority,
            description=description,
            cover_art=altAlbum,
            unlocked=unlocked,
        )
        BdgrAutoDefineList.append(class_name)


    def bdgr_get_music_channel_info():
        """
        Gets the info of the music channel for exiting purposes.
        """

        global BdgrPrevTrack

        BdgrPrevTrack = music.get_playing(channel="music")
        if BdgrPrevTrack is None:
            BdgrPrevTrack = False


    def bdgr_check_paused_state():
        """
        Checks if the music player is in a paused state for exiting purposes.
        """

        if not bdgr_game_soundtrack or BdgrPausedstate:
            return
        else:
            bdgr_current_music_pause()


    def bdgr_ost_start():
        bdgr_get_music_channel_info()
        bdgr_resort()


    def bdgr_ost_quit():
        bdgr_check_paused_state()


