.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/kernel/numa.c

.. _`build_cpu_to_node_map`:

build_cpu_to_node_map
=====================

.. c:function:: void build_cpu_to_node_map( void)

    setup cpu to node and node to cpumask arrays

    :param void:
        no arguments
    :type void: 

.. _`build_cpu_to_node_map.description`:

Description
-----------

Build cpu to node mapping and initialize the per node cpu masks using
info from the node_cpuid array handed to us by ACPI.

.. This file was automatic generated / don't edit.

