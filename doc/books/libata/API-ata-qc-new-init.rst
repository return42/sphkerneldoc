.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-qc-new-init:

===============
ata_qc_new_init
===============

*man ata_qc_new_init(9)*

*4.6.0-rc5*

Request an available ATA command, and initialize it


Synopsis
========

.. c:function:: struct ata_queued_cmd * ata_qc_new_init( struct ata_device * dev, int tag )

Arguments
=========

``dev``
    Device from whom we request an available command structure

``tag``
    tag


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
