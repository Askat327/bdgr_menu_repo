init python:

    # Стиль кнопок в меню сохранений/загрузки
    style.bdgr_save_load_button =                            Style(style.button)
    style.bdgr_save_load_button.background =                 "bdgr/imgs/gui/save_load/saveload_idle.png"
    style.bdgr_save_load_button.hover_background =           "bdgr/imgs/gui/save_load/saveload_hover.png"
    style.bdgr_save_load_button.selected_background =        "bdgr/imgs/gui/save_load/saveload_selected.png"
    style.bdgr_save_load_button.selected_hover_background =  "bdgr/imgs/gui/save_load/saveload_selected.png"
    style.bdgr_save_load_button.selected_idle_background =   "bdgr/imgs/gui/save_load/saveload_selected.png"

    # Стиль текстовых кнопок (и текста тоже) в меню настроек
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

    # Спсиок ЦГ
    bdgr_gallery_cg = [
    "d1_food_normal",
    ]

    # Список БГ
    bdgr_gallery_bg = [
    "bus_stop",  "ext_aidpost_day", "ext_aidpost_night",
    ]

    # Список спрайтов
    bdgr_gallery_sp = ["mi", "mt", "dv",]

    # Словарь эмоций
    bdgr_gallery_sp_emo = {
    "mi" : [ "normal", "shocked", "smile", "happy", "shy", "upset", "serious", "surprise", "sad", "dontlike", "angry", "grin", "scared", "rage", "cry", "laugh", "cry_smile" ],
    "dv" : [ "normal", "angry", "smile", "sad", "rage", "grin", "guilty", "shy", "laugh", "surprise", "shocked", "scared", "cry" ],
    "mt" : [ "normal", "smile", "surprise", "rage", "angry", "sad", "grin", "laugh", "scared", "shocked" ],
    }

    # Словарь одежды
    bdgr_gallery_sp_dress = {
    "mi" : [ "pioneer", "swim" ],
    "dv" : [ "pioneer", "pioneer2", "swim" ],
    "mt" : [ "pioneer", "dress", "swim" ],
    }

    # Страницы в меню просмотра спрайтов
    body = 0
    emote = 0
    dress = 0
    gallery_page = 0

    def showcase_actual(mode):
        """
        Волшебная функция для экрана просмотра спрайтов
        """
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
                pass
                # ui.text("[[ДАННЫЕ НЕДОСТУПНЫ]", xpos=centered, ypos=centered, xalign=centered, yalign=centered)

    def get_value_cnt(dic):
        """
        Функция для предотвращения ошибок с несуществующими спрайтами
        """
        name = bdgr_gallery_sp[body]

        get_some_list = dic.get(name)
        get_len = len(get_some_list)-1
        return get_len

    def music_pause():
        renpy.music.set_pause(True)
    def music_unpause():
        renpy.music.set_pause(False)

init:
    image bdgr_skip_anim_winter:
        "bdgr/imgs/gui/dialogue_box/winter/skip_1.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_2.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_3.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_4.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_5.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_6.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_7.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/winter/skip_8.png"
        pause 0.1
        repeat

    image bdgr_skip_anim_spring:
        "bdgr/imgs/gui/dialogue_box/spring/skip_1.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_2.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_3.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_4.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_5.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_6.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_7.png"
        pause 0.1
        "bdgr/imgs/gui/dialogue_box/spring/skip_8.png"
        pause 0.1
        repeat

    screen bdgr_skip_button():
        $ timeofday = persistent.bdgr_timeofday

        # if not config.skipping:
        #     imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/forward_%s.png" pos(1810,946) action Skip() mouse "hover_anim"
        # else:
        if config.skipping:
            if timeofday == "winter":
                add "bdgr_skip_anim_winter" pos(1810,946)
            elif  timeofday == "spring":
                add "bdgr_skip_anim_spring" pos(1810,946)
    
    screen mm_music_button():
        if renpy.music.get_pause():
            imagebutton auto "bdgr/imgs/gui/save_load/sound_off_%s.png" pos(1724,183) action Function(music_unpause) mouse "hover_anim"
        else:
            imagebutton auto "bdgr/imgs/gui/save_load/sound_on_%s.png" pos(1724,183) action Function(music_pause) mouse "hover_anim"

