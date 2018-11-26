.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/smp.c

.. _`smp_startup_cpu`:

smp_startup_cpu
===============

.. c:function:: int smp_startup_cpu(unsigned int lcpu)

    start the given cpu

    :param lcpu:
        *undescribed*
    :type lcpu: unsigned int

.. _`smp_startup_cpu.description`:

Description
-----------

At boot time, there is nothing to do for primary threads which were
started from Open Firmware.  For anything else, call RTAS with the
appropriate start location.

.. _`smp_startup_cpu.return`:

Return
------

0       - failure
1       - success

.. This file was automatic generated / don't edit.

