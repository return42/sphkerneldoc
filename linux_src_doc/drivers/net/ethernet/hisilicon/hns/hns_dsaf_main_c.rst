.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_main.c

.. _`hns_dsaf_sbm_link_sram_init_en`:

hns_dsaf_sbm_link_sram_init_en
==============================

.. c:function:: void hns_dsaf_sbm_link_sram_init_en(struct dsaf_device *dsaf_dev)

    config dsaf_sbm_init_en

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_reg_cnt_clr_ce`:

hns_dsaf_reg_cnt_clr_ce
=======================

.. c:function:: void hns_dsaf_reg_cnt_clr_ce(struct dsaf_device *dsaf_dev, u32 reg_cnt_clr_ce)

    config hns_dsaf_reg_cnt_clr_ce

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param reg_cnt_clr_ce:
        *undescribed*
    :type reg_cnt_clr_ce: u32

.. _`hns_dsaf_ppe_qid_cfg`:

hns_dsaf_ppe_qid_cfg
====================

.. c:function:: void hns_dsaf_ppe_qid_cfg(struct dsaf_device *dsaf_dev, u32 qid_cfg)

    config ppe qid

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param qid_cfg:
        *undescribed*
    :type qid_cfg: u32

.. _`hns_dsaf_sw_port_type_cfg`:

hns_dsaf_sw_port_type_cfg
=========================

.. c:function:: void hns_dsaf_sw_port_type_cfg(struct dsaf_device *dsaf_dev, enum dsaf_sw_port_type port_type)

    cfg sw type

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param port_type:
        *undescribed*
    :type port_type: enum dsaf_sw_port_type

.. _`hns_dsaf_stp_port_type_cfg`:

hns_dsaf_stp_port_type_cfg
==========================

.. c:function:: void hns_dsaf_stp_port_type_cfg(struct dsaf_device *dsaf_dev, enum dsaf_stp_port_type port_type)

    cfg stp type

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param port_type:
        *undescribed*
    :type port_type: enum dsaf_stp_port_type

.. _`hns_dsaf_sbm_cfg`:

hns_dsaf_sbm_cfg
================

.. c:function:: void hns_dsaf_sbm_cfg(struct dsaf_device *dsaf_dev)

    config sbm

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_sbm_cfg_mib_en`:

hns_dsaf_sbm_cfg_mib_en
=======================

.. c:function:: int hns_dsaf_sbm_cfg_mib_en(struct dsaf_device *dsaf_dev)

    config sbm

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_sbm_bp_wl_cfg`:

hns_dsaf_sbm_bp_wl_cfg
======================

.. c:function:: void hns_dsaf_sbm_bp_wl_cfg(struct dsaf_device *dsaf_dev)

    config sbm

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_voq_bp_all_thrd_cfg`:

hns_dsaf_voq_bp_all_thrd_cfg
============================

.. c:function:: void hns_dsaf_voq_bp_all_thrd_cfg(struct dsaf_device *dsaf_dev)

    voq

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_tcam_data_cfg`:

hns_dsaf_tbl_tcam_data_cfg
==========================

.. c:function:: void hns_dsaf_tbl_tcam_data_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_tcam_data *ptbl_tcam_data)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param ptbl_tcam_data:
        addr
    :type ptbl_tcam_data: struct dsaf_tbl_tcam_data \*

.. _`hns_dsaf_tbl_tcam_mcast_cfg`:

hns_dsaf_tbl_tcam_mcast_cfg
===========================

.. c:function:: void hns_dsaf_tbl_tcam_mcast_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_tcam_mcast_cfg *mcast)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param mcast:
        *undescribed*
    :type mcast: struct dsaf_tbl_tcam_mcast_cfg \*

.. _`hns_dsaf_tbl_tcam_ucast_cfg`:

hns_dsaf_tbl_tcam_ucast_cfg
===========================

.. c:function:: void hns_dsaf_tbl_tcam_ucast_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_tcam_ucast_cfg *tbl_tcam_ucast)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param tbl_tcam_ucast:
        *undescribed*
    :type tbl_tcam_ucast: struct dsaf_tbl_tcam_ucast_cfg \*

.. _`hns_dsaf_tbl_line_cfg`:

hns_dsaf_tbl_line_cfg
=====================

.. c:function:: void hns_dsaf_tbl_line_cfg(struct dsaf_device *dsaf_dev, struct dsaf_tbl_line_cfg *tbl_lin)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param tbl_lin:
        *undescribed*
    :type tbl_lin: struct dsaf_tbl_line_cfg \*

.. _`hns_dsaf_tbl_tcam_mcast_pul`:

hns_dsaf_tbl_tcam_mcast_pul
===========================

.. c:function:: void hns_dsaf_tbl_tcam_mcast_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_line_pul`:

hns_dsaf_tbl_line_pul
=====================

