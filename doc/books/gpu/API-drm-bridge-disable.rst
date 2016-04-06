
.. _API-drm-bridge-disable:

==================
drm_bridge_disable
==================

*man drm_bridge_disable(9)*

*4.6.0-rc1*

calls ->``disable`` ``drm_bridge_funcs`` op for all bridges in the encoder chain.


Synopsis
========

.. c:function:: void drm_bridge_disable( struct drm_bridge * bridge )

Arguments
=========

``bridge``
    bridge control structure


Description
===========

Calls ->``disable`` ``drm_bridge_funcs`` op for all the bridges in the encoder chain, starting from the last bridge to the first. These are called before calling the encoder's
prepare op.


Note
====

the bridge passed should be the one closest to the encoder
