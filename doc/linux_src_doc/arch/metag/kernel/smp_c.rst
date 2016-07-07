.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/kernel/smp.c

.. _`describe_cachepart_change`:

describe_cachepart_change
=========================

.. c:function:: void describe_cachepart_change(unsigned int thread, const char *label, unsigned int sz, unsigned int old, unsigned int new)

    describe a change to cache partitions.

    :param unsigned int thread:
        Hardware thread number.

    :param const char \*label:
        Label of cache type, e.g. "dcache" or "icache".

    :param unsigned int sz:
        Total size of the cache.

    :param unsigned int old:
        Old cache partition configuration (\*CPART\* register).

    :param unsigned int new:
        New cache partition configuration (\*CPART\* register).

.. _`describe_cachepart_change.description`:

Description
-----------

If the cache partition has changed, prints a message to the log describing
those changes.

.. _`setup_smp_cache`:

setup_smp_cache
===============

.. c:function:: void setup_smp_cache(unsigned int thread)

    ensure cache coherency for new SMP thread.

    :param unsigned int thread:
        New hardware thread number.

.. _`setup_smp_cache.description`:

Description
-----------

Ensures that coherency is enabled and that the threads share the same cache
partitions.

.. This file was automatic generated / don't edit.

