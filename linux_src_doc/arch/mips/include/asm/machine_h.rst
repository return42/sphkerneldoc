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

.. This file was automatic generated / don't edit.

