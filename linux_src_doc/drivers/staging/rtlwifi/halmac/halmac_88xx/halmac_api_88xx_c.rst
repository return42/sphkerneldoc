.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_88xx/halmac_api_88xx.c

.. _`halmac_init_adapter_para_88xx`:

halmac_init_adapter_para_88xx
=============================

.. c:function:: void halmac_init_adapter_para_88xx(struct halmac_adapter *halmac_adapter)

    int halmac adapter \ ``halmac_adapter``\ 

    :param halmac_adapter:
        *undescribed*
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_adapter_para_88xx.description`:

Description
-----------

SD1 internal use

Author : KaiYuan Chang/Ivan Lin
Return : void

.. _`halmac_init_adapter_dynamic_para_88xx`:

halmac_init_adapter_dynamic_para_88xx
=====================================

.. c:function:: void halmac_init_adapter_dynamic_para_88xx(struct halmac_adapter *halmac_adapter)

    int halmac adapter \ ``halmac_adapter``\ 

    :param halmac_adapter:
        *undescribed*
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_adapter_dynamic_para_88xx.description`:

Description
-----------

SD1 internal use

Author : KaiYuan Chang/Ivan Lin
Return : void

.. _`halmac_init_state_machine_88xx`:

halmac_init_state_machine_88xx
==============================

.. c:function:: void halmac_init_state_machine_88xx(struct halmac_adapter *halmac_adapter)

    init halmac software state machine \ ``halmac_adapter``\ 

    :param halmac_adapter:
        *undescribed*
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_state_machine_88xx.description`:

Description
-----------

SD1 internal use.

Author : KaiYuan Chang/Ivan Lin
Return : void

.. _`halmac_mount_api_88xx`:

halmac_mount_api_88xx
=====================

.. c:function:: enum halmac_ret_status halmac_mount_api_88xx(struct halmac_adapter *halmac_adapter)

    attach functions to function pointer \ ``halmac_adapter``\ 

    :param halmac_adapter:
        *undescribed*
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_mount_api_88xx.description`:

Description
-----------

SD1 internal use

Author : KaiYuan Chang/Ivan Lin
Return : enum halmac_ret_status

.. _`halmac_download_firmware_88xx`:

halmac_download_firmware_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_download_firmware_88xx(struct halmac_adapter *halmac_adapter, u8 *hamacl_fw, u32 halmac_fw_size)

    download Firmware

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param hamacl_fw:
        firmware bin
    :type hamacl_fw: u8 \*

    :param halmac_fw_size:
        firmware size
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_fw_size: u32

.. _`halmac_free_download_firmware_88xx`:

halmac_free_download_firmware_88xx
==================================

.. c:function:: enum halmac_ret_status halmac_free_download_firmware_88xx(struct halmac_adapter *halmac_adapter, enum halmac_dlfw_mem dlfw_mem, u8 *hamacl_fw, u32 halmac_fw_size)

    download specific memory firmware \ ``halmac_adapter``\ 

    :param halmac_adapter:
        *undescribed*
    :type halmac_adapter: struct halmac_adapter \*

    :param dlfw_mem:
        memory selection
    :type dlfw_mem: enum halmac_dlfw_mem

    :param hamacl_fw:
        firmware bin
    :type hamacl_fw: u8 \*

    :param halmac_fw_size:
        firmware size
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
    :type halmac_fw_size: u32

.. _`halmac_get_fw_version_88xx`:

halmac_get_fw_version_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_get_fw_version_88xx(struct halmac_adapter *halmac_adapter, struct halmac_fw_version *fw_version)

    get FW version

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param fw_version:
        fw version info
        Author : Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type fw_version: struct halmac_fw_version \*

.. _`halmac_cfg_mac_addr_88xx`:

halmac_cfg_mac_addr_88xx
========================

.. c:function:: enum halmac_ret_status halmac_cfg_mac_addr_88xx(struct halmac_adapter *halmac_adapter, u8 halmac_port, union halmac_wlan_addr *hal_address)

    config mac address

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_port:
        0 for port0, 1 for port1, 2 for port2, 3 for port3, 4 for port4
    :type halmac_port: u8

    :param hal_address:
        mac address
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type hal_address: union halmac_wlan_addr \*

.. _`halmac_cfg_bssid_88xx`:

