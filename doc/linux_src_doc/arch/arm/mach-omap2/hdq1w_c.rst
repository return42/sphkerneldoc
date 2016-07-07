.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/hdq1w.c

.. _`omap_hdq1w_reset`:

omap_hdq1w_reset
================

.. c:function:: int omap_hdq1w_reset(struct omap_hwmod *oh)

    reset the OMAP HDQ1W module

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hdq1w_reset.description`:

Description
-----------

OCP soft reset the HDQ1W IP block.  Section 20.6.1.4 "HDQ1W/1-Wire
Software Reset" of the OMAP34xx Technical Reference Manual Revision
ZR (SWPU223R) does not include the rather important fact that, for
the reset to succeed, the HDQ1W module's internal clock gate must be
programmed to allow the clock to propagate to the rest of the
module.  In this sense, it's rather similar to the I2C custom reset
function.  Returns 0.

.. This file was automatic generated / don't edit.

