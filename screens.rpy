init python:

    style.bdgr_save_load_button =                            Style(style.button)
    style.bdgr_save_load_button.background =                 "bdgr/imgs/gui/save_load/saveload_idle.png"
    style.bdgr_save_load_button.hover_background =           "bdgr/imgs/gui/save_load/saveload_hover.png"
    style.bdgr_save_load_button.selected_background =        "bdgr/imgs/gui/save_load/saveload_selected.png"
    style.bdgr_save_load_button.selected_hover_background =  "bdgr/imgs/gui/save_load/saveload_selected.png"
    style.bdgr_save_load_button.selected_idle_background =   "bdgr/imgs/gui/save_load/saveload_selected.png"

    style.bdgr_phone_menu =                                   Style(style.default)
    style.bdgr_phone_menu.font =                              "bdgr/fonts/Montserrat-Regular.ttf"
    style.bdgr_phone_menu.size =                              40
    style.bdgr_phone_menu.color =                             "#fff"
    style.bdgr_phone_menu.hover_color =                       "#a4ccf1"
    style.bdgr_phone_menu.idle_outlines =                     [(2, "#ffffff00", 0, 0)]
    style.bdgr_phone_menu.hover_outlines =                    [(2, "#373950", 0, 0)]
    style.bdgr_phone_menu.background =                        Null()

    bdgr_g = Gallery()

    bdgr_page = 0
    bdgr_gallery_mode = "cg"

    bdgr_g.locked_button = get_image("gui/gallery/not_opened_idle.png")
    bdgr_g.navigation = False

    bdgr_rows = 3
    bdgr_cols = 3
    bdgr_cells = bdgr_rows * bdgr_cols


    bdgr_gallery_cg = [
    "d1_food_normal",
    ]

    bdgr_gallery_bg = [
    "bus_stop",  "ext_aidpost_day", "ext_aidpost_night",
    ]

    bdgr_gallery_sp = ["mi", "mt", "dv",]

    bdgr_gallery_sp_emo = {
    "mi" : [ "normal", "shocked", "smile", "happy", "shy", "upset", "serious", "surprise", "sad", "dontlike", "angry", "grin", "scared", "rage", "cry", "laugh", "cry_smile" ],
    "dv" : [ "normal", "angry", "smile", "sad", "rage", "grin", "guilty", "shy", "laugh", "surprise", "shocked", "scared", "cry" ],
    "mt" : [ "normal", "smile", "surprise", "rage", "angry", "sad", "grin", "laugh", "scared", "shocked" ],
    }

    bdgr_gallery_sp_dress = {
    "mi" : [ "pioneer", "swim" ],
    "dv" : [ "pioneer", "pioneer2", "swim" ],
    "mt" : [ "pioneer", "dress", "swim" ],
    }

    body = 0
    emote = 0
    dress = 0
    gallery_page = 0

    def showcase_actual(mode):
        centered = 0.5

        if mode == "bg":
            ui.add((bdgr_gallery_bg[gallery_page]), xpos=centered, ypos=centered, xalign=centered, yalign=centered)
        if mode == "spr":
            name = bdgr_gallery_sp[body]

            get_emo_list = bdgr_gallery_sp_emo.get(name)
            emo = get_emo_list[emote]

            get_dress_list = bdgr_gallery_sp_dress.get(name)
            dress_name = get_dress_list[dress]

            sprite_name = name+" "+emo+" "+dress_name

            try:
                ui.add(sprite_name, xpos=centered, ypos=1.0, xalign=centered, yalign=1.0, zoom=0.7)
            except:
                ui.text("[[ДАННЫЕ НЕДОСТУПНЫ]", xpos=centered, ypos=centered, xalign=centered, yalign=centered)

    def get_value_cnt(dic):
        name = bdgr_gallery_sp[body]

        get_some_list = dic.get(name)
        get_len = len(get_some_list)-1
        return get_len

