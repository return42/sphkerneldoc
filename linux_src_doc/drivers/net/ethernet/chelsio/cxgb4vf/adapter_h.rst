.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/adapter.h

.. _`t4_read_reg`:

t4_read_reg
===========

.. c:function:: u32 t4_read_reg(struct adapter *adapter, u32 reg_addr)

    read a HW register

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param reg_addr:
        the register address
    :type reg_addr: u32

.. _`t4_read_reg.description`:

Description
-----------

Returns the 32-bit value of the given HW register.

.. _`t4_write_reg`:

t4_write_reg
============

.. c:function:: void t4_write_reg(struct adapter *adapter, u32 reg_addr, u32 val)

    write a HW register

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param reg_addr:
        the register address
    :type reg_addr: u32

    :param val:
        the value to write
    :type val: u32

.. _`t4_write_reg.description`:

Description
-----------

Write a 32-bit value into the given HW register.

.. _`t4_read_reg64`:

t4_read_reg64
=============

.. c:function:: u64 t4_read_reg64(struct adapter *adapter, u32 reg_addr)

    read a 64-bit HW register

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param reg_addr:
        the register address
    :type reg_addr: u32

.. _`t4_read_reg64.description`:

Description
-----------

Returns the 64-bit value of the given HW register.

.. _`t4_write_reg64`:

t4_write_reg64
==============

.. c:function:: void t4_write_reg64(struct adapter *adapter, u32 reg_addr, u64 val)

    write a 64-bit HW register

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param reg_addr:
        the register address
    :type reg_addr: u32

    :param val:
        the value to write
    :type val: u64

.. _`t4_write_reg64.description`:

Description
-----------

Write a 64-bit value into the given HW register.

.. _`port_name`:

port_name
=========

.. c:function:: const char *port_name(struct adapter *adapter, int pidx)

    return the string name of a port

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

.. _`port_name.description`:

Description
-----------

Return the string name of the selected port.

.. _`t4_os_set_hw_addr`:

t4_os_set_hw_addr
=================

.. c:function:: void t4_os_set_hw_addr(struct adapter *adapter, int pidx, u8 hw_addr)

    store a port's MAC address in SW

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

    :param hw_addr:
        the Ethernet address
    :type hw_addr: u8

.. _`t4_os_set_hw_addr.description`:

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

.. c:function:: struct port_info *adap2pinfo(struct adapter *adapter, int pidx)

    return the port_info of a port

    :param adapter:
        *undescribed*
    :type adapter: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

.. _`adap2pinfo.description`:

Description
-----------

Return the port_info structure for the adapter.

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

.. This file was automatic generated / don't edit.

