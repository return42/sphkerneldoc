.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/marvell.c

.. _`ethtool_adv_to_fiber_adv_t`:

ethtool_adv_to_fiber_adv_t
==========================

.. c:function:: u32 ethtool_adv_to_fiber_adv_t(u32 ethadv)

    :param ethadv:
        the ethtool advertisement settings
    :type ethadv: u32

.. _`ethtool_adv_to_fiber_adv_t.description`:

Description
-----------

A small helper function that translates ethtool advertisement
settings to phy autonegotiation advertisements for the
MII_ADV register for fiber link.

.. _`marvell_config_aneg_fiber`:

marvell_config_aneg_fiber
=========================

.. c:function:: int marvell_config_aneg_fiber(struct phy_device *phydev)

    restart auto-negotiation or write BMCR

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`marvell_config_aneg_fiber.description`:

Description
-----------

If auto-negotiation is enabled, we configure the
advertising, and then restart auto-negotiation.  If it is not
enabled, then we write the BMCR. Adapted for fiber link in
some Marvell's devices.

.. _`fiber_lpa_to_ethtool_lpa_t`:

fiber_lpa_to_ethtool_lpa_t
==========================

.. c:function:: u32 fiber_lpa_to_ethtool_lpa_t(u32 lpa)

    :param lpa:
        value of the MII_LPA register for fiber link
    :type lpa: u32

.. _`fiber_lpa_to_ethtool_lpa_t.description`:

Description
-----------

A small helper function that translates MII_LPA
bits to ethtool LP advertisement settings.

.. _`marvell_update_link`:

marvell_update_link
===================

.. c:function:: int marvell_update_link(struct phy_device *phydev, int fiber)

    update link status in real time in \ ``phydev``\ 

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

    :param fiber:
        *undescribed*
    :type fiber: int

.. _`marvell_update_link.description`:

Description
-----------

Update the value in phydev->link to reflect the
current link value.

.. This file was automatic generated / don't edit.

