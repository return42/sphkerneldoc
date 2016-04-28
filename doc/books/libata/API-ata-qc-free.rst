.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-qc-free:

===========
ata_qc_free
===========

*man ata_qc_free(9)*

*4.6.0-rc5*

free unused ata_queued_cmd


Synopsis
========

.. c:function:: void ata_qc_free( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Command to complete


Description
===========

Designed to free unused ata_queued_cmd object in case something
prevents using it.


LOCKING
=======

spin_lock_irqsave(host lock)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
