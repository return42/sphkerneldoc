.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_main.c

.. _`nfp_net_get_mac_addr`:

nfp_net_get_mac_addr
====================

.. c:function:: void nfp_net_get_mac_addr(struct nfp_pf *pf, struct net_device *netdev, struct nfp_port *port)

    Get the MAC address.

    :param pf:
        NFP PF handle
    :type pf: struct nfp_pf \*

    :param netdev:
        net_device to set MAC address on
    :type netdev: struct net_device \*

    :param port:
        NFP port structure
    :type port: struct nfp_port \*

.. _`nfp_net_get_mac_addr.description`:

Description
-----------

First try to get the MAC address from NSP ETH table. If that
fails generate a random address.

.. This file was automatic generated / don't edit.

