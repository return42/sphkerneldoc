.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4.h

.. _`t4_set_hw_addr`:

t4_set_hw_addr
==============

.. c:function:: void t4_set_hw_addr(struct adapter *adapter, int port_idx, u8 hw_addr)

    store a port's MAC address in SW

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param port_idx:
        the port index
    :type port_idx: int

    :param hw_addr:
        the Ethernet address
    :type hw_addr: u8

.. _`t4_set_hw_addr.description`:

Description
-----------

Store the Ethernet address of the given port in SW.  Called by the common
code when it retrieves a port's Ethernet address from EEPROM.

.. _`netdev2pinfo`:

netdev2pinfo
============

.. c:function:: struct port_info *netdev2pinfo(const struct net_device *dev)

    return the port_info structure associated with a net_device

    :param dev:
        the netdev
    :type dev: const struct net_device \*

.. _`netdev2pinfo.description`:

Description
-----------

Return the struct port_info associated with a net_device

.. _`adap2pinfo`:

adap2pinfo
==========

.. c:function:: struct port_info *adap2pinfo(struct adapter *adap, int idx)

    return the port_info of a port

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param idx:
        the port index
    :type idx: int

.. _`adap2pinfo.description`:

Description
-----------

Return the port_info structure for the port of the given index.

.. _`netdev2adap`:

netdev2adap
===========

.. c:function:: struct adapter *netdev2adap(const struct net_device *dev)

    return the adapter structure associated with a net_device

    :param dev:
        the netdev
    :type dev: const struct net_device \*

.. _`netdev2adap.description`:

Description
-----------

Return the struct adapter associated with a net_device

.. _`hash_mac_addr`:

hash_mac_addr
=============

.. c:function:: int hash_mac_addr(const u8 *addr)

    return the hash value of a MAC address

    :param addr:
        the 48-bit Ethernet MAC address
    :type addr: const u8 \*

.. _`hash_mac_addr.description`:

Description
-----------

Hashes a MAC address according to the hash function used by HW inexact
(hash) address matching.

.. _`t4_is_inserted_mod_type`:

t4_is_inserted_mod_type
=======================

.. c:function:: bool t4_is_inserted_mod_type(unsigned int fw_mod_type)

    is a plugged in Firmware Module Type

    :param fw_mod_type:
        the Firmware Mofule Type
    :type fw_mod_type: unsigned int

.. _`t4_is_inserted_mod_type.description`:

Description
-----------

Return whether the Firmware Module Type represents a real Transceiver
Module/Cable Module Type which has been inserted.

.. This file was automatic generated / don't edit.

