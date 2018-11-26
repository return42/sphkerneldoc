.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/um/kernel/physmem.c

.. _`setup_physmem`:

setup_physmem
=============

.. c:function:: void setup_physmem(unsigned long start, unsigned long reserve_end, unsigned long len, unsigned long long highmem)

    Setup physical memory for UML

    :param start:
        Start address of the physical kernel memory,
        i.e start address of the executable image.
    :type start: unsigned long

    :param reserve_end:
        end address of the physical kernel memory.
    :type reserve_end: unsigned long

    :param len:
        Length of total physical memory that should be mapped/made
        available, in bytes.
    :type len: unsigned long

    :param highmem:
        Number of highmem bytes that should be mapped/made available.
    :type highmem: unsigned long long

.. _`setup_physmem.description`:

Description
-----------

Creates an unlinked temporary file of size (len + highmem) and memory maps
it on the last executable image address (uml_reserved).

The offset is needed as the length of the total physical memory
(len + highmem) includes the size of the memory used be the executable image,
but the mapped-to address is the last address of the executable image
(uml_reserved == end address of executable image).

The memory mapped memory of the temporary file is used as backing memory
of all user space processes/kernel tasks.

.. This file was automatic generated / don't edit.

