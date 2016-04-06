
.. _API-drm-for-each-encoder-mask:

=========================
drm_for_each_encoder_mask
=========================

*man drm_for_each_encoder_mask(9)*

*4.6.0-rc1*

iterate over encoders specified by bitmask


Synopsis
========

.. c:function:: drm_for_each_encoder_mask( encoder, dev, encoder_mask )

Arguments
=========

``encoder``
    the loop cursor

``dev``
    the DRM device

``encoder_mask``
    bitmask of encoder indices


Description
===========

Iterate over all encoders specified by bitmask.
