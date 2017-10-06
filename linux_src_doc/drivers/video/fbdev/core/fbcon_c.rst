.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbcon.c

.. _`set_con2fb_map`:

set_con2fb_map
==============

.. c:function:: int set_con2fb_map(int unit, int newidx, int user)

    map console to frame buffer device

    :param int unit:
        virtual console number to map

    :param int newidx:
        frame buffer index to map virtual console to

    :param int user:
        user request

.. _`set_con2fb_map.description`:

Description
-----------

Maps a virtual console \ ``unit``\  to a frame buffer device
\ ``newidx``\ .

This should be called with the console lock held.

.. This file was automatic generated / don't edit.

