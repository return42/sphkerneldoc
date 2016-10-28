.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/fadump.c

.. _`fadump_calculate_reserve_size`:

fadump_calculate_reserve_size
=============================

.. c:function:: unsigned long fadump_calculate_reserve_size( void)

    reserve variable boot area 5% of System RAM

    :param  void:
        no arguments

.. _`fadump_calculate_reserve_size.description`:

Description
-----------

Function to find the largest memory size we need to reserve during early
boot process. This will be the size of the memory that is required for a
kernel to boot successfully.

This function has been taken from phyp-assisted dump feature implementation.

returns larger of 256MB or 5% rounded down to multiples of 256MB.

.. _`fadump_calculate_reserve_size.todo`:

TODO
----

Come up with better approach to find out more accurate memory size
that is required for a kernel to boot successfully.

.. This file was automatic generated / don't edit.

