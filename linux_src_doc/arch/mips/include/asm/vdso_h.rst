.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/vdso.h

.. _`mips_vdso_image`:

struct mips_vdso_image
======================

.. c:type:: struct mips_vdso_image

    Details of a VDSO image.

.. _`mips_vdso_image.definition`:

Definition
----------

.. code-block:: c

    struct mips_vdso_image {
        void *data;
        unsigned long size;
        unsigned long off_sigreturn;
        unsigned long off_rt_sigreturn;
        struct vm_special_mapping mapping;
    }

.. _`mips_vdso_image.members`:

Members
-------

data
    Pointer to VDSO image data (page-aligned).

size
    Size of the VDSO image data (page-aligned).

off_sigreturn
    Offset of the \ :c:func:`sigreturn`\  trampoline.

off_rt_sigreturn
    Offset of the \ :c:func:`rt_sigreturn`\  trampoline.

mapping
    Special mapping structure.

.. _`mips_vdso_image.description`:

Description
-----------

This structure contains details of a VDSO image, including the image data
and offsets of certain symbols required by the kernel. It is generated as
part of the VDSO build process, aside from the mapping page array, which is
populated at runtime.

.. _`mips_vdso_data`:

union mips_vdso_data
====================

.. c:type:: struct mips_vdso_data

    Data provided by the kernel for the VDSO.

.. _`mips_vdso_data.definition`:

Definition
----------

.. code-block:: c

    union mips_vdso_data {
        struct {
            u64 xtime_sec;
            u64 xtime_nsec;
            u64 wall_to_mono_sec;
            u64 wall_to_mono_nsec;
            u32 seq_count;
            u32 cs_shift;
            u8 clock_mode;
            u32 cs_mult;
            u64 cs_cycle_last;
            u64 cs_mask;
            s32 tz_minuteswest;
            s32 tz_dsttime;
        } ;
        u8 page[PAGE_SIZE];
    }

.. _`mips_vdso_data.members`:

Members
-------

{unnamed_struct}
    anonymous

xtime_sec
    Current real time (seconds part).

xtime_nsec
    Current real time (nanoseconds part, shifted).

wall_to_mono_sec
    Wall-to-monotonic offset (seconds part).

wall_to_mono_nsec
    Wall-to-monotonic offset (nanoseconds part).

seq_count
    Counter to synchronise updates (odd = updating).

cs_shift
    Clocksource shift value.

clock_mode
    Clocksource to use for time functions.

cs_mult
    Clocksource multiplier value.

cs_cycle_last
    Clock cycle value at last update.

cs_mask
    Clocksource mask value.

tz_minuteswest
    Minutes west of Greenwich (from timezone).

tz_dsttime
    Type of DST correction (from timezone).

page
    *undescribed*

.. _`mips_vdso_data.description`:

Description
-----------

This structure contains data needed by functions within the VDSO. It is
populated by the kernel and mapped read-only into user memory. The time
fields are mirrors of internal data from the timekeeping infrastructure.

.. _`mips_vdso_data.note`:

Note
----

Care should be taken when modifying as the layout must remain the same
for both 64- and 32-bit (for 32-bit userland on 64-bit kernel).

.. This file was automatic generated / don't edit.

