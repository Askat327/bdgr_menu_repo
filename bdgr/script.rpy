python early:

    def bdgr_default():
        rgsn = renpy.game.script.namemap
        rgsn["splashscreen"] = rgsn["bdgr"]


init python:
    mods["bdgr"] = u"Я.Д.С.Д Главное меню"

    persistent.game_mode == "static"

    bdgr_screen_list = ["main_menu","save","load","gallery","gallery_sp","preferences","yesno_prompt","game_menu_selector","music_room","say","nvl","text_history_screen","choice","quit"]

    bdgr_main_menu_music = "sound/music/blow_with_the_fires.ogg"

    def bdgr_screens_save():
        for screens in bdgr_screen_list:
            renpy.display.screen.screens[("bdgr_old_"+screens, None)] = renpy.display.screen.screens[(screens, None)]

    def bdgr_screens_activate():
        bdgr_mouse_change("winter")

        for screens in bdgr_screen_list:
            renpy.display.screen.screens[(screens, None)] = renpy.display.screen.screens[("bdgr_"+screens, None)]

    def bdgr_screens_default():
        config.mouse_displayable = MouseDisplayable("images/misc/mouse/1.png", 0, 0)

        for screens in bdgr_screen_list:
            renpy.display.screen.screens[(screens, None)] = renpy.display.screen.screens[("bdgr_old_"+screens, None)]
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def bdgr_screens_save_activate():
        bdgr_screens_save()
        bdgr_screens_activate()

    def bdgr_mouse_change(tod="winter"):
        if tod == "winter":
            config.mouse_displayable = MouseDisplayable("bdgr/imgs/gui/cursor/winter/mouse_default.png", 0, 0).add("hover_anim", "bdgr_cursor_anim_w", 0, 0)
        elif tod == "spring":
            config.mouse_displayable = MouseDisplayable("bdgr/imgs/gui/cursor/spring/mouse_default.png", 0, 0).add("hover_anim", "bdgr_cursor_anim_s", 0, 0)

    bdgr_characters = {
        "narrator":[None, None],
        "th":[None, None],

        "me":[u"Семён", "#d9b09c"],
        "grl":[u"Девочка", "#c2616e"],
        "who":[u"Кто", "#000"],

        "us":[u"Ульяна", "#cd5050"],
        "dv":[u"Алиса", "#ec8b3d"],
        "ma":[u"Маша", "#34bdbd"],
        "un":[u"Лена", "#224cff"],
        "sus":[u"Славя", "#f2b31c"],
    }

    def bdgr_chars_define(kind=adv):
        gl = globals()
    # присваивания ctc
        if kind == nvl:
            who_suffix = ":"
            ctc_star = "ctc_star_nvl"
            ctc_bfly = "ctc_bfly_nvl"
            ctc_someone = "ctc_someone_nvl"
            ctc_bimba = "ctc_bimba_nvl"
            ctc_guitar = "ctc_guitar_nvl"
            ctc_leaf = "ctc_leaf_nvl"
            ctc_moon = "ctc_moon_nvl"
            ctc_sun = "ctc_sun_nvl"
        else:
            who_suffix = ""
            ctc_star = "ctc_star"
            ctc_bfly = "ctc_bfly"
            ctc_someone = "ctc_someone"
            ctc_bimba = "ctc_bimba"
            ctc_guitar = "ctc_guitar"
            ctc_leaf = "ctc_leaf"
            ctc_moon = "ctc_moon"
            ctc_sun = "ctc_sun"

        what_color = "#FFDD7D"
        drop_shadow = (2, 2)

        for i, j in bdgr_characters.items():
            if i == "th":
                gl[i] = Character(None, kind=kind, what_color="#d6d6d6", what_drop_shadow=drop_shadow, what_prefix="~ ", what_suffix=" ~", ctc=ctc_star, ctc_position="fixed")

            elif i == "me":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_star, ctc_position="fixed")
            elif i == "grl":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_bfly, ctc_position="fixed")
            elif i == "who":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_someone, ctc_position="fixed")

            elif i == "us":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_bimba, ctc_position="fixed")
            elif i == "dv":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_guitar, ctc_position="fixed")
            elif i == "ma":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_leaf, ctc_position="fixed")
            elif i == "un":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_moon, ctc_position="fixed")
            elif i == "sus":
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_sun, ctc_position="fixed")
            else:
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_star, ctc_position="fixed")
            #     gl[i+"_v"] = Character(u"Голос", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc_star, ctc_position="fixed")

    def bdgr_set_mode(mode=adv):
        nvl_clear()
        bdgr_chars_define(kind=mode)
    
    vertical_dis = ImageDissolve("bdgr/imgs/misc/vertical_dissolve.jpg", 1.5)

    bdgr_default()

