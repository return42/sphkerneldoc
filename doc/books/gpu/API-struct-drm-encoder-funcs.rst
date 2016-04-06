
.. _API-struct-drm-encoder-funcs:

========================
struct drm_encoder_funcs
========================

*man struct drm_encoder_funcs(9)*

*4.6.0-rc1*

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
    Reset encoder hardware and software state to off. This function isn't called by the core directly, only through ``drm_mode_config_reset``. It's not a helper hook only for
    historical reasons.

destroy
    Clean up encoder resources. This is only called at driver unload time through ``drm_mode_config_cleanup`` since an encoder cannot be hotplugged in DRM.


Description
===========

Encoders sit between CRTCs and connectors.