halmac_cfg_bssid_88xx
=====================

.. c:function:: enum halmac_ret_status halmac_cfg_bssid_88xx(struct halmac_adapter *halmac_adapter, u8 halmac_port, union halmac_wlan_addr *hal_address)

    config BSSID

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_port:
        0 for port0, 1 for port1, 2 for port2, 3 for port3, 4 for port4
    :type halmac_port: u8

    :param hal_address:
        bssid
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type hal_address: union halmac_wlan_addr \*

.. _`halmac_cfg_multicast_addr_88xx`:

halmac_cfg_multicast_addr_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_cfg_multicast_addr_88xx(struct halmac_adapter *halmac_adapter, union halmac_wlan_addr *hal_address)

    config multicast address

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param hal_address:
        multicast address
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type hal_address: union halmac_wlan_addr \*

.. _`halmac_pre_init_system_cfg_88xx`:

halmac_pre_init_system_cfg_88xx
===============================

.. c:function:: enum halmac_ret_status halmac_pre_init_system_cfg_88xx(struct halmac_adapter *halmac_adapter)

    pre-init system config

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_system_cfg_88xx`:

halmac_init_system_cfg_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_init_system_cfg_88xx(struct halmac_adapter *halmac_adapter)

    init system config

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_edca_cfg_88xx`:

halmac_init_edca_cfg_88xx
=========================

.. c:function:: enum halmac_ret_status halmac_init_edca_cfg_88xx(struct halmac_adapter *halmac_adapter)

    init EDCA config

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_wmac_cfg_88xx`:

halmac_init_wmac_cfg_88xx
=========================

.. c:function:: enum halmac_ret_status halmac_init_wmac_cfg_88xx(struct halmac_adapter *halmac_adapter)

    init wmac config

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_init_mac_cfg_88xx`:

halmac_init_mac_cfg_88xx
========================

.. c:function:: enum halmac_ret_status halmac_init_mac_cfg_88xx(struct halmac_adapter *halmac_adapter, enum halmac_trx_mode mode)

    config page1~page7 register

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param mode:
        trx mode
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type mode: enum halmac_trx_mode

.. _`halmac_cfg_operation_mode_88xx`:

halmac_cfg_operation_mode_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_cfg_operation_mode_88xx(struct halmac_adapter *halmac_adapter, enum halmac_wireless_mode wireless_mode)

    config operation mode

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param wireless_mode:
        802.11 standard(b/g/n/ac)
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type wireless_mode: enum halmac_wireless_mode

.. _`halmac_cfg_ch_bw_88xx`:

halmac_cfg_ch_bw_88xx
=====================

.. c:function:: enum halmac_ret_status halmac_cfg_ch_bw_88xx(struct halmac_adapter *halmac_adapter, u8 channel, enum halmac_pri_ch_idx pri_ch_idx, enum halmac_bw bw)

    config channel & bandwidth

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param channel:
        WLAN channel, support 2.4G & 5G
    :type channel: u8

    :param pri_ch_idx:
        primary channel index, idx1, idx2, idx3, idx4
    :type pri_ch_idx: enum halmac_pri_ch_idx

    :param bw:
        band width, 20, 40, 80, 160, 5 ,10
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type bw: enum halmac_bw

.. _`halmac_cfg_bw_88xx`:

halmac_cfg_bw_88xx
==================

.. c:function:: enum halmac_ret_status halmac_cfg_bw_88xx(struct halmac_adapter *halmac_adapter, enum halmac_bw bw)

    config bandwidth

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param bw:
        band width, 20, 40, 80, 160, 5 ,10
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type bw: enum halmac_bw

.. _`halmac_dump_efuse_map_88xx`:

halmac_dump_efuse_map_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_dump_efuse_map_88xx(struct halmac_adapter *halmac_adapter, enum halmac_efuse_read_cfg cfg)

    dump "physical" efuse map

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param cfg:
        dump efuse method
        Author : Ivan Lin/KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type cfg: enum halmac_efuse_read_cfg

.. _`halmac_dump_efuse_map_bt_88xx`:

