.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-rbuf-put:

=================
ata_scsi_rbuf_put
=================

*man ata_scsi_rbuf_put(9)*

*4.6.0-rc5*

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

Returns rbuf buffer. The result is copied to ``cmd``'s buffer if
``copy_back`` is true.


LOCKING
=======

Unlocks ata_scsi_rbuf_lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
