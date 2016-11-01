.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_pcs.h

.. _`dwmac_pcs_isr`:

dwmac_pcs_isr
=============

.. c:function:: void dwmac_pcs_isr(void __iomem *ioaddr, u32 reg, unsigned int intr_status, struct stmmac_extra_stats *x)

    TBI, RTBI, or SGMII PHY ISR

    :param void __iomem \*ioaddr:
        IO registers pointer

    :param u32 reg:
        Base address of the AN Control Register.

    :param unsigned int intr_status:
        GMAC core interrupt status

    :param struct stmmac_extra_stats \*x:
        pointer to log these events as stats

.. _`dwmac_pcs_isr.description`:

Description
-----------

it is the ISR for PCS events: Auto-Negotiation Completed and
Link status.

.. _`dwmac_rane`:

dwmac_rane
==========

.. c:function:: void dwmac_rane(void __iomem *ioaddr, u32 reg, bool restart)

    To restart ANE

    :param void __iomem \*ioaddr:
        IO registers pointer

    :param u32 reg:
        Base address of the AN Control Register.

    :param bool restart:
        to restart ANE

.. _`dwmac_rane.description`:

Description
-----------

this is to just restart the Auto-Negotiation.

.. _`dwmac_ctrl_ane`:

dwmac_ctrl_ane
==============

.. c:function:: void dwmac_ctrl_ane(void __iomem *ioaddr, u32 reg, bool ane, bool srgmi_ral, bool loopback)

    To program the AN Control Register.

    :param void __iomem \*ioaddr:
        IO registers pointer

    :param u32 reg:
        Base address of the AN Control Register.

    :param bool ane:
        to enable the auto-negotiation

    :param bool srgmi_ral:
        to manage MAC-2-MAC SGMII connections.

    :param bool loopback:
        to cause the PHY to loopback tx data into rx path.

.. _`dwmac_ctrl_ane.description`:

Description
-----------

this is the main function to configure the AN control register
and init the ANE, select loopback (usually for debugging purpose) and
configure SGMII RAL.

.. _`dwmac_get_adv_lp`:

dwmac_get_adv_lp
================

.. c:function:: void dwmac_get_adv_lp(void __iomem *ioaddr, u32 reg, struct rgmii_adv *adv_lp)

    Get ADV and LP cap

    :param void __iomem \*ioaddr:
        IO registers pointer

    :param u32 reg:
        Base address of the AN Control Register.

    :param struct rgmii_adv \*adv_lp:
        structure to store the adv,lp status

.. _`dwmac_get_adv_lp.description`:

Description
-----------

this is to expose the ANE advertisement and Link partner ability
status to ethtool support.

.. This file was automatic generated / don't edit.