halmac_dump_efuse_map_bt_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_dump_efuse_map_bt_88xx(struct halmac_adapter *halmac_adapter, enum halmac_efuse_bank halmac_efuse_bank, u32 bt_efuse_map_size, u8 *bt_efuse_map)

    dump "BT physical" efuse map

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_efuse_bank:
        bt efuse bank
    :type halmac_efuse_bank: enum halmac_efuse_bank

    :param bt_efuse_map_size:
        bt efuse map size. get from halmac_get_efuse_size API
    :type bt_efuse_map_size: u32

    :param bt_efuse_map:
        bt efuse map
        Author : Soar / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type bt_efuse_map: u8 \*

.. _`halmac_write_efuse_bt_88xx`:

halmac_write_efuse_bt_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_write_efuse_bt_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u8 halmac_value, enum halmac_efuse_bank halmac_efuse_bank)

    write "BT physical" efuse offset

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        offset
    :type halmac_offset: u32

    :param halmac_value:
        Write value
    :type halmac_value: u8

    :param halmac_efuse_bank:
        *undescribed*
    :type halmac_efuse_bank: enum halmac_efuse_bank

.. _`halmac_get_efuse_available_size_88xx`:

halmac_get_efuse_available_size_88xx
====================================

.. c:function:: enum halmac_ret_status halmac_get_efuse_available_size_88xx(struct halmac_adapter *halmac_adapter, u32 *halmac_size)

    get efuse available size

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_size:
        physical efuse available size
        Author : Soar
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_size: u32 \*

.. _`halmac_get_efuse_size_88xx`:

halmac_get_efuse_size_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_get_efuse_size_88xx(struct halmac_adapter *halmac_adapter, u32 *halmac_size)

    get "physical" efuse size

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_size:
        physical efuse size
        Author : Ivan Lin/KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_size: u32 \*

.. _`halmac_get_logical_efuse_size_88xx`:

halmac_get_logical_efuse_size_88xx
==================================

.. c:function:: enum halmac_ret_status halmac_get_logical_efuse_size_88xx(struct halmac_adapter *halmac_adapter, u32 *halmac_size)

    get "logical" efuse size

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_size:
        logical efuse size
        Author : Ivan Lin/KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_size: u32 \*

.. _`halmac_dump_logical_efuse_map_88xx`:

halmac_dump_logical_efuse_map_88xx
==================================

.. c:function:: enum halmac_ret_status halmac_dump_logical_efuse_map_88xx(struct halmac_adapter *halmac_adapter, enum halmac_efuse_read_cfg cfg)

    dump "logical" efuse map

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param cfg:
        dump efuse method
        Author : Soar
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type cfg: enum halmac_efuse_read_cfg

.. _`halmac_read_logical_efuse_88xx`:

halmac_read_logical_efuse_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_read_logical_efuse_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u8 *value)

    read logical efuse map 1 byte

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        offset
    :type halmac_offset: u32

    :param value:
        1 byte efuse value
        Author : Soar
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type value: u8 \*

.. _`halmac_write_logical_efuse_88xx`:

halmac_write_logical_efuse_88xx
===============================

.. c:function:: enum halmac_ret_status halmac_write_logical_efuse_88xx(struct halmac_adapter *halmac_adapter, u32 halmac_offset, u8 halmac_value)

    write "logical" efuse offset

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_offset:
        offset
    :type halmac_offset: u32

    :param halmac_value:
        value
        Author : Soar
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_value: u8

.. _`halmac_pg_efuse_by_map_88xx`:

halmac_pg_efuse_by_map_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_pg_efuse_by_map_88xx(struct halmac_adapter *halmac_adapter, struct halmac_pg_efuse_info *pg_efuse_info, enum halmac_efuse_read_cfg cfg)

    pg logical efuse by map

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param pg_efuse_info:
        efuse map information
    :type pg_efuse_info: struct halmac_pg_efuse_info \*

    :param cfg:
        dump efuse method
        Author : Soar
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type cfg: enum halmac_efuse_read_cfg

.. _`halmac_get_c2h_info_88xx`:

halmac_get_c2h_info_88xx
========================

.. c:function:: enum halmac_ret_status halmac_get_c2h_info_88xx(struct halmac_adapter *halmac_adapter, u8 *halmac_buf, u32 halmac_size)

    process halmac C2H packet

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_buf:
        RX Packet pointer
    :type halmac_buf: u8 \*

    :param halmac_size:
        RX Packet size
        Author : KaiYuan Chang/Ivan Lin
    :type halmac_size: u32

