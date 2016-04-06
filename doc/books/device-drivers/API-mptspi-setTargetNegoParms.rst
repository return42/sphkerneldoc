
.. _API-mptspi-setTargetNegoParms:

=========================
mptspi_setTargetNegoParms
=========================

*man mptspi_setTargetNegoParms(9)*

*4.6.0-rc1*

Update the target negotiation parameters


Synopsis
========

.. c:function:: void mptspi_setTargetNegoParms( MPT_SCSI_HOST * hd, VirtTarget * target, struct scsi_device * sdev )

Arguments
=========

``hd``
    Pointer to a SCSI Host Structure

``target``
    per target private data

``sdev``
    SCSI device


Description
===========

Update the target negotiation parameters based on the the Inquiry data, adapter capabilities, and NVRAM settings.
