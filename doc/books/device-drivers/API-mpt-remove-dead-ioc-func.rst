
.. _API-mpt-remove-dead-ioc-func:

========================
mpt_remove_dead_ioc_func
========================

*man mpt_remove_dead_ioc_func(9)*

*4.6.0-rc1*

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

Return 0 if controller is removed from pci subsystem. Return -1 for other case.
