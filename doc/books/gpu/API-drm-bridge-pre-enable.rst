
.. _API-drm-bridge-pre-enable:

=====================
drm_bridge_pre_enable
=====================

*man drm_bridge_pre_enable(9)*

*4.6.0-rc1*

calls ->``pre_enable`` ``drm_bridge_funcs`` op for all bridges in the encoder chain.


Synopsis
========

.. c:function:: void drm_bridge_pre_enable( struct drm_bridge * bridge )

Arguments
=========

``bridge``
    bridge control structure


Description
===========

Calls ->``pre_enable`` ``drm_bridge_funcs`` op for all the bridges in the encoder chain, starting from the last bridge to the first. These are called before calling the encoder's
commit op.


Note
====

the bridge passed should be the one closest to the encoder
