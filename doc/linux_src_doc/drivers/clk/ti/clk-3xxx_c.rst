.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clk-3xxx.c

.. _`omap3430es2_clk_ssi_find_idlest`:

omap3430es2_clk_ssi_find_idlest
===============================

.. c:function:: void omap3430es2_clk_ssi_find_idlest(struct clk_hw_omap *clk, void __iomem **idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for SSI

    :param struct clk_hw_omap \*clk:
        struct clk \* being enabled

    :param void __iomem \*\*idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into

    :param u8 \*idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into

    :param u8 \*idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator

.. _`omap3430es2_clk_ssi_find_idlest.description`:

Description
-----------

The OMAP3430ES2 SSI target CM_IDLEST bit is at a different shift
from the CM_{I,F}CLKEN bit.  Pass back the correct info via
\ ``idlest_reg``\  and \ ``idlest_bit``\ .  No return value.

.. _`omap3430es2_clk_dss_usbhost_find_idlest`:

omap3430es2_clk_dss_usbhost_find_idlest
=======================================

.. c:function:: void omap3430es2_clk_dss_usbhost_find_idlest(struct clk_hw_omap *clk, void __iomem **idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    CM_IDLEST info for DSS, USBHOST

    :param struct clk_hw_omap \*clk:
        struct clk \* being enabled

    :param void __iomem \*\*idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into

    :param u8 \*idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into

    :param u8 \*idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator

.. _`omap3430es2_clk_dss_usbhost_find_idlest.description`:

Description
-----------

Some OMAP modules on OMAP3 ES2+ chips have both initiator and
target IDLEST bits.  For our purposes, we are concerned with the
target IDLEST bits, which exist at a different bit position than
the \*CLKEN bit position for these modules (DSS and USBHOST) (The
default find_idlest code assumes that they are at the same
position.)  No return value.

.. _`omap3430es2_clk_hsotgusb_find_idlest`:

omap3430es2_clk_hsotgusb_find_idlest
====================================

.. c:function:: void omap3430es2_clk_hsotgusb_find_idlest(struct clk_hw_omap *clk, void __iomem **idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for HSOTGUSB

    :param struct clk_hw_omap \*clk:
        struct clk \* being enabled

    :param void __iomem \*\*idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into

    :param u8 \*idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into

    :param u8 \*idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator

.. _`omap3430es2_clk_hsotgusb_find_idlest.description`:

Description
-----------

The OMAP3430ES2 HSOTGUSB target CM_IDLEST bit is at a different
shift from the CM_{I,F}CLKEN bit.  Pass back the correct info via
\ ``idlest_reg``\  and \ ``idlest_bit``\ .  No return value.

.. _`am35xx_clk_find_idlest`:

am35xx_clk_find_idlest
======================

.. c:function:: void am35xx_clk_find_idlest(struct clk_hw_omap *clk, void __iomem **idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return clock ACK info for AM35XX IPSS

    :param struct clk_hw_omap \*clk:
        struct clk \* being enabled

    :param void __iomem \*\*idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into

    :param u8 \*idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into

    :param u8 \*idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator

.. _`am35xx_clk_find_idlest.description`:

Description
-----------

The interface clocks on AM35xx IPSS reflects the clock idle status
in the enable register itsel at a bit offset of 4 from the enable
bit. A value of 1 indicates that clock is enabled.

.. _`am35xx_clk_find_companion`:

am35xx_clk_find_companion
=========================

.. c:function:: void am35xx_clk_find_companion(struct clk_hw_omap *clk, void __iomem **other_reg, u8 *other_bit)

    find companion clock to \ ``clk``\ 

    :param struct clk_hw_omap \*clk:
        struct clk \* to find the companion clock of

    :param void __iomem \*\*other_reg:
        void \__iomem \*\* to return the companion clock CM\_\*CLKEN va in

    :param u8 \*other_bit:
        u8 \*\* to return the companion clock bit shift in

.. _`am35xx_clk_find_companion.description`:

Description
-----------

Some clocks don't have companion clocks.  For example, modules with
only an interface clock (such as HECC) don't have a companion
clock.  Right now, this code relies on the hardware exporting a bit
in the correct companion register that indicates that the
nonexistent 'companion clock' is active.  Future patches will
associate this type of code with per-module data structures to
avoid this issue, and remove the casts.  No return value.

.. _`am35xx_clk_ipss_find_idlest`:

am35xx_clk_ipss_find_idlest
===========================

.. c:function:: void am35xx_clk_ipss_find_idlest(struct clk_hw_omap *clk, void __iomem **idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for IPSS

    :param struct clk_hw_omap \*clk:
        struct clk \* being enabled

    :param void __iomem \*\*idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into

    :param u8 \*idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into

    :param u8 \*idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator

.. _`am35xx_clk_ipss_find_idlest.description`:

Description
-----------

The IPSS target CM_IDLEST bit is at a different shift from the
CM_{I,F}CLKEN bit.  Pass back the correct info via \ ``idlest_reg``\ 
and \ ``idlest_bit``\ .  No return value.

.. _`omap3_clk_lock_dpll5`:

omap3_clk_lock_dpll5
====================

.. c:function:: void omap3_clk_lock_dpll5( void)

    locks DPLL5

    :param  void:
        no arguments

.. _`omap3_clk_lock_dpll5.description`:

Description
-----------

Locks DPLL5 to a pre-defined frequency. This is required for proper
operation of USB.

.. This file was automatic generated / don't edit.

