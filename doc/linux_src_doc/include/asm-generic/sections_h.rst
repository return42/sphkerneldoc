.. -*- coding: utf-8; mode: rst -*-

==========
sections.h
==========


.. _`memory_contains`:

memory_contains
===============

.. c:function:: bool memory_contains (void *begin, void *end, void *virt, size_t size)

    checks if an object is contained within a memory region

    :param void \*begin:
        virtual address of the beginning of the memory region

    :param void \*end:
        virtual address of the end of the memory region

    :param void \*virt:
        virtual address of the memory object

    :param size_t size:
        size of the memory object



.. _`memory_contains.returns`:

Returns
-------

true if the object specified by ``virt`` and ``size`` is entirely
contained within the memory region defined by ``begin`` and ``end``\ , false
otherwise.



.. _`memory_intersects`:

memory_intersects
=================

.. c:function:: bool memory_intersects (void *begin, void *end, void *virt, size_t size)

    checks if the region occupied by an object intersects with another memory region

    :param void \*begin:
        virtual address of the beginning of the memory regien

    :param void \*end:
        virtual address of the end of the memory region

    :param void \*virt:
        virtual address of the memory object

    :param size_t size:
        size of the memory object



.. _`memory_intersects.returns`:

Returns
-------

true if an object's memory region, specified by ``virt`` and ``size``\ ,
intersects with the region specified by ``begin`` and ``end``\ , false otherwise.



.. _`init_section_contains`:

init_section_contains
=====================

.. c:function:: bool init_section_contains (void *virt, size_t size)

    checks if an object is contained within the init section

    :param void \*virt:
        virtual address of the memory object

    :param size_t size:
        size of the memory object



.. _`init_section_contains.returns`:

Returns
-------

true if the object specified by ``virt`` and ``size`` is entirely
contained within the init section, false otherwise.



.. _`init_section_intersects`:

init_section_intersects
=======================

.. c:function:: bool init_section_intersects (void *virt, size_t size)

    checks if the region occupied by an object intersects with the init section

    :param void \*virt:
        virtual address of the memory object

    :param size_t size:
        size of the memory object



.. _`init_section_intersects.returns`:

Returns
-------

true if an object's memory region, specified by ``virt`` and ``size``\ ,
intersects with the init section, false otherwise.

