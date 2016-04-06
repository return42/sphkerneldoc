
.. _API-unregister-framebuffer:

======================
unregister_framebuffer
======================

*man unregister_framebuffer(9)*

*4.6.0-rc1*

releases a frame buffer device


Synopsis
========

.. c:function:: int unregister_framebuffer( struct fb_info * fb_info )

Arguments
=========

``fb_info``
    frame buffer info structure


Description
===========

Unregisters a frame buffer device ``fb_info``.

Returns negative errno on error, or zero for success.

This function will also notify the framebuffer console to release the driver.

This is meant to be called within a driver's ``module_exit`` function. If this is called outside ``module_exit``, ensure that the driver implements ``fb_open`` and ``fb_release``
to check that no processes are using the device.
