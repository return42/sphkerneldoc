.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/cpu/sh4/sq.c

.. _`sq_flush_range`:

sq_flush_range
==============

.. c:function:: void sq_flush_range(unsigned long start, unsigned int len)

    Flush (prefetch) a specific SQ range

    :param start:
        the store queue address to start flushing from
    :type start: unsigned long

    :param len:
        the length to flush
    :type len: unsigned int

.. _`sq_flush_range.description`:

Description
-----------

Flushes the store queue cache from \ ``start``\  to \ ``start``\  + \ ``len``\  in a
linear fashion.

.. _`sq_remap`:

sq_remap
========

.. c:function:: unsigned long sq_remap(unsigned long phys, unsigned int size, const char *name, pgprot_t prot)

    Map a physical address through the Store Queues

    :param phys:
        Physical address of mapping.
    :type phys: unsigned long

    :param size:
        Length of mapping.
    :type size: unsigned int

    :param name:
        User invoking mapping.
    :type name: const char \*

    :param prot:
        Protection bits.
    :type prot: pgprot_t

.. _`sq_remap.description`:

Description
-----------

Remaps the physical address \ ``phys``\  through the next available store queue
address of \ ``size``\  length. \ ``name``\  is logged at boot time as well as through
the sysfs interface.

.. _`sq_unmap`:

sq_unmap
========

.. c:function:: void sq_unmap(unsigned long vaddr)

    Unmap a Store Queue allocation

    :param vaddr:
        Pre-allocated Store Queue mapping.
    :type vaddr: unsigned long

.. _`sq_unmap.description`:

Description
-----------

Unmaps the store queue allocation \ ``map``\  that was previously created by
\ :c:func:`sq_remap`\ . Also frees up the pte that was previously inserted into
the kernel page table and discards the UTLB translation.

.. This file was automatic generated / don't edit.

