.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-encoder-funcs:

========================
struct drm_encoder_funcs
========================

*man struct drm_encoder_funcs(9)*

*4.6.0-rc5*

encoder controls


Synopsis
========

.. code-block:: c

    struct drm_encoder_funcs {
      void (* reset) (struct drm_encoder *encoder);
      void (* destroy) (struct drm_encoder *encoder);
    };


Members
=======

reset
    Reset encoder hardware and software state to off. This function
    isn't called by the core directly, only through
    ``drm_mode_config_reset``. It's not a helper hook only for
    historical reasons.

destroy
    Clean up encoder resources. This is only called at driver unload
    time through ``drm_mode_config_cleanup`` since an encoder cannot be
    hotplugged in DRM.


Description
===========

Encoders sit between CRTCs and connectors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
