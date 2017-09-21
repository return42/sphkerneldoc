.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_port.c

.. _`nfp_port_configure`:

nfp_port_configure
==================

.. c:function:: int nfp_port_configure(struct net_device *netdev, bool configed)

    helper to set the interface configured bit

    :param struct net_device \*netdev:
        net_device instance

    :param bool configed:
        Desired state

.. _`nfp_port_configure.description`:

Description
-----------

Helper to set the ifup/ifdown state on the PHY only if there is a physical
interface associated with the netdev.

.. _`nfp_port_configure.return`:

Return
------

0 - configuration successful (or no change);
-ERRNO - configuration failed.

.. This file was automatic generated / don't edit.

