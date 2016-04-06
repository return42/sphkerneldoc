
.. _API-drm-bridge-mode-fixup:

=====================
drm_bridge_mode_fixup
=====================

*man drm_bridge_mode_fixup(9)*

*4.6.0-rc1*

fixup proposed mode for all bridges in the encoder chain


Synopsis
========

.. c:function:: bool drm_bridge_mode_fixup( struct drm_bridge * bridge, const struct drm_display_mode * mode, struct drm_display_mode * adjusted_mode )

Arguments
=========

``bridge``
    bridge control structure

``mode``
    desired mode to be set for the bridge

``adjusted_mode``
    updated mode that works for this bridge


Description
===========

Calls ->``mode_fixup`` ``drm_bridge_funcs`` op for all the bridges in the encoder chain, starting from the first bridge to the last.


Note
====

the bridge passed should be the one closest to the encoder


RETURNS
=======

true on success, false on failure
