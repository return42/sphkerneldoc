
.. _API-scsi-is-sas-phy:

===============
scsi_is_sas_phy
===============

*man scsi_is_sas_phy(9)*

*4.6.0-rc1*

check if a struct device represents a SAS PHY


Synopsis
========

.. c:function:: int scsi_is_sas_phy( const struct device * dev )

Arguments
=========

``dev``
    device to check


Returns
=======

``1`` if the device represents a SAS PHY, ``0`` else
