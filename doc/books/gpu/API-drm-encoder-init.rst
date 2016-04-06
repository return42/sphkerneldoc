
.. _API-drm-encoder-init:

================
drm_encoder_init
================

*man drm_encoder_init(9)*

*4.6.0-rc1*

Init a preallocated encoder


Synopsis
========

.. c:function:: int drm_encoder_init( struct drm_device * dev, struct drm_encoder * encoder, const struct drm_encoder_funcs * funcs, int encoder_type, const char * name, ... )

Arguments
=========

``dev``
    drm device

``encoder``
    the encoder to init

``funcs``
    callbacks for this encoder

``encoder_type``
    user visible type of the encoder

``name``
    printf style format string for the encoder name, or NULL for default name

``...``
    variable arguments


Description
===========

Initialises a preallocated encoder. Encoder should be subclassed as part of driver encoder objects.


Returns
=======

Zero on success, error code on failure.
