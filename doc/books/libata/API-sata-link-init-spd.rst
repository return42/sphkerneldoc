.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-link-init-spd:

==================
sata_link_init_spd
==================

*man sata_link_init_spd(9)*

*4.6.0-rc5*

Initialize link->sata_spd_limit


Synopsis
========

.. c:function:: int sata_link_init_spd( struct ata_link * link )

Arguments
=========

``link``
    Link to configure sata_spd_limit for


Description
===========

Initialize ``link``->[hw_]sata_spd_limit to the currently configured
value.


LOCKING
=======

Kernel thread context (may sleep).


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
