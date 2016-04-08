
.. _API-ata-dev-init:

============
ata_dev_init
============

*man ata_dev_init(9)*

*4.6.0-rc1*

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
