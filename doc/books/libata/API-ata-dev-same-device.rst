.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-same-device:

===================
ata_dev_same_device
===================

*man ata_dev_same_device(9)*

*4.6.0-rc5*

Determine whether new ID matches configured device


Synopsis
========

.. c:function:: int ata_dev_same_device( struct ata_device * dev, unsigned int new_class, const u16 * new_id )

Arguments
=========

``dev``
    device to compare against

``new_class``
    class of the new device

``new_id``
    IDENTIFY page of the new device


Description
===========

Compare ``new_class`` and ``new_id`` against ``dev`` and determine
whether ``dev`` is the device indicated by ``new_class`` and ``new_id``.


LOCKING
=======

None.


RETURNS
=======

1 if ``dev`` matches ``new_class`` and ``new_id``, 0 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