.. _`halmac_get_c2h_info_88xx.description`:

Description
-----------

Used to process c2h packet info from RX path. After receiving the packet,
user need to call this api and pass the packet pointer.

Return : enum halmac_ret_status
More details of status code can be found in prototype document

.. _`halmac_debug_88xx`:

halmac_debug_88xx
=================

.. c:function:: enum halmac_ret_status halmac_debug_88xx(struct halmac_adapter *halmac_adapter)

    dump information for debugging

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_cfg_parameter_88xx`:

halmac_cfg_parameter_88xx
=========================

.. c:function:: enum halmac_ret_status halmac_cfg_parameter_88xx(struct halmac_adapter *halmac_adapter, struct halmac_phy_parameter_info *para_info, u8 full_fifo)

    config parameter by FW

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param para_info:
        cmd id, content
    :type para_info: struct halmac_phy_parameter_info \*

    :param full_fifo:
        parameter information
    :type full_fifo: u8

.. _`halmac_cfg_parameter_88xx.description`:

Description
-----------

If msk_en = true, the format of array is {reg_info, mask, value}.
If msk_en =_FAUSE, the format of array is {reg_info, value}
The format of reg_info is
reg_info[31]=rf_reg, 0: MAC_BB reg, 1: RF reg
reg_info[27:24]=rf_path, 0: path_A, 1: path_B
if rf_reg=0(MAC_BB reg), rf_path is meaningless.
ref_info[15:0]=offset

.. _`halmac_cfg_parameter_88xx.example`:

Example
-------

.. code-block:: c

    msk_en = false
    {0x8100000a, 0x00001122}
    =>Set RF register, path_B, offset 0xA to 0x00001122
    {0x00000824, 0x11224433}
    =>Set MAC_BB register, offset 0x800 to 0x11224433

    Note : full fifo mode only for init flow

    Author : KaiYuan Chang/Ivan Lin
    Return : enum halmac_ret_status
    More details of status code can be found in prototype document


.. _`halmac_update_packet_88xx`:

halmac_update_packet_88xx
=========================

.. c:function:: enum halmac_ret_status halmac_update_packet_88xx(struct halmac_adapter *halmac_adapter, enum halmac_packet_id pkt_id, u8 *pkt, u32 pkt_size)

    send specific packet to FW

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param pkt_id:
        packet id, to know the purpose of this packet
    :type pkt_id: enum halmac_packet_id

    :param pkt:
        packet
    :type pkt: u8 \*

    :param pkt_size:
        packet size
    :type pkt_size: u32

.. _`halmac_update_packet_88xx.description`:

Description
-----------

Note : TX_DESC is not included in the pkt

Author : KaiYuan Chang/Ivan Lin
Return : enum halmac_ret_status
More details of status code can be found in prototype document

.. _`halmac_cfg_drv_info_88xx`:

halmac_cfg_drv_info_88xx
========================

.. c:function:: enum halmac_ret_status halmac_cfg_drv_info_88xx(struct halmac_adapter *halmac_adapter, enum halmac_drv_info halmac_drv_info)

    config driver info

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_drv_info:
        driver information selection
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_drv_info: enum halmac_drv_info

.. _`halmac_fill_txdesc_check_sum_88xx`:

halmac_fill_txdesc_check_sum_88xx
=================================

.. c:function:: enum halmac_ret_status halmac_fill_txdesc_check_sum_88xx(struct halmac_adapter *halmac_adapter, u8 *cur_desc)

    fill in tx desc check sum

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param cur_desc:
        tx desc packet
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type cur_desc: u8 \*

.. _`halmac_dump_fifo_88xx`:

halmac_dump_fifo_88xx
=====================

.. c:function:: enum halmac_ret_status halmac_dump_fifo_88xx(struct halmac_adapter *halmac_adapter, enum hal_fifo_sel halmac_fifo_sel, u32 halmac_start_addr, u32 halmac_fifo_dump_size, u8 *fifo_map)

    dump fifo data

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_fifo_sel:
        FIFO selection
    :type halmac_fifo_sel: enum hal_fifo_sel

    :param halmac_start_addr:
        start address of selected FIFO
    :type halmac_start_addr: u32

    :param halmac_fifo_dump_size:
        dump size of selected FIFO
    :type halmac_fifo_dump_size: u32

    :param fifo_map:
        FIFO data
    :type fifo_map: u8 \*

.. _`halmac_dump_fifo_88xx.description`:

Description
-----------

Note : before dump fifo, user need to call halmac_get_fifo_size to
get fifo size. Then input this size to halmac_dump_fifo.

Author : Ivan Lin/KaiYuan Chang
Return : enum halmac_ret_status
More details of status code can be found in prototype document

.. _`halmac_get_fifo_size_88xx`:

halmac_get_fifo_size_88xx
=========================

.. c:function:: u32 halmac_get_fifo_size_88xx(struct halmac_adapter *halmac_adapter, enum hal_fifo_sel halmac_fifo_sel)

    get fifo size

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_fifo_sel:
        FIFO selection
        Author : Ivan Lin/KaiYuan Chang
        Return : u32
        More details of status code can be found in prototype document
    :type halmac_fifo_sel: enum hal_fifo_sel

.. _`halmac_cfg_txbf_88xx`:

halmac_cfg_txbf_88xx
====================

.. c:function:: enum halmac_ret_status halmac_cfg_txbf_88xx(struct halmac_adapter *halmac_adapter, u8 userid, enum halmac_bw bw, u8 txbf_en)

    enable/disable specific user's txbf

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param userid:
        su bfee userid = 0 or 1 to apply TXBF
    :type userid: u8

    :param bw:
        the sounding bandwidth
    :type bw: enum halmac_bw

    :param txbf_en:
        0: disable TXBF, 1: enable TXBF
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type txbf_en: u8

.. _`halmac_cfg_mumimo_88xx`:

halmac_cfg_mumimo_88xx
======================

.. c:function:: enum halmac_ret_status halmac_cfg_mumimo_88xx(struct halmac_adapter *halmac_adapter, struct halmac_cfg_mumimo_para *cfgmu)

    config mumimo

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param cfgmu:
        parameters to configure MU PPDU Tx/Rx
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type cfgmu: struct halmac_cfg_mumimo_para \*

.. _`halmac_cfg_sounding_88xx`:

halmac_cfg_sounding_88xx
========================

.. c:function:: enum halmac_ret_status halmac_cfg_sounding_88xx(struct halmac_adapter *halmac_adapter, enum halmac_snd_role role, enum halmac_data_rate datarate)

    configure general sounding

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param role:
        driver's role, BFer or BFee
    :type role: enum halmac_snd_role

    :param datarate:
        set ndpa tx rate if driver is BFer, or set csi response rate
        if driver is BFee
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type datarate: enum halmac_data_rate

.. _`halmac_del_sounding_88xx`:

halmac_del_sounding_88xx
========================

.. c:function:: enum halmac_ret_status halmac_del_sounding_88xx(struct halmac_adapter *halmac_adapter, enum halmac_snd_role role)

    reset general sounding

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param role:
        driver's role, BFer or BFee
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type role: enum halmac_snd_role

.. _`halmac_su_bfee_entry_init_88xx`:

halmac_su_bfee_entry_init_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_su_bfee_entry_init_88xx(struct halmac_adapter *halmac_adapter, u8 userid, u16 paid)

    config SU beamformee's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param userid:
        SU bfee userid = 0 or 1 to be added
    :type userid: u8

    :param paid:
        partial AID of this bfee
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type paid: u16

.. _`halmac_su_bfer_entry_init_88xx`:

halmac_su_bfer_entry_init_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_su_bfer_entry_init_88xx(struct halmac_adapter *halmac_adapter, struct halmac_su_bfer_init_para *su_bfer_init)

    config SU beamformer's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param su_bfer_init:
        parameters to configure SU BFER entry
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type su_bfer_init: struct halmac_su_bfer_init_para \*

.. _`halmac_mu_bfee_entry_init_88xx`:

halmac_mu_bfee_entry_init_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_mu_bfee_entry_init_88xx(struct halmac_adapter *halmac_adapter, struct halmac_mu_bfee_init_para *mu_bfee_init)

    config MU beamformee's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param mu_bfee_init:
        parameters to configure MU BFEE entry
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type mu_bfee_init: struct halmac_mu_bfee_init_para \*

.. _`halmac_mu_bfer_entry_init_88xx`:

halmac_mu_bfer_entry_init_88xx
==============================

.. c:function:: enum halmac_ret_status halmac_mu_bfer_entry_init_88xx(struct halmac_adapter *halmac_adapter, struct halmac_mu_bfer_init_para *mu_bfer_init)

    config MU beamformer's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param mu_bfer_init:
        parameters to configure MU BFER entry
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type mu_bfer_init: struct halmac_mu_bfer_init_para \*

.. _`halmac_su_bfee_entry_del_88xx`:

halmac_su_bfee_entry_del_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_su_bfee_entry_del_88xx(struct halmac_adapter *halmac_adapter, u8 userid)

    reset SU beamformee's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param userid:
        the SU BFee userid to be deleted
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type userid: u8

.. _`halmac_su_bfer_entry_del_88xx`:

halmac_su_bfer_entry_del_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_su_bfer_entry_del_88xx(struct halmac_adapter *halmac_adapter, u8 userid)

    reset SU beamformer's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param userid:
        the SU BFer userid to be deleted
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type userid: u8

.. _`halmac_mu_bfee_entry_del_88xx`:

halmac_mu_bfee_entry_del_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_mu_bfee_entry_del_88xx(struct halmac_adapter *halmac_adapter, u8 userid)

    reset MU beamformee's registers

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param userid:
        the MU STA userid to be deleted
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type userid: u8

.. _`halmac_mu_bfer_entry_del_88xx`:

halmac_mu_bfer_entry_del_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_mu_bfer_entry_del_88xx(struct halmac_adapter *halmac_adapter)

    reset MU beamformer's registers

    :param halmac_adapter:
        the adapter of halmac
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_add_ch_info_88xx`:

