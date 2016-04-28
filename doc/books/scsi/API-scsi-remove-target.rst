.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-remove-target:

==================
scsi_remove_target
==================

*man scsi_remove_target(9)*

*4.6.0-rc5*

try to remove a target and all its devices


Synopsis
========

.. c:function:: void scsi_remove_target( struct device * dev )

Arguments
=========

``dev``
    generic starget or parent of generic stargets to be removed


Note
====

This is slightly racy. It is possible that if the user requests the
addition of another device then the target won't be removed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
