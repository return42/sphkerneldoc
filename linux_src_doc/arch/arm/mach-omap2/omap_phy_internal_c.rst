.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_phy_internal.c

.. _`omap4430_phy_power_down`:

omap4430_phy_power_down
=======================

.. c:function:: int omap4430_phy_power_down( void)

    disable MUSB PHY during early init

    :param void:
        no arguments
    :type void: 

.. _`omap4430_phy_power_down.description`:

Description
-----------

OMAP4 MUSB PHY module is enabled by default on reset, but this will
prevent core retention if not disabled by SW. USB driver will
later on enable this, once and if the driver needs it.

.. This file was automatic generated / don't edit.