halmac_add_ch_info_88xx
=======================

.. c:function:: enum halmac_ret_status halmac_add_ch_info_88xx(struct halmac_adapter *halmac_adapter, struct halmac_ch_info *ch_info)

    add channel information

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param ch_info:
        channel information
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type ch_info: struct halmac_ch_info \*

.. _`halmac_add_extra_ch_info_88xx`:

halmac_add_extra_ch_info_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_add_extra_ch_info_88xx(struct halmac_adapter *halmac_adapter, struct halmac_ch_extra_info *ch_extra_info)

    add extra channel information

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param ch_extra_info:
        extra channel information
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type ch_extra_info: struct halmac_ch_extra_info \*

.. _`halmac_ctrl_ch_switch_88xx`:

halmac_ctrl_ch_switch_88xx
==========================

.. c:function:: enum halmac_ret_status halmac_ctrl_ch_switch_88xx(struct halmac_adapter *halmac_adapter, struct halmac_ch_switch_option *cs_option)

    send channel switch cmd

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param cs_option:
        channel switch config
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type cs_option: struct halmac_ch_switch_option \*

.. _`halmac_clear_ch_info_88xx`:

halmac_clear_ch_info_88xx
=========================

.. c:function:: enum halmac_ret_status halmac_clear_ch_info_88xx(struct halmac_adapter *halmac_adapter)

    clear channel information

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_send_general_info_88xx`:

halmac_send_general_info_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_send_general_info_88xx(struct halmac_adapter *halmac_adapter, struct halmac_general_info *general_info)

    send general information to FW

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param general_info:
        general information
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type general_info: struct halmac_general_info \*

.. _`halmac_start_iqk_88xx`:

halmac_start_iqk_88xx
=====================

.. c:function:: enum halmac_ret_status halmac_start_iqk_88xx(struct halmac_adapter *halmac_adapter, struct halmac_iqk_para_ *iqk_para)

    trigger FW IQK

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param iqk_para:
        IQK parameter
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type iqk_para: struct halmac_iqk_para_ \*

.. _`halmac_ctrl_pwr_tracking_88xx`:

halmac_ctrl_pwr_tracking_88xx
=============================

.. c:function:: enum halmac_ret_status halmac_ctrl_pwr_tracking_88xx(struct halmac_adapter *halmac_adapter, struct halmac_pwr_tracking_option *pwr_tracking_opt)

    trigger FW power tracking

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param pwr_tracking_opt:
        power tracking option
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type pwr_tracking_opt: struct halmac_pwr_tracking_option \*

.. _`halmac_query_status_88xx`:

halmac_query_status_88xx
========================

.. c:function:: enum halmac_ret_status halmac_query_status_88xx(struct halmac_adapter *halmac_adapter, enum halmac_feature_id feature_id, enum halmac_cmd_process_status *process_status, u8 *data, u32 *size)

    query the offload feature status

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param feature_id:
        feature_id
    :type feature_id: enum halmac_feature_id

    :param process_status:
        feature_status
    :type process_status: enum halmac_cmd_process_status \*

    :param data:
        data buffer
    :type data: u8 \*

    :param size:
        data size
    :type size: u32 \*

.. _`halmac_query_status_88xx.description`:

Description
-----------

Note :
If user wants to know the data size, use can allocate zero
size buffer first. If this size less than the data size, halmac
will return  HALMAC_RET_BUFFER_TOO_SMALL. User need to
re-allocate data buffer with correct data size.

Author : Ivan Lin/KaiYuan Chang
Return : enum halmac_ret_status
More details of status code can be found in prototype document

.. _`halmac_reset_feature_88xx`:

halmac_reset_feature_88xx
=========================

.. c:function:: enum halmac_ret_status halmac_reset_feature_88xx(struct halmac_adapter *halmac_adapter, enum halmac_feature_id feature_id)

    reset async api cmd status

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param feature_id:
        feature_id
        Author : Ivan Lin/KaiYuan Chang
        Return : enum halmac_ret_status.
        More details of status code can be found in prototype document
    :type feature_id: enum halmac_feature_id

.. _`halmac_check_fw_status_88xx`:

halmac_check_fw_status_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_check_fw_status_88xx(struct halmac_adapter *halmac_adapter, bool *fw_status)

    check fw status

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param fw_status:
        fw status
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type fw_status: bool \*

.. _`halmac_cfg_max_dl_size_88xx`:

halmac_cfg_max_dl_size_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_cfg_max_dl_size_88xx(struct halmac_adapter *halmac_adapter, u32 size)

    config max download FW size

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param size:
        max download fw size
    :type size: u32

.. _`halmac_cfg_max_dl_size_88xx.description`:

Description
-----------

Halmac uses this setting to set max packet size for
download FW.
If user has not called this API, halmac use default
setting for download FW
Note1 : size need multiple of 2
Note2 : max size is 31K

Author : Ivan Lin/KaiYuan Chang
Return : enum halmac_ret_status
More details of status code can be found in prototype document

.. _`halmac_psd_88xx`:

halmac_psd_88xx
===============

.. c:function:: enum halmac_ret_status halmac_psd_88xx(struct halmac_adapter *halmac_adapter, u16 start_psd, u16 end_psd)

    trigger fw psd

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param start_psd:
        start PSD
    :type start_psd: u16

    :param end_psd:
        end PSD
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type end_psd: u16

.. _`halmac_cfg_la_mode_88xx`:

halmac_cfg_la_mode_88xx
=======================

.. c:function:: enum halmac_ret_status halmac_cfg_la_mode_88xx(struct halmac_adapter *halmac_adapter, enum halmac_la_mode la_mode)

    config la mode

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param la_mode:
        disable : no TXFF space reserved for LA debug
        partial : partial TXFF space is reserved for LA debug
        full : all TXFF space is reserved for LA debug
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type la_mode: enum halmac_la_mode

.. _`halmac_cfg_rx_fifo_expanding_mode_88xx`:

halmac_cfg_rx_fifo_expanding_mode_88xx
======================================

.. c:function:: enum halmac_ret_status halmac_cfg_rx_fifo_expanding_mode_88xx(struct halmac_adapter *halmac_adapter, enum halmac_rx_fifo_expanding_mode rx_fifo_expanding_mode)

    rx fifo expanding

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param rx_fifo_expanding_mode:
        *undescribed*
    :type rx_fifo_expanding_mode: enum halmac_rx_fifo_expanding_mode

.. _`halmac_get_hw_value_88xx`:

halmac_get_hw_value_88xx
========================

.. c:function:: enum halmac_ret_status halmac_get_hw_value_88xx(struct halmac_adapter *halmac_adapter, enum halmac_hw_id hw_id, void *pvalue)

    get hw config value

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param hw_id:
        hw id for driver to query
    :type hw_id: enum halmac_hw_id

    :param pvalue:
        hw value, reference table to get data type
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type pvalue: void \*

.. _`halmac_set_hw_value_88xx`:

halmac_set_hw_value_88xx
========================

.. c:function:: enum halmac_ret_status halmac_set_hw_value_88xx(struct halmac_adapter *halmac_adapter, enum halmac_hw_id hw_id, void *pvalue)

    set hw config value

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param hw_id:
        hw id for driver to config
    :type hw_id: enum halmac_hw_id

    :param pvalue:
        hw value, reference table to get data type
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type pvalue: void \*

.. _`halmac_cfg_drv_rsvd_pg_num_88xx`:

halmac_cfg_drv_rsvd_pg_num_88xx
===============================

.. c:function:: enum halmac_ret_status halmac_cfg_drv_rsvd_pg_num_88xx(struct halmac_adapter *halmac_adapter, enum halmac_drv_rsvd_pg_num pg_num)

    config reserved page number for driver

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param pg_num:
        page number
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type pg_num: enum halmac_drv_rsvd_pg_num

.. _`halmac_chk_txdesc_88xx`:

halmac_chk_txdesc_88xx
======================

.. c:function:: enum halmac_ret_status halmac_chk_txdesc_88xx(struct halmac_adapter *halmac_adapter, u8 *halmac_buf, u32 halmac_size)

    check if the tx packet format is incorrect

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param halmac_buf:
        tx Packet buffer, tx desc is included
    :type halmac_buf: u8 \*

    :param halmac_size:
        tx packet size
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_size: u32

.. _`halmac_dl_drv_rsvd_page_88xx`:

halmac_dl_drv_rsvd_page_88xx
============================

.. c:function:: enum halmac_ret_status halmac_dl_drv_rsvd_page_88xx(struct halmac_adapter *halmac_adapter, u8 pg_offset, u8 *halmac_buf, u32 halmac_size)

    download packet to rsvd page

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param pg_offset:
        page offset of driver's rsvd page
    :type pg_offset: u8

    :param halmac_buf:
        data to be downloaded, tx_desc is not included
    :type halmac_buf: u8 \*

    :param halmac_size:
        data size to be downloaded
        Author : KaiYuan Chang
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_size: u32

.. _`halmac_cfg_csi_rate_88xx`:

halmac_cfg_csi_rate_88xx
========================

.. c:function:: enum halmac_ret_status halmac_cfg_csi_rate_88xx(struct halmac_adapter *halmac_adapter, u8 rssi, u8 current_rate, u8 fixrate_en, u8 *new_rate)

    config CSI frame Tx rate

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param rssi:
        rssi in decimal value
    :type rssi: u8

    :param current_rate:
        current CSI frame rate
    :type current_rate: u8

    :param fixrate_en:
        enable to fix CSI frame in VHT rate, otherwise legacy OFDM rate
    :type fixrate_en: u8

    :param new_rate:
        API returns the final CSI frame rate
        Author : chunchu
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type new_rate: u8 \*

.. _`halmac_sdio_cmd53_4byte_88xx`:

halmac_sdio_cmd53_4byte_88xx
============================

.. c:function:: enum halmac_ret_status halmac_sdio_cmd53_4byte_88xx(struct halmac_adapter *halmac_adapter, enum halmac_sdio_cmd53_4byte_mode cmd53_4byte_mode)

    cmd53 only for 4byte len register IO

    :param halmac_adapter:
        the adapter of halmac
    :type halmac_adapter: struct halmac_adapter \*

    :param cmd53_4byte_mode:
        *undescribed*
    :type cmd53_4byte_mode: enum halmac_sdio_cmd53_4byte_mode

.. _`halmac_txfifo_is_empty_88xx`:

halmac_txfifo_is_empty_88xx
===========================

.. c:function:: enum halmac_ret_status halmac_txfifo_is_empty_88xx(struct halmac_adapter *halmac_adapter, u32 chk_num)

    check if txfifo is empty

    :param halmac_adapter:
        the adapter of halmac
        Author : Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

    :param chk_num:
        *undescribed*
    :type chk_num: u32

.. This file was automatic generated / don't edit.

