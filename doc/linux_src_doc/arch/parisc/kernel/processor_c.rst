.. -*- coding: utf-8; mode: rst -*-

===========
processor.c
===========


.. _`init_percpu_prof`:

init_percpu_prof
================

.. c:function:: void init_percpu_prof (unsigned long cpunum)

    enable/setup per cpu profiling hooks.

    :param unsigned long cpunum:
        The processor instance.



.. _`init_percpu_prof.fixme`:

FIXME
-----

doesn't do much yet...



.. _`processor_probe`:

processor_probe
===============

.. c:function:: int processor_probe (struct parisc_device *dev)

    Determine if processor driver should claim this device.

    :param struct parisc_device \*dev:
        The device which has been found.



.. _`processor_probe.description`:

Description
-----------

Determine if processor driver should claim this chip (return 0) or not 
(return 1).  If so, initialize the chip and tell other partners in crime 
they have work to do.



.. _`collect_boot_cpu_data`:

collect_boot_cpu_data
=====================

.. c:function:: void collect_boot_cpu_data ( void)

    Fill the boot_cpu_data structure.

    :param void:
        no arguments



.. _`collect_boot_cpu_data.description`:

Description
-----------


This function collects and stores the generic processor information
in the boot_cpu_data structure.



.. _`init_per_cpu`:

init_per_cpu
============

.. c:function:: int init_per_cpu (int cpunum)

    Handle individual processor initializations.

    :param int cpunum:
        logical processor number.



.. _`init_per_cpu.description`:

Description
-----------

This function handles initialization for \*every\* CPU



.. _`init_per_cpu.in-the-system`:

in the system
-------------


o Set "default" CPU width for trap handlers

o Enable FP coprocessor



.. _`init_per_cpu.revisit`:

REVISIT
-------

this could be done in the "code 22" trap handler.
(frowands idea - that way we know which processes need FP
registers saved on the interrupt stack.)



.. _`init_per_cpu.news-flash`:

NEWS FLASH
----------

wide kernels need FP coprocessor enabled to handle
formatted printing of ``lx`` for example (double divides I think)

o Enable CPU profiling hooks.



.. _`processor_init`:

processor_init
==============

.. c:function:: void processor_init ( void)

    Processor initialization procedure.

    :param void:
        no arguments



.. _`processor_init.description`:

Description
-----------


Register this driver.

