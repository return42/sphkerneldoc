.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_88xx/halmac_8822b/halmac_api_8822b_usb.c

.. _`halmac_mac_power_switch_8822b_usb`:

halmac_mac_power_switch_8822b_usb
=================================

.. c:function:: enum halmac_ret_status halmac_mac_power_switch_8822b_usb(struct halmac_adapter *halmac_adapter, enum halmac_mac_power halmac_power)

    switch mac power

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_power:
        power state
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_power: enum halmac_mac_power

.. _`halmac_phy_cfg_8822b_usb`:

halmac_phy_cfg_8822b_usb
========================

.. c:function:: enum halmac_ret_status halmac_phy_cfg_8822b_usb(struct halmac_adapter *halmac_adapter, enum halmac_intf_phy_platform platform)

    phy config

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

    :param platform:
        *undescribed*
    :type platform: enum halmac_intf_phy_platform

.. _`halmac_interface_integration_tuning_8822b_usb`:

halmac_interface_integration_tuning_8822b_usb
=============================================

.. c:function:: enum halmac_ret_status halmac_interface_integration_tuning_8822b_usb(struct halmac_adapter *halmac_adapter)

    usb interface fine tuning

    :param halmac_adapter:
        the adapter of halmac
        Author : Ivan
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. This file was automatic generated / don't edit.