screen bdgr_main_menu:
    modal True tag menu

    add "bdgr/imgs/gui/main_menu/main_menu_background.jpg"
    imagebutton ypos 14 auto "bdgr/imgs/gui/main_menu/phone_%s.png" action NullAction()
    add "bdgr/imgs/gui/main_menu/logo_rus.png" pos(692,392)

    imagebutton:
        pos(205,301)
        auto "bdgr/imgs/gui/main_menu/start_%s.png"
        action Start("bdgr_start")

    grid 3 2:
        pos(159,473)
        xspacing 6 yspacing 26
        imagebutton:
            auto "bdgr/imgs/gui/main_menu/load_%s.png"
            action ShowMenu("load")

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/prefs_%s.png"
            action ShowMenu("preferences")

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/gallery_%s.png"
            action ShowMenu("gallery")

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/authors_%s.png"
            action NullAction()

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/ds_%s.png"
            action NullAction()

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/vk_%s.png"
            action OpenURL("https://vk.com/es.bdgr")

    imagebutton:
        pos(300,900)
        auto "bdgr/imgs/gui/main_menu/exit_%s.png"
        action [Hide("bdgr_main_menu"), (Function(bdgr_screens_default)), ShowMenu("main_menu")]

    key "K_ESCAPE" action [Hide("bdgr_main_menu"), (Function(bdgr_screens_default)), ShowMenu("main_menu")]

screen bdgr_load:
    modal True tag menu

    window background "bdgr/imgs/gui/save_load/saveload_background.jpg":

        imagebutton auto "bdgr/imgs/gui/save_load/settings_%s.png"   pos(94,72) action ShowMenu('preferences')
        imagebutton auto "bdgr/imgs/gui/save_load/savescreen_%s.png" pos(1724,72) action ShowMenu('load')
        if _preferences.mute[u'music']:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_off_%s.png" pos(1724,183) action Preference("all mute", "disable")
        else:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_on_%s.png" pos(1724,183) action Preference("all mute", "enable")
        add "bdgr/imgs/gui/save_load/saves.png" xalign 0.5 pos(0.5,110)
        imagebutton auto "bdgr/imgs/gui/save_load/back_%s.png" pos(82,362) action Return()

        imagebutton auto "bdgr/imgs/gui/save_load/save_%s.png"   pos(395,900) action (FunctionCallback(on_save_callback,selected_slot), FileSave(selected_slot))
        imagebutton auto "bdgr/imgs/gui/save_load/load_%s.png"  pos(1232,900) action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))
        imagebutton auto "bdgr/imgs/gui/save_load/delete_%s.png" pos(848,900) action FileDelete(selected_slot)

        imagebutton auto "bdgr/imgs/gui/save_load/left_%s.png"  pos(260,0.45)  action (FilePageNext(10,True,False,False), SetVariable("selected_slot", False))
        imagebutton auto "bdgr/imgs/gui/save_load/right_%s.png" pos(1580,0.45) action (FilePagePrevious(10,True,False,False) , SetVariable("selected_slot", False))

        grid bdgr_rows bdgr_cols:
            area(305,160,1276,725)
            transpose False
            xfill True
            yfill True
            for i in range(1, 10):

                fixed:
                    add FileScreenshot(i) pos(30,30) zoom 1.2
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "bdgr_save_load_button"
                        has fixed
                    text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" color "#fff" text_align 1.0 xalign 1.0 pos(0.96,35)

screen bdgr_save:
    modal True tag menu
    use bdgr_load

