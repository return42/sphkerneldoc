.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-down-spd-limit:

===================
sata_down_spd_limit
===================

*man sata_down_spd_limit(9)*

*4.6.0-rc5*

adjust SATA spd limit downward


Synopsis
========

.. c:function:: int sata_down_spd_limit( struct ata_link * link, u32 spd_limit )

Arguments
=========

``link``
    Link to adjust SATA spd limit for

``spd_limit``
    Additional limit


Description
===========

Adjust SATA spd limit of ``link`` downward. Note that this function only
adjusts the limit. The change must be applied using ``sata_set_spd``.

If ``spd_limit`` is non-zero, the speed is limited to equal to or lower
than ``spd_limit`` if such speed is supported. If ``spd_limit`` is
slower than any supported speed, only the lowest supported speed is
allowed.


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
