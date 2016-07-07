.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mips-cm.h

.. _`__mips_cm_phys_base`:

__mips_cm_phys_base
===================

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

.. _`mips_cm_numcores`:

mips_cm_numcores
================

.. c:function:: unsigned mips_cm_numcores( void)

    return the number of cores present in the system

    :param  void:
        no arguments

.. _`mips_cm_numcores.description`:

Description
-----------

Returns the value of the PCORES field of the GCR_CONFIG register plus 1, or
zero if no Coherence Manager is present.

.. _`mips_cm_numiocu`:

mips_cm_numiocu
===============

.. c:function:: unsigned mips_cm_numiocu( void)

    return the number of IOCUs present in the system

    :param  void:
        no arguments

.. _`mips_cm_numiocu.description`:

Description
-----------

Returns the value of the NUMIOCU field of the GCR_CONFIG register, or zero
if no Coherence Manager is present.

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

.. c:function:: void mips_cm_lock_other(unsigned int core, unsigned int vp)

    lock access to another core

    :param unsigned int core:
        the other core to be accessed

    :param unsigned int vp:
        the VP within the other core to be accessed

.. _`mips_cm_lock_other.description`:

Description
-----------

Call before operating upon a core via the 'other' register region in
order to prevent the region being moved during access. Must be followed
by a call to mips_cm_unlock_other.

.. _`mips_cm_unlock_other`:

mips_cm_unlock_other
====================

.. c:function:: void mips_cm_unlock_other( void)

    unlock access to another core

    :param  void:
        no arguments

.. _`mips_cm_unlock_other.description`:

Description
-----------

Call after operating upon another core via the 'other' register region.
Must be called after mips_cm_lock_other.

.. This file was automatic generated / don't edit.