screen bdgr_main_menu:
    modal True tag menu

    add "bdgr/imgs/gui/main_menu/main_menu_background.jpg"
    imagebutton ypos 14 auto "bdgr/imgs/gui/main_menu/phone_%s.png" action NullAction()
    add "bdgr/imgs/gui/main_menu/logo_rus.png" pos(692,392)

    imagebutton:
        pos(205,301)
        auto "bdgr/imgs/gui/main_menu/start_%s.png"
        action Start("bdgr_start") mouse "hover_anim"

    grid 3 2:
        pos(159,473)
        xspacing 6 yspacing 26
        imagebutton:
            auto "bdgr/imgs/gui/main_menu/load_%s.png"
            action ShowMenu("load") mouse "hover_anim"

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/prefs_%s.png"
            action ShowMenu("preferences") mouse "hover_anim"

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/gallery_%s.png"
            action ShowMenu("gallery") mouse "hover_anim"

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/authors_%s.png"
            action NullAction() mouse "hover_anim"

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/ds_%s.png"
            action NullAction() mouse "hover_anim"

        imagebutton:
            auto "bdgr/imgs/gui/main_menu/vk_%s.png"
            action OpenURL("https://vk.com/es.bdgr") mouse "hover_anim"

    imagebutton:
        pos(300,900)
        auto "bdgr/imgs/gui/main_menu/exit_%s.png"
        action [Hide("bdgr_main_menu"), (Function(bdgr_screens_default)), ShowMenu("main_menu")] mouse "hover_anim"

    key "K_ESCAPE" action [Hide("bdgr_main_menu"), (Function(bdgr_screens_default)), ShowMenu("main_menu")]

screen bdgr_load:
    modal True tag menu

    window background "bdgr/imgs/gui/save_load/saveload_background.jpg":

        imagebutton auto "bdgr/imgs/gui/save_load/settings_%s.png"   pos(94,72) action ShowMenu('preferences') mouse "hover_anim"
        imagebutton auto "bdgr/imgs/gui/save_load/savescreen_%s.png" pos(1724,72) action ShowMenu('load') mouse "hover_anim"
        use mm_music_button
        add "bdgr/imgs/gui/save_load/saves.png" xalign 0.5 pos(0.5,110)
        imagebutton auto "bdgr/imgs/gui/save_load/back_%s.png" pos(82,362) action Return() mouse "hover_anim"

        imagebutton auto "bdgr/imgs/gui/save_load/save_%s.png"   pos(395,900) action (FunctionCallback(on_save_callback,selected_slot), FileSave(selected_slot)) mouse "hover_anim"
        imagebutton auto "bdgr/imgs/gui/save_load/load_%s.png"  pos(1232,900) action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot)) mouse "hover_anim"
        imagebutton auto "bdgr/imgs/gui/save_load/delete_%s.png" pos(848,900) action FileDelete(selected_slot) mouse "hover_anim"

        imagebutton auto "bdgr/imgs/gui/save_load/left_%s.png"  pos(260,0.45)  action (FilePageNext(10,True,False,False), SetVariable("selected_slot", False)) mouse "hover_anim"
        imagebutton auto "bdgr/imgs/gui/save_load/right_%s.png" pos(1580,0.45) action (FilePagePrevious(10,True,False,False) , SetVariable("selected_slot", False)) mouse "hover_anim"

        grid bdgr_rows bdgr_cols:
            area(305,160,1276,725)
            transpose False
           
            yfill True
            for i in range(1, 10):

                fixed:
                    add FileScreenshot(i) pos(30,30) zoom 1.2
                    button:
                        action SetVariable("selected_slot", i)
                        mouse "hover_anim"
                        xfill False
                        yfill False
                        style "bdgr_save_load_button"
                        has fixed
                    text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" color "#fff" text_align 1.0 xalign 1.0 pos(0.96,35)