.. c:function:: void hns_dsaf_tbl_line_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_tcam_data_mcast_pul`:

hns_dsaf_tbl_tcam_data_mcast_pul
================================

.. c:function:: void hns_dsaf_tbl_tcam_data_mcast_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_tcam_data_ucast_pul`:

hns_dsaf_tbl_tcam_data_ucast_pul
================================

.. c:function:: void hns_dsaf_tbl_tcam_data_ucast_pul(struct dsaf_device *dsaf_dev)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_stat_en`:

hns_dsaf_tbl_stat_en
====================

.. c:function:: void hns_dsaf_tbl_stat_en(struct dsaf_device *dsaf_dev)

    tbl

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_rocee_bp_en`:

hns_dsaf_rocee_bp_en
====================

.. c:function:: void hns_dsaf_rocee_bp_en(struct dsaf_device *dsaf_dev)

    rocee back press enable

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_single_line_tbl_cfg`:

hns_dsaf_single_line_tbl_cfg
============================

.. c:function:: void hns_dsaf_single_line_tbl_cfg(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_line_cfg *ptbl_line)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param address:
        *undescribed*
    :type address: u32

    :param ptbl_line:
        *undescribed*
    :type ptbl_line: struct dsaf_tbl_line_cfg \*

.. _`hns_dsaf_tcam_uc_cfg`:

hns_dsaf_tcam_uc_cfg
====================

.. c:function:: void hns_dsaf_tcam_uc_cfg(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_ucast_cfg *ptbl_tcam_ucast)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param address:
        *undescribed*
    :type address: u32

    :param ptbl_tcam_data:
        *undescribed*
    :type ptbl_tcam_data: struct dsaf_tbl_tcam_data \*

    :param ptbl_tcam_ucast:
        *undescribed*
    :type ptbl_tcam_ucast: struct dsaf_tbl_tcam_ucast_cfg \*

.. _`hns_dsaf_tcam_mc_cfg`:

hns_dsaf_tcam_mc_cfg
====================

.. c:function:: void hns_dsaf_tcam_mc_cfg(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_data *ptbl_tcam_mask, struct dsaf_tbl_tcam_mcast_cfg *ptbl_tcam_mcast)

    cfg the tcam for mc

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param address:
        tcam index
    :type address: u32

    :param ptbl_tcam_data:
        tcam data struct pointer
    :type ptbl_tcam_data: struct dsaf_tbl_tcam_data \*

    :param ptbl_tcam_mask:
        *undescribed*
    :type ptbl_tcam_mask: struct dsaf_tbl_tcam_data \*

    :param ptbl_tcam_mcast:
        tcam mask struct pointer, it must be null for HNSv1
    :type ptbl_tcam_mcast: struct dsaf_tbl_tcam_mcast_cfg \*

.. _`hns_dsaf_tcam_mc_invld`:

hns_dsaf_tcam_mc_invld
======================

.. c:function:: void hns_dsaf_tcam_mc_invld(struct dsaf_device *dsaf_dev, u32 address)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param address:
        *undescribed*
    :type address: u32

.. _`hns_dsaf_tcam_uc_get`:

hns_dsaf_tcam_uc_get
====================

.. c:function:: void hns_dsaf_tcam_uc_get(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_ucast_cfg *ptbl_tcam_ucast)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param address:
        *undescribed*
    :type address: u32

    :param ptbl_tcam_data:
        *undescribed*
    :type ptbl_tcam_data: struct dsaf_tbl_tcam_data \*

    :param ptbl_tcam_ucast:
        *undescribed*
    :type ptbl_tcam_ucast: struct dsaf_tbl_tcam_ucast_cfg \*

.. _`hns_dsaf_tcam_mc_get`:

hns_dsaf_tcam_mc_get
====================

.. c:function:: void hns_dsaf_tcam_mc_get(struct dsaf_device *dsaf_dev, u32 address, struct dsaf_tbl_tcam_data *ptbl_tcam_data, struct dsaf_tbl_tcam_mcast_cfg *ptbl_tcam_mcast)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param address:
        *undescribed*
    :type address: u32

    :param ptbl_tcam_data:
        *undescribed*
    :type ptbl_tcam_data: struct dsaf_tbl_tcam_data \*

    :param ptbl_tcam_mcast:
        *undescribed*
    :type ptbl_tcam_mcast: struct dsaf_tbl_tcam_mcast_cfg \*

.. _`hns_dsaf_tbl_line_init`:

hns_dsaf_tbl_line_init
======================

.. c:function:: void hns_dsaf_tbl_line_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_tcam_init`:

hns_dsaf_tbl_tcam_init
======================

