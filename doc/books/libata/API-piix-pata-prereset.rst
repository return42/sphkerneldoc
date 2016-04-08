
.. _API-piix-pata-prereset:

==================
piix_pata_prereset
==================

*man piix_pata_prereset(9)*

*4.6.0-rc1*

prereset for PATA host controller


Synopsis
========

.. c:function:: int piix_pata_prereset( struct ata_link * link, unsigned long deadline )

Arguments
=========

``link``
    Target link

``deadline``
    deadline jiffies for the operation


LOCKING
=======

None (inherited from caller).
