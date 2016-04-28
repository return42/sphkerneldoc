.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-bridge-mode-set:

===================
drm_bridge_mode_set
===================

*man drm_bridge_mode_set(9)*

*4.6.0-rc5*

set proposed mode for all bridges in the encoder chain


Synopsis
========

.. c:function:: void drm_bridge_mode_set( struct drm_bridge * bridge, struct drm_display_mode * mode, struct drm_display_mode * adjusted_mode )

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

Calls ->``mode_set`` ``drm_bridge_funcs`` op for all the bridges in the
encoder chain, starting from the first bridge to the last.


Note
====

the bridge passed should be the one closest to the encoder


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
