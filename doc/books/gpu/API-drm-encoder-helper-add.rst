.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-encoder-helper-add:

======================
drm_encoder_helper_add
======================

*man drm_encoder_helper_add(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
