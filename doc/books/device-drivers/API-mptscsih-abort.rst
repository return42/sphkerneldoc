
.. _API-mptscsih-abort:

==============
mptscsih_abort
==============

*man mptscsih_abort(9)*

*4.6.0-rc1*

Abort linux scsi_cmnd routine, new_eh variant


Synopsis
========

.. c:function:: int mptscsih_abort( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure, IO to be aborted


Description
===========

(linux scsi_host_template.eh_abort_handler routine)

Returns SUCCESS or FAILED.
