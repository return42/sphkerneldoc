
.. _API-drm-helper-encoder-in-use:

=========================
drm_helper_encoder_in_use
=========================

*man drm_helper_encoder_in_use(9)*

*4.6.0-rc1*

check if a given encoder is in use


Synopsis
========

.. c:function:: bool drm_helper_encoder_in_use( struct drm_encoder * encoder )

Arguments
=========

``encoder``
    encoder to check


Description
===========

Checks whether ``encoder`` is with the current mode setting output configuration in use by any connector. This doesn't mean that it is actually enabled since the DPMS state is
tracked separately.


Returns
=======

True if ``encoder`` is used, false otherwise.
