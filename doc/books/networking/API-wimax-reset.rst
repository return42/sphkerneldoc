
.. _API-wimax-reset:

===========
wimax_reset
===========

*man wimax_reset(9)*

*4.6.0-rc1*

Reset a WiMAX device


Synopsis
========

.. c:function:: int wimax_reset( struct wimax_dev * wimax_dev )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor


Returns
=======

``0`` if ok and a warm reset was done (the device still exists in the system).

-``ENODEV`` if a cold/bus reset had to be done (device has disconnected and reconnected, so current handle is not valid any more).

-``EINVAL`` if the device is not even registered.

Any other negative error code shall be considered as non-recoverable.


Description
===========

Called when wanting to reset the device for any reason. Device is taken back to power on status.

This call blocks; on successful return, the device has completed the reset process and is ready to operate.
