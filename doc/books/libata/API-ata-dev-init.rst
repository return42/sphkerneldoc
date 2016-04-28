.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-init:

============
ata_dev_init
============

*man ata_dev_init(9)*

*4.6.0-rc5*

Initialize an ata_device structure


Synopsis
========

.. c:function:: void ata_dev_init( struct ata_device * dev )

Arguments
=========

``dev``
    Device structure to initialize


Description
===========

Initialize ``dev`` in preparation for probing.


LOCKING
=======

Inherited from caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
