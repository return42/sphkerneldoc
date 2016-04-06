
.. _API-scsi-is-sas-rphy:

================
scsi_is_sas_rphy
================

*man scsi_is_sas_rphy(9)*

*4.6.0-rc1*

check if a struct device represents a SAS remote PHY


Synopsis
========

.. c:function:: int scsi_is_sas_rphy( const struct device * dev )

Arguments
=========

``dev``
    device to check


Returns
=======

``1`` if the device represents a SAS remote PHY, ``0`` else
