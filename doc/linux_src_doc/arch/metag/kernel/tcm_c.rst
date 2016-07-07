.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/kernel/tcm.c

.. _`tcm_alloc`:

tcm_alloc
=========

.. c:function:: unsigned long tcm_alloc(unsigned int tag, size_t len)

    allocate memory from a TCM pool

    :param unsigned int tag:
        tag of the pool to allocate memory from

    :param size_t len:
        number of bytes to be allocated

.. _`tcm_alloc.description`:

Description
-----------

Allocate the requested number of bytes from the pool matching
the specified tag. Returns the address of the allocated memory
or zero on failure.

.. _`tcm_free`:

tcm_free
========

.. c:function:: void tcm_free(unsigned int tag, unsigned long addr, size_t len)

    free a block of memory to a TCM pool

    :param unsigned int tag:
        tag of the pool to free memory to

    :param unsigned long addr:
        address of the memory to be freed

    :param size_t len:
        number of bytes to be freed

.. _`tcm_free.description`:

Description
-----------

Free the requested number of bytes at a specific address to the
pool matching the specified tag.

.. _`tcm_lookup_tag`:

tcm_lookup_tag
==============

.. c:function:: unsigned int tcm_lookup_tag(unsigned long p)

    find the tag matching an address

    :param unsigned long p:
        memory address to lookup the tag for

.. _`tcm_lookup_tag.description`:

Description
-----------

Find the tag of the tcm memory region that contains the
specified address. Returns \ ``TCM_INVALID_TAG``\  if no such
memory region could be found.

.. _`tcm_add_region`:

tcm_add_region
==============

.. c:function:: int tcm_add_region(struct tcm_region *reg)

    add a memory region to TCM pool list

    :param struct tcm_region \*reg:
        descriptor of region to be added

.. _`tcm_add_region.description`:

Description
-----------

Add a region of memory to the TCM pool list. Returns 0 on success.

.. This file was automatic generated / don't edit.

