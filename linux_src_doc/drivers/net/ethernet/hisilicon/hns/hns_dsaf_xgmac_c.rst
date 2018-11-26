.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_xgmac.c

.. _`hns_xgmac_tx_enable`:

hns_xgmac_tx_enable
===================

.. c:function:: void hns_xgmac_tx_enable(struct mac_driver *drv, u32 value)

    xgmac port tx enable \ ``drv``\ : mac driver \ ``value``\ : value of enable

    :param drv:
        *undescribed*
    :type drv: struct mac_driver \*

    :param value:
        *undescribed*
    :type value: u32

.. _`hns_xgmac_rx_enable`:

hns_xgmac_rx_enable
===================

.. c:function:: void hns_xgmac_rx_enable(struct mac_driver *drv, u32 value)

    xgmac port rx enable \ ``drv``\ : mac driver \ ``value``\ : value of enable

    :param drv:
        *undescribed*
    :type drv: struct mac_driver \*

    :param value:
        *undescribed*
    :type value: u32

.. _`hns_xgmac_lf_rf_insert`:

hns_xgmac_lf_rf_insert
======================

.. c:function:: void hns_xgmac_lf_rf_insert(struct mac_driver *mac_drv, u32 mode)

    insert lf rf control about xgmac

    :param mac_drv:
        mac driver
    :type mac_drv: struct mac_driver \*

    :param mode:
        inserf rf or lf
    :type mode: u32

.. _`hns_xgmac_lf_rf_control_init`:

hns_xgmac_lf_rf_control_init
============================

.. c:function:: void hns_xgmac_lf_rf_control_init(struct mac_driver *mac_drv)

    initial the lf rf control register

    :param mac_drv:
        mac driver
    :type mac_drv: struct mac_driver \*

.. _`hns_xgmac_enable`:

hns_xgmac_enable
================

.. c:function:: void hns_xgmac_enable(void *mac_drv, enum mac_commom_mode mode)

    enable xgmac port \ ``drv``\ : mac driver \ ``mode``\ : mode of mac port

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param mode:
        *undescribed*
    :type mode: enum mac_commom_mode

.. _`hns_xgmac_disable`:

hns_xgmac_disable
=================

.. c:function:: void hns_xgmac_disable(void *mac_drv, enum mac_commom_mode mode)

    disable xgmac port \ ``mac_drv``\ : mac driver \ ``mode``\ : mode of mac port

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param mode:
        *undescribed*
    :type mode: enum mac_commom_mode

.. _`hns_xgmac_pma_fec_enable`:

hns_xgmac_pma_fec_enable
========================

.. c:function:: void hns_xgmac_pma_fec_enable(struct mac_driver *drv, u32 tx_value, u32 rx_value)

    xgmac PMA FEC enable \ ``drv``\ : mac driver \ ``tx_value``\ : tx value \ ``rx_value``\ : rx value return status

    :param drv:
        *undescribed*
    :type drv: struct mac_driver \*

    :param tx_value:
        *undescribed*
    :type tx_value: u32

    :param rx_value:
        *undescribed*
    :type rx_value: u32

.. _`hns_xgmac_init`:

hns_xgmac_init
==============

.. c:function:: void hns_xgmac_init(void *mac_drv)

    initialize XGE \ ``mac_drv``\ : mac driver

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

.. _`hns_xgmac_config_pad_and_crc`:

hns_xgmac_config_pad_and_crc
============================

.. c:function:: void hns_xgmac_config_pad_and_crc(void *mac_drv, u8 newval)

    set xgmac pad and crc enable the same time \ ``mac_drv``\ : mac driver \ ``newval``\ :enable of pad and crc

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param newval:
        *undescribed*
    :type newval: u8

.. _`hns_xgmac_pausefrm_cfg`:

hns_xgmac_pausefrm_cfg
======================

.. c:function:: void hns_xgmac_pausefrm_cfg(void *mac_drv, u32 rx_en, u32 tx_en)

    set pause param about xgmac \ ``mac_drv``\ : mac driver \ ``newval``\ :enable of pad and crc

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param rx_en:
        *undescribed*
    :type rx_en: u32

    :param tx_en:
        *undescribed*
    :type tx_en: u32

.. _`hns_xgmac_set_rx_ignore_pause_frames`:

hns_xgmac_set_rx_ignore_pause_frames
====================================

