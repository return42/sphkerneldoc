.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_88xx/halmac_api_88xx_usb.c

.. _`halmac_init_usb_cfg_88xx`:

halmac_init_usb_cfg_88xx
========================

.. c:function:: enum halmac_ret_status halmac_init_usb_cfg_88xx(struct halmac_adapter *halmac_adapter)

    init USB

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_deinit_usb_cfg_88xx`:

halmac_deinit_usb_cfg_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_deinit_usb_cfg_88xx(struct halmac_adapter *halmac_adapter)

    deinit USB

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_cfg_rx_aggregation_88xx_usb`:

halmac_cfg_rx_aggregation_88xx_usb
==================================

.. c:function:: enum halmac_ret_status halmac_cfg_rx_aggregation_88xx_usb(struct halmac_adapter *halmac_adapter, struct halmac_rxagg_cfg *phalmac_rxagg_cfg)

    config rx aggregation

    :param halmac_adapter:
        the adapter of halmac
        \ ``halmac_rx_agg_mode``\ 
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

    :param phalmac_rxagg_cfg:
        *undescribed*
    :type phalmac_rxagg_cfg: struct halmac_rxagg_cfg \*

.. _`halmac_reg_read_8_usb_88xx`:

halmac_reg_read_8_usb_88xx
==========================

.. c:function:: u8 halmac_reg_read_8_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset)

    read 1byte register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        register offset
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_offset: u32

.. _`halmac_reg_write_8_usb_88xx`:

halmac_reg_write_8_usb_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_reg_write_8_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u8 halmac_data)

    write 1byte register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        register offset
    :type halmac_offset: u32

    :param halmac_data:
        register value
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_data: u8

.. _`halmac_reg_read_16_usb_88xx`:

halmac_reg_read_16_usb_88xx
===========================

.. c:function:: u16 halmac_reg_read_16_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset)

    read 2byte register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        register offset
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_offset: u32

.. _`halmac_reg_write_16_usb_88xx`:

halmac_reg_write_16_usb_88xx
============================

.. c:function:: enum halmac_ret_status halmac_reg_write_16_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u16 halmac_data)

    write 2byte register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        register offset
    :type halmac_offset: u32

    :param halmac_data:
        register value
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_data: u16

.. _`halmac_reg_read_32_usb_88xx`:

halmac_reg_read_32_usb_88xx
===========================

.. c:function:: u32 halmac_reg_read_32_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset)

    read 4byte register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        register offset
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_offset: u32

.. _`halmac_reg_write_32_usb_88xx`:

halmac_reg_write_32_usb_88xx
============================

.. c:function:: enum halmac_ret_status halmac_reg_write_32_usb_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u32 halmac_data)

    write 4byte register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        register offset
    :type halmac_offset: u32

    :param halmac_data:
        register value
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_data: u32

.. _`halmac_set_bulkout_num_88xx`:

halmac_set_bulkout_num_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_set_bulkout_num_88xx(struct halmac_adapter *halmac_adapter, u8 bulkout_num)

    inform bulk-out num

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param bulkout_num:
        usb bulk-out number
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type bulkout_num: u8

.. _`halmac_get_usb_bulkout_id_88xx`:

halmac_get_usb_bulkout_id_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_get_usb_bulkout_id_88xx(struct halmac_adapter *halmac_adapter, u8 *halmac_buf, u32 halmac_size, u8 *bulkout_id)

    get bulk out id for the TX packet

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_buf:
        tx packet, include txdesc
    :type halmac_buf: u8 \*

    :param halmac_size:
        tx packet size
    :type halmac_size: u32

    :param bulkout_id:
        usb bulk-out id
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type bulkout_id: u8 \*

.. _`halmac_cfg_tx_agg_align_usb_not_support_88xx`:

halmac_cfg_tx_agg_align_usb_not_support_88xx
============================================

.. c:function:: enum halmac_ret_status halmac_cfg_tx_agg_align_usb_not_support_88xx(struct halmac_adapter *halmac_adapter, u8 enable, u16 align_size)

    config sdio bus tx agg alignment

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param enable:
        function enable(1)/disable(0)
    :type enable: u8

    :param align_size:
        sdio bus tx agg alignment size (2^n, n = 3~11)
        Author : Soar Tu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type align_size: u16

.. This file was automatic generated / don't edit.

