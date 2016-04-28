.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-msense-rw-recovery:

======================
ata_msense_rw_recovery
======================

*man ata_msense_rw_recovery(9)*

*4.6.0-rc5*

Simulate MODE SENSE r/w error recovery page


Synopsis
========

.. c:function:: unsigned int ata_msense_rw_recovery( u8 * buf, bool changeable )

Arguments
=========

``buf``
    output buffer

``changeable``
    whether changeable parameters are requested


Description
===========

Generate a generic MODE SENSE r/w error recovery page.


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
