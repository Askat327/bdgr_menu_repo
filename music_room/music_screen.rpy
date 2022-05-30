################################################################################
## This controls the music room player positions, sizes and more

init python early:
    renpy.music.register_channel(u'bdgr_music_room', mixer="bdgr_music_room_mixer", loop=False)
    min_func = min
    
init python:
    bdgr_append_collbacks()
    bdgr_set_ost_config()
    bdgr_set_ost_scale()
    bdgr_scan_song()
    bdgr_refresh_list()
    
    style.bdgr_music_room_button =                            Style(style.button)
    style.bdgr_music_room_button.background =                 "music_room/gui/song_idle.png"
    style.bdgr_music_room_button.hover_background =           "music_room/gui/song_hover.png"


## The positions and sizes of the music viewport list
define gui.bdgr_music_room_viewport_xsize = 0.7
define gui.bdgr_music_room_viewport_pos = 0.5
define gui.bdgr_music_room_spacing = 30
define gui.bdgr_music_room_viewport_ysize = 410

## The positions and sizes of the music information text
define gui.bdgr_music_room_information_xpos = 810
define gui.bdgr_music_room_information_ypos = 145
define gui.bdgr_music_room_information_xsize = 440

## The positions and sizes of the music controls
define gui.bdgr_music_room_options_xpos = 650
define gui.bdgr_music_room_options_ypos = 285
define gui.bdgr_music_room_options_spacing = 10
define gui.bdgr_music_room_options_button_size = 25

## The positions and sizes of the music progress bar
define gui.bdgr_music_room_progress_xsize = 596
define gui.bdgr_music_room_progress_xpos = 650
define gui.bdgr_music_room_progress_ypos = 330

## The positions and sizes of the music volume bar
define gui.bdgr_music_room_volume_xsize = 596
define gui.bdgr_music_room_volume_xpos = 650
define gui.bdgr_music_room_volume_ypos = 805


## The positions for the music progress/duration time text
 

define gui.bdgr_music_room_progress_text_xpos = 650 
define gui.bdgr_music_room_duration_text_xpos = 1205
define gui.bdgr_music_room_progress_text_ypos = 695
define gui.bdgr_music_room_text_size = 18

## The positions for the cover art and it's transform properties
define gui.bdgr_music_room_cover_art_xpos = 720
define gui.bdgr_music_room_cover_art_ypos = 205
define gui.bdgr_music_room_cover_art_size = 120

################################################################################
## Author / Name / Description

style st_song_author:
    size 38
    text_align .5
    font gui.interface_text_font
    outlines [(absolute(0), "#333b", absolute(1), absolute(1))]

style st_song_name:
    size 24
    text_align .5
    font gui.interface_text_font
    outlines [(absolute(0), "#333b", absolute(1), absolute(1))]

style st_song_description:
    size 18
    text_align .5
    font gui.interface_text_font

image authorName = DynamicDisplayable(bdgr_dynamic_author_text)
image titleName = DynamicDisplayable(bdgr_dynamic_title_text)
image songDescription = DynamicDisplayable(bdgr_dynamic_description_text)

################################################################################

image coverArt = DynamicDisplayable(bdgr_refresh_cover_data)
image readablePos = DynamicDisplayable(renpy.curry(bdgr_music_pos)(
                    "bdgr_music_room_progress_text"))
image readableDur = DynamicDisplayable(renpy.curry(bdgr_music_dur)(
                    "bdgr_music_room_duration_text"))


image playPauseButton = DynamicDisplayable(bdgr_auto_play_pause_button)

