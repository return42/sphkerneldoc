
.. _API-mac-vmode-to-var:

================
mac_vmode_to_var
================

*man mac_vmode_to_var(9)*

*4.6.0-rc1*

converts vmode/cmode pair to var structure


Synopsis
========

.. c:function:: int mac_vmode_to_var( int vmode, int cmode, struct fb_var_screeninfo * var )

Arguments
=========

``vmode``
    MacOS video mode

``cmode``
    MacOS color mode

``var``
    frame buffer video mode structure


Description
===========

Converts a MacOS vmode/cmode pair to a frame buffer video mode structure.

Returns negative errno on error, or zero for success.
