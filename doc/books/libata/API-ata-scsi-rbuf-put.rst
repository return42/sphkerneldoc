
.. _API-ata-scsi-rbuf-put:

=================
ata_scsi_rbuf_put
=================

*man ata_scsi_rbuf_put(9)*

*4.6.0-rc1*

Unmap response buffer.


Synopsis
========

.. c:function:: void ata_scsi_rbuf_put( struct scsi_cmnd * cmd, bool copy_out, unsigned long * flags )

Arguments
=========

``cmd``
    SCSI command containing buffer to be unmapped.

``copy_out``
    copy out result

``flags``
    ``flags`` passed to ``ata_scsi_rbuf_get``


Description
===========

Returns rbuf buffer. The result is copied to ``cmd``'s buffer if ``copy_back`` is true.


LOCKING
=======

Unlocks ata_scsi_rbuf_lock.
