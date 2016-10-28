.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/fsl_lbc.c

.. _`fsl_lbc_addr`:

fsl_lbc_addr
============

.. c:function:: u32 fsl_lbc_addr(phys_addr_t addr_base)

    convert the base address

    :param phys_addr_t addr_base:
        base address of the memory bank

.. _`fsl_lbc_addr.description`:

Description
-----------

This function converts a base address of lbc into the right format for the
BR register. If the SOC has eLBC then it returns 32bit physical address
else it convers a 34bit local bus physical address to correct format of
32bit address for BR register (Example: MPC8641).

.. _`fsl_lbc_find`:

fsl_lbc_find
============

.. c:function:: int fsl_lbc_find(phys_addr_t addr_base)

    find Localbus bank

    :param phys_addr_t addr_base:
        base address of the memory bank

.. _`fsl_lbc_find.description`:

Description
-----------

This function walks LBC banks comparing "Base address" field of the BR
registers with the supplied addr_base argument. When bases match this
function returns bank number (starting with 0), otherwise it returns
appropriate errno value.

.. _`fsl_upm_find`:

fsl_upm_find
============

.. c:function:: int fsl_upm_find(phys_addr_t addr_base, struct fsl_upm *upm)

    find pre-programmed UPM via base address

    :param phys_addr_t addr_base:
        base address of the memory bank controlled by the UPM

    :param struct fsl_upm \*upm:
        pointer to the allocated fsl_upm structure

.. _`fsl_upm_find.description`:

Description
-----------

This function fills fsl_upm structure so you can use it with the rest of
UPM API. On success this function returns 0, otherwise it returns
appropriate errno value.

.. _`fsl_upm_run_pattern`:

fsl_upm_run_pattern
===================

.. c:function:: int fsl_upm_run_pattern(struct fsl_upm *upm, void __iomem *io_base, u32 mar)

    actually run an UPM pattern

    :param struct fsl_upm \*upm:
        pointer to the fsl_upm structure obtained via fsl_upm_find

    :param void __iomem \*io_base:
        remapped pointer to where memory access should happen

    :param u32 mar:
        MAR register content during pattern execution

.. _`fsl_upm_run_pattern.description`:

Description
-----------

This function triggers dummy write to the memory specified by the io_base,
thus UPM pattern actually executed. Note that mar usage depends on the
pre-programmed AMX bits in the UPM RAM.

.. This file was automatic generated / don't edit.

