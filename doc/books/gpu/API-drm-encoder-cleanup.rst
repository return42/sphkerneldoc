.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-encoder-cleanup:

===================
drm_encoder_cleanup
===================

*man drm_encoder_cleanup(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
