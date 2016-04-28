.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-match-cea-mode:

==================
drm_match_cea_mode
==================

*man drm_match_cea_mode(9)*

*4.6.0-rc5*

look for a CEA mode matching given mode


Synopsis
========

.. c:function:: u8 drm_match_cea_mode( const struct drm_display_mode * to_match )

Arguments
=========

``to_match``
    display mode


Return
======

The CEA Video ID (VIC) of the mode or 0 if it isn't a CEA-861 mode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
