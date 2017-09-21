.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/machine.h

.. _`mips_machine_is_compatible`:

mips_machine_is_compatible
==========================

.. c:function:: const struct of_device_id *mips_machine_is_compatible(const struct mips_machine *mach, const void *fdt)

    check if a machine is compatible with an FDT

    :param const struct mips_machine \*mach:
        the machine struct to check

    :param const void \*fdt:
        the FDT to check for compatibility with

.. _`mips_machine_is_compatible.description`:

Description
-----------

Check whether the given machine \ ``mach``\  is compatible with the given flattened
device tree \ ``fdt``\ , based upon the compatibility property of the root node.

.. _`mips_machine_is_compatible.return`:

Return
------

the device id matched if any, else NULL

.. _`mips_fdt_fixup`:

struct mips_fdt_fixup
=====================

.. c:type:: struct mips_fdt_fixup

    Describe a fixup to apply to an FDT

.. _`mips_fdt_fixup.definition`:

Definition
----------

.. code-block:: c

    struct mips_fdt_fixup {
        int (*apply)(void *fdt);
        const char *description;
    }

.. _`mips_fdt_fixup.members`:

Members
-------

apply
    applies the fixup to \ ``fdt``\ , returns zero on success else -errno

description
    a short description of the fixup

.. _`mips_fdt_fixup.description`:

Description
-----------

Describes a fixup applied to an FDT blob by the \ ``apply``\  function. The
\ ``description``\  field provides a short description of the fixup intended for
use in error messages if the \ ``apply``\  function returns non-zero.

.. _`apply_mips_fdt_fixups`:

apply_mips_fdt_fixups
=====================

.. c:function:: int apply_mips_fdt_fixups(void *fdt_out, size_t fdt_out_size, const void *fdt_in, const struct mips_fdt_fixup *fixups)

    apply fixups to an FDT blob

    :param void \*fdt_out:
        buffer in which to place the fixed-up FDT

    :param size_t fdt_out_size:
        the size of the \ ``fdt_out``\  buffer

    :param const void \*fdt_in:
        the FDT blob

    :param const struct mips_fdt_fixup \*fixups:
        pointer to an array of fixups to be applied

.. _`apply_mips_fdt_fixups.description`:

Description
-----------

Loop through the array of fixups pointed to by \ ``fixups``\ , calling the apply
function on each until either one returns an error or we reach the end of
the list as indicated by an entry with a NULL apply field.

.. _`apply_mips_fdt_fixups.return`:

Return
------

zero on success, else -errno

.. This file was automatic generated / don't edit.

