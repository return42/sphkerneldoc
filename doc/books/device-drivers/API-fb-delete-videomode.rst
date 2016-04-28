.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-delete-videomode:

===================
fb_delete_videomode
===================

*man fb_delete_videomode(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
