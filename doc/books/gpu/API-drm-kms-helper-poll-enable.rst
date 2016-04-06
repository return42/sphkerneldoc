
.. _API-drm-kms-helper-poll-enable:

==========================
drm_kms_helper_poll_enable
==========================

*man drm_kms_helper_poll_enable(9)*

*4.6.0-rc1*

re-enable output polling.


Synopsis
========

.. c:function:: void drm_kms_helper_poll_enable( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device


Description
===========

This function re-enables the output polling work.

Drivers can call this helper from their device resume implementation. It is an error to call this when the output polling support has not yet been set up.
