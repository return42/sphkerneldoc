.. -*- coding: utf-8; mode: rst -*-

.. _API---sk-mem-schedule:

=================
__sk_mem_schedule
=================

*man __sk_mem_schedule(9)*

*4.6.0-rc5*

increase sk_forward_alloc and memory_allocated


Synopsis
========

.. c:function:: int __sk_mem_schedule( struct sock * sk, int size, int kind )

Arguments
=========

``sk``
    socket

``size``
    memory size to allocate

``kind``
    allocation type


Description
===========

If kind is SK_MEM_SEND, it means wmem allocation. Otherwise it means
rmem allocation. This function assumes that protocols which have
memory_pressure use sk_wmem_queued as write buffer accounting.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
