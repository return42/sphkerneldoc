.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/smsc/smc911x.c

.. _`smc911x_phy_reset`:

smc911x_phy_reset
=================

.. c:function:: int smc911x_phy_reset(struct net_device *dev, int phy)

    reset the phy

    :param struct net_device \*dev:
        net device

    :param int phy:
        phy address

.. _`smc911x_phy_reset.description`:

Description
-----------

Issue a software reset for the specified PHY and
wait up to 100ms for the reset to complete.   We should
not access the PHY for 50ms after issuing the reset.

The time to wait appears to be dependent on the PHY.

.. _`smc911x_phy_powerdown`:

smc911x_phy_powerdown
=====================

.. c:function:: void smc911x_phy_powerdown(struct net_device *dev, int phy)

    powerdown phy

    :param struct net_device \*dev:
        net device

    :param int phy:
        phy address

.. _`smc911x_phy_powerdown.description`:

Description
-----------

Power down the specified PHY

.. _`smc911x_phy_check_media`:

smc911x_phy_check_media
=======================

.. c:function:: void smc911x_phy_check_media(struct net_device *dev, int init)

    check the media status and adjust BMCR

    :param struct net_device \*dev:
        net device

    :param int init:
        set true for initialisation

.. _`smc911x_phy_check_media.description`:

Description
-----------

Select duplex mode depending on negotiation state.   This
also updates our carrier state.

.. This file was automatic generated / don't edit.

