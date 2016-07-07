.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-davinci/aemif.c

.. _`davinci_aemif_setup_timing`:

davinci_aemif_setup_timing
==========================

.. c:function:: int davinci_aemif_setup_timing(struct davinci_aemif_timing *t, void __iomem *base, unsigned cs, unsigned long clkrate)

    setup timing values for a given AEMIF interface

    :param struct davinci_aemif_timing \*t:
        timing values to be progammed

    :param void __iomem \*base:
        The virtual base address of the AEMIF interface

    :param unsigned cs:
        chip-select to program the timing values for

    :param unsigned long clkrate:
        the AEMIF clkrate

.. _`davinci_aemif_setup_timing.description`:

Description
-----------

This function programs the given timing values (in real clock) into the
AEMIF registers taking the AEMIF clock into account.

This function does not use any locking while programming the AEMIF
because it is expected that there is only one user of a given
chip-select.

Returns 0 on success, else negative errno.

.. _`davinci_aemif_setup`:

davinci_aemif_setup
===================

.. c:function:: int davinci_aemif_setup(struct platform_device *pdev)

    setup AEMIF interface by davinci_nand_pdata \ ``pdev``\  - link to platform device to setup settings for

    :param struct platform_device \*pdev:
        *undescribed*

.. _`davinci_aemif_setup.description`:

Description
-----------

This function does not use any locking while programming the AEMIF
because it is expected that there is only one user of a given
chip-select.

Returns 0 on success, else negative errno.

.. This file was automatic generated / don't edit.

