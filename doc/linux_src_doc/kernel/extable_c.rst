.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/extable.c

.. _`core_kernel_data`:

core_kernel_data
================

.. c:function:: int core_kernel_data(unsigned long addr)

    tell if addr points to kernel data

    :param unsigned long addr:
        address to test

.. _`core_kernel_data.description`:

Description
-----------

Returns true if \ ``addr``\  passed in is from the core kernel data
section.

.. _`core_kernel_data.note`:

Note
----

On some archs it may return true for core RODATA, and false
for others. But will always be true for core RW data.

.. This file was automatic generated / don't edit.

