.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/phy-c45.c

.. _`genphy_c45_pma_setup_forced`:

genphy_c45_pma_setup_forced
===========================

.. c:function:: int genphy_c45_pma_setup_forced(struct phy_device *phydev)

    configures a forced speed

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`genphy_c45_an_disable_aneg`:

genphy_c45_an_disable_aneg
==========================

.. c:function:: int genphy_c45_an_disable_aneg(struct phy_device *phydev)

    disable auto-negotiation

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`genphy_c45_an_disable_aneg.description`:

Description
-----------

Disable auto-negotiation in the Clause 45 PHY. The link parameters
parameters are controlled through the PMA/PMD MMD registers.

Returns zero on success, negative errno code on failure.

.. _`genphy_c45_restart_aneg`:

genphy_c45_restart_aneg
=======================

.. c:function:: int genphy_c45_restart_aneg(struct phy_device *phydev)

    Enable and restart auto-negotiation

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`genphy_c45_restart_aneg.description`:

Description
-----------

This assumes that the auto-negotiation MMD is present.

Enable and restart auto-negotiation.

.. _`genphy_c45_aneg_done`:

genphy_c45_aneg_done
====================

.. c:function:: int genphy_c45_aneg_done(struct phy_device *phydev)

    return auto-negotiation complete status

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`genphy_c45_aneg_done.description`:

Description
-----------

This assumes that the auto-negotiation MMD is present.

Reads the status register from the auto-negotiation MMD, returning:
- positive if auto-negotiation is complete
- negative errno code on error
- zero otherwise

.. _`genphy_c45_read_link`:

genphy_c45_read_link
====================

.. c:function:: int genphy_c45_read_link(struct phy_device *phydev, u32 mmd_mask)

    read the overall link status from the MMDs

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

    :param mmd_mask:
        MMDs to read status from
    :type mmd_mask: u32

.. _`genphy_c45_read_link.description`:

Description
-----------

Read the link status from the specified MMDs, and if they all indicate
that the link is up, return positive.  If an error is encountered,
a negative errno will be returned, otherwise zero.

.. _`genphy_c45_read_lpa`:

genphy_c45_read_lpa
===================

.. c:function:: int genphy_c45_read_lpa(struct phy_device *phydev)

    read the link partner advertisement and pause

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`genphy_c45_read_lpa.description`:

Description
-----------

Read the Clause 45 defined base (7.19) and 10G (7.33) status registers,
filling in the link partner advertisement, pause and asym_pause members
in \ ``phydev``\ .  This assumes that the auto-negotiation MMD is present, and
the backplane bit (7.48.0) is clear.  Clause 45 PHY drivers are expected
to fill in the remainder of the link partner advert from vendor registers.

.. _`genphy_c45_read_pma`:

genphy_c45_read_pma
===================

.. c:function:: int genphy_c45_read_pma(struct phy_device *phydev)

    read link speed etc from PMA

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. _`genphy_c45_read_mdix`:

genphy_c45_read_mdix
====================

.. c:function:: int genphy_c45_read_mdix(struct phy_device *phydev)

    read mdix status from PMA

    :param phydev:
        target phy_device struct
    :type phydev: struct phy_device \*

.. This file was automatic generated / don't edit.

