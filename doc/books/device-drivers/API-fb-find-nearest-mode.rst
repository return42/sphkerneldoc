
.. _API-fb-find-nearest-mode:

====================
fb_find_nearest_mode
====================

*man fb_find_nearest_mode(9)*

*4.6.0-rc1*

find closest videomode


Synopsis
========

.. c:function:: const struct fb_videomode ⋆ fb_find_nearest_mode( const struct fb_videomode * mode, struct list_head * head )

Arguments
=========

``mode``
    pointer to struct fb_videomode

``head``
    pointer to modelist


Description
===========

Finds best matching videomode, smaller or greater in dimension. If more than 1 videomode is found, will return the videomode with the closest refresh rate.
