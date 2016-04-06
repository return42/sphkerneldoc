
.. _API-blk-pre-runtime-suspend:

=======================
blk_pre_runtime_suspend
=======================

*man blk_pre_runtime_suspend(9)*

*4.6.0-rc1*

Pre runtime suspend check


Synopsis
========

.. c:function:: int blk_pre_runtime_suspend( struct request_queue * q )

Arguments
=========

``q``
    the queue of the device


Description
===========

This function will check if runtime suspend is allowed for the device by examining if there are any requests pending in the queue. If there are requests pending, the device can not
be runtime suspended; otherwise, the queue's status will be updated to SUSPENDING and the driver can proceed to suspend the device.

For the not allowed case, we mark last busy for the device so that runtime PM core will try to autosuspend it some time later.

This function should be called near the start of the device's runtime_suspend callback.


Return
======

0 - OK to runtime suspend the device -EBUSY - Device should not be runtime suspended
