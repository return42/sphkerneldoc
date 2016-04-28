.. -*- coding: utf-8; mode: rst -*-

.. _API-deactivate-super:

================
deactivate_super
================

*man deactivate_super(9)*

*4.6.0-rc5*

drop an active reference to superblock


Synopsis
========

.. c:function:: void deactivate_super( struct super_block * s )

Arguments
=========

``s``
    superblock to deactivate


Description
===========

Variant of ``deactivate_locked_super``, except that superblock is *not*
locked by caller. If we are going to drop the final active reference,
lock will be acquired prior to that.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
