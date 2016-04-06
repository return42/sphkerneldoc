
.. _API-drm-kms-helper-poll-disable:

===========================
drm_kms_helper_poll_disable
===========================

*man drm_kms_helper_poll_disable(9)*

*4.6.0-rc1*

disable output polling


Synopsis
========

.. c:function:: void drm_kms_helper_poll_disable( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device


Description
===========

This function disables the output polling work.

Drivers can call this helper from their device suspend implementation. It is not an error to call this even when output polling isn't enabled or arlready disabled.
