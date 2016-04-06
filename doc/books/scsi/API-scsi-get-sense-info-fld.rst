
.. _API-scsi-get-sense-info-fld:

=======================
scsi_get_sense_info_fld
=======================

*man scsi_get_sense_info_fld(9)*

*4.6.0-rc1*

get information field from sense data (either fixed or descriptor format)


Synopsis
========

.. c:function:: int scsi_get_sense_info_fld( const u8 * sense_buffer, int sb_len, u64 * info_out )

Arguments
=========

``sense_buffer``
    byte array of sense data

``sb_len``
    number of valid bytes in sense_buffer

``info_out``
    pointer to 64 integer where 8 or 4 byte information field will be placed if found.


Return value
============

1 if information field found, 0 if not found.
