
.. _API-fb-videomode-to-modelist:

========================
fb_videomode_to_modelist
========================

*man fb_videomode_to_modelist(9)*

*4.6.0-rc1*

convert mode array to mode list


Synopsis
========

.. c:function:: void fb_videomode_to_modelist( const struct fb_videomode * modedb, int num, struct list_head * head )

Arguments
=========

``modedb``
    array of struct fb_videomode

``num``
    number of entries in array

``head``
    struct list_head of modelist
