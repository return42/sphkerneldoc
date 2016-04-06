
.. _API-drm-encoder-crtc-ok:

===================
drm_encoder_crtc_ok
===================

*man drm_encoder_crtc_ok(9)*

*4.6.0-rc1*

can a given crtc drive a given encoder?


Synopsis
========

.. c:function:: bool drm_encoder_crtc_ok( struct drm_encoder * encoder, struct drm_crtc * crtc )

Arguments
=========

``encoder``
    encoder to test

``crtc``
    crtc to test


Description
===========

Return false if ``encoder`` can't be driven by ``crtc``, true otherwise.
