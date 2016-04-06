
.. _API-fb-add-videomode:

================
fb_add_videomode
================

*man fb_add_videomode(9)*

*4.6.0-rc1*

adds videomode entry to modelist


Synopsis
========

.. c:function:: int fb_add_videomode( const struct fb_videomode * mode, struct list_head * head )

Arguments
=========

``mode``
    videomode to add

``head``
    struct list_head of modelist


NOTES
=====

Will only add unmatched mode entries
