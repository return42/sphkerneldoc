.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/msdi.c

.. _`omap_msdi_reset`:

omap_msdi_reset
===============

.. c:function:: int omap_msdi_reset(struct omap_hwmod *oh)

    reset the MSDI IP block

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_msdi_reset.description`:

Description
-----------

The MSDI IP block on OMAP2420 has to have both the POW and CLKD
fields set inside its CON register for a reset to complete
successfully.  This is not documented in the TRM.  For CLKD, we use
the value that results in the lowest possible clock rate, to attempt
to avoid disturbing any cards.

.. This file was automatic generated / don't edit.

