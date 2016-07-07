.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_xgmac.c

.. _`hns_xgmac_tx_enable`:

hns_xgmac_tx_enable
===================

.. c:function:: void hns_xgmac_tx_enable(struct mac_driver *drv, u32 value)

    xgmac port tx enable \ ``drv``\ : mac driver \ ``value``\ : value of enable

    :param struct mac_driver \*drv:
        *undescribed*

    :param u32 value:
        *undescribed*

.. _`hns_xgmac_rx_enable`:

hns_xgmac_rx_enable
===================

.. c:function:: void hns_xgmac_rx_enable(struct mac_driver *drv, u32 value)

    xgmac port rx enable \ ``drv``\ : mac driver \ ``value``\ : value of enable

    :param struct mac_driver \*drv:
        *undescribed*

    :param u32 value:
        *undescribed*

.. _`hns_xgmac_enable`:

hns_xgmac_enable
================

.. c:function:: void hns_xgmac_enable(void *mac_drv, enum mac_commom_mode mode)

    enable xgmac port \ ``drv``\ : mac driver \ ``mode``\ : mode of mac port

    :param void \*mac_drv:
        *undescribed*

    :param enum mac_commom_mode mode:
        *undescribed*

.. _`hns_xgmac_disable`:

hns_xgmac_disable
=================

.. c:function:: void hns_xgmac_disable(void *mac_drv, enum mac_commom_mode mode)

    disable xgmac port \ ``mac_drv``\ : mac driver \ ``mode``\ : mode of mac port

    :param void \*mac_drv:
        *undescribed*

    :param enum mac_commom_mode mode:
        *undescribed*

.. _`hns_xgmac_pma_fec_enable`:

hns_xgmac_pma_fec_enable
========================

.. c:function:: void hns_xgmac_pma_fec_enable(struct mac_driver *drv, u32 tx_value, u32 rx_value)

    xgmac PMA FEC enable \ ``drv``\ : mac driver \ ``tx_value``\ : tx value \ ``rx_value``\ : rx value return status

    :param struct mac_driver \*drv:
        *undescribed*

    :param u32 tx_value:
        *undescribed*

    :param u32 rx_value:
        *undescribed*

.. _`hns_xgmac_init`:

hns_xgmac_init
==============

.. c:function:: void hns_xgmac_init(void *mac_drv)

    initialize XGE \ ``mac_drv``\ : mac driver

    :param void \*mac_drv:
        *undescribed*

.. _`hns_xgmac_config_pad_and_crc`:

hns_xgmac_config_pad_and_crc
============================

.. c:function:: void hns_xgmac_config_pad_and_crc(void *mac_drv, u8 newval)

    set xgmac pad and crc enable the same time \ ``mac_drv``\ : mac driver \ ``newval``\ :enable of pad and crc

    :param void \*mac_drv:
        *undescribed*

    :param u8 newval:
        *undescribed*

.. _`hns_xgmac_pausefrm_cfg`:

hns_xgmac_pausefrm_cfg
======================

.. c:function:: void hns_xgmac_pausefrm_cfg(void *mac_drv, u32 rx_en, u32 tx_en)

    set pause param about xgmac \ ``mac_drv``\ : mac driver \ ``newval``\ :enable of pad and crc

    :param void \*mac_drv:
        *undescribed*

    :param u32 rx_en:
        *undescribed*

    :param u32 tx_en:
        *undescribed*

.. _`hns_xgmac_set_rx_ignore_pause_frames`:

hns_xgmac_set_rx_ignore_pause_frames
====================================

.. c:function:: void hns_xgmac_set_rx_ignore_pause_frames(void *mac_drv, u32 enable)

    set rx pause param about xgmac \ ``mac_drv``\ : mac driver \ ``enable``\ :enable rx pause param

    :param void \*mac_drv:
        *undescribed*

    :param u32 enable:
        *undescribed*

.. _`hns_xgmac_set_tx_auto_pause_frames`:

hns_xgmac_set_tx_auto_pause_frames
==================================

.. c:function:: void hns_xgmac_set_tx_auto_pause_frames(void *mac_drv, u16 enable)

    set tx pause param about xgmac \ ``mac_drv``\ : mac driver \ ``enable``\ :enable tx pause param

    :param void \*mac_drv:
        *undescribed*

    :param u16 enable:
        *undescribed*

