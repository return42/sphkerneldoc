
.. _API-scsi-vpd-lun-id:

===============
scsi_vpd_lun_id
===============

*man scsi_vpd_lun_id(9)*

*4.6.0-rc1*

return a unique device identification


Synopsis
========

.. c:function:: int scsi_vpd_lun_id( struct scsi_device * sdev, char * id, size_t id_len )

Arguments
=========

``sdev``
    SCSI device

``id``
    buffer for the identification

``id_len``
    length of the buffer


Description
===========

Copies a unique device identification into ``id`` based on the information in the VPD page 0x83 of the device. The string will be formatted as a SCSI name string.

Returns the length of the identification or error on failure. If the identifier is longer than the supplied buffer the actual identifier length is returned and the buffer is not
zero-padded.
