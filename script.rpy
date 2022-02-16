init python:
    mods["bdofr"] = u"Я.Д.С.Д Главное меню"

    def bdofr_screens_save():
        renpy.display.screen.screens[("bdofr_old_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]

    def bdofr_screens_activate():
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("bdofr_main_menu", None)]

    def bdofr_screens_default():
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("bdofr_old_main_menu", None)]
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def bdofr_screens_save_activate():
        bdofr_screens_save()
        bdofr_screens_activate()

    style.bdofr_main_menu_button =                              Style(style.default)
    style.bdofr_main_menu_button.background =                   "#0000007b"
    style.bdofr_main_menu_button.hover_background =             "#0e0e0e7b"
    style.bdofr_main_menu_button.selected_background =          "#0e0e0e7b"
    style.bdofr_main_menu_button.selected_hover_background =    "#0e0e0e7b"
    style.bdofr_main_menu_button.selected_idle_background =     "#0e0e0e7b"

transform rotate_atl:
    rotate 0
    linear 2.0 rotate 360
    repeat

screen bdofr_main_menu:
    modal True tag menu

    add "white"
    text "Animeted background" size 150 color "#bababa" align(0.5,0.5) at rotate_atl
    text "Bright Days Of Grey Reality" size 75 color "#000" pos(867,446)

    frame:
        minimum(582,994) maximum(582,994) pos(74,23)
        background "#0000007b"

    side "c":
        area(74,23,582,994)
        grid 2 3 xfill False spacing 36 align(0.5,0.5):

            button:
                maximum(231,209) minimum(231,209)
                action Start("bdofr_start")
                style "bdofr_main_menu_button"
                text "New Game"
            button:
                maximum(231,209) minimum(231,209)
                action ShowMenu("load")
                style "bdofr_main_menu_button"
                text "Load"

            button:
                maximum(231,209) minimum(231,209)
                action NullAction()
                style "bdofr_main_menu_button"
                text "Gallery"
            button:
                maximum(231,209) minimum(231,209)
                action NullAction()
                style "bdofr_main_menu_button"
                text "Titles"

            button:
                maximum(231,209) minimum(231,209)
                action NullAction()
                style "bdofr_main_menu_button"
                text "Discord"
            button:
                maximum(231,209) minimum(231,209)
                action OpenURL("https://vk.com/es.bdgr")
                style "bdofr_main_menu_button"
                text "VK"

    button:
        maximum(364,78) minimum(364,78) pos(1556,981)
        action [Hide("bdofr_main_menu"), (Function(bdofr_screens_default)), ShowMenu("main_menu")]
        style "bdofr_main_menu_button"
        text "exit"

label bdofr:
    $ bdofr_screens_save_activate()
    return

label bdofr_start:
    scene bg room
    show semen pioneer
    with dissolve
    "Здесь должен был быть сюжет"