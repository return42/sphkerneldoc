.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-find-best-mode:

=================
fb_find_best_mode
=================

*man fb_find_best_mode(9)*

*4.6.0-rc5*

find best matching videomode


Synopsis
========

.. c:function:: const struct fb_videomode * fb_find_best_mode( const struct fb_var_screeninfo * var, struct list_head * head )

Arguments
=========

``var``
    pointer to struct fb_var_screeninfo

``head``
    pointer to struct list_head of modelist


RETURNS
=======

struct fb_videomode, NULL if none found


IMPORTANT
=========

This function assumes that all modelist entries in info->modelist are
valid.


NOTES
=====

Finds best matching videomode which has an equal or greater dimension
than var->xres and var->yres. If more than 1 videomode is found, will
return the videomode with the highest refresh rate


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
