.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-std-postreset:

=================
ata_std_postreset
=================

*man ata_std_postreset(9)*

*4.6.0-rc5*

standard postreset callback


Synopsis
========

.. c:function:: void ata_std_postreset( struct ata_link * link, unsigned int * classes )

Arguments
=========

``link``
    the target ata_link

``classes``
    classes of attached devices


Description
===========

This function is invoked after a successful reset. Note that the device
might have been reset more than once using different reset methods
before postreset is invoked.


LOCKING
=======

Kernel thread context (may sleep)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
