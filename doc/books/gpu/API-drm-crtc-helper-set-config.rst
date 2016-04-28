.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-helper-set-config:

==========================
drm_crtc_helper_set_config
==========================

*man drm_crtc_helper_set_config(9)*

*4.6.0-rc5*

set a new config from userspace


Synopsis
========

.. c:function:: int drm_crtc_helper_set_config( struct drm_mode_set * set )

Arguments
=========

``set``
    mode set configuration


Description
===========

The ``drm_crtc_helper_set_config`` helper function implements the
set_config callback of struct ``drm_crtc_funcs`` for drivers using the
legacy CRTC helpers.

It first tries to locate the best encoder for each connector by calling
the connector ->``best_encoder`` (struct ``drm_connector_helper_funcs``)
helper operation.

After locating the appropriate encoders, the helper function will call
the mode_fixup encoder and CRTC helper operations to adjust the
requested mode, or reject it completely in which case an error will be
returned to the application. If the new configuration after mode
adjustment is identical to the current configuration the helper function
will return without performing any other operation.

If the adjusted mode is identical to the current mode but changes to the
frame buffer need to be applied, the ``drm_crtc_helper_set_config``
function will call the CRTC ->``mode_set_base`` (struct
``drm_crtc_helper_funcs``) helper operation.

If the adjusted mode differs from the current mode, or if the
->``mode_set_base`` helper operation is not provided, the helper
function performs a full mode set sequence by calling the ->``prepare``,
->``mode_set`` and ->``commit`` CRTC and encoder helper operations, in
that order. Alternatively it can also use the dpms and disable helper
operations. For details see struct ``drm_crtc_helper_funcs`` and struct
``drm_encoder_helper_funcs``.

This function is deprecated. New drivers must implement atomic modeset
support, for which this function is unsuitable. Instead drivers should
use ``drm_atomic_helper_set_config``.


Returns
=======

Returns 0 on success, negative errno numbers on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
