
.. _API-fb-delete-videomode:

===================
fb_delete_videomode
===================

*man fb_delete_videomode(9)*

*4.6.0-rc1*

removed videomode entry from modelist


Synopsis
========

.. c:function:: void fb_delete_videomode( const struct fb_videomode * mode, struct list_head * head )

Arguments
=========

``mode``
    videomode to remove

``head``
    struct list_head of modelist


NOTES
=====

Will remove all matching mode entries
