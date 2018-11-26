.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/pm.c

.. _`mips_cpu_save`:

mips_cpu_save
=============

.. c:function:: int mips_cpu_save( void)

    Save general CPU state. Ensures that general CPU context is saved, notably FPU and DSP.

    :param void:
        no arguments
    :type void: 

.. _`mips_cpu_restore`:

mips_cpu_restore
================

.. c:function:: void mips_cpu_restore( void)

    Restore general CPU state. Restores important CPU context.

    :param void:
        no arguments
    :type void: 

.. _`mips_pm_notifier`:

mips_pm_notifier
================

.. c:function:: int mips_pm_notifier(struct notifier_block *self, unsigned long cmd, void *v)

    Notifier for preserving general CPU context.

    :param self:
        Notifier block.
    :type self: struct notifier_block \*

    :param cmd:
        CPU PM event.
    :type cmd: unsigned long

    :param v:
        Private data (unused).
    :type v: void \*

.. _`mips_pm_notifier.description`:

Description
-----------

This is called when a CPU power management event occurs, and is used to
ensure that important CPU context is preserved across a CPU power down.

.. This file was automatic generated / don't edit.

