init python:
    mods["bdgr"] = u"Я.Д.С.Д Главное меню"

    def bdgr_screens_save():
        renpy.display.screen.screens[("bdgr_old_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]

    def bdgr_screens_activate():
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("bdgr_main_menu", None)]

    def bdgr_screens_default():
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("bdgr_old_main_menu", None)]
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def bdgr_screens_save_activate():
        bdgr_screens_save()
        bdgr_screens_activate()

    style.bdgr_main_menu_button =                              Style(style.default)
    style.bdgr_main_menu_button.background =                   "#0000007b"
    style.bdgr_main_menu_button.hover_background =             "#0e0e0e7b"
    style.bdgr_main_menu_button.selected_background =          "#0e0e0e7b"
    style.bdgr_main_menu_button.selected_hover_background =    "#0e0e0e7b"
    style.bdgr_main_menu_button.selected_idle_background =     "#0e0e0e7b"

transform rotate_atl:
    rotate 0
    linear 2.0 rotate 360
    repeat

screen bdgr_main_menu:
    modal True tag menu

    add "bdgr/imgs/gui/main_menu_background.jpg"
    add "bdgr/imgs/gui/phone.png" ypos 14
    add "bdgr/imgs/gui/logo_rus.png" pos(692,392)

    imagebutton:
        pos(152,281)
        auto "bdgr/imgs/gui/start_%s.png"
        action Start("bdgr_start")

    imagebutton:
        pos(142,505)
        auto "bdgr/imgs/gui/load_%s.png"
        action ShowMenu("load")

    imagebutton:
        pos(287,505)
        auto "bdgr/imgs/gui/prefs_%s.png"
        action ShowMenu("preferences")

    imagebutton:
        pos(442,505)
        auto "bdgr/imgs/gui/gallery_%s.png"
        action NullAction() #ShowMenu("gallery")

    imagebutton:
        pos(171,684)
        auto "bdgr/imgs/gui/authors_%s.png"
        action NullAction()

    imagebutton:
        pos(304,684)
        auto "bdgr/imgs/gui/ds_%s.png"
        action NullAction()

    imagebutton:
        pos(442,684)
        auto "bdgr/imgs/gui/vk_%s.png"
        action OpenURL("https://vk.com/es.bdgr")

    imagebutton:
        pos(270,877)
        auto "bdgr/imgs/gui/exit_%s.png"
        action [Hide("bdgr_main_menu"), (Function(bdgr_screens_default)), ShowMenu("main_menu")]

    key "K_ESCAPE" action [Hide("bdgr_main_menu"), (Function(bdgr_screens_default)), ShowMenu("main_menu")]

label bdgr:
    $ bdgr_screens_save_activate()
    return

label bdgr_start:
    scene bg room
    show semen pioneer
    with dissolve
    "Здесь должен был быть сюжет"