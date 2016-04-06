
.. _API-drm-bridge-enable:

=================
drm_bridge_enable
=================

*man drm_bridge_enable(9)*

*4.6.0-rc1*

calls ->``enable`` ``drm_bridge_funcs`` op for all bridges in the encoder chain.


Synopsis
========

.. c:function:: void drm_bridge_enable( struct drm_bridge * bridge )

Arguments
=========

``bridge``
    bridge control structure


Description
===========

Calls ->``enable`` ``drm_bridge_funcs`` op for all the bridges in the encoder chain, starting from the first bridge to the last. These are called after completing the encoder's
commit op.

Note that the bridge passed should be the one closest to the encoder
