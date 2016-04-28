.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-single-add-all-connectors:

=======================================
drm_fb_helper_single_add_all_connectors
=======================================

*man drm_fb_helper_single_add_all_connectors(9)*

*4.6.0-rc5*

add all connectors to fbdev emulation helper


Synopsis
========

.. c:function:: int drm_fb_helper_single_add_all_connectors( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    fbdev initialized with drm_fb_helper_init


Description
===========

This functions adds all the available connectors for use with the given
fb_helper. This is a separate step to allow drivers to freely assign
connectors to the fbdev, e.g. if some are reserved for special purposes
or not adequate to be used for the fbcon.

This function is protected against concurrent connector hotadds/removals
using ``drm_fb_helper_add_one_connector`` and
``drm_fb_helper_remove_one_connector``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
