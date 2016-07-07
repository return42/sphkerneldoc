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
        struct {unnamed_struct};
        u8 page[PAGE_SIZE];
    }

.. _`mips_vdso_data.members`:

Members
-------

{unnamed_struct}
    anonymous


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

