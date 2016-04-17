.. -*- coding: utf-8; mode: rst -*-

=========
smpboot.c
=========


.. _`topology_phys_to_logical_pkg`:

topology_phys_to_logical_pkg
============================

.. c:function:: int topology_phys_to_logical_pkg (unsigned int phys_pkg)

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

.. c:function:: void arch_disable_smp_support ( void)

    disables SMP support for x86 at runtime

    :param void:
        no arguments

