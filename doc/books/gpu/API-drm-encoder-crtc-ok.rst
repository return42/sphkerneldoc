.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-encoder-crtc-ok:

===================
drm_encoder_crtc_ok
===================

*man drm_encoder_crtc_ok(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
