
.. _API-ata-scsi-rbuf-get:

=================
ata_scsi_rbuf_get
=================

*man ata_scsi_rbuf_get(9)*

*4.6.0-rc1*

Map response buffer.


Synopsis
========

.. c:function:: void ⋆ ata_scsi_rbuf_get( struct scsi_cmnd * cmd, bool copy_in, unsigned long * flags )

Arguments
=========

``cmd``
    SCSI command containing buffer to be mapped.

``copy_in``
    copy in from user buffer

``flags``
    unsigned long variable to store irq enable status


Description
===========

Prepare buffer for simulated SCSI commands.


LOCKING
=======

spin_lock_irqsave(ata_scsi_rbuf_lock) on success


RETURNS
=======

Pointer to response buffer.