screen bdgr_save: # Т.к. загрузочное меню и меню сохранения едины
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
            imagebutton auto "bdgr/imgs/gui/save_load/mus_%s.png" pos(94,72) action (SetVariable('bdgr_page', 0), ShowMenu("music_room")) mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(1724,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), ShowMenu("gallery")) mouse "hover_anim"
            add "bdgr/imgs/gui/save_load/CG.png" xalign 0.5 pos(0.5,115)
        elif bdgr_gallery_mode == "bg":
            imagebutton auto "bdgr/imgs/gui/save_load/cg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "cg"), SetVariable('bdgr_page', 0), ShowMenu("gallery")) mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/save_load/spr_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), ShowMenu("gallery_sp")) mouse "hover_anim"
            add "bdgr/imgs/gui/save_load/BG.png" xalign 0.5 pos(0.5,113)

        use mm_music_button
        imagebutton auto "bdgr/imgs/gui/save_load/back_%s.png" pos(82,362) action Return() mouse "hover_anim"

        grid bdgr_rows bdgr_cols:
            area(305,160,1276,725)
           
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
            imagebutton auto "bdgr/imgs/gui/save_load/left_%s.png" pos(262,0.45) action (SetVariable('bdgr_page', bdgr_page-1), ShowMenu("gallery")) mouse "hover_anim"
        else:
            imagebutton auto "bdgr/imgs/gui/save_load/left_%s.png" pos(262,0.45) action NullAction()
        imagebutton auto "bdgr/imgs/gui/save_load/right_%s.png" pos(1562,0.45) action (SetVariable('bdgr_page', next_page), ShowMenu("gallery")) mouse "hover_anim"


screen bdgr_gallery_sp:
    modal True tag menu

    $ persistent.sprite_time = "day"

    frame:
        area(919,134,700,723)
        $ showcase_actual("bg")
        $ showcase_actual("spr")

    add "bdgr/imgs/gui/sprites/front.png"
    text translation_new["chars"] pos(785,70) style "bdgr_phone_menu" size 50 color "#e8f2fb"

    imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), ShowMenu("gallery")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/save_load/mus_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), ShowMenu("music_room")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Return() mouse "hover_anim"
    use mm_music_button

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(291,343) action ShowMenu("bdgr_show_spr") mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(452,343) action ShowMenu("bdgr_show_dress") mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(291,518) action ShowMenu("bdgr_show_emo") mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(452,518) action ShowMenu("bdgr_show_bg") mouse "hover_anim"

screen bdgr_show_bg:
    modal True

    imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), Hide("bdgr_show_bg"), ShowMenu("gallery")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/save_load/mus_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), Hide("bdgr_show_bg"), ShowMenu("music_room")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Return() mouse "hover_anim"
    use mm_music_button

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(291,343) action [ShowMenu("bdgr_show_spr"), Hide("bdgr_show_bg")] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(452,343) action [ShowMenu("bdgr_show_dress"), Hide("bdgr_show_bg")] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(291,518) action [ShowMenu("bdgr_show_emo"), Hide("bdgr_show_bg")] mouse "hover_anim"
    imagebutton idle "bdgr/imgs/gui/sprites/bg_hover.png" pos(452,518) action Return() mouse "hover_anim"

    if gallery_page < len(bdgr_gallery_bg)-1:
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action SetVariable("gallery_page", gallery_page+1) mouse "hover_anim"
    if gallery_page != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action SetVariable("gallery_page", gallery_page-1) mouse "hover_anim"

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Hide("bdgr_show_bg") mouse "hover_anim"

