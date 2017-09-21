.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_88xx/halmac_api_88xx_usb.c

.. _`halmac_init_usb_cfg_88xx`:

halmac_init_usb_cfg_88xx
========================

.. c:function:: enum halmac_ret_status halmac_init_usb_cfg_88xx(struct halmac_adapter *halmac_adapter)

    init USB

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_deinit_usb_cfg_88xx`:

halmac_deinit_usb_cfg_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_deinit_usb_cfg_88xx(struct halmac_adapter *halmac_adapter)

    deinit USB

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_cfg_rx_aggregation_88xx_usb`:

halmac_cfg_rx_aggregation_88xx_usb
==================================

.. c:function:: enum halmac_ret_status halmac_cfg_rx_aggregation_88xx_usb(struct halmac_adapter *halmac_adapter, struct halmac_rxagg_cfg *phalmac_rxagg_cfg)

    config rx aggregation

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        \ ``halmac_rx_agg_mode``\ 
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

    :param struct halmac_rxagg_cfg \*phalmac_rxagg_cfg:
        *undescribed*

.. _`halmac_reg_read_8_usb_88xx`:

halmac_reg_read_8_usb_88xx
==========================

.. c:function:: u8 halmac_reg_read_8_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset)

    read 1byte register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u32 halmac_offset:
        register offset
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_reg_write_8_usb_88xx`:

halmac_reg_write_8_usb_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_reg_write_8_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u8 halmac_data)

    write 1byte register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u32 halmac_offset:
        register offset

    :param u8 halmac_data:
        register value
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_reg_read_16_usb_88xx`:

halmac_reg_read_16_usb_88xx
===========================

.. c:function:: u16 halmac_reg_read_16_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset)

    read 2byte register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u32 halmac_offset:
        register offset
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_reg_write_16_usb_88xx`:

halmac_reg_write_16_usb_88xx
============================

.. c:function:: enum halmac_ret_status halmac_reg_write_16_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u16 halmac_data)

    write 2byte register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u32 halmac_offset:
        register offset

    :param u16 halmac_data:
        register value
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_reg_read_32_usb_88xx`:

halmac_reg_read_32_usb_88xx
===========================

.. c:function:: u32 halmac_reg_read_32_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset)

    read 4byte register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u32 halmac_offset:
        register offset
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_reg_write_32_usb_88xx`:

halmac_reg_write_32_usb_88xx
============================

.. c:function:: enum halmac_ret_status halmac_reg_write_32_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u32 halmac_data)

    write 4byte register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u32 halmac_offset:
        register offset

    :param u32 halmac_data:
        register value
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_set_bulkout_num_88xx`:

halmac_set_bulkout_num_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_set_bulkout_num_88xx(struct halmac_adapter *halmac_adapter, u8 bulkout_num)

    inform bulk-out num

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u8 bulkout_num:
        usb bulk-out number
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_get_usb_bulkout_id_88xx`:

halmac_get_usb_bulkout_id_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_get_usb_bulkout_id_88xx(struct halmac_adapter *halmac_adapter, u8 *halmac_buf, u32 halmac_size, u8 *bulkout_id)

    get bulk out id for the TX packet

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u8 \*halmac_buf:
        tx packet, include txdesc

    :param u32 halmac_size:
        tx packet size

    :param u8 \*bulkout_id:
        usb bulk-out id
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_cfg_tx_agg_align_usb_not_support_88xx`:

halmac_cfg_tx_agg_align_usb_not_support_88xx
============================================

.. c:function:: enum halmac_ret_status halmac_cfg_tx_agg_align_usb_not_support_88xx(struct halmac_adapter *halmac_adapter, u8 enable, u16 align_size)

    config sdio bus tx agg alignment

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param u8 enable:
        function enable(1)/disable(0)

    :param u16 align_size:
        sdio bus tx agg alignment size (2^n, n = 3~11)
        Author : Soar Tu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. This file was automatic generated / don't edit.

