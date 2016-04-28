.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-prune-invalid:

======================
drm_mode_prune_invalid
======================

*man drm_mode_prune_invalid(9)*

*4.6.0-rc5*

remove invalid modes from mode list


Synopsis
========

.. c:function:: void drm_mode_prune_invalid( struct drm_device * dev, struct list_head * mode_list, bool verbose )

Arguments
=========

``dev``
    DRM device

``mode_list``
    list of modes to check

``verbose``
    be verbose about it


Description
===========

This helper function can be used to prune a display mode list after
validation has been completed. All modes who's status is not MODE_OK
will be removed from the list, and if ``verbose`` the status code and
mode name is also printed to dmesg.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