.. _`hns_xgmac_get_id`:

hns_xgmac_get_id
================

.. c:function:: void hns_xgmac_get_id(void *mac_drv, u8 *mac_id)

    get xgmac port id \ ``mac_drv``\ : mac driver \ ``newval``\ :xgmac max frame length

    :param void \*mac_drv:
        *undescribed*

    :param u8 \*mac_id:
        *undescribed*

.. _`hns_xgmac_config_max_frame_length`:

hns_xgmac_config_max_frame_length
=================================

.. c:function:: void hns_xgmac_config_max_frame_length(void *mac_drv, u16 newval)

    set xgmac max frame length \ ``mac_drv``\ : mac driver \ ``newval``\ :xgmac max frame length

    :param void \*mac_drv:
        *undescribed*

    :param u16 newval:
        *undescribed*

.. _`hns_xgmac_free`:

hns_xgmac_free
==============

.. c:function:: void hns_xgmac_free(void *mac_drv)

    free xgmac driver \ ``mac_drv``\ : mac driver

    :param void \*mac_drv:
        *undescribed*

.. _`hns_xgmac_get_info`:

hns_xgmac_get_info
==================

.. c:function:: void hns_xgmac_get_info(void *mac_drv, struct mac_info *mac_info)

    get xgmac information \ ``mac_drv``\ : mac driver \ ``mac_info``\ :mac information

    :param void \*mac_drv:
        *undescribed*

    :param struct mac_info \*mac_info:
        *undescribed*

.. _`hns_xgmac_get_pausefrm_cfg`:

hns_xgmac_get_pausefrm_cfg
==========================

.. c:function:: void hns_xgmac_get_pausefrm_cfg(void *mac_drv, u32 *rx_en, u32 *tx_en)

    get xgmac pause param \ ``mac_drv``\ : mac driver \ ``rx_en``\ :xgmac rx pause enable \ ``tx_en``\ :xgmac tx pause enable

    :param void \*mac_drv:
        *undescribed*

    :param u32 \*rx_en:
        *undescribed*

    :param u32 \*tx_en:
        *undescribed*

.. _`hns_xgmac_get_link_status`:

hns_xgmac_get_link_status
=========================

.. c:function:: void hns_xgmac_get_link_status(void *mac_drv, u32 *link_stat)

    get xgmac link status \ ``mac_drv``\ : mac driver \ ``link_stat``\ : xgmac link stat

    :param void \*mac_drv:
        *undescribed*

    :param u32 \*link_stat:
        *undescribed*

.. _`hns_xgmac_get_regs`:

hns_xgmac_get_regs
==================

.. c:function:: void hns_xgmac_get_regs(void *mac_drv, void *data)

    dump xgmac regs \ ``mac_drv``\ : mac driver \ ``cmd``\ :ethtool cmd \ ``data``\ :data for value of regs

    :param void \*mac_drv:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`hns_xgmac_get_stats`:

hns_xgmac_get_stats
===================

.. c:function:: void hns_xgmac_get_stats(void *mac_drv, u64 *data)

    get xgmac statistic \ ``mac_drv``\ : mac driver \ ``data``\ :data for value of stats regs

    :param void \*mac_drv:
        *undescribed*

    :param u64 \*data:
        *undescribed*

.. _`hns_xgmac_get_strings`:

hns_xgmac_get_strings
=====================

.. c:function:: void hns_xgmac_get_strings(u32 stringset, u8 *data)

    get xgmac strings name \ ``stringset``\ : type of values in data \ ``data``\ :data for value of string name

    :param u32 stringset:
        *undescribed*

    :param u8 \*data:
        *undescribed*

.. _`hns_xgmac_get_sset_count`:

hns_xgmac_get_sset_count
========================

.. c:function:: int hns_xgmac_get_sset_count(int stringset)

    get xgmac string set count \ ``stringset``\ : type of values in data return xgmac string set count

    :param int stringset:
        *undescribed*

.. _`hns_xgmac_get_regs_count`:

hns_xgmac_get_regs_count
========================

.. c:function:: int hns_xgmac_get_regs_count( void)

    get xgmac regs count return xgmac regs count

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

