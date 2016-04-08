
.. _API-phy-poll-reset:

==============
phy_poll_reset
==============

*man phy_poll_reset(9)*

*4.6.0-rc1*

Safely wait until a PHY reset has properly completed


Synopsis
========

.. c:function:: int phy_poll_reset( struct phy_device * phydev )

Arguments
=========

``phydev``
    The PHY device to poll


Description
===========

According to IEEE 802.3, Section 2, Subsection 22.2.4.1.1, as published in 2008, a PHY reset may take up to 0.5 seconds. The MII BMCR register must be polled until the BMCR_RESET
bit clears.

Furthermore, any attempts to write to PHY registers may have no effect or even generate MDIO bus errors until this is complete.

Some PHYs (such as the Marvell 88E1111) don't entirely conform to the standard and do not fully reset after the BMCR_RESET bit is set, and may even ⋆REQUIRE⋆ a soft-reset to
properly restart autonegotiation. In an effort to support such broken PHYs, this function is separate from the standard ``phy_init_hw`` which will zero all the other bits in the
BMCR and reapply all driver-specific and board-specific fixups.
