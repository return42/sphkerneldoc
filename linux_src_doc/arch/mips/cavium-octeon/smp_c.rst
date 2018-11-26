.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/smp.c

.. _`octeon_send_ipi_single`:

octeon_send_ipi_single
======================

.. c:function:: void octeon_send_ipi_single(int cpu, unsigned int action)

    cpu.  When the function has finished, increment the finished field of call_data.

    :param cpu:
        *undescribed*
    :type cpu: int

    :param action:
        *undescribed*
    :type action: unsigned int

.. _`octeon_smp_hotplug_setup`:

octeon_smp_hotplug_setup
========================

.. c:function:: void octeon_smp_hotplug_setup( void)

    :param void:
        no arguments
    :type void: 

.. _`octeon_boot_secondary`:

octeon_boot_secondary
=====================

.. c:function:: int octeon_boot_secondary(int cpu, struct task_struct *idle)

    :param cpu:
        *undescribed*
    :type cpu: int

    :param idle:
        *undescribed*
    :type idle: struct task_struct \*

.. _`octeon_init_secondary`:

octeon_init_secondary
=====================

.. c:function:: void octeon_init_secondary( void)

    board code to clean up state, if needed

    :param void:
        no arguments
    :type void: 

.. _`octeon_prepare_cpus`:

octeon_prepare_cpus
===================

.. c:function:: void octeon_prepare_cpus(unsigned int max_cpus)

    :param max_cpus:
        *undescribed*
    :type max_cpus: unsigned int

.. _`octeon_smp_finish`:

octeon_smp_finish
=================

.. c:function:: void octeon_smp_finish( void)

    the CPU is "online".

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

