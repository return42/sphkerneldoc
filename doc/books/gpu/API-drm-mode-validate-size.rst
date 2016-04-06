
.. _API-drm-mode-validate-size:

======================
drm_mode_validate_size
======================

*man drm_mode_validate_size(9)*

*4.6.0-rc1*

make sure modes adhere to size constraints


Synopsis
========

.. c:function:: enum drm_mode_status drm_mode_validate_size( const struct drm_display_mode * mode, int maxX, int maxY )

Arguments
=========

``mode``
    mode to check

``maxX``
    maximum width

``maxY``
    maximum height


Description
===========

This function is a helper which can be used to validate modes against size limitations of the DRM device/connector. If a mode is too big its status member is updated with the
appropriate validation failure code. The list itself is not changed.


Returns
=======

The mode status
