label aftermath:
    show screen aftermath
    call screen aftermath

    return

label aftermath_prep:
    stop music fadeout 1.0

    scene black
    with config.game_main_transition
    pause 2.0

    call aftermath_start

    return