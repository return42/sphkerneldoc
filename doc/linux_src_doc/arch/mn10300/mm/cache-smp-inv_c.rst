.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/mm/cache-smp-inv.c

.. _`mn10300_icache_inv`:

mn10300_icache_inv
==================

.. c:function:: void mn10300_icache_inv( void)

    Globally invalidate instruction cache

    :param  void:
        no arguments

.. _`mn10300_icache_inv.description`:

Description
-----------

Invalidate the instruction cache on all CPUs.

.. _`mn10300_icache_inv_page`:

mn10300_icache_inv_page
=======================

.. c:function:: void mn10300_icache_inv_page(unsigned long start)

    Globally invalidate a page of instruction cache

    :param unsigned long start:
        The address of the page of memory to be invalidated.

.. _`mn10300_icache_inv_page.description`:

Description
-----------

Invalidate a range of addresses in the instruction cache on all CPUs
covering the page that includes the given address.

.. _`mn10300_icache_inv_range`:

mn10300_icache_inv_range
========================

.. c:function:: void mn10300_icache_inv_range(unsigned long start, unsigned long end)

    Globally invalidate range of instruction cache

    :param unsigned long start:
        The start address of the region to be invalidated.

    :param unsigned long end:
        The end address of the region to be invalidated.

.. _`mn10300_icache_inv_range.description`:

Description
-----------

Invalidate a range of addresses in the instruction cache on all CPUs,
between start and end-1 inclusive.

.. _`mn10300_icache_inv_range2`:

mn10300_icache_inv_range2
=========================

.. c:function:: void mn10300_icache_inv_range2(unsigned long start, unsigned long size)

    Globally invalidate range of instruction cache

    :param unsigned long start:
        The start address of the region to be invalidated.

    :param unsigned long size:
        The size of the region to be invalidated.

.. _`mn10300_icache_inv_range2.description`:

Description
-----------

Invalidate a range of addresses in the instruction cache on all CPUs,
between start and start+size-1 inclusive.

.. _`mn10300_dcache_inv`:

mn10300_dcache_inv
==================

.. c:function:: void mn10300_dcache_inv( void)

    Globally invalidate data cache

    :param  void:
        no arguments

.. _`mn10300_dcache_inv.description`:

Description
-----------

Invalidate the data cache on all CPUs.

.. _`mn10300_dcache_inv_page`:

mn10300_dcache_inv_page
=======================

.. c:function:: void mn10300_dcache_inv_page(unsigned long start)

    Globally invalidate a page of data cache

    :param unsigned long start:
        The address of the page of memory to be invalidated.

.. _`mn10300_dcache_inv_page.description`:

Description
-----------

Invalidate a range of addresses in the data cache on all CPUs covering the
page that includes the given address.

.. _`mn10300_dcache_inv_range`:

mn10300_dcache_inv_range
========================

.. c:function:: void mn10300_dcache_inv_range(unsigned long start, unsigned long end)

    Globally invalidate range of data cache

    :param unsigned long start:
        The start address of the region to be invalidated.

    :param unsigned long end:
        The end address of the region to be invalidated.

.. _`mn10300_dcache_inv_range.description`:

Description
-----------

Invalidate a range of addresses in the data cache on all CPUs, between start
and end-1 inclusive.

.. _`mn10300_dcache_inv_range2`:

mn10300_dcache_inv_range2
=========================

.. c:function:: void mn10300_dcache_inv_range2(unsigned long start, unsigned long size)

    Globally invalidate range of data cache

    :param unsigned long start:
        The start address of the region to be invalidated.

    :param unsigned long size:
        The size of the region to be invalidated.

.. _`mn10300_dcache_inv_range2.description`:

Description
-----------

Invalidate a range of addresses in the data cache on all CPUs, between start
and start+size-1 inclusive.

.. This file was automatic generated / don't edit.

