.. -*- coding: utf-8; mode: rst -*-

.. _API-setup-per-zone-wmarks:

=====================
setup_per_zone_wmarks
=====================

*man setup_per_zone_wmarks(9)*

*4.6.0-rc5*

called when min_free_kbytes changes or when memory is
hot-{added|removed}


Synopsis
========

.. c:function:: void setup_per_zone_wmarks( void )

Arguments
=========

``void``
    no arguments


Description
===========

Ensures that the watermark[min,low,high] values for each zone are set
correctly with respect to min_free_kbytes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
