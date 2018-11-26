.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/mtrr/generic.c

.. _`mtrr_type_lookup_fixed`:

mtrr_type_lookup_fixed
======================

.. c:function:: u8 mtrr_type_lookup_fixed(u64 start, u64 end)

    look up memory type in MTRR fixed entries

    :param start:
        *undescribed*
    :type start: u64

    :param end:
        *undescribed*
    :type end: u64

.. _`mtrr_type_lookup_fixed.description`:

Description
-----------

Return the MTRR fixed memory type of 'start'.

.. _`mtrr_type_lookup_fixed.mtrr-fixed-entries-are-divided-into-the-following-ways`:

MTRR fixed entries are divided into the following ways
------------------------------------------------------

0x00000 - 0x7FFFF : This range is divided into eight 64KB sub-ranges
0x80000 - 0xBFFFF : This range is divided into sixteen 16KB sub-ranges
0xC0000 - 0xFFFFF : This range is divided into sixty-four 4KB sub-ranges

.. _`mtrr_type_lookup_fixed.return-values`:

Return Values
-------------

MTRR_TYPE_(type)  - Matched memory type
MTRR_TYPE_INVALID - Unmatched

.. _`mtrr_type_lookup_variable`:

mtrr_type_lookup_variable
=========================

.. c:function:: u8 mtrr_type_lookup_variable(u64 start, u64 end, u64 *partial_end, int *repeat, u8 *uniform)

    look up memory type in MTRR variable entries

    :param start:
        *undescribed*
    :type start: u64

    :param end:
        *undescribed*
    :type end: u64

    :param partial_end:
        *undescribed*
    :type partial_end: u64 \*

    :param repeat:
        *undescribed*
    :type repeat: int \*

    :param uniform:
        *undescribed*
    :type uniform: u8 \*

.. _`mtrr_type_lookup_variable.return-value`:

Return Value
------------

MTRR_TYPE_(type) - Matched memory type or default memory type (unmatched)

.. _`mtrr_type_lookup_variable.output-arguments`:

Output Arguments
----------------

repeat - Set to 1 when [start:end] spanned across MTRR range and type
returned corresponds only to [start:\*partial_end].  Caller has
to lookup again for [\*partial_end:end].

uniform - Set to 1 when an MTRR covers the region uniformly, i.e. the
region is fully covered by a single MTRR entry or the default
type.

.. _`mtrr_type_lookup`:

mtrr_type_lookup
================

.. c:function:: u8 mtrr_type_lookup(u64 start, u64 end, u8 *uniform)

    look up memory type in MTRR

    :param start:
        *undescribed*
    :type start: u64

    :param end:
        *undescribed*
    :type end: u64

    :param uniform:
        *undescribed*
    :type uniform: u8 \*

.. _`mtrr_type_lookup.return-values`:

Return Values
-------------

MTRR_TYPE_(type)  - The effective MTRR type for the region
MTRR_TYPE_INVALID - MTRR is disabled

.. _`mtrr_type_lookup.output-argument`:

Output Argument
---------------

uniform - Set to 1 when an MTRR covers the region uniformly, i.e. the
region is fully covered by a single MTRR entry or the default
type.

.. _`set_fixed_range`:

set_fixed_range
===============

.. c:function:: void set_fixed_range(int msr, bool *changed, unsigned int *msrwords)

    checks & updates a fixed-range MTRR if it differs from the value it should have

    :param msr:
        MSR address of the MTTR which should be checked and updated
    :type msr: int

    :param changed:
        pointer which indicates whether the MTRR needed to be changed
    :type changed: bool \*

    :param msrwords:
        pointer to the MSR values which the MSR should have
    :type msrwords: unsigned int \*

.. _`generic_get_free_region`:

generic_get_free_region
=======================

.. c:function:: int generic_get_free_region(unsigned long base, unsigned long size, int replace_reg)

    Get a free MTRR.

    :param base:
        The starting (base) address of the region.
    :type base: unsigned long

    :param size:
        The size (in bytes) of the region.
    :type size: unsigned long

    :param replace_reg:
        mtrr index to be replaced; set to invalid value if none.
    :type replace_reg: int

.. _`generic_get_free_region.return`:

Return
------

The index of the region on success, else negative on error.

.. _`set_fixed_ranges`:

set_fixed_ranges
================

.. c:function:: int set_fixed_ranges(mtrr_type *frs)

    checks & updates the fixed-range MTRRs if they differ from the saved set

    :param frs:
        pointer to fixed-range MTRR values, saved by \ :c:func:`get_fixed_ranges`\ 
    :type frs: mtrr_type \*

.. _`set_mtrr_state`:

set_mtrr_state
==============

.. c:function:: unsigned long set_mtrr_state( void)

    Set the MTRR state for this CPU.

    :param void:
        no arguments
    :type void: 

.. _`set_mtrr_state.note`:

NOTE
----

The CPU must already be in a safe state for MTRR changes.

.. _`set_mtrr_state.return`:

Return
------

0 if no changes made, else a mask indicating what was changed.

.. _`generic_set_mtrr`:

generic_set_mtrr
================

.. c:function:: void generic_set_mtrr(unsigned int reg, unsigned long base, unsigned long size, mtrr_type type)

    set variable MTRR register on the local CPU.

    :param reg:
        The register to set.
    :type reg: unsigned int

    :param base:
        The base address of the region.
    :type base: unsigned long

    :param size:
        The size of the region. If this is 0 the region is disabled.
    :type size: unsigned long

    :param type:
        The type of the region.
    :type type: mtrr_type

.. _`generic_set_mtrr.description`:

Description
-----------

Returns nothing.

.. This file was automatic generated / don't edit.

