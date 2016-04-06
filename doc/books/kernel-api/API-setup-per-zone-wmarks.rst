
.. _API-setup-per-zone-wmarks:

=====================
setup_per_zone_wmarks
=====================

*man setup_per_zone_wmarks(9)*

*4.6.0-rc1*

called when min_free_kbytes changes or when memory is hot-{added|removed}


Synopsis
========

.. c:function:: void setup_per_zone_wmarks( void )

Arguments
=========

``void``
    no arguments


Description
===========

Ensures that the watermark[min,low,high] values for each zone are set correctly with respect to min_free_kbytes.
