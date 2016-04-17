.. -*- coding: utf-8; mode: rst -*-

=======
cache.c
=======


.. _`sn_flush_all_caches`:

sn_flush_all_caches
===================

.. c:function:: void sn_flush_all_caches (long flush_addr, long bytes)

    flush a range of address from all caches (incl. L4)

    :param long flush_addr:
        identity mapped region 7 address to start flushing

    :param long bytes:
        number of bytes to flush



.. _`sn_flush_all_caches.description`:

Description
-----------

Flush a range of addresses from all caches including L4. 
All addresses fully or partially contained within 
``flush_addr`` to ``flush_addr`` + ``bytes`` are flushed
from all caches.

