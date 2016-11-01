.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_mac.c

.. _`hns_mac_get_inner_port_num`:

hns_mac_get_inner_port_num
==========================

.. c:function:: int hns_mac_get_inner_port_num(struct hns_mac_cb *mac_cb, u8 vmid, u8 *port_num)

    get mac table inner port number \ ``mac_cb``\ : mac device \ ``vmid``\ : vm id \ ``port_num``\ :port number

    :param struct hns_mac_cb \*mac_cb:
        *undescribed*

    :param u8 vmid:
        *undescribed*

    :param u8 \*port_num:
        *undescribed*

.. _`hns_mac_change_vf_addr`:

hns_mac_change_vf_addr
======================

.. c:function:: int hns_mac_change_vf_addr(struct hns_mac_cb *mac_cb, u32 vmid, char *addr)

    change vf mac address \ ``mac_cb``\ : mac device \ ``vmid``\ : vmid \ ``addr``\ :mac address

    :param struct hns_mac_cb \*mac_cb:
        *undescribed*

    :param u32 vmid:
        *undescribed*

    :param char \*addr:
        *undescribed*

.. _`hns_mac_del_mac`:

hns_mac_del_mac
===============

.. c:function:: int hns_mac_del_mac(struct hns_mac_cb *mac_cb, u32 vfn, char *mac)

    delete mac address into dsaf table,can't delete the same address twice \ ``net_dev``\ : net device \ ``vfn``\  :   vf lan \ ``mac``\  : mac address return status

    :param struct hns_mac_cb \*mac_cb:
        *undescribed*

    :param u32 vfn:
        *undescribed*

    :param char \*mac:
        *undescribed*

.. _`hns_mac_port_config_bc_en`:

hns_mac_port_config_bc_en
=========================

.. c:function:: int hns_mac_port_config_bc_en(struct hns_mac_cb *mac_cb, u32 port_num, u16 vlan_id, bool enable)

    set broadcast rx&tx enable \ ``mac_cb``\ : mac device \ ``queue``\ : queue number \ ``en``\ :enable retuen 0 - success , negative --fail

    :param struct hns_mac_cb \*mac_cb:
        *undescribed*

    :param u32 port_num:
        *undescribed*

    :param u16 vlan_id:
        *undescribed*

    :param bool enable:
        *undescribed*

.. _`hns_mac_vm_config_bc_en`:

hns_mac_vm_config_bc_en
=======================

.. c:function:: int hns_mac_vm_config_bc_en(struct hns_mac_cb *mac_cb, u32 vmid, bool enable)

    set broadcast rx&tx enable \ ``mac_cb``\ : mac device \ ``vmid``\ : vm id \ ``en``\ :enable retuen 0 - success , negative --fail

    :param struct hns_mac_cb \*mac_cb:
        *undescribed*

    :param u32 vmid:
        *undescribed*

    :param bool enable:
        *undescribed*

.. _`hns_mac_get_autoneg`:

hns_mac_get_autoneg
===================

.. c:function:: void hns_mac_get_autoneg(struct hns_mac_cb *mac_cb, u32 *auto_neg)

    get auto autonegotiation

    :param struct hns_mac_cb \*mac_cb:
        mac control block

    :param u32 \*auto_neg:
        *undescribed*

.. _`hns_mac_get_pauseparam`:

hns_mac_get_pauseparam
======================

.. c:function:: void hns_mac_get_pauseparam(struct hns_mac_cb *mac_cb, u32 *rx_en, u32 *tx_en)

    set rx & tx pause parameter

    :param struct hns_mac_cb \*mac_cb:
        mac control block

    :param u32 \*rx_en:
        rx enable status

    :param u32 \*tx_en:
        tx enable status
        retuen 0 - success , negative --fail

.. _`hns_mac_set_autoneg`:

hns_mac_set_autoneg
===================

.. c:function:: int hns_mac_set_autoneg(struct hns_mac_cb *mac_cb, u8 enable)

    set auto autonegotiation

    :param struct hns_mac_cb \*mac_cb:
        mac control block

    :param u8 enable:
        enable or not
        retuen 0 - success , negative --fail

.. _`hns_mac_set_pauseparam`:

hns_mac_set_pauseparam
======================

.. c:function:: int hns_mac_set_pauseparam(struct hns_mac_cb *mac_cb, u32 rx_en, u32 tx_en)

    set rx & tx pause parameter

    :param struct hns_mac_cb \*mac_cb:
        mac control block

    :param u32 rx_en:
        rx enable or not

    :param u32 tx_en:
        tx enable or not
        return 0 - success , negative --fail

.. _`hns_mac_init_ex`:

hns_mac_init_ex
===============

.. c:function:: int hns_mac_init_ex(struct hns_mac_cb *mac_cb)

    mac init

    :param struct hns_mac_cb \*mac_cb:
        mac control block
        retuen 0 - success , negative --fail

.. _`hns_mac_get_info`:

hns_mac_get_info
================

.. c:function:: int hns_mac_get_info(struct hns_mac_cb *mac_cb)

    get mac information from device node \ ``mac_cb``\ : mac device \ ``np``\ :device node

    :param struct hns_mac_cb \*mac_cb:
        *undescribed*

.. _`hns_mac_get_info.return`:

Return
------

0 --success, negative --fail

.. _`hns_mac_get_mode`:

hns_mac_get_mode
================

.. c:function:: int hns_mac_get_mode(phy_interface_t phy_if)

    get mac mode

    :param phy_interface_t phy_if:
        phy interface
        retuen 0 - gmac, 1 - xgmac , negative --fail

.. _`hns_mac_get_cfg`:

hns_mac_get_cfg
===============

.. c:function:: int hns_mac_get_cfg(struct dsaf_device *dsaf_dev, struct hns_mac_cb *mac_cb)

    get mac cfg from dtb or acpi table

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct hns_mac_cb \*mac_cb:
        mac control block
        return 0 - success , negative --fail

.. _`hns_mac_init`:

hns_mac_init
============

.. c:function:: int hns_mac_init(struct dsaf_device *dsaf_dev)

    init mac

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer
        return 0 - success , negative --fail

.. This file was automatic generated / don't edit.

