.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sis/sis190.c

.. _`sis190_default_phy`:

sis190_default_phy
==================

.. c:function:: u16 sis190_default_phy(struct net_device *dev)

    Select default PHY for sis190 mac.

    :param dev:
        the net device to probe for
    :type dev: struct net_device \*

.. _`sis190_default_phy.description`:

Description
-----------

Select first detected PHY with link as default.
If no one is link on, select PHY whose types is HOME as default.
If HOME doesn't exist, select LAN.

.. _`sis190_mii_probe`:

sis190_mii_probe
================

.. c:function:: int sis190_mii_probe(struct net_device *dev)

    Probe MII PHY for sis190

    :param dev:
        the net device to probe for
    :type dev: struct net_device \*

.. _`sis190_mii_probe.description`:

Description
-----------

Search for total of 32 possible mii phy addresses.
Identify and set current phy if found one,
return error if it failed to found.

.. _`sis190_get_mac_addr_from_apc`:

sis190_get_mac_addr_from_apc
============================

.. c:function:: int sis190_get_mac_addr_from_apc(struct pci_dev *pdev, struct net_device *dev)

    Get MAC address for SiS96x model

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param dev:
        network device to get address for
    :type dev: struct net_device \*

.. _`sis190_get_mac_addr_from_apc.description`:

Description
-----------

SiS96x model, use APC CMOS RAM to store MAC address.
APC CMOS RAM is accessed through ISA bridge.
MAC address is read into \ ``net_dev->dev_addr``\ .

.. _`sis190_init_rxfilter`:

sis190_init_rxfilter
====================

.. c:function:: void sis190_init_rxfilter(struct net_device *dev)

    Initialize the Rx filter

    :param dev:
        network device to initialize
    :type dev: struct net_device \*

.. _`sis190_init_rxfilter.description`:

Description
-----------

Set receive filter address to our MAC address
and enable packet filtering.

.. This file was automatic generated / don't edit.