screen bdgr_show_spr:
    modal True

    imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), Hide("bdgr_show_spr"), ShowMenu("gallery")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/save_load/mus_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), Hide("bdgr_show_spr"), ShowMenu("music_room")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Return() mouse "hover_anim"
    use mm_music_button

    imagebutton idle "bdgr/imgs/gui/sprites/sprites_hover.png" pos(291,343) action Return() mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(452,343) action [ShowMenu("bdgr_show_dress"), Hide("bdgr_show_spr")] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(291,518) action [ShowMenu("bdgr_show_emo"), Hide("bdgr_show_spr")] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(452,518) action [ShowMenu("bdgr_show_bg"), Hide("bdgr_show_spr")] mouse "hover_anim"

    if body < len(bdgr_gallery_sp)-1:
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action [SetVariable("emote", 0), SetVariable("dress", 0), SetVariable("body", body+1)] mouse "hover_anim"
    if body != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action [SetVariable("emote", 0), SetVariable("dress", 0), SetVariable("body", body-1)] mouse "hover_anim"

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Hide("bdgr_show_spr") mouse "hover_anim"

screen bdgr_show_dress:
    modal True

    imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), Hide("bdgr_show_dress"), ShowMenu("gallery")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/save_load/mus_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), Hide("bdgr_show_dress"), ShowMenu("music_room")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Return() mouse "hover_anim"
    use mm_music_button

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(291,343) action [ShowMenu("bdgr_show_spr"), Hide("bdgr_show_dress")] mouse "hover_anim"
    imagebutton idle "bdgr/imgs/gui/sprites/dress_hover.png" pos(452,343) action Return() mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/emo_%s.png" pos(291,518) action [ShowMenu("bdgr_show_emo"), Hide("bdgr_show_dress")] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(452,518) action [ShowMenu("bdgr_show_bg"), Hide("bdgr_show_dress")] mouse "hover_anim"

    if dress < get_value_cnt(bdgr_gallery_sp_dress):
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action SetVariable("dress", dress+1) mouse "hover_anim"
    if dress != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action SetVariable("dress", dress-1) mouse "hover_anim"

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Hide("bdgr_show_dress") mouse "hover_anim"

