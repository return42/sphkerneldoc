.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-add-videomode:

================
fb_add_videomode
================

*man fb_add_videomode(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
