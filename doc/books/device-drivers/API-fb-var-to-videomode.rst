.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-var-to-videomode:

===================
fb_var_to_videomode
===================

*man fb_var_to_videomode(9)*

*4.6.0-rc5*

convert fb_var_screeninfo to fb_videomode


Synopsis
========

.. c:function:: void fb_var_to_videomode( struct fb_videomode * mode, const struct fb_var_screeninfo * var )

Arguments
=========

``mode``
    pointer to struct fb_videomode

``var``
    pointer to struct fb_var_screeninfo


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
