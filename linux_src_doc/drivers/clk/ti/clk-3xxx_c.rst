.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clk-3xxx.c

.. _`omap3430es2_clk_ssi_find_idlest`:

omap3430es2_clk_ssi_find_idlest
===============================

.. c:function:: void omap3430es2_clk_ssi_find_idlest(struct clk_hw_omap *clk, struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for SSI

    :param clk:
        struct clk \* being enabled
    :type clk: struct clk_hw_omap \*

    :param idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into
    :type idlest_reg: struct clk_omap_reg \*

    :param idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into
    :type idlest_bit: u8 \*

    :param idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator
    :type idlest_val: u8 \*

.. _`omap3430es2_clk_ssi_find_idlest.description`:

Description
-----------

The OMAP3430ES2 SSI target CM_IDLEST bit is at a different shift
from the CM_{I,F}CLKEN bit.  Pass back the correct info via
\ ``idlest_reg``\  and \ ``idlest_bit``\ .  No return value.

.. _`omap3430es2_clk_dss_usbhost_find_idlest`:

omap3430es2_clk_dss_usbhost_find_idlest
=======================================

.. c:function:: void omap3430es2_clk_dss_usbhost_find_idlest(struct clk_hw_omap *clk, struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    CM_IDLEST info for DSS, USBHOST

    :param clk:
        struct clk \* being enabled
    :type clk: struct clk_hw_omap \*

    :param idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into
    :type idlest_reg: struct clk_omap_reg \*

    :param idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into
    :type idlest_bit: u8 \*

    :param idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator
    :type idlest_val: u8 \*

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

.. c:function:: void omap3430es2_clk_hsotgusb_find_idlest(struct clk_hw_omap *clk, struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for HSOTGUSB

    :param clk:
        struct clk \* being enabled
    :type clk: struct clk_hw_omap \*

    :param idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into
    :type idlest_reg: struct clk_omap_reg \*

    :param idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into
    :type idlest_bit: u8 \*

    :param idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator
    :type idlest_val: u8 \*

.. _`omap3430es2_clk_hsotgusb_find_idlest.description`:

Description
-----------

The OMAP3430ES2 HSOTGUSB target CM_IDLEST bit is at a different
shift from the CM_{I,F}CLKEN bit.  Pass back the correct info via
\ ``idlest_reg``\  and \ ``idlest_bit``\ .  No return value.

.. _`am35xx_clk_find_idlest`:

am35xx_clk_find_idlest
======================

.. c:function:: void am35xx_clk_find_idlest(struct clk_hw_omap *clk, struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return clock ACK info for AM35XX IPSS

    :param clk:
        struct clk \* being enabled
    :type clk: struct clk_hw_omap \*

    :param idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into
    :type idlest_reg: struct clk_omap_reg \*

    :param idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into
    :type idlest_bit: u8 \*

    :param idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator
    :type idlest_val: u8 \*

.. _`am35xx_clk_find_idlest.description`:

Description
-----------

The interface clocks on AM35xx IPSS reflects the clock idle status
in the enable register itsel at a bit offset of 4 from the enable
bit. A value of 1 indicates that clock is enabled.

.. _`am35xx_clk_find_companion`:

am35xx_clk_find_companion
=========================

.. c:function:: void am35xx_clk_find_companion(struct clk_hw_omap *clk, struct clk_omap_reg *other_reg, u8 *other_bit)

    find companion clock to \ ``clk``\ 

    :param clk:
        struct clk \* to find the companion clock of
    :type clk: struct clk_hw_omap \*

    :param other_reg:
        void \__iomem \*\* to return the companion clock CM\_\*CLKEN va in
    :type other_reg: struct clk_omap_reg \*

    :param other_bit:
        u8 \*\* to return the companion clock bit shift in
    :type other_bit: u8 \*

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

.. c:function:: void am35xx_clk_ipss_find_idlest(struct clk_hw_omap *clk, struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for IPSS

    :param clk:
        struct clk \* being enabled
    :type clk: struct clk_hw_omap \*

    :param idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into
    :type idlest_reg: struct clk_omap_reg \*

    :param idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into
    :type idlest_bit: u8 \*

    :param idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator
    :type idlest_val: u8 \*

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

    :param void:
        no arguments
    :type void: 

.. _`omap3_clk_lock_dpll5.description`:

Description
-----------

Locks DPLL5 to a pre-defined frequency. This is required for proper
operation of USB.

.. This file was automatic generated / don't edit.

