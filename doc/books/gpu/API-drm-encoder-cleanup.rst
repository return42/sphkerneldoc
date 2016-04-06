
.. _API-drm-encoder-cleanup:

===================
drm_encoder_cleanup
===================

*man drm_encoder_cleanup(9)*

*4.6.0-rc1*

cleans up an initialised encoder


Synopsis
========

.. c:function:: void drm_encoder_cleanup( struct drm_encoder * encoder )

Arguments
=========

``encoder``
    encoder to cleanup


Description
===========

Cleans up the encoder but doesn't free the object.
