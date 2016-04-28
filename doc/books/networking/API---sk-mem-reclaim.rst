.. -*- coding: utf-8; mode: rst -*-

.. _API---sk-mem-reclaim:

================
__sk_mem_reclaim
================

*man __sk_mem_reclaim(9)*

*4.6.0-rc5*

reclaim memory_allocated


Synopsis
========

.. c:function:: void __sk_mem_reclaim( struct sock * sk, int amount )

Arguments
=========

``sk``
    socket

``amount``
    number of bytes (rounded down to a SK_MEM_QUANTUM multiple)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