screen bdgr_gallery:
    modal True tag menu

    $ bdgr_gallery_table = []
    if bdgr_gallery_mode == "cg":
        $ bdgr_gallery_table = bdgr_gallery_cg
    else:
        $ bdgr_gallery_table = bdgr_gallery_bg

    $ bdgr_len_table = len(bdgr_gallery_table)

    frame background "bdgr/imgs/gui/save_load/saveload_background.jpg":

        if bdgr_gallery_mode == "cg":
            textbutton translation_new["MUSIC"] style "bdgr_phone_menu" text_style "settings_link" xalign 0.02 yalign 0.08 action NullAction()#(SetVariable('bdgr_page', 0), ShowMenu("music_room"))
            imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(1724,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), ShowMenu("gallery"))
            add "bdgr/imgs/gui/save_load/CG.png" xalign 0.5 pos(0.5,115)
        elif bdgr_gallery_mode == "bg":
            imagebutton auto "bdgr/imgs/gui/save_load/cg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "cg"), SetVariable('bdgr_page', 0), ShowMenu("gallery"))
            imagebutton auto "bdgr/imgs/gui/save_load/spr_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), ShowMenu("gallery_sp"))
            add "bdgr/imgs/gui/save_load/BG.png" xalign 0.5 pos(0.5,113)

        if _preferences.mute[u'music']:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_off_%s.png" pos(1724,183) action Preference("all mute", "disable")
        else:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_on_%s.png" pos(1724,183) action Preference("all mute", "enable")
        imagebutton auto "bdgr/imgs/gui/save_load/back_%s.png" pos(82,362) action Return()

        grid bdgr_rows bdgr_cols:
            area(305,160,1276,725)
            xfill True
            yfill True
            $ cg_displayed = 0
            $ next_page = bdgr_page + 1
            if next_page > int(bdgr_len_table/bdgr_cells):
                $ next_page = 0
            for n in range(0, bdgr_len_table):
                if n < (bdgr_page+1)*bdgr_cells and n>=bdgr_page*bdgr_cells:
                    python:
                        if bdgr_gallery_mode == "cg":
                            _t = im.Crop("images/cg/"+bdgr_gallery_table[n]+".jpg" , (0,0,1920,1080))
                        elif bdgr_gallery_mode == "bg":
                            _t = im.Crop("images/bg/"+bdgr_gallery_table[n]+".jpg" , (0,0,1920,1080))
                        th = im.Scale(_t,  385, 210)
                        img = im.Composite((424,255),(30,30),im.Alpha(th,0.9),(5,2),im.Image("bdgr/imgs/gui/save_load/saveload_idle.png"))
                        imgh = im.Composite((424,255),(30,30),th,(5,2),im.Image("bdgr/imgs/gui/save_load/saveload_hover.png"))
                        alfa = im.Alpha("bdgr/imgs/gui/save_load/saveload_idle.png", 1.0)
                    add g.make_button(bdgr_gallery_table[n], alfa, None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                    $ cg_displayed += 1

                    if n+1 == bdgr_len_table:
                        $ next_page = 0

            for j in range(0, bdgr_cells-cg_displayed):
                null

        if bdgr_page != 0:
            imagebutton auto "bdgr/imgs/gui/save_load/left_%s.png" pos(262,0.45) action (SetVariable('bdgr_page', bdgr_page-1), ShowMenu("gallery"))
        else:
            imagebutton auto "bdgr/imgs/gui/save_load/left_%s.png" pos(262,0.45) action NullAction()
        imagebutton auto "bdgr/imgs/gui/save_load/right_%s.png" pos(1562,0.45) action (SetVariable('bdgr_page', next_page), ShowMenu("gallery"))


screen bdgr_gallery_sp:
    modal True tag menu

    $ persistent.sprite_time = "day"

    frame:
        area(919,134,700,723)
        $ showcase_actual("bg")
        $ showcase_actual("spr")

    add "bdgr/imgs/gui/sprites/front.png"
    add "bdgr/imgs/gui/sprites/sprites_text.png" pos(801,-3)

    imagebutton auto "bdgr/imgs/gui/save_load/cg_%s.png" pos(0,9) action (SetVariable('bdgr_gallery_mode', "cg"), SetVariable('bdgr_page', 0), ShowMenu("gallery"))
    imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(1811,9) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), ShowMenu("gallery"))
    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(286,879) action Return()

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(187,258) action ShowMenu("bdgr_show_spr")
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(407,254) action ShowMenu("bdgr_show_dress")
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(185,471) action ShowMenu("bdgr_show_emo")
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(396,471) action ShowMenu("bdgr_show_bg")

