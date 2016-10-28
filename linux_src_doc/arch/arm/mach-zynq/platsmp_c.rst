.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-zynq/platsmp.c

.. _`zynq_secondary_init`:

zynq_secondary_init
===================

.. c:function:: void zynq_secondary_init(unsigned int cpu)

    Initialize secondary CPU cores

    :param unsigned int cpu:
        CPU that is initialized

.. _`zynq_secondary_init.description`:

Description
-----------

This function is in the hotplug path. Don't move it into the
init section!!

.. _`zynq_cpu_die`:

zynq_cpu_die
============

.. c:function:: void zynq_cpu_die(unsigned int cpu)

    Let a CPU core die

    :param unsigned int cpu:
        Dying CPU

.. _`zynq_cpu_die.description`:

Description
-----------

Platform-specific code to shutdown a CPU.
Called with IRQs disabled on the dying CPU.

.. This file was automatic generated / don't edit.

