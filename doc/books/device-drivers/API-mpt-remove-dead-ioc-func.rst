.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-remove-dead-ioc-func:

========================
mpt_remove_dead_ioc_func
========================

*man mpt_remove_dead_ioc_func(9)*

*4.6.0-rc5*

kthread context to remove dead ioc


Synopsis
========

.. c:function:: int mpt_remove_dead_ioc_func( void * arg )

Arguments
=========

``arg``
    input argument, used to derive ioc


Description
===========

Return 0 if controller is removed from pci subsystem. Return -1 for
other case.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
