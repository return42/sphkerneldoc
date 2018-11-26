.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kernel/setup.c

.. _`smp_build_mpidr_hash`:

smp_build_mpidr_hash
====================

.. c:function:: void smp_build_mpidr_hash( void)

    Pre-compute shifts required at each affinity level in order to build a linear index from an MPIDR value. Resulting algorithm is a collision free hash carried out through shifting and ORing

    :param void:
        no arguments
    :type void: 

.. _`reserve_crashkernel`:

reserve_crashkernel
===================

.. c:function:: void reserve_crashkernel( void)

    reserves memory are for crash kernel

    :param void:
        no arguments
    :type void: 

.. _`reserve_crashkernel.description`:

Description
-----------

This function reserves memory area given in "crashkernel=" kernel command
line parameter. The memory reserved is used by a dump capture kernel when
primary kernel is crashing.

.. This file was automatic generated / don't edit.

