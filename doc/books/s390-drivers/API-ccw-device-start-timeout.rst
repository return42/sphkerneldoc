
.. _API-ccw-device-start-timeout:

========================
ccw_device_start_timeout
========================

*man ccw_device_start_timeout(9)*

*4.6.0-rc1*

start a s390 channel program with timeout


Synopsis
========

.. c:function:: int ccw_device_start_timeout( struct ccw_device * cdev, struct ccw1 * cpa, unsigned long intparm, __u8 lpm, unsigned long flags, int expires )

Arguments
=========

``cdev``
    target ccw device

``cpa``
    logical start address of channel program

``intparm``
    user specific interruption parameter; will be presented back to ``cdev``'s interrupt handler. Allows a device driver to associate the interrupt with a particular I/O request.

``lpm``
    defines the channel path to be used for a specific I/O request. A value of 0 will make cio use the opm.

``flags``
    additional flags; defines the action to be performed for I/O processing.

``expires``
    timeout value in jiffies


Description
===========

Start a S/390 channel program. When the interrupt arrives, the IRQ handler is called, either immediately, delayed (dev-end missing, or sense required) or never (no IRQ handler
registered). This function notifies the device driver if the channel program has not completed during the time specified by ``expires``. If a timeout occurs, the channel program is
terminated via xsch, hsch or csch, and the device's interrupt handler will be called with an irb containing ERR_PTR(- ``ETIMEDOUT``).


Returns
=======

``0``, if the operation was successful; -``EBUSY``, if the device is busy, or status pending; -``EACCES``, if no path specified in ``lpm`` is operational; -``ENODEV``, if the
device is not operational.


Context
=======

Interrupts disabled, ccw device lock held