.. c:function:: void hns_dsaf_tbl_tcam_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_pfc_en_cfg`:

hns_dsaf_pfc_en_cfg
===================

.. c:function:: void hns_dsaf_pfc_en_cfg(struct dsaf_device *dsaf_dev, int mac_id, int tc_en)

    dsaf pfc pause cfg

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param mac_id:
        *undescribed*
    :type mac_id: int

    :param tc_en:
        *undescribed*
    :type tc_en: int

.. _`hns_dsaf_comm_init`:

hns_dsaf_comm_init
==================

.. c:function:: void hns_dsaf_comm_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_inode_init`:

hns_dsaf_inode_init
===================

.. c:function:: void hns_dsaf_inode_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_sbm_init`:

hns_dsaf_sbm_init
=================

.. c:function:: int hns_dsaf_sbm_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_tbl_init`:

hns_dsaf_tbl_init
=================

.. c:function:: void hns_dsaf_tbl_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_voq_init`:

hns_dsaf_voq_init
=================

.. c:function:: void hns_dsaf_voq_init(struct dsaf_device *dsaf_dev)

    INT

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_init_hw`:

hns_dsaf_init_hw
================

.. c:function:: int hns_dsaf_init_hw(struct dsaf_device *dsaf_dev)

    init dsa fabric hardware

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_remove_hw`:

hns_dsaf_remove_hw
==================

.. c:function:: void hns_dsaf_remove_hw(struct dsaf_device *dsaf_dev)

    uninit dsa fabric hardware

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_init`:

hns_dsaf_init
=============

.. c:function:: int hns_dsaf_init(struct dsaf_device *dsaf_dev)

    init dsa fabric

    :param dsaf_dev:
        dsa fabric device struct pointer
        retuen 0 - success , negative --fail
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_free`:

hns_dsaf_free
=============

.. c:function:: void hns_dsaf_free(struct dsaf_device *dsaf_dev)

    free dsa fabric

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_find_soft_mac_entry`:

hns_dsaf_find_soft_mac_entry
============================

.. c:function:: u16 hns_dsaf_find_soft_mac_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_tbl_tcam_key *mac_key)

    find dsa fabric soft entry

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param mac_key:
        mac entry struct pointer
    :type mac_key: struct dsaf_drv_tbl_tcam_key \*

.. _`hns_dsaf_find_empty_mac_entry`:

hns_dsaf_find_empty_mac_entry
=============================

.. c:function:: u16 hns_dsaf_find_empty_mac_entry(struct dsaf_device *dsaf_dev)

    search dsa fabric soft empty-entry

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_set_mac_key`:

hns_dsaf_set_mac_key
====================

.. c:function:: void hns_dsaf_set_mac_key(struct dsaf_device *dsaf_dev, struct dsaf_drv_tbl_tcam_key *mac_key, u16 vlan_id, u8 in_port_num, u8 *addr)

    set mac key

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param mac_key:
        tcam key pointer
    :type mac_key: struct dsaf_drv_tbl_tcam_key \*

    :param vlan_id:
        vlan id
    :type vlan_id: u16

    :param in_port_num:
        input port num
    :type in_port_num: u8

    :param addr:
        mac addr
    :type addr: u8 \*

.. _`hns_dsaf_set_mac_uc_entry`:

hns_dsaf_set_mac_uc_entry
=========================

.. c:function:: int hns_dsaf_set_mac_uc_entry(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    set mac uc-entry

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param mac_entry:
        uc-mac entry
    :type mac_entry: struct dsaf_drv_mac_single_dest_entry \*

.. _`hns_dsaf_add_mac_mc_port`:

hns_dsaf_add_mac_mc_port
========================

.. c:function:: int hns_dsaf_add_mac_mc_port(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    add mac mc-port

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param mac_entry:
        mc-mac entry
    :type mac_entry: struct dsaf_drv_mac_single_dest_entry \*

.. _`hns_dsaf_del_mac_entry`:

hns_dsaf_del_mac_entry
======================

.. c:function:: int hns_dsaf_del_mac_entry(struct dsaf_device *dsaf_dev, u16 vlan_id, u8 in_port_num, u8 *addr)

    del mac mc-port

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param vlan_id:
        vlian id
    :type vlan_id: u16

    :param in_port_num:
        input port num
    :type in_port_num: u8

    :param addr:
        mac addr
    :type addr: u8 \*

.. _`hns_dsaf_del_mac_mc_port`:

hns_dsaf_del_mac_mc_port
========================

.. c:function:: int hns_dsaf_del_mac_mc_port(struct dsaf_device *dsaf_dev, struct dsaf_drv_mac_single_dest_entry *mac_entry)

    del mac mc- port

    :param dsaf_dev:
        dsa fabric device struct pointer
    :type dsaf_dev: struct dsaf_device \*

    :param mac_entry:
        mac entry
    :type mac_entry: struct dsaf_drv_mac_single_dest_entry \*

.. _`hns_dsaf_free_dev`:

hns_dsaf_free_dev
=================

.. c:function:: void hns_dsaf_free_dev(struct dsaf_device *dsaf_dev)

    free dev mem

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_pfc_unit_cnt`:

