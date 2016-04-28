.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-print-link-status:

======================
sata_print_link_status
======================

*man sata_print_link_status(9)*

*4.6.0-rc5*

Print SATA link status


Synopsis
========

.. c:function:: void sata_print_link_status( struct ata_link * link )

Arguments
=========

``link``
    SATA link to printk link status about


Description
===========

This function prints link speed and status of a SATA link.


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
