
.. _API-ata-dev-pair:

============
ata_dev_pair
============

*man ata_dev_pair(9)*

*4.6.0-rc1*

return other device on cable


Synopsis
========

.. c:function:: struct ata_device ⋆ ata_dev_pair( struct ata_device * adev )

Arguments
=========

``adev``
    device


Description
===========

Obtain the other device on the same cable, or if none is present NULL is returned
