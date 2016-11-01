.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_main.c

.. _`hns_dsaf_sbm_link_sram_init_en`:

hns_dsaf_sbm_link_sram_init_en
==============================

.. c:function:: void hns_dsaf_sbm_link_sram_init_en(struct dsaf_device *dsaf_dev)

    config dsaf_sbm_init_en

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_reg_cnt_clr_ce`:

hns_dsaf_reg_cnt_clr_ce
=======================

.. c:function:: void hns_dsaf_reg_cnt_clr_ce(struct dsaf_device *dsaf_dev, u32 reg_cnt_clr_ce)

    config hns_dsaf_reg_cnt_clr_ce

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 reg_cnt_clr_ce:
        *undescribed*

.. _`hns_dsaf_ppe_qid_cfg`:

hns_dsaf_ppe_qid_cfg
====================

.. c:function:: void hns_dsaf_ppe_qid_cfg(struct dsaf_device *dsaf_dev, u32 qid_cfg)

    config ppe qid

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 qid_cfg:
        *undescribed*

.. _`hns_dsaf_sw_port_type_cfg`:

hns_dsaf_sw_port_type_cfg
=========================

.. c:function:: void hns_dsaf_sw_port_type_cfg(struct dsaf_device *dsaf_dev, enum dsaf_sw_port_type port_type)

    cfg sw type

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param enum dsaf_sw_port_type port_type:
        *undescribed*

.. _`hns_dsaf_stp_port_type_cfg`:

hns_dsaf_stp_port_type_cfg
==========================

.. c:function:: void hns_dsaf_stp_port_type_cfg(struct dsaf_device *dsaf_dev, enum dsaf_stp_port_type port_type)

    cfg stp type

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param enum dsaf_stp_port_type port_type:
        *undescribed*

.. _`hns_dsaf_sbm_cfg`:

hns_dsaf_sbm_cfg
================

.. c:function:: void hns_dsaf_sbm_cfg(struct dsaf_device *dsaf_dev)

    config sbm

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_sbm_cfg_mib_en`:

hns_dsaf_sbm_cfg_mib_en
=======================

.. c:function:: int hns_dsaf_sbm_cfg_mib_en(struct dsaf_device *dsaf_dev)

    config sbm

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_sbm_bp_wl_cfg`:

hns_dsaf_sbm_bp_wl_cfg
======================

.. c:function:: void hns_dsaf_sbm_bp_wl_cfg(struct dsaf_device *dsaf_dev)

    config sbm

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_voq_bp_all_thrd_cfg`:

hns_dsaf_voq_bp_all_thrd_cfg
============================

.. c:function:: void hns_dsaf_voq_bp_all_thrd_cfg(struct dsaf_device *dsaf_dev)

    voq

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_tcam_data_cfg`:

hns_dsaf_tbl_tcam_data_cfg
==========================

.. c:function:: void hns_dsaf_tbl_tcam_data_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_tcam_data *ptbl_tcam_data)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param struct dsaf_tbl_tcam_data \*ptbl_tcam_data:
        addr

.. _`hns_dsaf_tbl_tcam_mcast_cfg`:

hns_dsaf_tbl_tcam_mcast_cfg
===========================

.. c:function:: void hns_dsaf_tbl_tcam_mcast_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_tcam_mcast_cfg *mcast)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param struct dsaf_tbl_tcam_mcast_cfg \*mcast:
        *undescribed*

.. _`hns_dsaf_tbl_tcam_ucast_cfg`:

hns_dsaf_tbl_tcam_ucast_cfg
===========================

.. c:function:: void hns_dsaf_tbl_tcam_ucast_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_tcam_ucast_cfg *tbl_tcam_ucast)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param struct dsaf_tbl_tcam_ucast_cfg \*tbl_tcam_ucast:
        *undescribed*

.. _`hns_dsaf_tbl_line_cfg`:

hns_dsaf_tbl_line_cfg
=====================

.. c:function:: void hns_dsaf_tbl_line_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_line_cfg *tbl_lin)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param struct dsaf_tbl_line_cfg \*tbl_lin:
        *undescribed*

.. _`hns_dsaf_tbl_tcam_mcast_pul`:

hns_dsaf_tbl_tcam_mcast_pul
===========================

.. c:function:: void hns_dsaf_tbl_tcam_mcast_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_line_pul`:

hns_dsaf_tbl_line_pul
=====================

.. c:function:: void hns_dsaf_tbl_line_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_tcam_data_mcast_pul`:

hns_dsaf_tbl_tcam_data_mcast_pul
================================

.. c:function:: void hns_dsaf_tbl_tcam_data_mcast_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_tcam_data_ucast_pul`:

