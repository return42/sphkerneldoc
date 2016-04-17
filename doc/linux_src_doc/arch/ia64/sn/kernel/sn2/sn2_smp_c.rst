.. -*- coding: utf-8; mode: rst -*-

=========
sn2_smp.c
=========


.. _`sn_migrate`:

sn_migrate
==========

.. c:function:: void sn_migrate (struct task_struct *task)

    SN-specific task migration actions

    :param struct task_struct \*task:
        Task being migrated to new CPU



.. _`sn_migrate.description`:

Description
-----------

SN2 PIO writes from separate CPUs are not guaranteed to arrive in order.
Context switching user threads which have memory-mapped MMIO may cause
PIOs to issue from separate CPUs, thus the PIO writes must be drained
from the previous CPU's Shub before execution resumes on the new CPU.



.. _`sn2_global_tlb_purge`:

sn2_global_tlb_purge
====================

.. c:function:: void sn2_global_tlb_purge (struct mm_struct *mm, unsigned long start, unsigned long end, unsigned long nbits)

    globally purge translation cache of virtual address range

    :param struct mm_struct \*mm:
        mm_struct containing virtual address range

    :param unsigned long start:
        start of virtual address range

    :param unsigned long end:
        end of virtual address range

    :param unsigned long nbits:
        specifies number of bytes to purge per instruction (num = 1<<(nbits & 0xfc))



.. _`sn2_global_tlb_purge.description`:

Description
-----------

Purges the translation caches of all processors of the given virtual address
range.



.. _`sn2_global_tlb_purge.note`:

Note
----

- cpu_vm_mask is a bit mask that indicates which cpus have loaded the context.
- cpu_vm_mask is converted into a nodemask of the nodes containing the

  cpus in cpu_vm_mask.

- if only one bit is set in cpu_vm_mask & it is the current cpu & the

  process is purging its own virtual address range, then only the
  local TLB needs to be flushed. This flushing can be done using
  ptc.l. This is the common case & avoids the global spinlock.

- if multiple cpus have loaded the context, then flushing has to be

  done with ptc.g/MMRs under protection of the global ptc_lock.



.. _`sn_send_ipi_phys`:

sn_send_IPI_phys
================

.. c:function:: void sn_send_IPI_phys (int nasid, long physid, int vector, int delivery_mode)

    send an IPI to a Nasid and slice

    :param int nasid:
        nasid to receive the interrupt (may be outside partition)

    :param long physid:
        physical cpuid to receive the interrupt.

    :param int vector:
        command to send

    :param int delivery_mode:
        delivery mechanism



.. _`sn_send_ipi_phys.description`:

Description
-----------

Sends an IPI (interprocessor interrupt) to the processor specified by
``physid``

``delivery_mode`` can be one of the following

``IA64_IPI_DM_INT`` - pend an interrupt
``IA64_IPI_DM_PMI`` - pend a PMI
``IA64_IPI_DM_NMI`` - pend an NMI
``IA64_IPI_DM_INIT`` - pend an INIT interrupt



.. _`sn2_send_ipi`:

sn2_send_IPI
============

.. c:function:: void sn2_send_IPI (int cpuid, int vector, int delivery_mode, int redirect)

    send an IPI to a processor

    :param int cpuid:
        target of the IPI

    :param int vector:
        command to send

    :param int delivery_mode:
        delivery mechanism

    :param int redirect:
        redirect the IPI?



.. _`sn2_send_ipi.description`:

Description
-----------

Sends an IPI (InterProcessor Interrupt) to the processor specified by
``cpuid``\ .  ``vector`` specifies the command to send, while ``delivery_mode`` can 
be one of the following

``IA64_IPI_DM_INT`` - pend an interrupt
``IA64_IPI_DM_PMI`` - pend a PMI
``IA64_IPI_DM_NMI`` - pend an NMI
``IA64_IPI_DM_INIT`` - pend an INIT interrupt



.. _`sn_cpu_disable_allowed`:

sn_cpu_disable_allowed
======================

.. c:function:: bool sn_cpu_disable_allowed (int cpu)

    Determine if a CPU can be disabled. @cpu - CPU that is requested to be disabled.

    :param int cpu:

        *undescribed*



.. _`sn_cpu_disable_allowed.description`:

Description
-----------


CPU disable is only allowed on SHub2 systems running with a PROM
that supports CPU disable. It is not permitted to disable the boot processor.

