init python:
    mods["bdgr"] = u"Я.Д.С.Д Главное меню"

    persistent.game_mode == "static"

    bdgr_screen_list = ["main_menu","save","load","gallery","gallery_sp","preferences"]

    def bdgr_screens_save():
        for screens in bdgr_screen_list:
            renpy.display.screen.screens[("bdgr_old_"+screens, None)] = renpy.display.screen.screens[(screens, None)]

    def bdgr_screens_activate():
        for screens in bdgr_screen_list:
            renpy.display.screen.screens[(screens, None)] = renpy.display.screen.screens[("bdgr_"+screens, None)]

    def bdgr_screens_default():
        for screens in bdgr_screen_list:
            renpy.display.screen.screens[(screens, None)] = renpy.display.screen.screens[("bdgr_old_"+screens, None)]
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def bdgr_screens_save_activate():
        bdgr_screens_save()
        bdgr_screens_activate()


label bdgr:
    $ bdgr_screens_save_activate()
    return

label bdgr_start:
    scene bg room
    show semen pioneer
    with dissolve
    "Здесь должен был быть сюжет"