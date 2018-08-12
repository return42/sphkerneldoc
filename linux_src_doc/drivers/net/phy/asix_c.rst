.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/asix.c

.. _`asix_soft_reset`:

asix_soft_reset
===============

.. c:function:: int asix_soft_reset(struct phy_device *phydev)

    software reset the PHY via BMCR_RESET bit

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`asix_soft_reset.description`:

Description
-----------

Perform a software PHY reset using the standard
BMCR_RESET bit and poll for the reset bit to be cleared.
Toggle BMCR_RESET bit off to accommodate broken AX8796B PHY implementation
such as used on the Individual Computers' X-Surf 100 Zorro card.

.. _`asix_soft_reset.return`:

Return
------

0 on success, < 0 on failure

.. This file was automatic generated / don't edit.

