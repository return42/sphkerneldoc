
.. _API-fb-try-mode:

===========
fb_try_mode
===========

*man fb_try_mode(9)*

*4.6.0-rc1*

test a video mode


Synopsis
========

.. c:function:: int fb_try_mode( struct fb_var_screeninfo * var, struct fb_info * info, const struct fb_videomode * mode, unsigned int bpp )

Arguments
=========

``var``
    frame buffer user defined part of display

``info``
    frame buffer info structure

``mode``
    frame buffer video mode structure

``bpp``
    color depth in bits per pixel


Description
===========

Tries a video mode to test it's validity for device ``info``.

Returns 1 on success.
