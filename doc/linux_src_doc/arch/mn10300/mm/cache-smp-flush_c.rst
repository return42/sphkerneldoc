.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/mm/cache-smp-flush.c

.. _`mn10300_dcache_flush`:

mn10300_dcache_flush
====================

.. c:function:: void mn10300_dcache_flush( void)

    Globally flush data cache

    :param  void:
        no arguments

.. _`mn10300_dcache_flush.description`:

Description
-----------

Flush the data cache on all CPUs.

.. _`mn10300_dcache_flush_page`:

mn10300_dcache_flush_page
=========================

.. c:function:: void mn10300_dcache_flush_page(unsigned long start)

    Globally flush a page of data cache

    :param unsigned long start:
        The address of the page of memory to be flushed.

.. _`mn10300_dcache_flush_page.description`:

Description
-----------

Flush a range of addresses in the data cache on all CPUs covering
the page that includes the given address.

.. _`mn10300_dcache_flush_range`:

mn10300_dcache_flush_range
==========================

.. c:function:: void mn10300_dcache_flush_range(unsigned long start, unsigned long end)

    Globally flush range of data cache

    :param unsigned long start:
        The start address of the region to be flushed.

    :param unsigned long end:
        The end address of the region to be flushed.

.. _`mn10300_dcache_flush_range.description`:

Description
-----------

Flush a range of addresses in the data cache on all CPUs, between start and
end-1 inclusive.

.. _`mn10300_dcache_flush_range2`:

mn10300_dcache_flush_range2
===========================

.. c:function:: void mn10300_dcache_flush_range2(unsigned long start, unsigned long size)

    Globally flush range of data cache

    :param unsigned long start:
        The start address of the region to be flushed.

    :param unsigned long size:
        The size of the region to be flushed.

.. _`mn10300_dcache_flush_range2.description`:

Description
-----------

Flush a range of addresses in the data cache on all CPUs, between start and
start+size-1 inclusive.

.. _`mn10300_dcache_flush_inv`:

mn10300_dcache_flush_inv
========================

.. c:function:: void mn10300_dcache_flush_inv( void)

    Globally flush and invalidate data cache

    :param  void:
        no arguments

.. _`mn10300_dcache_flush_inv.description`:

Description
-----------

Flush and invalidate the data cache on all CPUs.

.. _`mn10300_dcache_flush_inv_page`:

mn10300_dcache_flush_inv_page
=============================

.. c:function:: void mn10300_dcache_flush_inv_page(unsigned long start)

    Globally flush and invalidate a page of data cache

    :param unsigned long start:
        The address of the page of memory to be flushed and invalidated.

.. _`mn10300_dcache_flush_inv_page.description`:

Description
-----------

Flush and invalidate a range of addresses in the data cache on all CPUs
covering the page that includes the given address.

.. _`mn10300_dcache_flush_inv_range`:

mn10300_dcache_flush_inv_range
==============================

.. c:function:: void mn10300_dcache_flush_inv_range(unsigned long start, unsigned long end)

    Globally flush and invalidate range of data cache

    :param unsigned long start:
        The start address of the region to be flushed and invalidated.

    :param unsigned long end:
        The end address of the region to be flushed and invalidated.

.. _`mn10300_dcache_flush_inv_range.description`:

Description
-----------

Flush and invalidate a range of addresses in the data cache on all CPUs,
between start and end-1 inclusive.

.. _`mn10300_dcache_flush_inv_range2`:

mn10300_dcache_flush_inv_range2
===============================

.. c:function:: void mn10300_dcache_flush_inv_range2(unsigned long start, unsigned long size)

    Globally flush and invalidate range of data cache

    :param unsigned long start:
        The start address of the region to be flushed and invalidated.

    :param unsigned long size:
        The size of the region to be flushed and invalidated.

.. _`mn10300_dcache_flush_inv_range2.description`:

Description
-----------

Flush and invalidate a range of addresses in the data cache on all CPUs,
between start and start+size-1 inclusive.

.. This file was automatic generated / don't edit.

