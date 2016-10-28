.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/nvidia/forcedeth.c

.. _`nv_update_linkspeed`:

nv_update_linkspeed
===================

.. c:function:: int nv_update_linkspeed(struct net_device *dev)

    Setup the MAC according to the link partner

    :param struct net_device \*dev:
        Network device to be configured

.. _`nv_update_linkspeed.description`:

Description
-----------

The function queries the PHY and checks if there is a link partner.
If yes, then it sets up the MAC accordingly. Otherwise, the MAC is
set to 10 MBit HD.

The function returns 0 if there is no link partner and 1 if there is
a good link partner.

.. This file was automatic generated / don't edit.