hns_dsaf_tbl_tcam_data_ucast_pul
================================

.. c:function:: void hns_dsaf_tbl_tcam_data_ucast_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_stat_en`:

hns_dsaf_tbl_stat_en
====================

.. c:function:: void hns_dsaf_tbl_stat_en(struct dsaf_device *dsaf_dev)

    tbl

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_rocee_bp_en`:

hns_dsaf_rocee_bp_en
====================

.. c:function:: void hns_dsaf_rocee_bp_en(struct dsaf_device *dsaf_dev)

    rocee back press enable

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_single_line_tbl_cfg`:

hns_dsaf_single_line_tbl_cfg
============================

.. c:function:: void hns_dsaf_single_line_tbl_cfg(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_line_cfg *ptbl_line)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 address:
        *undescribed*

    :param struct dsaf_tbl_line_cfg \*ptbl_line:
        *undescribed*

.. _`hns_dsaf_tcam_uc_cfg`:

hns_dsaf_tcam_uc_cfg
====================

.. c:function:: void hns_dsaf_tcam_uc_cfg(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_ucast_cfg *ptbl_tcam_ucast)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 address:
        *undescribed*

    :param struct dsaf_tbl_tcam_data \*ptbl_tcam_data:
        *undescribed*

    :param struct dsaf_tbl_tcam_ucast_cfg \*ptbl_tcam_ucast:
        *undescribed*

.. _`hns_dsaf_tcam_mc_cfg`:

hns_dsaf_tcam_mc_cfg
====================

.. c:function:: void hns_dsaf_tcam_mc_cfg(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_mcast_cfg *ptbl_tcam_mcast)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 address:
        *undescribed*

    :param struct dsaf_tbl_tcam_data \*ptbl_tcam_data:
        *undescribed*

    :param struct dsaf_tbl_tcam_mcast_cfg \*ptbl_tcam_mcast:
        *undescribed*

.. _`hns_dsaf_tcam_mc_invld`:

hns_dsaf_tcam_mc_invld
======================

.. c:function:: void hns_dsaf_tcam_mc_invld(struct dsaf_device *dsaf_dev, u32 address)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 address:
        *undescribed*

.. _`hns_dsaf_tcam_uc_get`:

hns_dsaf_tcam_uc_get
====================

.. c:function:: void hns_dsaf_tcam_uc_get(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_ucast_cfg *ptbl_tcam_ucast)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 address:
        *undescribed*

    :param struct dsaf_tbl_tcam_data \*ptbl_tcam_data:
        *undescribed*

    :param struct dsaf_tbl_tcam_ucast_cfg \*ptbl_tcam_ucast:
        *undescribed*

.. _`hns_dsaf_tcam_mc_get`:

hns_dsaf_tcam_mc_get
====================

.. c:function:: void hns_dsaf_tcam_mc_get(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_mcast_cfg *ptbl_tcam_mcast)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param u32 address:
        *undescribed*

    :param struct dsaf_tbl_tcam_data \*ptbl_tcam_data:
        *undescribed*

    :param struct dsaf_tbl_tcam_mcast_cfg \*ptbl_tcam_mcast:
        *undescribed*

.. _`hns_dsaf_tbl_line_init`:

hns_dsaf_tbl_line_init
======================

.. c:function:: void hns_dsaf_tbl_line_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_tcam_init`:

hns_dsaf_tbl_tcam_init
======================

.. c:function:: void hns_dsaf_tbl_tcam_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_pfc_en_cfg`:

hns_dsaf_pfc_en_cfg
===================

.. c:function:: void hns_dsaf_pfc_en_cfg(struct dsaf_device *dsaf_dev, int mac_id, int tc_en)

    dsaf pfc pause cfg

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param int mac_id:
        *undescribed*

    :param int tc_en:
        *undescribed*

.. _`hns_dsaf_comm_init`:

hns_dsaf_comm_init
==================

.. c:function:: void hns_dsaf_comm_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_inode_init`:

hns_dsaf_inode_init
===================

.. c:function:: void hns_dsaf_inode_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_sbm_init`:

hns_dsaf_sbm_init
=================

.. c:function:: int hns_dsaf_sbm_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_tbl_init`:

hns_dsaf_tbl_init
=================

.. c:function:: void hns_dsaf_tbl_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_voq_init`:

hns_dsaf_voq_init
=================

.. c:function:: void hns_dsaf_voq_init(struct dsaf_device *dsaf_dev)

    INT

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_init_hw`:

