
.. _API-sata-print-link-status:

======================
sata_print_link_status
======================

*man sata_print_link_status(9)*

*4.6.0-rc1*

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
