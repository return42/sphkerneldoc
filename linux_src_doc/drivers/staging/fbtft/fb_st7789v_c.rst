.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fbtft/fb_st7789v.c

.. _`st7789v_command`:

enum st7789v_command
====================

.. c:type:: enum st7789v_command

    ST7789V display controller commands

.. _`st7789v_command.definition`:

Definition
----------

.. code-block:: c

    enum st7789v_command {
        PORCTRL,
        GCTRL,
        VCOMS,
        VDVVRHEN,
        VRHS,
        VDVS,
        VCMOFSET,
        PWCTRL1,
        PVGAMCTRL,
        NVGAMCTRL
    };

.. _`st7789v_command.constants`:

Constants
---------

PORCTRL
    porch setting

GCTRL
    gate control

VCOMS
    VCOM setting

VDVVRHEN
    VDV and VRH command enable

VRHS
    VRH set

VDVS
    VDV set

VCMOFSET
    VCOM offset set

PWCTRL1
    power control 1

PVGAMCTRL
    positive voltage gamma control

NVGAMCTRL
    negative voltage gamma control

.. _`st7789v_command.description`:

Description
-----------

The command names are the same as those found in the datasheet to ease
looking up their semantics and usage.

Note that the ST7789V display controller offers quite a few more commands
which have been omitted from this list as they are not used at the moment.
Furthermore, commands that are compliant with the MIPI DCS have been left
out as well to avoid duplicate entries.

.. _`init_display`:

init_display
============

.. c:function:: int init_display(struct fbtft_par *par)

    initialize the display controller

    :param struct fbtft_par \*par:
        FBTFT parameter object

.. _`init_display.description`:

Description
-----------

Most of the commands in this init function set their parameters to the
same default values which are already in place after the display has been
powered up. (The main exception to this rule is the pixel format which
would default to 18 instead of 16 bit per pixel.)
Nonetheless, this sequence can be used as a template for concrete
displays which usually need some adjustments.

.. _`init_display.return`:

Return
------

0 on success, < 0 if error occurred.

.. _`set_var`:

set_var
=======

.. c:function:: int set_var(struct fbtft_par *par)

    apply LCD properties like rotation and BGR mode

    :param struct fbtft_par \*par:
        FBTFT parameter object

.. _`set_var.return`:

Return
------

0 on success, < 0 if error occurred.

.. _`set_gamma`:

set_gamma
=========

.. c:function:: int set_gamma(struct fbtft_par *par, unsigned long *curves)

    set gamma curves

    :param struct fbtft_par \*par:
        FBTFT parameter object

    :param unsigned long \*curves:
        gamma curves

.. _`set_gamma.description`:

Description
-----------

Before the gamma curves are applied, they are preprocessed with a bitmask
to ensure syntactically correct input for the display controller.
This implies that the curves input parameter might be changed by this
function and that illegal gamma values are auto-corrected and not
reported as errors.

.. _`set_gamma.return`:

Return
------

0 on success, < 0 if error occurred.

.. _`blank`:

blank
=====

.. c:function:: int blank(struct fbtft_par *par, bool on)

    blank the display

    :param struct fbtft_par \*par:
        FBTFT parameter object

    :param bool on:
        whether to enable or disable blanking the display

.. _`blank.return`:

Return
------

0 on success, < 0 if error occurred.

.. This file was automatic generated / don't edit.

