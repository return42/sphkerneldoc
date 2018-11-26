.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-mdio.c

.. _`cvm_oct_ioctl`:

cvm_oct_ioctl
=============

.. c:function:: int cvm_oct_ioctl(struct net_device *dev, struct ifreq *rq, int cmd)

    IOCTL support for PHY control

    :param dev:
        Device to change
    :type dev: struct net_device \*

    :param rq:
        the request
    :type rq: struct ifreq \*

    :param cmd:
        the command
    :type cmd: int

.. _`cvm_oct_ioctl.description`:

Description
-----------

Returns Zero on success

.. _`cvm_oct_phy_setup_device`:

cvm_oct_phy_setup_device
========================

.. c:function:: int cvm_oct_phy_setup_device(struct net_device *dev)

    setup the PHY

    :param dev:
        Device to setup
    :type dev: struct net_device \*

.. _`cvm_oct_phy_setup_device.description`:

Description
-----------

Returns Zero on success, negative on failure

.. This file was automatic generated / don't edit.

