
.. _API---sk-mem-reclaim:

================
__sk_mem_reclaim
================

*man __sk_mem_reclaim(9)*

*4.6.0-rc1*

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
