.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-set-spd:

============
sata_set_spd
============

*man sata_set_spd(9)*

*4.6.0-rc5*

set SATA spd according to spd limit


Synopsis
========

.. c:function:: int sata_set_spd( struct ata_link * link )

Arguments
=========

``link``
    Link to set SATA spd for


Description
===========

Set SATA spd of ``link`` according to sata_spd_limit.


LOCKING
=======

Inherited from caller.


RETURNS
=======

0 if spd doesn't need to be changed, 1 if spd has been changed. Negative
errno if SCR registers are inaccessible.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
