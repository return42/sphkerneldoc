.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/sn/kernel/sn2/cache.c

.. _`sn_flush_all_caches`:

sn_flush_all_caches
===================

.. c:function:: void sn_flush_all_caches(long flush_addr, long bytes)

    flush a range of address from all caches (incl. L4)

    :param flush_addr:
        identity mapped region 7 address to start flushing
    :type flush_addr: long

    :param bytes:
        number of bytes to flush
    :type bytes: long

.. _`sn_flush_all_caches.description`:

Description
-----------

Flush a range of addresses from all caches including L4.
All addresses fully or partially contained within
\ ``flush_addr``\  to \ ``flush_addr``\  + \ ``bytes``\  are flushed
from all caches.

.. This file was automatic generated / don't edit.

