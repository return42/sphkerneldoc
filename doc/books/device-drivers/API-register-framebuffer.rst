
.. _API-register-framebuffer:

====================
register_framebuffer
====================

*man register_framebuffer(9)*

*4.6.0-rc1*

registers a frame buffer device


Synopsis
========

.. c:function:: int register_framebuffer( struct fb_info * fb_info )

Arguments
=========

``fb_info``
    frame buffer info structure


Description
===========

Registers a frame buffer device ``fb_info``.

Returns negative errno on error, or zero for success.
