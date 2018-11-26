.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/mm/pgalloc.c

.. _`base_asce_free`:

base_asce_free
==============

.. c:function:: void base_asce_free(unsigned long asce)

    free asce and tables returned from \ :c:func:`base_asce_alloc`\ 

    :param asce:
        asce to be freed
    :type asce: unsigned long

.. _`base_asce_free.description`:

Description
-----------

Frees all region, segment, and page tables that were allocated with a
corresponding \ :c:func:`base_asce_alloc`\  call.

.. _`base_asce_alloc`:

base_asce_alloc
===============

.. c:function:: unsigned long base_asce_alloc(unsigned long addr, unsigned long num_pages)

    create kernel mapping without enhanced DAT features

    :param addr:
        virtual start address of kernel mapping
    :type addr: unsigned long

    :param num_pages:
        number of consecutive pages
    :type num_pages: unsigned long

.. _`base_asce_alloc.description`:

Description
-----------

Generate an asce, including all required region, segment and page tables,
that can be used to access the virtual kernel mapping. The difference is
that the returned asce does not make use of any enhanced DAT features like
e.g. large pages. This is required for some I/O functions that pass an
asce, like e.g. some service call requests.

.. _`base_asce_alloc.note`:

Note
----

the returned asce may NEVER be attached to any cpu. It may only be
used for I/O requests. tlb entries that might result because the
asce was attached to a cpu won't be cleared.

.. This file was automatic generated / don't edit.

