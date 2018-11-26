.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_port.c

.. _`change_mac`:

change_mac
==========

.. c:function:: int change_mac(struct hinic_dev *nic_dev, const u8 *addr, u16 vlan_id, enum mac_op op)

    change(add or delete) mac address

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param addr:
        mac address
    :type addr: const u8 \*

    :param vlan_id:
        vlan number to set with the mac
    :type vlan_id: u16

    :param op:
        add or delete the mac
    :type op: enum mac_op

.. _`change_mac.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_add_mac`:

hinic_port_add_mac
==================

.. c:function:: int hinic_port_add_mac(struct hinic_dev *nic_dev, const u8 *addr, u16 vlan_id)

    add mac address

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param addr:
        mac address
    :type addr: const u8 \*

    :param vlan_id:
        vlan number to set with the mac
    :type vlan_id: u16

.. _`hinic_port_add_mac.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_del_mac`:

hinic_port_del_mac
==================

.. c:function:: int hinic_port_del_mac(struct hinic_dev *nic_dev, const u8 *addr, u16 vlan_id)

    remove mac address

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param addr:
        mac address
    :type addr: const u8 \*

    :param vlan_id:
        vlan number that is connected to the mac
    :type vlan_id: u16

.. _`hinic_port_del_mac.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_get_mac`:

hinic_port_get_mac
==================

.. c:function:: int hinic_port_get_mac(struct hinic_dev *nic_dev, u8 *addr)

    get the mac address of the nic device

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param addr:
        returned mac address
    :type addr: u8 \*

.. _`hinic_port_get_mac.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_set_mtu`:

hinic_port_set_mtu
==================

.. c:function:: int hinic_port_set_mtu(struct hinic_dev *nic_dev, int new_mtu)

    set mtu

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param new_mtu:
        new mtu
    :type new_mtu: int

.. _`hinic_port_set_mtu.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_add_vlan`:

hinic_port_add_vlan
===================

.. c:function:: int hinic_port_add_vlan(struct hinic_dev *nic_dev, u16 vlan_id)

    add vlan to the nic device

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param vlan_id:
        the vlan number to add
    :type vlan_id: u16

.. _`hinic_port_add_vlan.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_del_vlan`:

hinic_port_del_vlan
===================

.. c:function:: int hinic_port_del_vlan(struct hinic_dev *nic_dev, u16 vlan_id)

    delete vlan from the nic device

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param vlan_id:
        the vlan number to delete
    :type vlan_id: u16

.. _`hinic_port_del_vlan.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_set_rx_mode`:

hinic_port_set_rx_mode
======================

.. c:function:: int hinic_port_set_rx_mode(struct hinic_dev *nic_dev, u32 rx_mode)

    set rx mode in the nic device

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param rx_mode:
        the rx mode to set
    :type rx_mode: u32

.. _`hinic_port_set_rx_mode.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_link_state`:

hinic_port_link_state
=====================

.. c:function:: int hinic_port_link_state(struct hinic_dev *nic_dev, enum hinic_port_link_state *link_state)

    get the link state

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param link_state:
        the returned link state
    :type link_state: enum hinic_port_link_state \*

.. _`hinic_port_link_state.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_set_state`:

hinic_port_set_state
====================

.. c:function:: int hinic_port_set_state(struct hinic_dev *nic_dev, enum hinic_port_state state)

    set port state

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param state:
        the state to set
    :type state: enum hinic_port_state

.. _`hinic_port_set_state.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_set_func_state`:

hinic_port_set_func_state
=========================

.. c:function:: int hinic_port_set_func_state(struct hinic_dev *nic_dev, enum hinic_func_port_state state)

    set func device state

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param state:
        the state to set
    :type state: enum hinic_func_port_state

.. _`hinic_port_set_func_state.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_get_cap`:

hinic_port_get_cap
==================

.. c:function:: int hinic_port_get_cap(struct hinic_dev *nic_dev, struct hinic_port_cap *port_cap)

    get port capabilities

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param port_cap:
        returned port capabilities
    :type port_cap: struct hinic_port_cap \*

.. _`hinic_port_get_cap.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_port_set_tso`:

hinic_port_set_tso
==================

.. c:function:: int hinic_port_set_tso(struct hinic_dev *nic_dev, enum hinic_tso_state state)

    set port tso configuration

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param state:
        the tso state to set
    :type state: enum hinic_tso_state

.. _`hinic_port_set_tso.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. This file was automatic generated / don't edit.

