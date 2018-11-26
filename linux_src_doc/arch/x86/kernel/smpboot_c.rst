.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/smpboot.c

.. _`topology_is_primary_thread`:

topology_is_primary_thread
==========================

.. c:function:: bool topology_is_primary_thread(unsigned int cpu)

    Check whether CPU is the primary SMT thread

    :param cpu:
        CPU to check
    :type cpu: unsigned int

.. _`topology_smt_supported`:

topology_smt_supported
======================

.. c:function:: bool topology_smt_supported( void)

    Check whether SMT is supported by the CPUs

    :param void:
        no arguments
    :type void: 

.. _`topology_phys_to_logical_pkg`:

topology_phys_to_logical_pkg
============================

.. c:function:: int topology_phys_to_logical_pkg(unsigned int phys_pkg)

    Map a physical package id to a logical

    :param phys_pkg:
        *undescribed*
    :type phys_pkg: unsigned int

.. _`topology_phys_to_logical_pkg.description`:

Description
-----------

Returns logical package id or -1 if not found

.. _`topology_update_package_map`:

topology_update_package_map
===========================

.. c:function:: int topology_update_package_map(unsigned int pkg, unsigned int cpu)

    Update the physical to logical package map

    :param pkg:
        The physical package id as retrieved via CPUID
    :type pkg: unsigned int

    :param cpu:
        The cpu for which this is updated
    :type cpu: unsigned int

.. _`arch_disable_smp_support`:

arch_disable_smp_support
========================

.. c:function:: void arch_disable_smp_support( void)

    disables SMP support for x86 at runtime

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

