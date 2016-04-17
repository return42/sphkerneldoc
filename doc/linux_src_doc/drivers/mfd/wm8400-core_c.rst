.. -*- coding: utf-8; mode: rst -*-

=============
wm8400-core.c
=============


.. _`wm8400_reg_read`:

wm8400_reg_read
===============

.. c:function:: u16 wm8400_reg_read (struct wm8400 *wm8400, u8 reg)

    Single register read

    :param struct wm8400 \*wm8400:
        Pointer to wm8400 control structure

    :param u8 reg:
        Register to read



.. _`wm8400_reg_read.description`:

Description
-----------

``return``  Read value



.. _`wm8400_reset_codec_reg_cache`:

wm8400_reset_codec_reg_cache
============================

.. c:function:: void wm8400_reset_codec_reg_cache (struct wm8400 *wm8400)

    Reset cached codec registers to their default values.

    :param struct wm8400 \*wm8400:

        *undescribed*