hns_dsaf_init_hw
================

.. c:function:: int hns_dsaf_init_hw(struct dsaf_device *dsaf_dev)

    init dsa fabric hardware

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

.. _`hns_dsaf_remove_hw`:

hns_dsaf_remove_hw
==================

.. c:function:: void hns_dsaf_remove_hw(struct dsaf_device *dsaf_dev)

    uninit dsa fabric hardware

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

.. _`hns_dsaf_init`:

hns_dsaf_init
=============

.. c:function:: int hns_dsaf_init(struct dsaf_device *dsaf_dev)

    init dsa fabric

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer
        retuen 0 - success , negative --fail

.. _`hns_dsaf_free`:

hns_dsaf_free
=============

.. c:function:: void hns_dsaf_free(struct dsaf_device *dsaf_dev)

    free dsa fabric

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

.. _`hns_dsaf_find_soft_mac_entry`:

hns_dsaf_find_soft_mac_entry
============================

.. c:function:: u16 hns_dsaf_find_soft_mac_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_tbl_tcam_key *mac_key)

    find dsa fabric soft entry

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_tbl_tcam_key \*mac_key:
        mac entry struct pointer

.. _`hns_dsaf_find_empty_mac_entry`:

hns_dsaf_find_empty_mac_entry
=============================

.. c:function:: u16 hns_dsaf_find_empty_mac_entry(struct dsaf_device *dsaf_dev)

    search dsa fabric soft empty-entry

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

.. _`hns_dsaf_set_mac_key`:

hns_dsaf_set_mac_key
====================

.. c:function:: void hns_dsaf_set_mac_key(struct dsaf_device *dsaf_dev, struct dsaf_drv_tbl_tcam_key *mac_key, u16 vlan_id, u8 in_port_num, u8 *addr)

    set mac key

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_tbl_tcam_key \*mac_key:
        tcam key pointer

    :param u16 vlan_id:
        vlan id

    :param u8 in_port_num:
        input port num

    :param u8 \*addr:
        mac addr

.. _`hns_dsaf_set_mac_uc_entry`:

hns_dsaf_set_mac_uc_entry
=========================

.. c:function:: int hns_dsaf_set_mac_uc_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    set mac uc-entry

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_mac_single_dest_entry \*mac_entry:
        uc-mac entry

.. _`hns_dsaf_set_mac_mc_entry`:

hns_dsaf_set_mac_mc_entry
=========================

.. c:function:: int hns_dsaf_set_mac_mc_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_multi_dest_entry *mac_entry)

    set mac mc-entry

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_mac_multi_dest_entry \*mac_entry:
        mc-mac entry

.. _`hns_dsaf_add_mac_mc_port`:

hns_dsaf_add_mac_mc_port
========================

