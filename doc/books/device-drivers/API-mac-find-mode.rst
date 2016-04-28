.. -*- coding: utf-8; mode: rst -*-

.. _API-mac-find-mode:

=============
mac_find_mode
=============

*man mac_find_mode(9)*

*4.6.0-rc5*

find a video mode


Synopsis
========

.. c:function:: int mac_find_mode( struct fb_var_screeninfo * var, struct fb_info * info, const char * mode_option, unsigned int default_bpp )

Arguments
=========

``var``
    frame buffer user defined part of display

``info``
    frame buffer info structure

``mode_option``
    video mode name (see mac_modedb[])

``default_bpp``
    default color depth in bits per pixel


Description
===========

Finds a suitable video mode. Tries to set mode specified by
``mode_option``. If the name of the wanted mode begins with 'mac', the
Mac video mode database will be used, otherwise it will fall back to the
standard video mode database.


Note
====

Function marked as __init and can only be used during system boot.

Returns error code from fb_find_mode (see fb_find_mode function).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