screen bdgr_music_room():
    modal True tag menu

    style_prefix "bdgr_music_room"

    default bar_val = BdgrAdjustableAudioPositionValue()
    default track_opened = bool(bdgr_game_soundtrack)

    add "images/bg/ext_beach_sunset.jpg"
    add "music_room/gui/player.png" pos(589,24)
    text translation_new["mus"] pos(815,50) style "bdgr_phone_menu" size 50 color "#e8f2fb"
    

    vbox pos(1315,167) spacing 56:
        imagebutton:
            auto "music_room/gui/volume_max_%s.png"
            action Function(preferences.set_volume, u'bdgr_music_room_mixer',
                            volume=min_func(1.0, preferences.get_volume(u'bdgr_music_room_mixer') + .1))
            mouse "hover_anim" 

        imagebutton:
            auto "music_room/gui/volume_min_%s.png"
            action Function(preferences.set_volume, u'bdgr_music_room_mixer',
                            volume=max(0.0, preferences.get_volume(u'bdgr_music_room_mixer') - .1))
            mouse "hover_anim" 
                            
    ########################################################################
    # Volume

    vbar:
        anchor (.5, .5)
        xpos 1285
        ypos 315

        ysize 280

        value Preference("bdgr_music_room_mixer volume")
        mouse "hover_anim" bottom_bar "music_room/gui/vbar_full.png" top_bar "music_room/gui/vbar_null.png" thumb "music_room/gui/vthumb_idle.png" hover_thumb "music_room/gui/vthumb_hover.png" thumb_offset 21.5

    ########################################################################

    if not track_opened:

        viewport:
            id "vpo"
            mousewheel True

            pos (637,208)
            yoffset -85

            xsize 621
            ysize 728

            has vbox
            align (.5, .5)
            spacing 7

            for st in BdgrSoundtracks:
                textbutton "[st.name]":
                    # at transform:
                    #     on hover:
                    #         easein_back .3 xoffset 15
                    #     on idle:
                    #         linear .2 xoffset 0

                    text_style "bdgr_music_room_list_button"
                    style "bdgr_music_room_button"

                    action [ SetVariable("bdgr_game_soundtrack", st),
                             SetVariable("BdgrPausedstate", False),
                             SetScreenVariable('track_opened', True),
                             Stop("music", fadeout=.5),
                             Play("bdgr_music_room", st.path, loop=BdgrLoopSong, fadein=.5) ]
                    mouse "hover_anim" 

        vbar:
            value YScrollValue("vpo")

            pos(1241,122)

            xsize 17
            ysize 727

            mouse "hover_anim" bottom_bar "music_room/gui/vbar2_list.png" top_bar "music_room/gui/vbar2_list.png" thumb "music_room/gui/vthumb2_idle.png" hover_thumb "music_room/gui/vthumb2_hover.png"


    else:

        ########################################################################
        # Album Cover

        # if bdgr_game_soundtrack.cover_art:

        add "music_room/gui/play_bg.png" pos(638,197)

        fixed:
            align (.5, .5)
            yoffset -150
            xoffset -10

            # at transform:
            #     subpixel True
            #     zoom .5
            #     alpha .0
            #     easein_back .2 alpha 1.0 zoom 1.0
            #     subpixel False

            add "coverArt":
                align (.5, .5)
                xsize 400
                fit 'cover'

            add "playPauseButton":
                align (.5, .5)
                xsize 300
                fit 'cover'

        ########################################################################
        # Meta

        if bdgr_game_soundtrack.author:

            add "authorName":
                xalign .5
                ypos 650

            add "titleName":
                xalign .5
                ypos 700

            if bdgr_game_soundtrack.description:
                add "songDescription":
                    xalign .5
                    ypos 140

        ########################################################################
        ## Loop / Random

        vbox:
            anchor (.5, .5)
            pos (694, 385)
            spacing 30
            
            
            # repeat song button
            imagebutton:
                at transform:
                    xysize (64, 64)

                if BdgrLoopSong:
                    idle "music_room/gui/repeat_hover.png"
                else:
                    auto "music_room/gui/repeat_%s.png"

                action ToggleVariable("BdgrLoopSong", False, True)
                mouse "hover_anim" 
            
            
            # random song button
            imagebutton:
                at transform:
                    xysize (64, 64)

                if BdgrRandomSong:
                    idle "music_room/gui/random_hover.png"
                else:
                    auto "music_room/gui/random_%s.png"
                
                action ToggleVariable("BdgrRandomSong", False, True) 
                mouse "hover_anim" 

            
            # next track button
            imagebutton: 
                at transform:
                    xysize (64, 64) 

                auto "music_room/gui/next_%s.png"

                if BdgrRandomSong: 
                    action [ Function(bdgr_random_song) ] 
                else: 
                    action [ Function(bdgr_next_track) ]
                mouse "hover_anim" 
                    
            
            # prev track button
            imagebutton: 
                at transform:
                    xysize (64, 64) 

                auto "music_room/gui/previous_%s.png"

                if BdgrRandomSong: 
                    action [ Function(bdgr_random_song) ] 
                else: 
                    action [ Function(bdgr_next_track, back=True) ]
                mouse "hover_anim" 
                  

        ########################################################################
        # Progress

        bar:
            at transform:
                on hover:
                    alpha 1.0

                on idle:
                    alpha .5

            style "bdgr_music_room_progress_bar"
            value bar_val
            hovered bar_val.hovered
            unhovered bar_val.unhovered
            ypos 820

            mouse "hover_anim" left_bar "music_room/gui/hbar_full.png" right_bar "music_room/gui/hbar_null.png" thumb "music_room/gui/hthumb_idle.png" hover_thumb "music_room/gui/hthumb_hover.png" thumb_offset 10

        # Do not delete
        add "readablePos" ypos 781
        add "readableDur" ypos 781


    imagebutton:
        pos (879,844)
        auto "music_room/gui/back_%s.png"
        if track_opened:
            action [ Function(bdgr_ost_quit), SetScreenVariable('track_opened', False), Play("music", "sound/music/blow_with_the_fires.ogg", fadein=.5) ]

        else:
            action [ Return(),
                     Function(bdgr_check_paused_state),
                     If(not BdgrPrevTrack, None, false=Play('music', BdgrPrevTrack, fadein=.5))]
        mouse "hover_anim" 

