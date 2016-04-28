.. -*- coding: utf-8; mode: rst -*-

.. _API-fb-videomode-to-var:

===================
fb_videomode_to_var
===================

*man fb_videomode_to_var(9)*

*4.6.0-rc5*

convert fb_videomode to fb_var_screeninfo


Synopsis
========

.. c:function:: void fb_videomode_to_var( struct fb_var_screeninfo * var, const struct fb_videomode * mode )

Arguments
=========

``var``
    pointer to struct fb_var_screeninfo

``mode``
    pointer to struct fb_videomode


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
