
.. _API-scsi-is-sas-port:

================
scsi_is_sas_port
================

*man scsi_is_sas_port(9)*

*4.6.0-rc1*

check if a struct device represents a SAS port


Synopsis
========

.. c:function:: int scsi_is_sas_port( const struct device * dev )

Arguments
=========

``dev``
    device to check


Returns
=======

``1`` if the device represents a SAS Port, ``0`` else
