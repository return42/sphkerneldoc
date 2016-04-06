
.. _API-mptscsih-info:

=============
mptscsih_info
=============

*man mptscsih_info(9)*

*4.6.0-rc1*

Return information about MPT adapter


Synopsis
========

.. c:function:: const char ⋆ mptscsih_info( struct Scsi_Host * SChost )

Arguments
=========

``SChost``
    Pointer to Scsi_Host structure


Description
===========

(linux scsi_host_template.info routine)

Returns pointer to buffer where information was written.
