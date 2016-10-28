.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/mtrr/main.c

.. _`mtrr_rendezvous_handler`:

mtrr_rendezvous_handler
=======================

.. c:function:: int mtrr_rendezvous_handler(void *info)

    Work done in the synchronization handler. Executed by all the CPUs.

    :param void \*info:
        pointer to mtrr configuration data

.. _`mtrr_rendezvous_handler.description`:

Description
-----------

Returns nothing.

.. _`set_mtrr`:

set_mtrr
========

.. c:function:: void set_mtrr(unsigned int reg, unsigned long base, unsigned long size, mtrr_type type)

    update mtrrs on all processors

    :param unsigned int reg:
        mtrr in question

    :param unsigned long base:
        mtrr base

    :param unsigned long size:
        mtrr size

    :param mtrr_type type:
        mtrr type

.. _`set_mtrr.description`:

Description
-----------

This is kinda tricky, but fortunately, Intel spelled it out for us cleanly:

1. Queue work to do the following on all processors:
2. Disable Interrupts
3. Wait for all procs to do so
4. Enter no-fill cache mode
5. Flush caches
6. Clear PGE bit
7. Flush all TLBs
8. Disable all range registers
9. Update the MTRRs
10. Enable all range registers
11. Flush all TLBs and caches again
12. Enter normal cache mode and reenable caching
13. Set PGE
14. Wait for buddies to catch up
15. Enable interrupts.

What does that mean for us? Well, \ :c:func:`stop_machine`\  will ensure that
the rendezvous handler is started on each CPU. And in lockstep they
do the state transition of disabling interrupts, updating MTRR's
(the CPU vendors may each do it differently, so we call mtrr_if->\ :c:func:`set`\ 
callback and let them take care of it.) and enabling interrupts.

Note that the mechanism is the same for UP systems, too; all the SMP stuff
becomes nops.

.. _`mtrr_add_page`:

mtrr_add_page
=============

.. c:function:: int mtrr_add_page(unsigned long base, unsigned long size, unsigned int type, bool increment)

    Add a memory type region

    :param unsigned long base:
        Physical base address of region in pages (in units of 4 kB!)

    :param unsigned long size:
        Physical size of region in pages (4 kB)

    :param unsigned int type:
        Type of MTRR desired

    :param bool increment:
        If this is true do usage counting on the region

.. _`mtrr_add_page.description`:

Description
-----------

Memory type region registers control the caching on newer Intel and
non Intel processors. This function allows drivers to request an
MTRR is added. The details and hardware specifics of each processor's
implementation are hidden from the caller, but nevertheless the
caller should expect to need to provide a power of two size on an
equivalent power of two boundary.

If the region cannot be added either because all regions are in use
or the CPU cannot support it a negative value is returned. On success
the register number for this entry is returned, but should be treated
as a cookie only.

On a multiprocessor machine the changes are made to all processors.
This is required on x86 by the Intel processors.

The available types are

\ ``MTRR_TYPE_UNCACHABLE``\  - No caching

\ ``MTRR_TYPE_WRBACK``\  - Write data back in bursts whenever

\ ``MTRR_TYPE_WRCOMB``\  - Write data back soon but allow bursts

\ ``MTRR_TYPE_WRTHROUGH``\  - Cache reads but not writes

.. _`mtrr_add_page.bugs`:

BUGS
----

Needs a quiet flag for the cases where drivers do not mind
failures and do not wish system log messages to be sent.

.. _`mtrr_add`:

mtrr_add
========

.. c:function:: int mtrr_add(unsigned long base, unsigned long size, unsigned int type, bool increment)

    Add a memory type region

    :param unsigned long base:
        Physical base address of region

    :param unsigned long size:
        Physical size of region

    :param unsigned int type:
        Type of MTRR desired

    :param bool increment:
        If this is true do usage counting on the region

.. _`mtrr_add.description`:

Description
-----------

Memory type region registers control the caching on newer Intel and
non Intel processors. This function allows drivers to request an
MTRR is added. The details and hardware specifics of each processor's
implementation are hidden from the caller, but nevertheless the
caller should expect to need to provide a power of two size on an
equivalent power of two boundary.

If the region cannot be added either because all regions are in use
or the CPU cannot support it a negative value is returned. On success
the register number for this entry is returned, but should be treated
as a cookie only.

On a multiprocessor machine the changes are made to all processors.
This is required on x86 by the Intel processors.

The available types are

\ ``MTRR_TYPE_UNCACHABLE``\  - No caching

\ ``MTRR_TYPE_WRBACK``\  - Write data back in bursts whenever

\ ``MTRR_TYPE_WRCOMB``\  - Write data back soon but allow bursts

\ ``MTRR_TYPE_WRTHROUGH``\  - Cache reads but not writes

.. _`mtrr_add.bugs`:

BUGS
----

Needs a quiet flag for the cases where drivers do not mind
failures and do not wish system log messages to be sent.

.. _`mtrr_del_page`:

mtrr_del_page
=============

.. c:function:: int mtrr_del_page(int reg, unsigned long base, unsigned long size)

    delete a memory type region

    :param int reg:
        Register returned by mtrr_add

    :param unsigned long base:
        Physical base address

    :param unsigned long size:
        Size of region

.. _`mtrr_del_page.description`:

Description
-----------

If register is supplied then base and size are ignored. This is
how drivers should call it.

Releases an MTRR region. If the usage count drops to zero the
register is freed and the region returns to default state.
On success the register is returned, on failure a negative error
code.

.. _`mtrr_del`:

mtrr_del
========

.. c:function:: int mtrr_del(int reg, unsigned long base, unsigned long size)

    delete a memory type region

    :param int reg:
        Register returned by mtrr_add

    :param unsigned long base:
        Physical base address

    :param unsigned long size:
        Size of region

.. _`mtrr_del.description`:

Description
-----------

If register is supplied then base and size are ignored. This is
how drivers should call it.

Releases an MTRR region. If the usage count drops to zero the
register is freed and the region returns to default state.
On success the register is returned, on failure a negative error
code.

.. _`arch_phys_wc_add`:

arch_phys_wc_add
================

.. c:function:: int arch_phys_wc_add(unsigned long base, unsigned long size)

    add a WC MTRR and handle errors if PAT is unavailable

    :param unsigned long base:
        Physical base address

    :param unsigned long size:
        Size of region

.. _`arch_phys_wc_add.description`:

Description
-----------

If PAT is available, this does nothing.  If PAT is unavailable, it
attempts to add a WC MTRR covering size bytes starting at base and
logs an error if this fails.

The called should provide a power of two size on an equivalent
power of two boundary.

Drivers must store the return value to pass to mtrr_del_wc_if_needed,
but drivers should not try to interpret that return value.

.. _`mtrr_bp_init`:

mtrr_bp_init
============

.. c:function:: void mtrr_bp_init( void)

    initialize mtrrs on the boot CPU

    :param  void:
        no arguments

.. _`mtrr_bp_init.description`:

Description
-----------

This needs to be called early; before any of the other CPUs are
initialized (i.e. before \ :c:func:`smp_init`\ ).

.. _`mtrr_save_state`:

mtrr_save_state
===============

.. c:function:: void mtrr_save_state( void)

    range MTRR state of the first cpu in cpu_online_mask.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

