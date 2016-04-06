
.. _API-mptscsih-host-reset:

===================
mptscsih_host_reset
===================

*man mptscsih_host_reset(9)*

*4.6.0-rc1*

Perform a SCSI host adapter RESET (new_eh variant)


Synopsis
========

.. c:function:: int mptscsih_host_reset( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure, IO which reset is due to


Description
===========

(linux scsi_host_template.eh_host_reset_handler routine)

Returns SUCCESS or FAILED.
