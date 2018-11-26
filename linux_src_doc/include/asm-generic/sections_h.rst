.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/sections.h

.. _`memory_contains`:

memory_contains
===============

.. c:function:: bool memory_contains(void *begin, void *end, void *virt, size_t size)

    checks if an object is contained within a memory region

    :param begin:
        virtual address of the beginning of the memory region
    :type begin: void \*

    :param end:
        virtual address of the end of the memory region
    :type end: void \*

    :param virt:
        virtual address of the memory object
    :type virt: void \*

    :param size:
        size of the memory object
    :type size: size_t

.. _`memory_contains.return`:

Return
------

true if the object specified by \ ``virt``\  and \ ``size``\  is entirely
contained within the memory region defined by \ ``begin``\  and \ ``end``\ , false
otherwise.

.. _`memory_intersects`:

memory_intersects
=================

.. c:function:: bool memory_intersects(void *begin, void *end, void *virt, size_t size)

    checks if the region occupied by an object intersects with another memory region

    :param begin:
        virtual address of the beginning of the memory regien
    :type begin: void \*

    :param end:
        virtual address of the end of the memory region
    :type end: void \*

    :param virt:
        virtual address of the memory object
    :type virt: void \*

    :param size:
        size of the memory object
    :type size: size_t

.. _`memory_intersects.return`:

Return
------

true if an object's memory region, specified by \ ``virt``\  and \ ``size``\ ,
intersects with the region specified by \ ``begin``\  and \ ``end``\ , false otherwise.

.. _`init_section_contains`:

init_section_contains
=====================

.. c:function:: bool init_section_contains(void *virt, size_t size)

    checks if an object is contained within the init section

    :param virt:
        virtual address of the memory object
    :type virt: void \*

    :param size:
        size of the memory object
    :type size: size_t

.. _`init_section_contains.return`:

Return
------

true if the object specified by \ ``virt``\  and \ ``size``\  is entirely
contained within the init section, false otherwise.

.. _`init_section_intersects`:

init_section_intersects
=======================

.. c:function:: bool init_section_intersects(void *virt, size_t size)

    checks if the region occupied by an object intersects with the init section

    :param virt:
        virtual address of the memory object
    :type virt: void \*

    :param size:
        size of the memory object
    :type size: size_t

.. _`init_section_intersects.return`:

Return
------

true if an object's memory region, specified by \ ``virt``\  and \ ``size``\ ,
intersects with the init section, false otherwise.

.. _`is_kernel_rodata`:

is_kernel_rodata
================

.. c:function:: bool is_kernel_rodata(unsigned long addr)

    checks if the pointer address is located in the .rodata section

    :param addr:
        address to check
    :type addr: unsigned long

.. _`is_kernel_rodata.return`:

Return
------

true if the address is located in .rodata, false otherwise.

.. This file was automatic generated / don't edit.

