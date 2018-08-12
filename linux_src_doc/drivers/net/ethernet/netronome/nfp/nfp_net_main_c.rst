.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_main.c

.. _`nfp_net_get_mac_addr`:

nfp_net_get_mac_addr
====================

.. c:function:: void nfp_net_get_mac_addr(struct nfp_pf *pf, struct net_device *netdev, struct nfp_port *port)

    Get the MAC address.

    :param struct nfp_pf \*pf:
        NFP PF handle

    :param struct net_device \*netdev:
        net_device to set MAC address on

    :param struct nfp_port \*port:
        NFP port structure

.. _`nfp_net_get_mac_addr.description`:

Description
-----------

First try to get the MAC address from NSP ETH table. If that
fails generate a random address.

.. This file was automatic generated / don't edit.

