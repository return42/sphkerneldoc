.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-down-xfermask-limit:

=======================
ata_down_xfermask_limit
=======================

*man ata_down_xfermask_limit(9)*

*4.6.0-rc5*

adjust dev xfer masks downward


Synopsis
========

.. c:function:: int ata_down_xfermask_limit( struct ata_device * dev, unsigned int sel )

Arguments
=========

``dev``
    Device to adjust xfer masks

``sel``
    ATA_DNXFER_* selector


Description
===========

Adjust xfer masks of ``dev`` downward. Note that this function does not
apply the change. Invoking ``ata_set_mode`` afterwards will apply the
limit.


LOCKING
=======

Inherited from caller.


RETURNS
=======

0 on success, negative errno on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