init:
    $ tod = persistent.bdgr_timeofday

    image bdgr_cursor_anim_w:
        "bdgr/imgs/gui/cursor/winter/1.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/2.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/3.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/4.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/5.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/6.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/7.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/8.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/9.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/10.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/11.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/winter/12.png"
        pause 0.1
        repeat

    image bdgr_cursor_anim_s:
        "bdgr/imgs/gui/cursor/spring/1.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/2.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/3.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/4.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/5.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/6.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/7.png"
        pause 0.1
        "bdgr/imgs/gui/cursor/spring/8.png"
        pause 0.1
        repeat

    image ctc_star = Animation("bdgr/imgs/gui/dialogue_box/ctc/star/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_bfly = Animation("bdgr/imgs/gui/dialogue_box/ctc/bfly/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_someone = Animation("bdgr/imgs/gui/dialogue_box/ctc/someone/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_bimba = Animation("bdgr/imgs/gui/dialogue_box/ctc/bimba/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_guitar = Animation("bdgr/imgs/gui/dialogue_box/ctc/guitar/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_leaf = Animation("bdgr/imgs/gui/dialogue_box/ctc/leaf/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_moon = Animation("bdgr/imgs/gui/dialogue_box/ctc/moon/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image ctc_sun = Animation("bdgr/imgs/gui/dialogue_box/ctc/sun/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/5.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)

    image ctc_bfly_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/bfly/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bfly/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_star_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/star/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/star/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_someone_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/someone/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/someone/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_bimba_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/bimba/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/bimba/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_guitar_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/guitar/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/guitar/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_leaf_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/leaf/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/leaf/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_moon_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/moon/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/moon/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
    image ctc_sun_nvl = Animation("bdgr/imgs/gui/dialogue_box/ctc/sun/1.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/2.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/3.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/4.png", 0.15, "bdgr/imgs/gui/dialogue_box/ctc/sun/5.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)

    image hold_up_white = "bdgr/imgs/misc/hold_up_white.png"
    image hold_up_color = "bdgr/imgs/misc/hold_up_color.png"
    image hold_on_team = "bdgr/imgs/misc/hold_on_team.png"

    image logo_rus_anim:
        im.Blur("bdgr/imgs/gui/main_menu/logo_rus.png", 4.0)
        pause 1.7
        "bdgr/imgs/gui/main_menu/logo_rus.png" with dissolve2
        pause 5.5
        im.MatrixColor("bdgr/imgs/gui/main_menu/logo_rus.png", im.matrix.brightness(1)) with dspr
        pause 0.2
        "bdgr/imgs/gui/main_menu/logo_rus.png" with dissolve


label bdgr:
    $ bdgr_screens_save_activate()

    scene black with dissolve

    show hold_up_white:
        pos(654,179)
    with dissolve2

    show hold_up_color:
        pos(654,179)
    hide hold_up_white
    with vertical_dis

    show hold_on_team:
        pos(711,842)
    with dissolve2
    pause 3.0

    scene black with dissolve
    pause 1.0

    scene bg bus_stop with Dissolve(3.0)
    show logo_rus_anim:
        zoom .2 align(0.5,0.5) subpixel True
        ease 6.0 zoom 1.2
    with Dissolve(3.3)
    pause 5.5

    show white
    pause .02
    hide white
    pause .02
    show white
    pause .02
    hide white
    pause .02
    show white
    pause .02
    hide white
    pause .02
    scene black with Fade(.02, 0, 1, color="#fff")

    return


label bdgr_start:
    $ bdgr_chars_define()
    show screen bdgr_skip_button
    scene winter
    show semen pioneer at right
    show bdgr_skip_anim_winter at truecenter, left
    with dissolve
    
    $ persistent.bdgr_timeofday = "winter"
    $ bdgr_mouse_change("winter")
    "persistent.bdgr_timeofday=\"winter\""
    "persistent.bdgr_timeofday=\"winter\""
    "persistent.bdgr_timeofday=\"winter\""
    me "Я Семён"
    grl "Я девочка"
    who "Сука я кто?"
    us "Я Ульяна"
    dv "Я Алиса"
    ma "Я Маша"
    un "Я Лена"
    sus "Я солнце"
    th "Я думаю"
    "Вот и всё"
    $ bdgr_set_mode(nvl)
    "nvl mode1"
    "nvl mode2"
    "nvl mode3"
    me "Я Семён"
    grl "Я девочка"
    who "Сука я кто?"
    us "Я Ульяна"
    dv "Я Алиса"
    ma "Я Маша"
    un "Я Лена"
    sus "Я солнце"
    th "Я думаю"
    "Вот и всё"
    $ bdgr_set_mode()
    menu continue:
        "Continue?"
        "Da":
            pass
        "Niet":
            $ persistent.bdgr_timeofday = "winter"
            $ bdgr_mouse_change("winter")
            return

    scene spring
    show semen pioneer at right
    show bdgr_skip_anim_spring at truecenter, left
    with dissolve

    $ persistent.bdgr_timeofday = "spring"
    $ bdgr_mouse_change("spring")
    "persistent.bdgr_timeofday=\"spring\""
    "persistent.bdgr_timeofday=\"spring\""
    "persistent.bdgr_timeofday=\"spring\""
    me "Я Семён"
    grl "Я девочка"
    who "Сука я кто?"
    us "Я Ульяна"
    dv "Я Алиса"
    ma "Я Маша"
    un "Я Лена"
    sus "Я солнце"
    th "Я думаю"
    "Вот и всё"
    $ bdgr_set_mode(nvl)
    "nvl mode1"
    "nvl mode2"
    "nvl mode3"
    me "Я Семён"
    grl "Я девочка"
    who "Сука я кто?"
    us "Я Ульяна"
    dv "Я Алиса"
    ma "Я Маша"
    un "Я Лена"
    sus "Я солнце"
    th "Я думаю"
    "Вот и всё"
    $ bdgr_set_mode()
    menu continue:
        "Continue?"
        "Da":
            "А дальше уже ничего нету."
            $ persistent.bdgr_timeofday = "winter"
            $ bdgr_mouse_change("winter")
            return
        "Niet":
            $ persistent.bdgr_timeofday = "winter"
            $ bdgr_mouse_change("winter")
            return