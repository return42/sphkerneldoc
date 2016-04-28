.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-match-mode:

=============
fb_match_mode
=============

*man fb_match_mode(9)*

*4.6.0-rc5*

find a videomode which exactly matches the timings in var


Synopsis
========

.. c:function:: const struct fb_videomode * fb_match_mode( const struct fb_var_screeninfo * var, struct list_head * head )

Arguments
=========

``var``
    pointer to struct fb_var_screeninfo

``head``
    pointer to struct list_head of modelist


RETURNS
=======

struct fb_videomode, NULL if none found


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
