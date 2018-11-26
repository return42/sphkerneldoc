.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_mac.c

.. _`hns_mac_need_adjust_link`:

hns_mac_need_adjust_link
========================

.. c:function:: bool hns_mac_need_adjust_link(struct hns_mac_cb *mac_cb, int speed, int duplex)

    check is need change mac speed and duplex register \ ``mac_cb``\ : mac device \ ``speed``\ : phy device speed \ ``duplex``\ :phy device duplex

    :param mac_cb:
        *undescribed*
    :type mac_cb: struct hns_mac_cb \*

    :param speed:
        *undescribed*
    :type speed: int

    :param duplex:
        *undescribed*
    :type duplex: int

.. _`hns_mac_get_inner_port_num`:

hns_mac_get_inner_port_num
==========================

.. c:function:: int hns_mac_get_inner_port_num(struct hns_mac_cb *mac_cb, u8 vmid, u8 *port_num)

    get mac table inner port number \ ``mac_cb``\ : mac device \ ``vmid``\ : vm id \ ``port_num``\ :port number

    :param mac_cb:
        *undescribed*
    :type mac_cb: struct hns_mac_cb \*

    :param vmid:
        *undescribed*
    :type vmid: u8

    :param port_num:
        *undescribed*
    :type port_num: u8 \*

.. _`hns_mac_change_vf_addr`:

hns_mac_change_vf_addr
======================

.. c:function:: int hns_mac_change_vf_addr(struct hns_mac_cb *mac_cb, u32 vmid, char *addr)

    change vf mac address \ ``mac_cb``\ : mac device \ ``vmid``\ : vmid \ ``addr``\ :mac address

    :param mac_cb:
        *undescribed*
    :type mac_cb: struct hns_mac_cb \*

    :param vmid:
        *undescribed*
    :type vmid: u32

    :param addr:
        *undescribed*
    :type addr: char \*

.. _`hns_mac_port_config_bc_en`:

hns_mac_port_config_bc_en
=========================

.. c:function:: int hns_mac_port_config_bc_en(struct hns_mac_cb *mac_cb, u32 port_num, u16 vlan_id, bool enable)

    set broadcast rx&tx enable \ ``mac_cb``\ : mac device \ ``queue``\ : queue number \ ``en``\ :enable retuen 0 - success , negative --fail

    :param mac_cb:
        *undescribed*
    :type mac_cb: struct hns_mac_cb \*

    :param port_num:
        *undescribed*
    :type port_num: u32

    :param vlan_id:
        *undescribed*
    :type vlan_id: u16

    :param enable:
        *undescribed*
    :type enable: bool

.. _`hns_mac_vm_config_bc_en`:

hns_mac_vm_config_bc_en
=======================

.. c:function:: int hns_mac_vm_config_bc_en(struct hns_mac_cb *mac_cb, u32 vmid, bool enable)

    set broadcast rx&tx enable \ ``mac_cb``\ : mac device \ ``vmid``\ : vm id \ ``en``\ :enable retuen 0 - success , negative --fail

    :param mac_cb:
        *undescribed*
    :type mac_cb: struct hns_mac_cb \*

    :param vmid:
        *undescribed*
    :type vmid: u32

    :param enable:
        *undescribed*
    :type enable: bool

.. _`hns_mac_get_autoneg`:

hns_mac_get_autoneg
===================

.. c:function:: void hns_mac_get_autoneg(struct hns_mac_cb *mac_cb, u32 *auto_neg)

    get auto autonegotiation

    :param mac_cb:
        mac control block
    :type mac_cb: struct hns_mac_cb \*

    :param auto_neg:
        *undescribed*
    :type auto_neg: u32 \*

.. _`hns_mac_get_pauseparam`:

hns_mac_get_pauseparam
======================

.. c:function:: void hns_mac_get_pauseparam(struct hns_mac_cb *mac_cb, u32 *rx_en, u32 *tx_en)

    set rx & tx pause parameter

    :param mac_cb:
        mac control block
    :type mac_cb: struct hns_mac_cb \*

    :param rx_en:
        rx enable status
    :type rx_en: u32 \*

    :param tx_en:
        tx enable status
        retuen 0 - success , negative --fail
    :type tx_en: u32 \*

.. _`hns_mac_set_autoneg`:

hns_mac_set_autoneg
===================

.. c:function:: int hns_mac_set_autoneg(struct hns_mac_cb *mac_cb, u8 enable)

    set auto autonegotiation

    :param mac_cb:
        mac control block
    :type mac_cb: struct hns_mac_cb \*

    :param enable:
        enable or not
        retuen 0 - success , negative --fail
    :type enable: u8

.. _`hns_mac_set_pauseparam`:

hns_mac_set_pauseparam
======================

.. c:function:: int hns_mac_set_pauseparam(struct hns_mac_cb *mac_cb, u32 rx_en, u32 tx_en)

    set rx & tx pause parameter

    :param mac_cb:
        mac control block
    :type mac_cb: struct hns_mac_cb \*

    :param rx_en:
        rx enable or not
    :type rx_en: u32

    :param tx_en:
        tx enable or not
        return 0 - success , negative --fail
    :type tx_en: u32

.. _`hns_mac_init_ex`:

hns_mac_init_ex
===============

.. c:function:: int hns_mac_init_ex(struct hns_mac_cb *mac_cb)

    mac init

    :param mac_cb:
        mac control block
        retuen 0 - success , negative --fail
    :type mac_cb: struct hns_mac_cb \*

.. _`hns_mac_get_info`:

hns_mac_get_info
================

.. c:function:: int hns_mac_get_info(struct hns_mac_cb *mac_cb)

    get mac information from device node \ ``mac_cb``\ : mac device \ ``np``\ :device node

    :param mac_cb:
        *undescribed*
    :type mac_cb: struct hns_mac_cb \*

.. _`hns_mac_get_info.return`:

Return
------

0 --success, negative --fail

.. _`hns_mac_get_mode`:

hns_mac_get_mode
================

.. c:function:: int hns_mac_get_mode(phy_interface_t phy_if)

    get mac mode

    :param phy_if:
        phy interface
        retuen 0 - gmac, 1 - xgmac , negative --fail
    :type phy_if: phy_interface_t

.. _`hns_mac_get_cfg`:

hns_mac_get_cfg
===============

.. c:function:: int hns_mac_get_cfg(struct dsaf_device *dsaf_dev, struct hns_mac_cb *mac_cb)

    get mac cfg from dtb or acpi table

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param mac_cb:
        mac control block
        return 0 - success , negative --fail
    :type mac_cb: struct hns_mac_cb \*

.. _`hns_mac_init`:

hns_mac_init
============

.. c:function:: int hns_mac_init(struct dsaf_device *dsaf_dev)

    init mac

    :param dsaf_dev:
        dsa fabric device struct pointer
        return 0 - success , negative --fail
    :type dsaf_dev: struct dsaf_device \*

.. This file was automatic generated / don't edit.

