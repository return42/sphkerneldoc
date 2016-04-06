
.. _API-drm-mode-set-config-internal:

============================
drm_mode_set_config_internal
============================

*man drm_mode_set_config_internal(9)*

*4.6.0-rc1*

helper to call ->set_config


Synopsis
========

.. c:function:: int drm_mode_set_config_internal( struct drm_mode_set * set )

Arguments
=========

``set``
    modeset config to set


Description
===========

This is a little helper to wrap internal calls to the ->set_config driver interface. The only thing it adds is correct refcounting dance.


Returns
=======

Zero on success, negative errno on failure.
