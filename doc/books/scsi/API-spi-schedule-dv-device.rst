
.. _API-spi-schedule-dv-device:

======================
spi_schedule_dv_device
======================

*man spi_schedule_dv_device(9)*

*4.6.0-rc1*

schedule domain validation to occur on the device


Synopsis
========

.. c:function:: void spi_schedule_dv_device( struct scsi_device * sdev )

Arguments
=========

``sdev``
    The device to validate


Description
===========

Identical to ``spi_dv_device`` above, except that the DV will be scheduled to occur in a workqueue later. All memory allocations are atomic, so may be called from any context
including those holding SCSI locks.
