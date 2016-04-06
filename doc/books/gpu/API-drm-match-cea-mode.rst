
.. _API-drm-match-cea-mode:

==================
drm_match_cea_mode
==================

*man drm_match_cea_mode(9)*

*4.6.0-rc1*

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
