.. -*- coding: utf-8; mode: rst -*-

.. _API-piix-pata-prereset:

==================
piix_pata_prereset
==================

*man piix_pata_prereset(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
