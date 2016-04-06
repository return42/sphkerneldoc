
.. _API-transport-configure-device:

==========================
transport_configure_device
==========================

*man transport_configure_device(9)*

*4.6.0-rc1*

configure an already set up device


Synopsis
========

.. c:function:: void transport_configure_device( struct device * dev )

Arguments
=========

``dev``
    generic device representing device to be configured


Description
===========

The idea of configure is simply to provide a point within the setup process to allow the transport class to extract information from a device after it has been setup. This is used
in SCSI because we have to have a setup device to begin using the HBA, but after we send the initial inquiry, we use configure to extract the device parameters. The device need not
have been added to be configured.