.. c:function:: int hns_dsaf_add_mac_mc_port(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    add mac mc-port

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_mac_single_dest_entry \*mac_entry:
        mc-mac entry

.. _`hns_dsaf_del_mac_entry`:

hns_dsaf_del_mac_entry
======================

.. c:function:: int hns_dsaf_del_mac_entry(struct dsaf_device *dsaf_dev, u16 vlan_id, u8 in_port_num, u8 *addr)

    del mac mc-port

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param u16 vlan_id:
        vlian id

    :param u8 in_port_num:
        input port num

    :param u8 \*addr:
        mac addr

.. _`hns_dsaf_del_mac_mc_port`:

hns_dsaf_del_mac_mc_port
========================

.. c:function:: int hns_dsaf_del_mac_mc_port(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    del mac mc- port

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_mac_single_dest_entry \*mac_entry:
        mac entry

.. _`hns_dsaf_get_mac_uc_entry`:

hns_dsaf_get_mac_uc_entry
=========================

.. c:function:: int hns_dsaf_get_mac_uc_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    get mac uc entry

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_mac_single_dest_entry \*mac_entry:
        mac entry

.. _`hns_dsaf_get_mac_mc_entry`:

hns_dsaf_get_mac_mc_entry
=========================

.. c:function:: int hns_dsaf_get_mac_mc_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_multi_dest_entry *mac_entry)

    get mac mc entry

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param struct dsaf_drv_mac_multi_dest_entry \*mac_entry:
        mac entry

.. _`hns_dsaf_get_mac_entry_by_index`:

hns_dsaf_get_mac_entry_by_index
===============================

.. c:function:: int hns_dsaf_get_mac_entry_by_index(struct dsaf_device *dsaf_dev, u16 entry_index, struct dsaf_drv_mac_multi_dest_entry *mac_entry)

    get mac entry by tab index

    :param struct dsaf_device \*dsaf_dev:
        dsa fabric device struct pointer

    :param u16 entry_index:
        tab entry index

    :param struct dsaf_drv_mac_multi_dest_entry \*mac_entry:
        mac entry

.. _`hns_dsaf_free_dev`:

hns_dsaf_free_dev
=================

.. c:function:: void hns_dsaf_free_dev(struct dsaf_device *dsaf_dev)

    free dev mem

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_pfc_unit_cnt`:

hns_dsaf_pfc_unit_cnt
=====================

.. c:function:: void hns_dsaf_pfc_unit_cnt(struct dsaf_device *dsaf_dev, int mac_id, enum dsaf_port_rate_mode rate)

    set pfc unit count

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param int mac_id:
        *undescribed*

    :param enum dsaf_port_rate_mode rate:
        *undescribed*

.. _`hns_dsaf_port_work_rate_cfg`:

hns_dsaf_port_work_rate_cfg
===========================

.. c:function:: void hns_dsaf_port_work_rate_cfg(struct dsaf_device *dsaf_dev, int mac_id, enum dsaf_port_rate_mode rate_mode)

    fifo

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param int mac_id:
        *undescribed*

    :param enum dsaf_port_rate_mode rate_mode:
        *undescribed*

.. _`hns_dsaf_fix_mac_mode`:

hns_dsaf_fix_mac_mode
=====================

.. c:function:: void hns_dsaf_fix_mac_mode(struct hns_mac_cb *mac_cb)

    dsaf modify mac mode

    :param struct hns_mac_cb \*mac_cb:
        mac contrl block

.. _`hns_dsaf_get_regs`:

hns_dsaf_get_regs
=================

.. c:function:: void hns_dsaf_get_regs(struct dsaf_device *ddev, u32 port, void *data)

    dump dsaf regs \ ``dsaf_dev``\ : dsaf device \ ``data``\ :data for value of regs

    :param struct dsaf_device \*ddev:
        *undescribed*

    :param u32 port:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`hns_dsaf_get_stats`:

hns_dsaf_get_stats
==================

.. c:function:: void hns_dsaf_get_stats(struct dsaf_device *ddev, u64 *data, int port)

    get dsaf statistic \ ``ddev``\ : dsaf device \ ``data``\ :statistic value \ ``port``\ : port num

    :param struct dsaf_device \*ddev:
        *undescribed*

    :param u64 \*data:
        *undescribed*

    :param int port:
        *undescribed*

.. _`hns_dsaf_get_sset_count`:

hns_dsaf_get_sset_count
=======================

.. c:function:: int hns_dsaf_get_sset_count(struct dsaf_device *dsaf_dev, int stringset)

    get dsaf string set count \ ``stringset``\ : type of values in data return dsaf string name count

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

    :param int stringset:
        *undescribed*

.. _`hns_dsaf_get_strings`:

hns_dsaf_get_strings
====================

.. c:function:: void hns_dsaf_get_strings(int stringset, u8 *data, int port, struct dsaf_device *dsaf_dev)

    get dsaf string set \ ``stringset``\ :srting set index \ ``data``\ :strings name value \ ``port``\ :port index

    :param int stringset:
        *undescribed*

    :param u8 \*data:
        *undescribed*

    :param int port:
        *undescribed*

    :param struct dsaf_device \*dsaf_dev:
        *undescribed*

.. _`hns_dsaf_get_regs_count`:

hns_dsaf_get_regs_count
=======================

.. c:function:: int hns_dsaf_get_regs_count( void)

    get dsaf regs count return dsaf regs count

    :param  void:
        no arguments

.. _`hns_dsaf_probe`:

hns_dsaf_probe
==============

.. c:function:: int hns_dsaf_probe(struct platform_device *pdev)

    probo dsaf dev

    :param struct platform_device \*pdev:
        dasf platform device
        retuen 0 - success , negative --fail

.. _`hns_dsaf_remove`:

hns_dsaf_remove
===============

.. c:function:: int hns_dsaf_remove(struct platform_device *pdev)

    remove dsaf dev

    :param struct platform_device \*pdev:
        dasf platform device

.. _`hns_dsaf_roce_reset`:

hns_dsaf_roce_reset
===================

.. c:function:: int hns_dsaf_roce_reset(struct fwnode_handle *dsaf_fwnode, bool dereset)

    reset dsaf and roce

    :param struct fwnode_handle \*dsaf_fwnode:
        Pointer to framework node for the dasf

    :param bool dereset:
        *undescribed*

.. This file was automatic generated / don't edit.

