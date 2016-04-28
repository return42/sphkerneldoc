.. -*- coding: utf-8; mode: rst -*-

.. _API-mac-map-monitor-sense:

=====================
mac_map_monitor_sense
=====================

*man mac_map_monitor_sense(9)*

*4.6.0-rc5*

Convert monitor sense to vmode


Synopsis
========

.. c:function:: int mac_map_monitor_sense( int sense )

Arguments
=========

``sense``
    Macintosh monitor sense number


Description
===========

Converts a Macintosh monitor sense number to a MacOS vmode number.

Returns MacOS vmode video mode number.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