.. c:function:: void hns_xgmac_set_rx_ignore_pause_frames(void *mac_drv, u32 enable)

    set rx pause param about xgmac \ ``mac_drv``\ : mac driver \ ``enable``\ :enable rx pause param

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param enable:
        *undescribed*
    :type enable: u32

.. _`hns_xgmac_set_tx_auto_pause_frames`:

hns_xgmac_set_tx_auto_pause_frames
==================================

.. c:function:: void hns_xgmac_set_tx_auto_pause_frames(void *mac_drv, u16 enable)

    set tx pause param about xgmac \ ``mac_drv``\ : mac driver \ ``enable``\ :enable tx pause param

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param enable:
        *undescribed*
    :type enable: u16

.. _`hns_xgmac_config_max_frame_length`:

hns_xgmac_config_max_frame_length
=================================

.. c:function:: void hns_xgmac_config_max_frame_length(void *mac_drv, u16 newval)

    set xgmac max frame length \ ``mac_drv``\ : mac driver \ ``newval``\ :xgmac max frame length

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param newval:
        *undescribed*
    :type newval: u16

.. _`hns_xgmac_free`:

hns_xgmac_free
==============

.. c:function:: void hns_xgmac_free(void *mac_drv)

    free xgmac driver \ ``mac_drv``\ : mac driver

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

.. _`hns_xgmac_get_info`:

hns_xgmac_get_info
==================

.. c:function:: void hns_xgmac_get_info(void *mac_drv, struct mac_info *mac_info)

    get xgmac information \ ``mac_drv``\ : mac driver \ ``mac_info``\ :mac information

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param mac_info:
        *undescribed*
    :type mac_info: struct mac_info \*

.. _`hns_xgmac_get_pausefrm_cfg`:

hns_xgmac_get_pausefrm_cfg
==========================

.. c:function:: void hns_xgmac_get_pausefrm_cfg(void *mac_drv, u32 *rx_en, u32 *tx_en)

    get xgmac pause param \ ``mac_drv``\ : mac driver \ ``rx_en``\ :xgmac rx pause enable \ ``tx_en``\ :xgmac tx pause enable

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param rx_en:
        *undescribed*
    :type rx_en: u32 \*

    :param tx_en:
        *undescribed*
    :type tx_en: u32 \*

.. _`hns_xgmac_get_link_status`:

hns_xgmac_get_link_status
=========================

.. c:function:: void hns_xgmac_get_link_status(void *mac_drv, u32 *link_stat)

    get xgmac link status \ ``mac_drv``\ : mac driver \ ``link_stat``\ : xgmac link stat

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param link_stat:
        *undescribed*
    :type link_stat: u32 \*

.. _`hns_xgmac_get_regs`:

hns_xgmac_get_regs
==================

.. c:function:: void hns_xgmac_get_regs(void *mac_drv, void *data)

    dump xgmac regs \ ``mac_drv``\ : mac driver \ ``cmd``\ :ethtool cmd \ ``data``\ :data for value of regs

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`hns_xgmac_get_stats`:

hns_xgmac_get_stats
===================

.. c:function:: void hns_xgmac_get_stats(void *mac_drv, u64 *data)

    get xgmac statistic \ ``mac_drv``\ : mac driver \ ``data``\ :data for value of stats regs

    :param mac_drv:
        *undescribed*
    :type mac_drv: void \*

    :param data:
        *undescribed*
    :type data: u64 \*

.. _`hns_xgmac_get_strings`:

hns_xgmac_get_strings
=====================

.. c:function:: void hns_xgmac_get_strings(u32 stringset, u8 *data)

    get xgmac strings name \ ``stringset``\ : type of values in data \ ``data``\ :data for value of string name

    :param stringset:
        *undescribed*
    :type stringset: u32

    :param data:
        *undescribed*
    :type data: u8 \*

.. _`hns_xgmac_get_sset_count`:

hns_xgmac_get_sset_count
========================

.. c:function:: int hns_xgmac_get_sset_count(int stringset)

    get xgmac string set count \ ``stringset``\ : type of values in data return xgmac string set count

    :param stringset:
        *undescribed*
    :type stringset: int

.. _`hns_xgmac_get_regs_count`:

hns_xgmac_get_regs_count
========================

.. c:function:: int hns_xgmac_get_regs_count( void)

    get xgmac regs count return xgmac regs count

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