screen bdgr_show_bg:
    modal True

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(187,258) action [ShowMenu("bdgr_show_spr"), Hide("bdgr_show_bg")]
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(407,254) action [ShowMenu("bdgr_show_dress"), Hide("bdgr_show_bg")]
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(185,471) action [ShowMenu("bdgr_show_emo"), Hide("bdgr_show_bg")]
    imagebutton idle "bdgr/imgs/gui/sprites/bg_hover.png" pos(396,471) action NullAction()

    if gallery_page < len(bdgr_gallery_bg)-1:
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action SetVariable("gallery_page", gallery_page+1)
    if gallery_page != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action SetVariable("gallery_page", gallery_page-1)

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(286,879) action Hide("bdgr_show_bg")

screen bdgr_show_spr:
    modal True

    imagebutton idle "bdgr/imgs/gui/sprites/sprites_hover.png" pos(187,258) action NullAction()
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(407,254) action [ShowMenu("bdgr_show_dress"), Hide("bdgr_show_spr")]
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(185,471) action [ShowMenu("bdgr_show_emo"), Hide("bdgr_show_spr")]
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(396,471) action [ShowMenu("bdgr_show_bg"), Hide("bdgr_show_spr")]

    if body < len(bdgr_gallery_sp)-1:
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action [SetVariable("emote", 0), SetVariable("dress", 0), SetVariable("body", body+1)]
    if body != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action [SetVariable("emote", 0), SetVariable("dress", 0), SetVariable("body", body-1)]

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(286,879) action Hide("bdgr_show_spr")

screen bdgr_show_dress:
    modal True

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(187,258) action [ShowMenu("bdgr_show_spr"), Hide("bdgr_show_dress")]
    imagebutton idle "bdgr/imgs/gui/sprites/dress_hover.png" pos(407,254) action NullAction()
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(185,471) action [ShowMenu("bdgr_show_emo"), Hide("bdgr_show_dress")]
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(396,471) action [ShowMenu("bdgr_show_bg"), Hide("bdgr_show_dress")]

    if dress < get_value_cnt(bdgr_gallery_sp_dress):
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action SetVariable("dress", dress+1)
    if dress != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action SetVariable("dress", dress-1)

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(286,879) action Hide("bdgr_show_dress")

screen bdgr_show_emo:
    modal True

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(187,258) action [ShowMenu("bdgr_show_spr"), Hide("bdgr_show_emo")]
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(407,254) action [ShowMenu("bdgr_show_dress"), Hide("bdgr_show_emo")]
    imagebutton idle "bdgr/imgs/gui/sprites/emo_hover.png" pos(185,471) action NullAction()
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(396,471) action [ShowMenu("bdgr_show_bg"), Hide("bdgr_show_emo")]

    if emote < get_value_cnt(bdgr_gallery_sp_emo):
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action SetVariable("emote", emote+1)
    if emote != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action SetVariable("emote", emote-1)

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(286,879) action Hide("bdgr_show_emo")

