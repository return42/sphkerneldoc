.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-pair:

============
ata_dev_pair
============

*man ata_dev_pair(9)*

*4.6.0-rc5*

return other device on cable


Synopsis
========

.. c:function:: struct ata_device * ata_dev_pair( struct ata_device * adev )

Arguments
=========

``adev``
    device


Description
===========

Obtain the other device on the same cable, or if none is present NULL is
returned


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
