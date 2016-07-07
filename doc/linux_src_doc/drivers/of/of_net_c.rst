.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_net.c

.. _`of_get_phy_mode`:

of_get_phy_mode
===============

.. c:function:: int of_get_phy_mode(struct device_node *np)

    Get phy mode for given device_node

    :param struct device_node \*np:
        Pointer to the given device_node

.. _`of_get_phy_mode.description`:

Description
-----------

The function gets phy interface string from property 'phy-mode' or
'phy-connection-type', and return its index in phy_modes table, or errno in
error case.

.. _`of_get_mac_address`:

of_get_mac_address
==================

.. c:function:: const void *of_get_mac_address(struct device_node *np)

    address' is checked first, because that is supposed to contain to "most recent" MAC address. If that isn't set, then 'local-mac-address' is checked next, because that is the default address.  If that isn't set, then the obsolete 'address' is checked, just in case we're using an old device tree.

    :param struct device_node \*np:
        *undescribed*

.. _`of_get_mac_address.description`:

Description
-----------

Note that the 'address' property is supposed to contain a virtual address of
the register set, but some DTS files have redefined that property to be the
MAC address.

All-zero MAC addresses are rejected, because those could be properties that
exist in the device tree, but were not set by U-Boot.  For example, the
DTS could define 'mac-address' and 'local-mac-address', with zero MAC
addresses.  Some older U-Boots only initialized 'local-mac-address'.  In
this case, the real MAC is in 'local-mac-address', and 'mac-address' exists
but is all zeros.

.. This file was automatic generated / don't edit.

