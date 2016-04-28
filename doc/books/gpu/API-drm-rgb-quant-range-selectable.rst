.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rgb-quant-range-selectable:

==============================
drm_rgb_quant_range_selectable
==============================

*man drm_rgb_quant_range_selectable(9)*

*4.6.0-rc5*

is RGB quantization range selectable?


Synopsis
========

.. c:function:: bool drm_rgb_quant_range_selectable( struct edid * edid )

Arguments
=========

``edid``
    EDID block to scan


Description
===========

Check whether the monitor reports the RGB quantization range selection
as supported. The AVI infoframe can then be used to inform the monitor
which quantization range (full or limited) is used.


Return
======

True if the RGB quantization range is selectable, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
