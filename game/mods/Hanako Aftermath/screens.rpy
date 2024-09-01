screen aftermath():
    tag menu
    style_prefix "aftermath"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"

        has vbox

        text _("Hanako Act 5: Aftermath"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:
                textbutton _("Start") action Start("aftermath_start")

            vbox:
                textbutton _("About") action ShowMenu("aftermath_about")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

screen aftermath_about():
    tag menu
    style_prefix "aftermath_about"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"
        xsize 1200

        has vbox

        text _("About Aftermath"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:

                text _("Fan made continuation of Hanako's story\n")

                text _("It focuses on what happened after the ending of Act 4\n")

                text _("Made by FgbThePoH|Gex.\n")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("aftermath")