style bdgr_music_room_viewport is gui_viewport
style bdgr_music_room_progress_bar is gui_slider
style bdgr_music_room_volume_bar is gui_slider
style bdgr_music_room_volume_options is gui_button
style bdgr_music_room_list_button is gui_button
style bdgr_music_room_control_options is gui_button
style bdgr_music_room_setting_options is gui_button
style bdgr_music_room_information_text is gui_text
style bdgr_music_room_progress_text is gui_text
style bdgr_music_room_duration_text is gui_text

style bdgr_music_room_list_button is default:
    size gui.interface_text_size
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    outlines [(absolute(0), "#333b", absolute(1), absolute(1))]
    #hover_sound gui.hover_sound
    #activate_sound gui.activate_sound
    line_spacing 5

style bdgr_music_room_viewport:
    xpos gui.bdgr_music_room_viewport_pos
    ypos gui.bdgr_music_room_viewport_pos
    xsize gui.bdgr_music_room_viewport_xsize
    ysize gui.bdgr_music_room_viewport_ysize

style bdgr_music_room_information_text:
    font gui.interface_text_font

style bdgr_music_room_control_options:
    xpos gui.bdgr_music_room_options_xpos
    ypos gui.bdgr_music_room_options_ypos
    spacing gui.bdgr_music_room_spacing



style bdgr_music_room_progress_bar:
    xsize gui.bdgr_music_room_progress_xsize
    xpos gui.bdgr_music_room_progress_xpos
    ypos gui.bdgr_music_room_progress_ypos

style bdgr_music_room_volume_bar:
    xsize gui.bdgr_music_room_volume_xsize
    xpos gui.bdgr_music_room_volume_xpos
    ypos gui.bdgr_music_room_volume_ypos



style bdgr_music_room_progress_text:
    font gui.interface_text_font
    size gui.bdgr_music_room_text_size 
    xpos gui.bdgr_music_room_progress_text_xpos
    ypos gui.bdgr_music_room_progress_text_ypos

style bdgr_music_room_duration_text is bdgr_music_room_progress_text:
    xpos gui.bdgr_music_room_duration_text_xpos

style bdgr_music_room_information_vbox:
    xsize gui.bdgr_music_room_information_xsize
    xfill True

transform cover_art_fade:
    anchor (0.5, 0.5)
    xpos gui.bdgr_music_room_cover_art_xpos
    ypos gui.bdgr_music_room_cover_art_ypos
    size (gui.bdgr_music_room_cover_art_size, gui.bdgr_music_room_cover_art_size)
    alpha 0
    linear 0.2 alpha 1

transform imagebutton_scale:
    size(gui.bdgr_music_room_options_button_size, gui.bdgr_music_room_options_button_size)
