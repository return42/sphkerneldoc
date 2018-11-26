.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_misc.c

.. _`hns_dsaf_srst_chns`:

hns_dsaf_srst_chns
==================

.. c:function:: void hns_dsaf_srst_chns(struct dsaf_device *dsaf_dev, u32 msk, bool dereset)

    reset dsaf channels

    :param dsaf_dev:
        dsaf device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param msk:
        xbar channels mask value:
        bit0-5 for xge0-5
        bit6-11 for ppe0-5
        bit12-17 for roce0-5
        bit18-19 for com/dfx
    :type msk: u32

    :param dereset:
        *undescribed*
    :type dereset: bool

.. _`hns_dsaf_srst_chns_acpi`:

hns_dsaf_srst_chns_acpi
=======================

.. c:function:: void hns_dsaf_srst_chns_acpi(struct dsaf_device *dsaf_dev, u32 msk, bool dereset)

    reset dsaf channels

    :param dsaf_dev:
        dsaf device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param msk:
        xbar channels mask value:
        bit0-5 for xge0-5
        bit6-11 for ppe0-5
        bit12-17 for roce0-5
        bit18-19 for com/dfx
    :type msk: u32

    :param dereset:
        *undescribed*
    :type dereset: bool

.. _`hns_mac_get_phy_if`:

hns_mac_get_phy_if
==================

.. c:function:: phy_interface_t hns_mac_get_phy_if(struct hns_mac_cb *mac_cb)

    get phy ifterface form serdes mode

    :param mac_cb:
        mac control block
        retuen phy interface
    :type mac_cb: struct hns_mac_cb \*

.. _`hns_mac_config_sds_loopback`:

hns_mac_config_sds_loopback
===========================

.. c:function:: int hns_mac_config_sds_loopback(struct hns_mac_cb *mac_cb, bool en)

    set loop back for serdes

    :param mac_cb:
        mac control block
        retuen 0 == success
    :type mac_cb: struct hns_mac_cb \*

    :param en:
        *undescribed*
    :type en: bool

.. This file was automatic generated / don't edit.

