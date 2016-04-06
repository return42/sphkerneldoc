
.. _API-drm-encoder-helper-add:

======================
drm_encoder_helper_add
======================

*man drm_encoder_helper_add(9)*

*4.6.0-rc1*

sets the helper vtable for an encoder


Synopsis
========

.. c:function:: void drm_encoder_helper_add( struct drm_encoder * encoder, const struct drm_encoder_helper_funcs * funcs )

Arguments
=========

``encoder``
    DRM encoder

``funcs``
    helper vtable to set for ``encoder``
