
.. _API-drm-mode-validate-basic:

=======================
drm_mode_validate_basic
=======================

*man drm_mode_validate_basic(9)*

*4.6.0-rc1*

make sure the mode is somewhat sane


Synopsis
========

.. c:function:: enum drm_mode_status drm_mode_validate_basic( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    mode to check


Description
===========

Check that the mode timings are at least somewhat reasonable. Any hardware specific limits are left up for each driver to check.


Returns
=======

The mode status
