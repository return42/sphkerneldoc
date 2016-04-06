
.. _API-drm-encoder-index:

=================
drm_encoder_index
=================

*man drm_encoder_index(9)*

*4.6.0-rc1*

find the index of a registered encoder


Synopsis
========

.. c:function:: unsigned int drm_encoder_index( struct drm_encoder * encoder )

Arguments
=========

``encoder``
    encoder to find index for


Description
===========

Given a registered encoder, return the index of that encoder within a DRM device's list of encoders.