screen bdgr_show_emo:
    modal True

    imagebutton auto "bdgr/imgs/gui/save_load/bg_%s.png" pos(94,72) action (SetVariable('bdgr_gallery_mode', "bg"), SetVariable('bdgr_page', 0), Hide("bdgr_show_emo"), ShowMenu("gallery")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/save_load/mus_%s.png" pos(1724,72) action (SetVariable('bdgr_page', 0), Hide("bdgr_show_emo"), ShowMenu("music_room")) mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Return() mouse "hover_anim"
    use mm_music_button

    imagebutton auto "bdgr/imgs/gui/sprites/sprites_%s.png" pos(291,343) action [ShowMenu("bdgr_show_spr"), Hide("bdgr_show_emo")] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/dress_%s.png" pos(452,343) action [ShowMenu("bdgr_show_dress"), Hide("bdgr_show_emo")] mouse "hover_anim"
    imagebutton idle "bdgr/imgs/gui/sprites/emo_hover.png" pos(291,518) action Return() mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/sprites/bg_%s.png" pos(452,518) action [ShowMenu("bdgr_show_bg"), Hide("bdgr_show_emo")] mouse "hover_anim"

    if emote < get_value_cnt(bdgr_gallery_sp_emo):
        imagebutton auto "bdgr/imgs/gui/sprites/right_%s.png" pos(1513,444) action SetVariable("emote", emote+1) mouse "hover_anim"
    if emote != 0:
        imagebutton auto "bdgr/imgs/gui/sprites/left_%s.png" pos(900,444) action SetVariable("emote", emote-1) mouse "hover_anim"

    imagebutton auto "bdgr/imgs/gui/sprites/back_%s.png" pos(377,833) action Hide("bdgr_show_emo") mouse "hover_anim"

screen bdgr_preferences:
    modal True tag menu

    window background "bdgr/imgs/gui/save_load/saveload_background.jpg":

        imagebutton auto "bdgr/imgs/gui/save_load/settings_%s.png"   pos(94,72) action ShowMenu('preferences') mouse "hover_anim"
        imagebutton auto "bdgr/imgs/gui/save_load/savescreen_%s.png" pos(1724,72) action ShowMenu('load') mouse "hover_anim"
        use mm_music_button
        imagebutton auto "bdgr/imgs/gui/save_load/back_%s.png" pos(82,362) action Return() mouse "hover_anim"

        add "bdgr/imgs/gui/settings/preferences.png" xalign 0.5 pos(0.5,110)
        add "bdgr/imgs/gui/settings/vbar.png" pos(1612,155)

        side "c r":
            area (311,166,1340,780)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 17 xfill True spacing 15
                null
                grid 3 1 xfill True:
                    text translation_new["Window_mode"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if not _preferences.fullscreen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Window"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("display", "window") mouse "hover_anim"

                    hbox:
                        if _preferences.fullscreen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Fullscreen"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("display", "fullscreen") mouse "hover_anim"

                text translation_new["game_mode"] style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 1 1 xfill True:
                    hbox:
                        if persistent.game_mode == "animated":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton "{color=#a4ccf1}"+translation_new["the_interactive"]+"{/color}"+translation_new["interactive_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "static") mouse "hover_anim"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["the_interactive"]+translation_new["interactive_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "animated") mouse "hover_anim"

                grid 1 1 xfill True:
                    hbox:
                        if persistent.game_mode == "static":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton "{color=#a4ccf1}"+translation_new["the_static"]+"{/color}"+translation_new["static_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "animated") mouse "hover_anim"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["the_static"]+translation_new["static_desc"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetVariable("persistent.game_mode", "static") mouse "hover_anim"

                text translation_new["the_text"] style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 3 1 xfill True:
                    text translation_new["Autoforward"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if _preferences.afm_time != 0:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["on"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("auto-forward after click", "enable") mouse "hover_anim"

                    hbox:
                        if _preferences.afm_time == 0:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["off"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable")) mouse "hover_anim"

                grid 2 1:
                    text translation_new["Autoforward_time"]+":" style "bdgr_phone_menu"
                    bar value Preference("auto-forward time") mouse "hover_anim" left_bar "bdgr/imgs/gui/settings/bar_full.png" right_bar "bdgr/imgs/gui/settings/bar_null.png" thumb "bdgr/imgs/gui/settings/htumb.png" hover_thumb "bdgr/imgs/gui/settings/htumb.png" thumb_offset 33 xsize 630 ysize 51 left_gutter 30
                
                grid 3 1 xfill True:
                    text translation_new["Font"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if persistent.font_size == "small":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["small"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetField(persistent, "font_size", "small") mouse "hover_anim"

                    hbox:
                        if not persistent.font_size == "small":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["large"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action SetField(persistent, "font_size", "large") mouse "hover_anim"
                
                grid 3 1 xfill True:
                    text translation_new["Skip"]+":" style "bdgr_phone_menu" yalign 0.5

                    hbox:
                        if not _preferences.skip_unseen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Skip_seen"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("skip", "seen") mouse "hover_anim"

                    hbox:
                        if _preferences.skip_unseen:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                        textbutton translation_new["Skip_all"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action Preference("skip", "all") mouse "hover_anim"

                grid 2 1:
                    text translation_new["Text_speed"]+":" style "bdgr_phone_menu"
                    bar value Preference("text speed") mouse "hover_anim" left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" thumb_offset 35 xsize 628 ysize 60 left_gutter 30

                text translation_new["Volume"]+":" style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 2 1:
                    textbutton translation_new["Music_lower"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" action Play("sound", "sound/test.ogg") mouse "hover_anim"
                    bar value Preference("music volume") mouse "hover_anim" left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" thumb_offset 35 xsize 628 ysize 60 left_gutter 30

                grid 2 1:
                    textbutton translation_new["Sound"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" action Play("sound", "sound/test.ogg") mouse "hover_anim"
                    bar value Preference("sound volume") mouse "hover_anim" left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" thumb_offset 35 xsize 628 ysize 60 left_gutter 30

                grid 2 1:
                    textbutton translation_new["Ambience"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" action Play("sound", "sound/test.ogg") mouse "hover_anim"
                    bar value Preference("voice volume") mouse "hover_anim" left_bar "bdgr/imgs/gui/settings/second_bar_full.png" right_bar "bdgr/imgs/gui/settings/second_bar_null.png" thumb "bdgr/imgs/gui/settings/second_htumb.png" hover_thumb "bdgr/imgs/gui/settings/second_htumb.png" thumb_offset 35 xsize 628 ysize 60 left_gutter 30

                text translation_new["Language"]+":" style "bdgr_phone_menu" xalign 0.5 color "#a4ccf1" size 55
                grid 2 1 xfill True:
                    hbox:
                        if _preferences.language == None:
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton translation_new["Russian"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action NullAction()
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["Russian"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action (SetField(config, "window_title", "Бесконечное Лето"), SetField(persistent, "show_hentai_ach", False), Language(None), Function(reload_names), Function(stop_music), Function(bdgr_screens_save_activate), Function(renpy.utter_restart)) mouse "hover_anim"

                    hbox:
                        if _preferences.language == "english":
                            add "bdgr/imgs/gui/settings/snowflake_on.png"
                            textbutton translation_new["English"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action NullAction()
                        else:
                            add "bdgr/imgs/gui/settings/snowflake_off.png"
                            textbutton translation_new["English"] style "bdgr_phone_menu" text_style "bdgr_phone_menu" yalign 0.5 action NullAction()#(SetField(config, "window_title", "Everlasting Summer"), SetField(persistent, "show_hentai_ach", False), Language("english"), Function(reload_names), Function(stop_music), Function(bdgr_screens_save_activate), Function(renpy.utter_restart)) mouse "hover_anim"

            vbar value YScrollValue("preferences") mouse "hover_anim" bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "bdgr/imgs/gui/settings/vthumb.png" xpos 14 xmaximum 46 ymaximum 804


screen bdgr_yesno_prompt:
    modal True
    $ tod = persistent.bdgr_timeofday

    add "bdgr/imgs/gui/o_rly/"+tod+"/based.png" xalign 0.5 yalign 0.5
    text _(message) text_align 0.5 yalign 0.46 xalign 0.5 style "bdgr_phone_menu"
    imagebutton auto "bdgr/imgs/gui/o_rly/"+tod+"/yes_%s.png" yalign 0.56 xalign 0.35 action [yes_action, Function(bdgr_mouse_change)] mouse "hover_anim"
    imagebutton auto "bdgr/imgs/gui/o_rly/"+tod+"/no_%s.png" yalign 0.56 xalign 0.65 action no_action mouse "hover_anim"


screen bdgr_game_menu_selector:
    modal True tag menu
    $ tod = persistent.bdgr_timeofday

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    add "bdgr/imgs/gui/ingame_menu/"+tod+"/ingame_menu.png" xalign 0.5 yalign 0.5
    imagemap:
        auto "bdgr/imgs/gui/ingame_menu/"+tod+"/ingame_menu_%s.png" xalign 0.5 yalign 0.5
        hotspot (133, 68,  478, 63) focus_mask None clicked MainMenu() mouse "hover_anim"
        hotspot (133, 133, 478, 63) focus_mask None clicked ShowMenu('save') mouse "hover_anim"
        hotspot (133, 197, 478, 63) focus_mask None clicked ShowMenu('load') mouse "hover_anim"
        hotspot (133, 262, 478, 63) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector')) mouse "hover_anim"
        hotspot (133, 326, 478, 63) focus_mask None clicked ShowMenu('quit') mouse "hover_anim"


screen bdgr_say:

    window background None id "window":

        $ timeofday = persistent.bdgr_timeofday

        if persistent.font_size == "large":

            add "bdgr/imgs/gui/dialogue_box/"+timeofday+"/dialogue_box_large.png" pos(128,858)

            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/save_%s.png"  pos(1602,865) action ShowMenu('save') mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/load_%s.png"  pos(1646,865) action ShowMenu('load') mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/hide_%s.png"  pos(1690,865) action HideInterface() mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/pause_%s.png" pos(1732,865) action ShowMenu('game_menu_selector') mouse "hover_anim"

            text what id "what" xpos 159 ypos 924 xmaximum 1541 size 23 line_spacing 1 font "bdgr/fonts/Montserrat-Regular.ttf"
            if who:
                text who id "who" xpos 159 ypos 875 size 26 line_spacing 1 font "bdgr/fonts/Montserrat-Regular.ttf"

        elif persistent.font_size == "small":

            add "bdgr/imgs/gui/dialogue_box/"+timeofday+"/dialogue_box.png" pos(128,898)

            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/save_%s.png"  pos(1602,898) action ShowMenu('save') mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/load_%s.png"  pos(1646,898) action ShowMenu('load') mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/hide_%s.png"  pos(1690,898) action HideInterface() mouse "hover_anim"
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/pause_%s.png" pos(1732,898) action ShowMenu('game_menu_selector') mouse "hover_anim"

            text what id "what" xpos 159 ypos 958 xmaximum 1541 size 23 line_spacing 1 font "bdgr/fonts/Montserrat-Regular.ttf"
            if who:
                text who id "who" xpos 159 ypos 914 size 26 line_spacing 1 font "bdgr/fonts/Montserrat-Regular.ttf"


        imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/backward_%s.png" pos(31,946) action ShowMenu("text_history") mouse "hover_anim"

        # use bdgr_skip_button
        if not config.skipping:
            imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/forward_%s.png" pos(1810,946) action Skip() mouse "hover_anim"


screen bdgr_nvl:

    $ timeofday = persistent.bdgr_timeofday

    window background Frame("bdgr/imgs/gui/dialogue_box/"+timeofday+"/nvl.png",103,17) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 5
                if persistent.font_size == "large":
                    if who is not None:
                        text who id who_id size 26
                    text what id what_id size 23
                elif persistent.font_size == "small":
                    if who is not None:
                        text who id who_id size 28
                    text what id what_id size 28
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                            mouse "hover_anim"
                    else:
                        text caption style "nvl_dialogue"

    imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/backward_%s.png" pos(31,946) action ShowMenu("text_history") mouse "hover_anim"

    # use bdgr_skip_button
    if not config.skipping:
        imagebutton auto "bdgr/imgs/gui/dialogue_box/"+timeofday+"/forward_%s.png" pos(1810,946) action Skip() mouse "hover_anim"


screen bdgr_text_history_screen:
    predict False tag menu

    $ timeofday = persistent.bdgr_timeofday

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "large":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "giant":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return() mouse "hover_anim"



    window background Frame("bdgr/imgs/gui/dialogue_box/"+timeofday+"/nvl.png",103,17) left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:

        viewport id "text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:

                if h.who:

                    text h.who:
                        font main_font
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what style "log_button" text_style "normal_day" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#40e138" xpos 100 mouse "hover_anim"

        vbar value YScrollValue("text_history_screen") mouse "hover_anim" bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "bdgr/imgs/gui/dialogue_box/"+timeofday+"/thumb_idle.png" hover_thumb "bdgr/imgs/gui/dialogue_box/"+timeofday+"/thumb_hover.png" xsize 47 xoffset 1705


screen bdgr_choice:

    modal True

    python:
        choice_colors_hover={
            'spring': "#dcd168",
            'winter': "#98d8da"
            }

        choice_colors={
            'spring': "#69652f",
            'winter': "#496463"
            }

        choice_colors_selected={
            'spring': "#42401e",
            'winter': "#2d3d3d",
            }

    window background Frame("bdgr/imgs/gui/choice/choice_box_"+persistent.bdgr_timeofday+".png",65,65) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 75 top_padding 75:

        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:

                button background None:
                    xalign 0.5
                    action action
                    mouse "hover_anim"
                    text caption font header_font size 37 hover_size 37 color choice_colors[persistent.bdgr_timeofday] hover_color choice_colors_hover[persistent.bdgr_timeofday] xcenter 0.5 text_align 0.5
            else:
                text caption font header_font size 60 color choice_colors[persistent.bdgr_timeofday] text_align 0.5 xcenter 0.5
