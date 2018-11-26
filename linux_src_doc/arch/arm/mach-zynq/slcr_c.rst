.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-zynq/slcr.c

.. _`zynq_slcr_write`:

zynq_slcr_write
===============

.. c:function:: int zynq_slcr_write(u32 val, u32 offset)

    Write to a register in SLCR block

    :param val:
        Value to write to the register
    :type val: u32

    :param offset:
        Register offset in SLCR block
    :type offset: u32

.. _`zynq_slcr_write.return`:

Return
------

a negative value on error, 0 on success

.. _`zynq_slcr_read`:

zynq_slcr_read
==============

.. c:function:: int zynq_slcr_read(u32 *val, u32 offset)

    Read a register in SLCR block

    :param val:
        Pointer to value to be read from SLCR
    :type val: u32 \*

    :param offset:
        Register offset in SLCR block
    :type offset: u32

.. _`zynq_slcr_read.return`:

Return
------

a negative value on error, 0 on success

.. _`zynq_slcr_unlock`:

zynq_slcr_unlock
================

.. c:function:: int zynq_slcr_unlock( void)

    Unlock SLCR registers

    :param void:
        no arguments
    :type void: 

.. _`zynq_slcr_unlock.return`:

Return
------

a negative value on error, 0 on success

.. _`zynq_slcr_get_device_id`:

zynq_slcr_get_device_id
=======================

.. c:function:: u32 zynq_slcr_get_device_id( void)

    Read device code id

    :param void:
        no arguments
    :type void: 

.. _`zynq_slcr_get_device_id.return`:

Return
------

Device code id

.. _`zynq_slcr_system_restart`:

zynq_slcr_system_restart
========================

.. c:function:: int zynq_slcr_system_restart(struct notifier_block *nb, unsigned long action, void *data)

    Restart the entire system.

    :param nb:
        Pointer to restart notifier block (unused)
    :type nb: struct notifier_block \*

    :param action:
        Reboot mode (unused)
    :type action: unsigned long

    :param data:
        Restart handler private data (unused)
    :type data: void \*

.. _`zynq_slcr_system_restart.return`:

Return
------

0 always

.. _`zynq_slcr_cpu_start`:

zynq_slcr_cpu_start
===================

.. c:function:: void zynq_slcr_cpu_start(int cpu)

    Start cpu

    :param cpu:
        cpu number
    :type cpu: int

.. _`zynq_slcr_cpu_stop`:

zynq_slcr_cpu_stop
==================

.. c:function:: void zynq_slcr_cpu_stop(int cpu)

    Stop cpu

    :param cpu:
        cpu number
    :type cpu: int

.. _`zynq_slcr_cpu_state_read`:

zynq_slcr_cpu_state_read
========================

.. c:function:: bool zynq_slcr_cpu_state_read(int cpu)

    Read/write cpu state

    :param cpu:
        cpu number
    :type cpu: int

.. _`zynq_slcr_cpu_state_read.description`:

Description
-----------

SLCR_REBOOT_STATUS save upper 2 bits (31/30 cpu states for cpu0 and cpu1)
0 means cpu is running, 1 cpu is going to die.

.. _`zynq_slcr_cpu_state_read.return`:

Return
------

true if cpu is running, false if cpu is going to die

.. _`zynq_slcr_cpu_state_write`:

zynq_slcr_cpu_state_write
=========================

.. c:function:: void zynq_slcr_cpu_state_write(int cpu, bool die)

    Read/write cpu state

    :param cpu:
        cpu number
    :type cpu: int

    :param die:
        cpu state - true if cpu is going to die
    :type die: bool

.. _`zynq_slcr_cpu_state_write.description`:

Description
-----------

SLCR_REBOOT_STATUS save upper 2 bits (31/30 cpu states for cpu0 and cpu1)
0 means cpu is running, 1 cpu is going to die.

.. _`zynq_early_slcr_init`:

zynq_early_slcr_init
====================

.. c:function:: int zynq_early_slcr_init( void)

    Early slcr init function

    :param void:
        no arguments
    :type void: 

.. _`zynq_early_slcr_init.return`:

Return
------

0 on success, negative errno otherwise.

Called very early during boot from platform code to unlock SLCR.

.. This file was automatic generated / don't edit.

