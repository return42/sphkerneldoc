
.. _API-mptscsih-dev-reset:

==================
mptscsih_dev_reset
==================

*man mptscsih_dev_reset(9)*

*4.6.0-rc1*

Perform a SCSI TARGET_RESET! new_eh variant


Synopsis
========

.. c:function:: int mptscsih_dev_reset( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure, IO which reset is due to


Description
===========

(linux scsi_host_template.eh_dev_reset_handler routine)

Returns SUCCESS or FAILED.
