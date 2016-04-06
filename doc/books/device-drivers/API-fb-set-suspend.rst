
.. _API-fb-set-suspend:

==============
fb_set_suspend
==============

*man fb_set_suspend(9)*

*4.6.0-rc1*

low level driver signals suspend


Synopsis
========

.. c:function:: void fb_set_suspend( struct fb_info * info, int state )

Arguments
=========

``info``
    framebuffer affected

``state``
    0 = resuming, !=0 = suspending


Description
===========

This is meant to be used by low level drivers to signal suspend/resume to the core & clients. It must be called with the console semaphore held
