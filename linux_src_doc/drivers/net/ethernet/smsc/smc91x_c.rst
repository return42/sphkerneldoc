.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/smsc/smc91x.c

.. _`smc_phy_reset`:

smc_phy_reset
=============

.. c:function:: int smc_phy_reset(struct net_device *dev, int phy)

    reset the phy

    :param dev:
        net device
    :type dev: struct net_device \*

    :param phy:
        phy address
    :type phy: int

.. _`smc_phy_reset.description`:

Description
-----------

Issue a software reset for the specified PHY and
wait up to 100ms for the reset to complete.  We should
not access the PHY for 50ms after issuing the reset.

The time to wait appears to be dependent on the PHY.

Must be called with lp->lock locked.

.. _`smc_phy_powerdown`:

smc_phy_powerdown
=================

.. c:function:: void smc_phy_powerdown(struct net_device *dev)

    powerdown phy

    :param dev:
        net device
    :type dev: struct net_device \*

.. _`smc_phy_powerdown.description`:

Description
-----------

Power down the specified PHY

.. _`smc_phy_check_media`:

smc_phy_check_media
===================

.. c:function:: void smc_phy_check_media(struct net_device *dev, int init)

    check the media status and adjust TCR

    :param dev:
        net device
    :type dev: struct net_device \*

    :param init:
        set true for initialisation
    :type init: int

.. _`smc_phy_check_media.description`:

Description
-----------

Select duplex mode depending on negotiation state.  This
also updates our carrier state.

.. _`try_toggle_control_gpio`:

try_toggle_control_gpio
=======================

.. c:function:: int try_toggle_control_gpio(struct device *dev, struct gpio_desc **desc, const char *name, int index, int value, unsigned int nsdelay)

    configure a gpio if it exists

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param desc:
        *undescribed*
    :type desc: struct gpio_desc \*\*

    :param name:
        *undescribed*
    :type name: const char \*

    :param index:
        *undescribed*
    :type index: int

    :param value:
        *undescribed*
    :type value: int

    :param nsdelay:
        *undescribed*
    :type nsdelay: unsigned int

.. This file was automatic generated / don't edit.

