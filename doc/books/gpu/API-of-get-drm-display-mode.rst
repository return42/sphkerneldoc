.. -*- coding: utf-8; mode: rst -*-

.. _API-of-get-drm-display-mode:

=======================
of_get_drm_display_mode
=======================

*man of_get_drm_display_mode(9)*

*4.6.0-rc5*

get a drm_display_mode from devicetree


Synopsis
========

.. c:function:: int of_get_drm_display_mode( struct device_node * np, struct drm_display_mode * dmode, int index )

Arguments
=========

``np``
    device_node with the timing specification

``dmode``
    will be set to the return value

``index``
    index into the list of display timings in devicetree


Description
===========

This function is expensive and should only be used, if only one mode is
to be read from DT. To get multiple modes start with
of_get_display_timings and work with that instead.


Returns
=======

0 on success, a negative errno code when no of videomode node was found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
