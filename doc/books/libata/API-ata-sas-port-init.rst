.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sas-port-init:

=================
ata_sas_port_init
=================

*man ata_sas_port_init(9)*

*4.6.0-rc5*

Initialize a SATA device


Synopsis
========

.. c:function:: int ata_sas_port_init( struct ata_port * ap )

Arguments
=========

``ap``
    SATA port to initialize


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

Zero on success, non-zero on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
