.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/i2c.c

.. _`omap_i2c_reset`:

omap_i2c_reset
==============

.. c:function:: int omap_i2c_reset(struct omap_hwmod *oh)

    reset the omap i2c module.

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_i2c_reset.description`:

Description
-----------

The i2c moudle in omap2, omap3 had a special sequence to reset. The

.. _`omap_i2c_reset.sequence-is`:

sequence is
-----------

- Disable the I2C.
- Write to SOFTRESET bit.
- Enable the I2C.
- Poll on the RESETDONE bit.
The sequence is implemented in below function. This is called for 2420,
2430 and omap3.

.. This file was automatic generated / don't edit.

