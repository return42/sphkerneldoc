.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_88xx/halmac_8822b/halmac_api_8822b_pcie.c

.. _`halmac_mac_power_switch_8822b_pcie`:

halmac_mac_power_switch_8822b_pcie
==================================

.. c:function:: enum halmac_ret_status halmac_mac_power_switch_8822b_pcie(struct halmac_adapter *halmac_adapter, enum halmac_mac_power halmac_power)

    switch mac power

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param enum halmac_mac_power halmac_power:
        power state
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_pcie_switch_8822b`:

halmac_pcie_switch_8822b
========================

.. c:function:: enum halmac_ret_status halmac_pcie_switch_8822b(struct halmac_adapter *halmac_adapter, enum halmac_pcie_cfg pcie_cfg)

    pcie gen1/gen2 switch

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param enum halmac_pcie_cfg pcie_cfg:
        gen1/gen2 selection
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_phy_cfg_8822b_pcie`:

halmac_phy_cfg_8822b_pcie
=========================

.. c:function:: enum halmac_ret_status halmac_phy_cfg_8822b_pcie(struct halmac_adapter *halmac_adapter, enum halmac_intf_phy_platform platform)

    phy config

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

    :param enum halmac_intf_phy_platform platform:
        *undescribed*

.. _`halmac_interface_integration_tuning_8822b_pcie`:

halmac_interface_integration_tuning_8822b_pcie
==============================================

.. c:function:: enum halmac_ret_status halmac_interface_integration_tuning_8822b_pcie(struct halmac_adapter *halmac_adapter)

    pcie interface fine tuning

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : Rick Liu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. This file was automatic generated / don't edit.

