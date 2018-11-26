.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mips-cpc.h

.. _`mips_cpc_default_phys_base`:

mips_cpc_default_phys_base
==========================

.. c:function:: phys_addr_t mips_cpc_default_phys_base( void)

    retrieve the default physical base address of the CPC

    :param void:
        no arguments
    :type void: 

.. _`mips_cpc_default_phys_base.description`:

Description
-----------

Returns the default physical base address of the Cluster Power Controller
memory mapped registers. This is platform dependant & must therefore be
implemented per-platform.

.. _`mips_cpc_probe`:

mips_cpc_probe
==============

.. c:function:: int mips_cpc_probe( void)

    probe for a Cluster Power Controller

    :param void:
        no arguments
    :type void: 

.. _`mips_cpc_probe.description`:

Description
-----------

Attempt to detect the presence of a Cluster Power Controller. Returns 0 if
a CPC is successfully detected, else -errno.

.. _`mips_cpc_present`:

mips_cpc_present
================

.. c:function:: bool mips_cpc_present( void)

    determine whether a Cluster Power Controller is present

    :param void:
        no arguments
    :type void: 

.. _`mips_cpc_present.description`:

Description
-----------

Returns true if a CPC is present in the system, else false.

.. _`mips_cpc_lock_other`:

mips_cpc_lock_other
===================

.. c:function:: void mips_cpc_lock_other(unsigned int core)

    lock access to another core

    :param core:
        *undescribed*
    :type core: unsigned int

.. _`mips_cpc_lock_other.core`:

core
----

the other core to be accessed

Call before operating upon a core via the 'other' register region in
order to prevent the region being moved during access. Must be called
within the bounds of a mips_cm_{lock,unlock}_other pair, and followed
by a call to mips_cpc_unlock_other.

.. _`mips_cpc_unlock_other`:

mips_cpc_unlock_other
=====================

.. c:function:: void mips_cpc_unlock_other( void)

    unlock access to another core

    :param void:
        no arguments
    :type void: 

.. _`mips_cpc_unlock_other.description`:

Description
-----------

Call after operating upon another core via the 'other' register region.
Must be called after mips_cpc_lock_other.

.. This file was automatic generated / don't edit.

