.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-encoder-index:

=================
drm_encoder_index
=================

*man drm_encoder_index(9)*

*4.6.0-rc5*

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

Given a registered encoder, return the index of that encoder within a
DRM device's list of encoders.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
