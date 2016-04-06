
.. _API-device-pm-wait-for-dev:

======================
device_pm_wait_for_dev
======================

*man device_pm_wait_for_dev(9)*

*4.6.0-rc1*

Wait for suspend/resume of a device to complete.


Synopsis
========

.. c:function:: int device_pm_wait_for_dev( struct device * subordinate, struct device * dev )

Arguments
=========

``subordinate``
    Device that needs to wait for ``dev``.

``dev``
    Device to wait for.
