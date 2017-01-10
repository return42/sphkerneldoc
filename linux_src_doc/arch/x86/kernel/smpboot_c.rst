.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/smpboot.c

.. _`topology_update_package_map`:

topology_update_package_map
===========================

.. c:function:: int topology_update_package_map(unsigned int pkg, unsigned int cpu)

    Update the physical to logical package map

    :param unsigned int pkg:
        The physical package id as retrieved via CPUID

    :param unsigned int cpu:
        The cpu for which this is updated

.. _`topology_phys_to_logical_pkg`:

topology_phys_to_logical_pkg
============================

.. c:function:: int topology_phys_to_logical_pkg(unsigned int phys_pkg)

    Map a physical package id to a logical

    :param unsigned int phys_pkg:
        *undescribed*

.. _`topology_phys_to_logical_pkg.description`:

Description
-----------

Returns logical package id or -1 if not found

.. _`arch_disable_smp_support`:

arch_disable_smp_support
========================

.. c:function:: void arch_disable_smp_support( void)

    disables SMP support for x86 at runtime

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

