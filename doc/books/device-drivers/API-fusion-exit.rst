.. -*- coding: utf-8; mode: rst -*-

.. _API-fusion-exit:

===========
fusion_exit
===========

*man fusion_exit(9)*

*4.6.0-rc5*

Perform driver unload cleanup.


Synopsis
========

.. c:function:: void __exit fusion_exit( void )

Arguments
=========

``void``
    no arguments


Description
===========

This routine frees all resources associated with each MPT adapter and
removes all ``MPT_PROCFS_MPTBASEDIR`` entries.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