hns_dsaf_pfc_unit_cnt
=====================

.. c:function:: void hns_dsaf_pfc_unit_cnt(struct dsaf_device *dsaf_dev, int mac_id, enum dsaf_port_rate_mode rate)

    set pfc unit count

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param mac_id:
        *undescribed*
    :type mac_id: int

    :param rate:
        *undescribed*
    :type rate: enum dsaf_port_rate_mode

.. _`hns_dsaf_port_work_rate_cfg`:

hns_dsaf_port_work_rate_cfg
===========================

.. c:function:: void hns_dsaf_port_work_rate_cfg(struct dsaf_device *dsaf_dev, int mac_id, enum dsaf_port_rate_mode rate_mode)

    fifo

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param mac_id:
        *undescribed*
    :type mac_id: int

    :param rate_mode:
        *undescribed*
    :type rate_mode: enum dsaf_port_rate_mode

.. _`hns_dsaf_fix_mac_mode`:

hns_dsaf_fix_mac_mode
=====================

.. c:function:: void hns_dsaf_fix_mac_mode(struct hns_mac_cb *mac_cb)

    dsaf modify mac mode

    :param mac_cb:
        mac contrl block
    :type mac_cb: struct hns_mac_cb \*

.. _`hns_dsaf_get_regs`:

hns_dsaf_get_regs
=================

.. c:function:: void hns_dsaf_get_regs(struct dsaf_device *ddev, u32 port, void *data)

    dump dsaf regs \ ``dsaf_dev``\ : dsaf device \ ``data``\ :data for value of regs

    :param ddev:
        *undescribed*
    :type ddev: struct dsaf_device \*

    :param port:
        *undescribed*
    :type port: u32

    :param data:
        *undescribed*
    :type data: void \*

.. _`hns_dsaf_get_stats`:

hns_dsaf_get_stats
==================

.. c:function:: void hns_dsaf_get_stats(struct dsaf_device *ddev, u64 *data, int port)

    get dsaf statistic \ ``ddev``\ : dsaf device \ ``data``\ :statistic value \ ``port``\ : port num

    :param ddev:
        *undescribed*
    :type ddev: struct dsaf_device \*

    :param data:
        *undescribed*
    :type data: u64 \*

    :param port:
        *undescribed*
    :type port: int

.. _`hns_dsaf_get_sset_count`:

hns_dsaf_get_sset_count
=======================

.. c:function:: int hns_dsaf_get_sset_count(struct dsaf_device *dsaf_dev, int stringset)

    get dsaf string set count \ ``stringset``\ : type of values in data return dsaf string name count

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

    :param stringset:
        *undescribed*
    :type stringset: int

.. _`hns_dsaf_get_strings`:

hns_dsaf_get_strings
====================

.. c:function:: void hns_dsaf_get_strings(int stringset, u8 *data, int port, struct dsaf_device *dsaf_dev)

    get dsaf string set \ ``stringset``\ :srting set index \ ``data``\ :strings name value \ ``port``\ :port index

    :param stringset:
        *undescribed*
    :type stringset: int

    :param data:
        *undescribed*
    :type data: u8 \*

    :param port:
        *undescribed*
    :type port: int

    :param dsaf_dev:
        *undescribed*
    :type dsaf_dev: struct dsaf_device \*

.. _`hns_dsaf_get_regs_count`:

hns_dsaf_get_regs_count
=======================

.. c:function:: int hns_dsaf_get_regs_count( void)

    get dsaf regs count return dsaf regs count

    :param void:
        no arguments
    :type void: 

.. _`hns_dsaf_probe`:

hns_dsaf_probe
==============

.. c:function:: int hns_dsaf_probe(struct platform_device *pdev)

    probo dsaf dev

    :param pdev:
        dasf platform device
        retuen 0 - success , negative --fail
    :type pdev: struct platform_device \*

.. _`hns_dsaf_remove`:

hns_dsaf_remove
===============

.. c:function:: int hns_dsaf_remove(struct platform_device *pdev)

    remove dsaf dev

    :param pdev:
        dasf platform device
    :type pdev: struct platform_device \*

.. _`hns_dsaf_roce_reset`:

hns_dsaf_roce_reset
===================

.. c:function:: int hns_dsaf_roce_reset(struct fwnode_handle *dsaf_fwnode, bool dereset)

    reset dsaf and roce

    :param dsaf_fwnode:
        Pointer to framework node for the dasf
    :type dsaf_fwnode: struct fwnode_handle \*

    :param dereset:
        *undescribed*
    :type dereset: bool

.. This file was automatic generated / don't edit.

