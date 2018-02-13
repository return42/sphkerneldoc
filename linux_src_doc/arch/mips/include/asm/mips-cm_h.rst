.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mips-cm.h

.. _`__mips_cm_phys_base`:

\__mips_cm_phys_base
====================

.. c:function:: phys_addr_t __mips_cm_phys_base( void)

    retrieve the physical base address of the CM

    :param  void:
        no arguments

.. _`__mips_cm_phys_base.description`:

Description
-----------

This function returns the physical base address of the Coherence Manager
global control block, or 0 if no Coherence Manager is present. It provides
a default implementation which reads the CMGCRBase register where available,
and may be overridden by platforms which determine this address in a
different way by defining a function with the same prototype except for the
name mips_cm_phys_base (without underscores).

.. _`mips_cm_error_report`:

mips_cm_error_report
====================

.. c:function:: void mips_cm_error_report( void)

    Report CM cache errors

    :param  void:
        no arguments

.. _`mips_cm_probe`:

mips_cm_probe
=============

.. c:function:: int mips_cm_probe( void)

    probe for a Coherence Manager

    :param  void:
        no arguments

.. _`mips_cm_probe.description`:

Description
-----------

Attempt to detect the presence of a Coherence Manager. Returns 0 if a CM
is successfully detected, else -errno.

.. _`mips_cm_present`:

mips_cm_present
===============

.. c:function:: bool mips_cm_present( void)

    determine whether a Coherence Manager is present

    :param  void:
        no arguments

.. _`mips_cm_present.description`:

Description
-----------

Returns true if a CM is present in the system, else false.

.. _`mips_cm_has_l2sync`:

mips_cm_has_l2sync
==================

.. c:function:: bool mips_cm_has_l2sync( void)

    determine whether an L2-only sync region is present

    :param  void:
        no arguments

.. _`mips_cm_has_l2sync.description`:

Description
-----------

Returns true if the system implements an L2-only sync region, else false.

.. _`mips_cm_l2sync`:

mips_cm_l2sync
==============

.. c:function:: int mips_cm_l2sync( void)

    perform an L2-only sync operation

    :param  void:
        no arguments

.. _`mips_cm_l2sync.description`:

Description
-----------

If an L2-only sync region is present in the system then this function
performs and L2-only sync and returns zero. Otherwise it returns -ENODEV.

.. _`mips_cm_revision`:

mips_cm_revision
================

.. c:function:: int mips_cm_revision( void)

    return CM revision

    :param  void:
        no arguments

.. _`mips_cm_revision.return`:

Return
------

The revision of the CM, from GCR_REV, or 0 if no CM is present. The
return value should be checked against the CM_REV\_\* macros.

.. _`mips_cm_max_vp_width`:

mips_cm_max_vp_width
====================

.. c:function:: unsigned int mips_cm_max_vp_width( void)

    return the width in bits of VP indices

    :param  void:
        no arguments

.. _`mips_cm_max_vp_width.return`:

Return
------

the width, in bits, of VP indices in fields that combine core & VP
indices.

.. _`mips_cm_vp_id`:

mips_cm_vp_id
=============

.. c:function:: unsigned int mips_cm_vp_id(unsigned int cpu)

    calculate the hardware VP ID for a CPU

    :param unsigned int cpu:
        the CPU whose VP ID to calculate

.. _`mips_cm_vp_id.description`:

Description
-----------

Hardware such as the GIC uses identifiers for VPs which may not match the
CPU numbers used by Linux. This function calculates the hardware VP
identifier corresponding to a given CPU.

.. _`mips_cm_vp_id.return`:

Return
------

the VP ID for the CPU.

.. _`mips_cm_lock_other`:

mips_cm_lock_other
==================

.. c:function:: void mips_cm_lock_other(unsigned int cluster, unsigned int core, unsigned int vp, unsigned int block)

    lock access to redirect/other region

    :param unsigned int cluster:
        the other cluster to be accessed

    :param unsigned int core:
        the other core to be accessed

    :param unsigned int vp:
        the VP within the other core to be accessed

    :param unsigned int block:
        the register block to be accessed

.. _`mips_cm_lock_other.description`:

Description
-----------

Configure the redirect/other region for the local core/VP (depending upon
the CM revision) to target the specified \ ``cluster``\ , \ ``core``\ , \ ``vp``\  & register
\ ``block``\ . Must be called before using the redirect/other region, and followed
by a call to \ :c:func:`mips_cm_unlock_other`\  when access to the redirect/other region
is complete.

This function acquires a spinlock such that code between it &
\ :c:func:`mips_cm_unlock_other`\  calls cannot be pre-empted by anything which may
reconfigure the redirect/other region, and cannot be interfered with by
another VP in the core. As such calls to this function should not be nested.

.. _`mips_cm_unlock_other`:

mips_cm_unlock_other
====================

.. c:function:: void mips_cm_unlock_other( void)

    unlock access to redirect/other region

    :param  void:
        no arguments

.. _`mips_cm_unlock_other.description`:

Description
-----------

Must be called after \ :c:func:`mips_cm_lock_other`\  once all required access to the
redirect/other region has been completed.

.. _`mips_cm_lock_other_cpu`:

mips_cm_lock_other_cpu
======================

.. c:function:: void mips_cm_lock_other_cpu(unsigned int cpu, unsigned int block)

    lock access to redirect/other region

    :param unsigned int cpu:
        the other CPU whose register we want to access

    :param unsigned int block:
        *undescribed*

.. _`mips_cm_lock_other_cpu.description`:

Description
-----------

Configure the redirect/other region for the local core/VP (depending upon
the CM revision) to target the specified \ ``cpu``\  & register \ ``block``\ . This is
equivalent to calling \ :c:func:`mips_cm_lock_other`\  but accepts a Linux CPU number
for convenience.

.. This file was automatic generated / don't edit.

