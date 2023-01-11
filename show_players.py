from helpers import clean_screen
from canvas import *
from decks import *


def show_players():
    clean_screen()

    aurora_btn = Button(
        root,
        text="Aurora",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1,
        command=aurora_deck
    )

    belica_btn = Button(
        root,
        text="Belica",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    countes_btn = Button(
        root,
        text="Countes",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    dekker_btn = Button(
        root,
        text="Dekker",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    feng_mao_btn = Button(
        root,
        text="Feng Mao",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    gadget_btn = Button(
        root,
        text="Gadget",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    gideon_btn = Button(
        root,
        text="Gideon",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    grux_btn = Button(
        root,
        text="Grux",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    howitzer_btn = Button(
        root,
        text="Howitzer",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    kallari_btn = Button(
        root,
        text="Kallari",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    khaimera_btn = Button(
        root,
        text="Khaimera",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    kwang_btn = Button(
        root,
        text="Kwang",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    murdock_btn = Button(
        root,
        text="Murdock",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    muriel_btn = Button(
        root,
        text="Muriel",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    narbash_btn = Button(
        root,
        text="Narbash",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    phase_btn = Button(
        root,
        text="Phase",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    rampage_btn = Button(
        root,
        text="Rampage",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    revenant_btn = Button(
        root,
        text="Revenant",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    serath_btn = Button(
        root,
        text="Serath",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    severog_btn = Button(
        root,
        text="Severog",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    shinbi_btn = Button(
        root,
        text="Shinbi",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    sparrow_btn = Button(
        root,
        text="Sparrow",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    steel_btn = Button(
        root,
        text="Steel",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    the_fey_btn = Button(
        root,
        text="The Fey",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    twinblast_btn = Button(
        root,
        text="Twinblast",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    wraith_btn = Button(
        root,
        text="Wraith",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )

    zena_btn = Button(
        root,
        text="Zena",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=10,
        height=1
    )
    frame.create_window(50, 50, window=aurora_btn)
    frame.create_window(50, 100, window=belica_btn)
    frame.create_window(50, 150, window=countes_btn)
    frame.create_window(50, 200, window=dekker_btn)
    frame.create_window(50, 250, window=feng_mao_btn)
    frame.create_window(150, 50, window=gadget_btn)
    frame.create_window(150, 100, window=gideon_btn)
    frame.create_window(150, 150, window=grux_btn)
    frame.create_window(150, 200, window=howitzer_btn)
    frame.create_window(150, 250, window=kallari_btn)
    frame.create_window(250, 50, window=khaimera_btn)
    frame.create_window(250, 100, window=kwang_btn)
    frame.create_window(250, 150, window=murdock_btn)
    frame.create_window(250, 200, window=muriel_btn)
    frame.create_window(250, 250, window=narbash_btn)
    frame.create_window(350, 50, window=phase_btn)
    frame.create_window(350, 100, window=rampage_btn)
    frame.create_window(350, 150, window=revenant_btn)
    frame.create_window(350, 200, window=serath_btn)
    frame.create_window(350, 250, window=severog_btn)
    frame.create_window(450, 50, window=shinbi_btn)
    frame.create_window(450, 100, window=sparrow_btn)
    frame.create_window(450, 150, window=steel_btn)
    frame.create_window(450, 200, window=the_fey_btn)
    frame.create_window(450, 250, window=twinblast_btn)
    frame.create_window(175, 300, window=wraith_btn)
    frame.create_window(275, 300, window=zena_btn)