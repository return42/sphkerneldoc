
.. _API-drm-bridge-post-disable:

=======================
drm_bridge_post_disable
=======================

*man drm_bridge_post_disable(9)*

*4.6.0-rc1*

calls ->``post_disable`` ``drm_bridge_funcs`` op for all bridges in the encoder chain.


Synopsis
========

.. c:function:: void drm_bridge_post_disable( struct drm_bridge * bridge )

Arguments
=========

``bridge``
    bridge control structure


Description
===========

Calls ->``post_disable`` ``drm_bridge_funcs`` op for all the bridges in the encoder chain, starting from the first bridge to the last. These are called after completing the
encoder's prepare op.


Note
====

the bridge passed should be the one closest to the encoder