screen bdgr_preferences:
    modal True tag menu

    window background "bdgr/imgs/gui/save_load/saveload_background.jpg":

        imagebutton auto "bdgr/imgs/gui/save_load/settings_%s.png"   pos(94,72) action ShowMenu('preferences')
        imagebutton auto "bdgr/imgs/gui/save_load/savescreen_%s.png" pos(1724,72) action ShowMenu('load')
        if _preferences.mute[u'music'] and _preferences.mute[u'sfx'] and _preferences.mute[u'voice']:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_off_%s.png" pos(1724,183) action Preference("all mute", "disable")
        else:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_on_%s.png" pos(1724,183) action Preference("all mute", "enable")
        imagebutton auto "bdgr/imgs/gui/save_load/back_%s.png" pos(82,362) action Return()

        add "bdgr/imgs/gui/settings/preferences.png" xalign 0.5 pos(0.5,110)
        add "bdgr/imgs/gui/settings/vbar.png" pos(1612,155)

        side "c r":
            area (311,166,1340,780)
            viewport id "preferences":
                xmaximum 1250
                mousewheel True
                scrollbars None
                has grid 1 16

                null

                grid 3 1 xfill True:
                    text translation_new["Window_mode"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if not _preferences.fullscreen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Window"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("display", "window")

                    hbox:
                        if _preferences.fullscreen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Fullscreen"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("display", "fullscreen")


                text translation_new["game_mode"] style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 1 2:
                    hbox:
                        if persistent.game_mode == "animated":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton "{color=#a4ccf1}"+translation_new["the_interactive"]+"{/color}"+translation_new["interactive_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "static")
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["the_interactive"]+translation_new["interactive_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "animated")

                    hbox:
                        if persistent.game_mode == "static":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton "{color=#a4ccf1}"+translation_new["the_static"]+"{/color}"+translation_new["static_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "animated")
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["the_static"]+translation_new["static_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "static")


                text translation_new["the_text"] style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 3 1 xfill True:
                    text translation_new["Autoforward"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if _preferences.afm_time != 0:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["on"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("auto-forward after click", "enable")

                    hbox:
                        if _preferences.afm_time == 0:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["off"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                grid 2 1 xfill True:
                    text translation_new["Autoforward_time"]+":" style "bdgr_phone_menu"
                    bar value Preference("auto-forward time") left_bar "bdgr/imgs/gui/settings/bar_full.png" right_bar "bdgr/imgs/gui/settings/bar_null.png" thumb "bdgr/imgs/gui/settings/htumb.png" hover_thumb "bdgr/imgs/gui/settings/htumb.png" xalign 1.0 xmaximum 606 ymaximum 51
                
                grid 3 1 xfill True:
                    text translation_new["Font"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if persistent.font_size == "small":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["small"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetField(persistent, "font_size", "small")

                    hbox:
                        if not persistent.font_size == "small":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["large"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetField(persistent, "font_size", "large")
                
                grid 3 1 xfill True:
                    text translation_new["Skip"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if not _preferences.skip_unseen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Skip_seen"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("skip", "seen") 

                    hbox:
                        if _preferences.skip_unseen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Skip_all"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("skip", "all")

                grid 2 1 xfill True:
                    text translation_new["Text_speed"]+":" style "bdgr_phone_menu"
                    bar value Preference("text speed") left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" xalign 1.0 xmaximum 604 ymaximum 60


                text translation_new["Volume"]+":" style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" action Play("sound", "sound/test.ogg")
                    bar value Preference("music volume") left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" xalign 1.0 xmaximum 604 ymaximum 60

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" action Play("sound", "sound/test.ogg")
                    bar value Preference("sound volume") left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" xalign 1.0 xmaximum 604 ymaximum 60

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" action Play("sound", "sound/test.ogg")
                    bar value Preference("voice volume") left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" xalign 1.0 xmaximum 604 ymaximum 60


                text translation_new["Language"]+":" style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid  2 1 xfill True:
                    hbox:
                        if _preferences.language == None:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton translation_new["Russian"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action NullAction()
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["Russian"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action (SetField(config, "window_title", "Бесконечное Лето"), SetField(persistent, "show_hentai_ach", False), Language(None), Function(reload_names), Function(stop_music), Function(bdgr_screens_save_activate), Function(renpy.utter_restart))

                    hbox:
                        if _preferences.language == "english":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton translation_new["English"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action NullAction()
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["English"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action (SetField(config, "window_title", "Everlasting Summer"), SetField(persistent, "show_hentai_ach", False), Language("english"), Function(reload_names), Function(stop_music), Function(bdgr_screens_save_activate), Function(renpy.utter_restart))


            vbar value YScrollValue("preferences") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "bdgr/imgs/gui/settings/vthumb.png" xpos 14 xmaximum 46 ymaximum 804
