.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_ctrl.c

.. _`i40iw_insert_wqe_hdr`:

i40iw_insert_wqe_hdr
====================

.. c:function:: void i40iw_insert_wqe_hdr(u64 *wqe, u64 header)

    write wqe header

    :param u64 \*wqe:
        cqp wqe for header

    :param u64 header:
        header for the cqp wqe

.. _`i40iw_get_cqp_reg_info`:

i40iw_get_cqp_reg_info
======================

.. c:function:: void i40iw_get_cqp_reg_info(struct i40iw_sc_cqp *cqp, u32 *val, u32 *tail, u32 *error)

    get head and tail for cqp using registers

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u32 \*val:
        cqp tail register value

    :param u32 \*tail:
        wqtail register value

    :param u32 \*error:
        cqp processing err

.. _`i40iw_cqp_poll_registers`:

i40iw_cqp_poll_registers
========================

.. c:function:: enum i40iw_status_code i40iw_cqp_poll_registers(struct i40iw_sc_cqp *cqp, u32 tail, u32 count)

    poll cqp registers

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u32 tail:
        wqtail register value

    :param u32 count:
        how many times to try for completion

.. _`i40iw_sc_parse_fpm_commit_buf`:

i40iw_sc_parse_fpm_commit_buf
=============================

.. c:function:: enum i40iw_status_code i40iw_sc_parse_fpm_commit_buf(u64 *buf, struct i40iw_hmc_obj_info *info, u32 *sd)

    parse fpm commit buffer

    :param u64 \*buf:
        ptr to fpm commit buffer

    :param struct i40iw_hmc_obj_info \*info:
        ptr to i40iw_hmc_obj_info struct

    :param u32 \*sd:
        number of SDs for HMC objects

.. _`i40iw_sc_parse_fpm_commit_buf.description`:

Description
-----------

parses fpm commit info and copy base value
of hmc objects in hmc_info

.. _`i40iw_sc_decode_fpm_query`:

i40iw_sc_decode_fpm_query
=========================

.. c:function:: u64 i40iw_sc_decode_fpm_query(u64 *buf, u32 buf_idx, struct i40iw_hmc_obj_info *obj_info, u32 rsrc_idx)

    Decode a 64 bit value into max count and size

    :param u64 \*buf:
        ptr to fpm query buffer

    :param u32 buf_idx:
        index into buf

    :param struct i40iw_hmc_obj_info \*obj_info:
        *undescribed*

    :param u32 rsrc_idx:
        resource index into info

.. _`i40iw_sc_decode_fpm_query.description`:

Description
-----------

Decode a 64 bit value from fpm query buffer into max count and size

.. _`i40iw_sc_parse_fpm_query_buf`:

i40iw_sc_parse_fpm_query_buf
============================

.. c:function:: enum i40iw_status_code i40iw_sc_parse_fpm_query_buf(u64 *buf, struct i40iw_hmc_info *hmc_info, struct i40iw_hmc_fpm_misc *hmc_fpm_misc)

    parses fpm query buffer

    :param u64 \*buf:
        ptr to fpm query buffer

    :param struct i40iw_hmc_info \*hmc_info:
        *undescribed*

    :param struct i40iw_hmc_fpm_misc \*hmc_fpm_misc:
        ptr to fpm data

.. _`i40iw_sc_parse_fpm_query_buf.description`:

Description
-----------

parses fpm query buffer and copy max_cnt and
size value of hmc objects in hmc_info

.. _`i40iw_fill_qos_list`:

i40iw_fill_qos_list
===================

.. c:function:: void i40iw_fill_qos_list(u16 *qs_list)

    Change all unknown qs handles to available ones

    :param u16 \*qs_list:
        list of qs_handles to be fixed with valid qs_handles

.. _`i40iw_qp_from_entry`:

i40iw_qp_from_entry
===================

.. c:function:: struct i40iw_sc_qp *i40iw_qp_from_entry(struct list_head *entry)

    Given entry, get to the qp structure

    :param struct list_head \*entry:
        Points to list of qp structure

.. _`i40iw_get_qp`:

i40iw_get_qp
============

.. c:function:: struct i40iw_sc_qp *i40iw_get_qp(struct list_head *head, struct i40iw_sc_qp *qp)

    get the next qp from the list given current qp

    :param struct list_head \*head:
        Listhead of qp's

    :param struct i40iw_sc_qp \*qp:
        current qp

.. _`i40iw_change_l2params`:

i40iw_change_l2params
=====================

.. c:function:: void i40iw_change_l2params(struct i40iw_sc_vsi *vsi, struct i40iw_l2params *l2params)

    given the new l2 parameters, change all qp

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

    :param struct i40iw_l2params \*l2params:
        New paramaters from l2

.. _`i40iw_qp_rem_qos`:

i40iw_qp_rem_qos
================

.. c:function:: void i40iw_qp_rem_qos(struct i40iw_sc_qp *qp)

    remove qp from qos lists during destroy qp

    :param struct i40iw_sc_qp \*qp:
        qp to be removed from qos

.. _`i40iw_qp_add_qos`:

i40iw_qp_add_qos
================

.. c:function:: void i40iw_qp_add_qos(struct i40iw_sc_qp *qp)

    called during setctx fot qp to be added to qos

    :param struct i40iw_sc_qp \*qp:
        qp to be added to qos

.. _`i40iw_sc_pd_init`:

i40iw_sc_pd_init
================

.. c:function:: void i40iw_sc_pd_init(struct i40iw_sc_dev *dev, struct i40iw_sc_pd *pd, u16 pd_id, int abi_ver)

    initialize sc pd struct

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_sc_pd \*pd:
        sc pd ptr

    :param u16 pd_id:
        pd_id for allocated pd

    :param int abi_ver:
        ABI version from user context, -1 if not valid

.. _`i40iw_get_encoded_wqe_size`:

i40iw_get_encoded_wqe_size
==========================

.. c:function:: u8 i40iw_get_encoded_wqe_size(u32 wqsize, bool cqpsq)

    given wq size, returns hardware encoded size

    :param u32 wqsize:
        size of the wq (sq, rq, srq) to encoded_size

    :param bool cqpsq:
        encoded size for sq for cqp as its encoded size is 1+ other wq's

.. _`i40iw_sc_cqp_init`:

i40iw_sc_cqp_init
=================

.. c:function:: enum i40iw_status_code i40iw_sc_cqp_init(struct i40iw_sc_cqp *cqp, struct i40iw_cqp_init_info *info)

    Initialize buffers for a control Queue Pair

    :param struct i40iw_sc_cqp \*cqp:
        IWARP control queue pair pointer

    :param struct i40iw_cqp_init_info \*info:
        IWARP control queue pair init info pointer

.. _`i40iw_sc_cqp_init.description`:

Description
-----------

Initializes the object and context buffers for a control Queue Pair.

.. _`i40iw_sc_cqp_create`:

i40iw_sc_cqp_create
===================

.. c:function:: enum i40iw_status_code i40iw_sc_cqp_create(struct i40iw_sc_cqp *cqp, u16 *maj_err, u16 *min_err)

    create cqp during bringup

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u16 \*maj_err:
        If error, major err number

    :param u16 \*min_err:
        If error, minor err number

.. _`i40iw_sc_cqp_post_sq`:

i40iw_sc_cqp_post_sq
====================

.. c:function:: void i40iw_sc_cqp_post_sq(struct i40iw_sc_cqp *cqp)

    post of cqp's sq

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

.. _`i40iw_sc_cqp_get_next_send_wqe_idx`:

i40iw_sc_cqp_get_next_send_wqe_idx
==================================

.. c:function:: u64 *i40iw_sc_cqp_get_next_send_wqe_idx(struct i40iw_sc_cqp *cqp, u64 scratch, u32 *wqe_idx)

    get next WQE on CQP SQ and pass back the index

    :param struct i40iw_sc_cqp \*cqp:
        pointer to CQP structure

    :param u64 scratch:
        private data for CQP WQE

    :param u32 \*wqe_idx:
        WQE index for next WQE on CQP SQ

.. _`i40iw_sc_cqp_get_next_send_wqe`:

i40iw_sc_cqp_get_next_send_wqe
==============================

.. c:function:: u64 *i40iw_sc_cqp_get_next_send_wqe(struct i40iw_sc_cqp *cqp, u64 scratch)

    get next wqe on cqp sq

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        private data for CQP WQE

.. _`i40iw_sc_cqp_destroy`:

i40iw_sc_cqp_destroy
====================

.. c:function:: enum i40iw_status_code i40iw_sc_cqp_destroy(struct i40iw_sc_cqp *cqp)

    destroy cqp during close

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

.. _`i40iw_sc_ccq_arm`:

i40iw_sc_ccq_arm
================

.. c:function:: void i40iw_sc_ccq_arm(struct i40iw_sc_cq *ccq)

    enable intr for control cq

    :param struct i40iw_sc_cq \*ccq:
        ccq sc struct

.. _`i40iw_sc_ccq_get_cqe_info`:

i40iw_sc_ccq_get_cqe_info
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_ccq_get_cqe_info(struct i40iw_sc_cq *ccq, struct i40iw_ccq_cqe_info *info)

    get ccq's cq entry

    :param struct i40iw_sc_cq \*ccq:
        ccq sc struct

    :param struct i40iw_ccq_cqe_info \*info:
        completion q entry to return

.. _`i40iw_sc_poll_for_cqp_op_done`:

i40iw_sc_poll_for_cqp_op_done
=============================

.. c:function:: enum i40iw_status_code i40iw_sc_poll_for_cqp_op_done(struct i40iw_sc_cqp *cqp, u8 op_code, struct i40iw_ccq_cqe_info *compl_info)

    Waits for last write to complete in CQP SQ

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u8 op_code:
        cqp opcode for completion

    :param struct i40iw_ccq_cqe_info \*compl_info:
        *undescribed*

.. _`i40iw_sc_manage_push_page`:

i40iw_sc_manage_push_page
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_manage_push_page(struct i40iw_sc_cqp *cqp, struct i40iw_cqp_manage_push_page_info *info, u64 scratch, bool post_sq)

    Handle push page

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_cqp_manage_push_page_info \*info:
        push page info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_manage_hmc_pm_func_table`:

i40iw_sc_manage_hmc_pm_func_table
=================================

.. c:function:: enum i40iw_status_code i40iw_sc_manage_hmc_pm_func_table(struct i40iw_sc_cqp *cqp, u64 scratch, u8 vf_index, bool free_pm_fcn, bool post_sq)

    manage of function table

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u8 vf_index:
        vf index for cqp

    :param bool free_pm_fcn:
        function number

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_set_hmc_resource_profile`:

i40iw_sc_set_hmc_resource_profile
=================================

.. c:function:: enum i40iw_status_code i40iw_sc_set_hmc_resource_profile(struct i40iw_sc_cqp *cqp, u64 scratch, u8 hmc_profile_type, u8 vf_num, bool post_sq, bool poll_registers)

    cqp wqe for hmc profile

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u8 hmc_profile_type:
        type of profile to set

    :param u8 vf_num:
        vf number for profile

    :param bool post_sq:
        flag for cqp db to ring

    :param bool poll_registers:
        flag to poll register for cqp completion

.. _`i40iw_sc_manage_hmc_pm_func_table_done`:

i40iw_sc_manage_hmc_pm_func_table_done
======================================

.. c:function:: enum i40iw_status_code i40iw_sc_manage_hmc_pm_func_table_done(struct i40iw_sc_cqp *cqp)

    wait for cqp wqe completion for function table

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

.. _`i40iw_sc_commit_fpm_values_done`:

i40iw_sc_commit_fpm_values_done
===============================

.. c:function:: enum i40iw_status_code i40iw_sc_commit_fpm_values_done(struct i40iw_sc_cqp *cqp)

    wait for cqp eqe completion for fpm commit

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

.. _`i40iw_sc_commit_fpm_values`:

i40iw_sc_commit_fpm_values
==========================

.. c:function:: enum i40iw_status_code i40iw_sc_commit_fpm_values(struct i40iw_sc_cqp *cqp, u64 scratch, u8 hmc_fn_id, struct i40iw_dma_mem *commit_fpm_mem, bool post_sq, u8 wait_type)

    cqp wqe for commit fpm values

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u8 hmc_fn_id:
        hmc function id
        \ ``commit_fpm_mem``\ ; Memory for fpm values

    :param struct i40iw_dma_mem \*commit_fpm_mem:
        *undescribed*

    :param bool post_sq:
        flag for cqp db to ring

    :param u8 wait_type:
        poll ccq or cqp registers for cqp completion

.. _`i40iw_sc_query_fpm_values_done`:

i40iw_sc_query_fpm_values_done
==============================

.. c:function:: enum i40iw_status_code i40iw_sc_query_fpm_values_done(struct i40iw_sc_cqp *cqp)

    poll for cqp wqe completion for query fpm

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

.. _`i40iw_sc_query_fpm_values`:

i40iw_sc_query_fpm_values
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_query_fpm_values(struct i40iw_sc_cqp *cqp, u64 scratch, u8 hmc_fn_id, struct i40iw_dma_mem *query_fpm_mem, bool post_sq, u8 wait_type)

    cqp wqe query fpm values

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u8 hmc_fn_id:
        hmc function id

    :param struct i40iw_dma_mem \*query_fpm_mem:
        memory for return fpm values

    :param bool post_sq:
        flag for cqp db to ring

    :param u8 wait_type:
        poll ccq or cqp registers for cqp completion

.. _`i40iw_sc_add_arp_cache_entry`:

i40iw_sc_add_arp_cache_entry
============================

.. c:function:: enum i40iw_status_code i40iw_sc_add_arp_cache_entry(struct i40iw_sc_cqp *cqp, struct i40iw_add_arp_cache_entry_info *info, u64 scratch, bool post_sq)

    cqp wqe add arp cache entry

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_add_arp_cache_entry_info \*info:
        arp entry information

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_del_arp_cache_entry`:

i40iw_sc_del_arp_cache_entry
============================

.. c:function:: enum i40iw_status_code i40iw_sc_del_arp_cache_entry(struct i40iw_sc_cqp *cqp, u64 scratch, u16 arp_index, bool post_sq)

    dele arp cache entry

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u16 arp_index:
        arp index to delete arp entry

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_query_arp_cache_entry`:

i40iw_sc_query_arp_cache_entry
==============================

.. c:function:: enum i40iw_status_code i40iw_sc_query_arp_cache_entry(struct i40iw_sc_cqp *cqp, u64 scratch, u16 arp_index, bool post_sq)

    cqp wqe to query arp and arp index

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u16 arp_index:
        arp index to delete arp entry

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_manage_apbvt_entry`:

i40iw_sc_manage_apbvt_entry
===========================

.. c:function:: enum i40iw_status_code i40iw_sc_manage_apbvt_entry(struct i40iw_sc_cqp *cqp, struct i40iw_apbvt_info *info, u64 scratch, bool post_sq)

    for adding and deleting apbvt entries

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_apbvt_info \*info:
        info for apbvt entry to add or delete

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_manage_qhash_table_entry`:

i40iw_sc_manage_qhash_table_entry
=================================

.. c:function:: enum i40iw_status_code i40iw_sc_manage_qhash_table_entry(struct i40iw_sc_cqp *cqp, struct i40iw_qhash_table_info *info, u64 scratch, bool post_sq)

    manage quad hash entries

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_qhash_table_info \*info:
        info for quad hash to manage

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_manage_qhash_table_entry.description`:

Description
-----------

This is called before connection establishment is started. For passive connections, when
listener is created, it will call with entry type of  I40IW_QHASH_TYPE_TCP_SYN with local
ip address and tcp port. When SYN is received (passive connections) or
sent (active connections), this routine is called with entry type of
I40IW_QHASH_TYPE_TCP_ESTABLISHED and quad is passed in info.

When iwarp connection is done and its state moves to RTS, the quad hash entry in
the hardware will point to iwarp's qp number and requires no calls from the driver.

.. _`i40iw_sc_alloc_local_mac_ipaddr_entry`:

i40iw_sc_alloc_local_mac_ipaddr_entry
=====================================

.. c:function:: enum i40iw_status_code i40iw_sc_alloc_local_mac_ipaddr_entry(struct i40iw_sc_cqp *cqp, u64 scratch, bool post_sq)

    cqp wqe for loc mac entry

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_add_local_mac_ipaddr_entry`:

i40iw_sc_add_local_mac_ipaddr_entry
===================================

.. c:function:: enum i40iw_status_code i40iw_sc_add_local_mac_ipaddr_entry(struct i40iw_sc_cqp *cqp, struct i40iw_local_mac_ipaddr_entry_info *info, u64 scratch, bool post_sq)

    add mac enry

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_local_mac_ipaddr_entry_info \*info:
        mac addr info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_del_local_mac_ipaddr_entry`:

i40iw_sc_del_local_mac_ipaddr_entry
===================================

.. c:function:: enum i40iw_status_code i40iw_sc_del_local_mac_ipaddr_entry(struct i40iw_sc_cqp *cqp, u64 scratch, u8 entry_idx, u8 ignore_ref_count, bool post_sq)

    cqp wqe to dele local mac

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u8 entry_idx:
        index of mac entry
        @ ignore_ref_count: to force mac adde delete

    :param u8 ignore_ref_count:
        *undescribed*

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_cqp_nop`:

i40iw_sc_cqp_nop
================

.. c:function:: enum i40iw_status_code i40iw_sc_cqp_nop(struct i40iw_sc_cqp *cqp, u64 scratch, bool post_sq)

    send a nop wqe

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_ceq_init`:

i40iw_sc_ceq_init
=================

.. c:function:: enum i40iw_status_code i40iw_sc_ceq_init(struct i40iw_sc_ceq *ceq, struct i40iw_ceq_init_info *info)

    initialize ceq

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

    :param struct i40iw_ceq_init_info \*info:
        ceq initialization info

.. _`i40iw_sc_ceq_create`:

i40iw_sc_ceq_create
===================

.. c:function:: enum i40iw_status_code i40iw_sc_ceq_create(struct i40iw_sc_ceq *ceq, u64 scratch, bool post_sq)

    create ceq wqe

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_cceq_create_done`:

i40iw_sc_cceq_create_done
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_cceq_create_done(struct i40iw_sc_ceq *ceq)

    poll for control ceq wqe to complete

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

.. _`i40iw_sc_cceq_destroy_done`:

i40iw_sc_cceq_destroy_done
==========================

.. c:function:: enum i40iw_status_code i40iw_sc_cceq_destroy_done(struct i40iw_sc_ceq *ceq)

    poll for destroy cceq to complete

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

.. _`i40iw_sc_cceq_create`:

i40iw_sc_cceq_create
====================

.. c:function:: enum i40iw_status_code i40iw_sc_cceq_create(struct i40iw_sc_ceq *ceq, u64 scratch)

    create cceq

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

    :param u64 scratch:
        u64 saved to be used during cqp completion

.. _`i40iw_sc_ceq_destroy`:

i40iw_sc_ceq_destroy
====================

.. c:function:: enum i40iw_status_code i40iw_sc_ceq_destroy(struct i40iw_sc_ceq *ceq, u64 scratch, bool post_sq)

    destroy ceq

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_process_ceq`:

i40iw_sc_process_ceq
====================

.. c:function:: void *i40iw_sc_process_ceq(struct i40iw_sc_dev *dev, struct i40iw_sc_ceq *ceq)

    process ceq

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_sc_ceq \*ceq:
        ceq sc structure

.. _`i40iw_sc_aeq_init`:

i40iw_sc_aeq_init
=================

.. c:function:: enum i40iw_status_code i40iw_sc_aeq_init(struct i40iw_sc_aeq *aeq, struct i40iw_aeq_init_info *info)

    initialize aeq

    :param struct i40iw_sc_aeq \*aeq:
        aeq structure ptr

    :param struct i40iw_aeq_init_info \*info:
        aeq initialization info

.. _`i40iw_sc_aeq_create`:

i40iw_sc_aeq_create
===================

.. c:function:: enum i40iw_status_code i40iw_sc_aeq_create(struct i40iw_sc_aeq *aeq, u64 scratch, bool post_sq)

    create aeq

    :param struct i40iw_sc_aeq \*aeq:
        aeq structure ptr

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_aeq_destroy`:

i40iw_sc_aeq_destroy
====================

.. c:function:: enum i40iw_status_code i40iw_sc_aeq_destroy(struct i40iw_sc_aeq *aeq, u64 scratch, bool post_sq)

    destroy aeq during close

    :param struct i40iw_sc_aeq \*aeq:
        aeq structure ptr

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_get_next_aeqe`:

i40iw_sc_get_next_aeqe
======================

.. c:function:: enum i40iw_status_code i40iw_sc_get_next_aeqe(struct i40iw_sc_aeq *aeq, struct i40iw_aeqe_info *info)

    get next aeq entry

    :param struct i40iw_sc_aeq \*aeq:
        aeq structure ptr

    :param struct i40iw_aeqe_info \*info:
        aeqe info to be returned

.. _`i40iw_sc_repost_aeq_entries`:

i40iw_sc_repost_aeq_entries
===========================

.. c:function:: enum i40iw_status_code i40iw_sc_repost_aeq_entries(struct i40iw_sc_dev *dev, u32 count)

    repost completed aeq entries

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param u32 count:
        allocate count

.. _`i40iw_sc_aeq_create_done`:

i40iw_sc_aeq_create_done
========================

.. c:function:: enum i40iw_status_code i40iw_sc_aeq_create_done(struct i40iw_sc_aeq *aeq)

    create aeq

    :param struct i40iw_sc_aeq \*aeq:
        aeq structure ptr

.. _`i40iw_sc_aeq_destroy_done`:

i40iw_sc_aeq_destroy_done
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_aeq_destroy_done(struct i40iw_sc_aeq *aeq)

    destroy of aeq during close

    :param struct i40iw_sc_aeq \*aeq:
        aeq structure ptr

.. _`i40iw_sc_ccq_init`:

i40iw_sc_ccq_init
=================

.. c:function:: enum i40iw_status_code i40iw_sc_ccq_init(struct i40iw_sc_cq *cq, struct i40iw_ccq_init_info *info)

    initialize control cq

    :param struct i40iw_sc_cq \*cq:
        sc's cq ctruct

    :param struct i40iw_ccq_init_info \*info:
        info for control cq initialization

.. _`i40iw_sc_ccq_create_done`:

i40iw_sc_ccq_create_done
========================

.. c:function:: enum i40iw_status_code i40iw_sc_ccq_create_done(struct i40iw_sc_cq *ccq)

    poll cqp for ccq create

    :param struct i40iw_sc_cq \*ccq:
        ccq sc struct

.. _`i40iw_sc_ccq_create`:

i40iw_sc_ccq_create
===================

.. c:function:: enum i40iw_status_code i40iw_sc_ccq_create(struct i40iw_sc_cq *ccq, u64 scratch, bool check_overflow, bool post_sq)

    create control cq

    :param struct i40iw_sc_cq \*ccq:
        ccq sc struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool check_overflow:
        overlow flag for ccq

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_ccq_destroy`:

i40iw_sc_ccq_destroy
====================

.. c:function:: enum i40iw_status_code i40iw_sc_ccq_destroy(struct i40iw_sc_cq *ccq, u64 scratch, bool post_sq)

    destroy ccq during close

    :param struct i40iw_sc_cq \*ccq:
        ccq sc struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_cq_init`:

i40iw_sc_cq_init
================

.. c:function:: enum i40iw_status_code i40iw_sc_cq_init(struct i40iw_sc_cq *cq, struct i40iw_cq_init_info *info)

    initialize completion q

    :param struct i40iw_sc_cq \*cq:
        cq struct

    :param struct i40iw_cq_init_info \*info:
        cq initialization info

.. _`i40iw_sc_cq_create`:

i40iw_sc_cq_create
==================

.. c:function:: enum i40iw_status_code i40iw_sc_cq_create(struct i40iw_sc_cq *cq, u64 scratch, bool check_overflow, bool post_sq)

    create completion q

    :param struct i40iw_sc_cq \*cq:
        cq struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool check_overflow:
        flag for overflow check

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_cq_destroy`:

i40iw_sc_cq_destroy
===================

.. c:function:: enum i40iw_status_code i40iw_sc_cq_destroy(struct i40iw_sc_cq *cq, u64 scratch, bool post_sq)

    destroy completion q

    :param struct i40iw_sc_cq \*cq:
        cq struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_cq_modify`:

i40iw_sc_cq_modify
==================

.. c:function:: enum i40iw_status_code i40iw_sc_cq_modify(struct i40iw_sc_cq *cq, struct i40iw_modify_cq_info *info, u64 scratch, bool post_sq)

    modify a Completion Queue

    :param struct i40iw_sc_cq \*cq:
        cq struct

    :param struct i40iw_modify_cq_info \*info:
        modification info struct

    :param u64 scratch:
        *undescribed*

    :param bool post_sq:
        flag to post to sq

.. _`i40iw_sc_qp_init`:

i40iw_sc_qp_init
================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_init(struct i40iw_sc_qp *qp, struct i40iw_qp_init_info *info)

    initialize qp

    :param struct i40iw_sc_qp \*qp:
        sc qp

    :param struct i40iw_qp_init_info \*info:
        initialization qp info

.. _`i40iw_sc_qp_create`:

i40iw_sc_qp_create
==================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_create(struct i40iw_sc_qp *qp, struct i40iw_create_qp_info *info, u64 scratch, bool post_sq)

    create qp

    :param struct i40iw_sc_qp \*qp:
        sc qp

    :param struct i40iw_create_qp_info \*info:
        qp create info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_qp_modify`:

i40iw_sc_qp_modify
==================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_modify(struct i40iw_sc_qp *qp, struct i40iw_modify_qp_info *info, u64 scratch, bool post_sq)

    modify qp cqp wqe

    :param struct i40iw_sc_qp \*qp:
        sc qp

    :param struct i40iw_modify_qp_info \*info:
        modify qp info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_qp_destroy`:

i40iw_sc_qp_destroy
===================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_destroy(struct i40iw_sc_qp *qp, u64 scratch, bool remove_hash_idx, bool ignore_mw_bnd, bool post_sq)

    cqp destroy qp

    :param struct i40iw_sc_qp \*qp:
        sc qp

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool remove_hash_idx:
        flag if to remove hash idx

    :param bool ignore_mw_bnd:
        memory window bind flag

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_qp_flush_wqes`:

i40iw_sc_qp_flush_wqes
======================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_flush_wqes(struct i40iw_sc_qp *qp, struct i40iw_qp_flush_info *info, u64 scratch, bool post_sq)

    flush qp's wqe

    :param struct i40iw_sc_qp \*qp:
        sc qp

    :param struct i40iw_qp_flush_info \*info:
        dlush information

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_qp_upload_context`:

i40iw_sc_qp_upload_context
==========================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_upload_context(struct i40iw_sc_dev *dev, struct i40iw_upload_context_info *info, u64 scratch, bool post_sq)

    upload qp's context

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_upload_context_info \*info:
        upload context info ptr for return

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_qp_setctx`:

i40iw_sc_qp_setctx
==================

.. c:function:: enum i40iw_status_code i40iw_sc_qp_setctx(struct i40iw_sc_qp *qp, u64 *qp_ctx, struct i40iw_qp_host_ctx_info *info)

    set qp's context

    :param struct i40iw_sc_qp \*qp:
        sc qp

    :param u64 \*qp_ctx:
        context ptr

    :param struct i40iw_qp_host_ctx_info \*info:
        ctx info

.. _`i40iw_sc_alloc_stag`:

i40iw_sc_alloc_stag
===================

.. c:function:: enum i40iw_status_code i40iw_sc_alloc_stag(struct i40iw_sc_dev *dev, struct i40iw_allocate_stag_info *info, u64 scratch, bool post_sq)

    mr stag alloc

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_allocate_stag_info \*info:
        stag info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_mr_reg_non_shared`:

i40iw_sc_mr_reg_non_shared
==========================

.. c:function:: enum i40iw_status_code i40iw_sc_mr_reg_non_shared(struct i40iw_sc_dev *dev, struct i40iw_reg_ns_stag_info *info, u64 scratch, bool post_sq)

    non-shared mr registration

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_reg_ns_stag_info \*info:
        mr info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_mr_reg_shared`:

i40iw_sc_mr_reg_shared
======================

.. c:function:: enum i40iw_status_code i40iw_sc_mr_reg_shared(struct i40iw_sc_dev *dev, struct i40iw_register_shared_stag *info, u64 scratch, bool post_sq)

    registered shared memory region

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_register_shared_stag \*info:
        info for shared memory registeration

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_dealloc_stag`:

i40iw_sc_dealloc_stag
=====================

.. c:function:: enum i40iw_status_code i40iw_sc_dealloc_stag(struct i40iw_sc_dev *dev, struct i40iw_dealloc_stag_info *info, u64 scratch, bool post_sq)

    deallocate stag

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_dealloc_stag_info \*info:
        dealloc stag info

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_query_stag`:

i40iw_sc_query_stag
===================

.. c:function:: enum i40iw_status_code i40iw_sc_query_stag(struct i40iw_sc_dev *dev, u64 scratch, u32 stag_index, bool post_sq)

    query hardware for stag

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u32 stag_index:
        stag index for query

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_mw_alloc`:

i40iw_sc_mw_alloc
=================

.. c:function:: enum i40iw_status_code i40iw_sc_mw_alloc(struct i40iw_sc_dev *dev, u64 scratch, u32 mw_stag_index, u16 pd_id, bool post_sq)

    mw allocate

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u32 mw_stag_index:
        stag index

    :param u16 pd_id:
        pd is for this mw

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_mr_fast_register`:

i40iw_sc_mr_fast_register
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_mr_fast_register(struct i40iw_sc_qp *qp, struct i40iw_fast_reg_stag_info *info, bool post_sq)

    Posts RDMA fast register mr WR to iwarp qp

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param struct i40iw_fast_reg_stag_info \*info:
        fast mr info

    :param bool post_sq:
        flag for cqp db to ring

.. _`i40iw_sc_send_lsmm`:

i40iw_sc_send_lsmm
==================

.. c:function:: void i40iw_sc_send_lsmm(struct i40iw_sc_qp *qp, void *lsmm_buf, u32 size, i40iw_stag stag)

    send last streaming mode message

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param void \*lsmm_buf:
        buffer with lsmm message

    :param u32 size:
        size of lsmm buffer

    :param i40iw_stag stag:
        stag of lsmm buffer

.. _`i40iw_sc_send_lsmm_nostag`:

i40iw_sc_send_lsmm_nostag
=========================

.. c:function:: void i40iw_sc_send_lsmm_nostag(struct i40iw_sc_qp *qp, void *lsmm_buf, u32 size)

    for privilege qp

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param void \*lsmm_buf:
        buffer with lsmm message

    :param u32 size:
        size of lsmm buffer

.. _`i40iw_sc_send_rtt`:

i40iw_sc_send_rtt
=================

.. c:function:: void i40iw_sc_send_rtt(struct i40iw_sc_qp *qp, bool read)

    send last read0 or write0

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param bool read:
        Do read0 or write0

.. _`i40iw_sc_post_wqe0`:

i40iw_sc_post_wqe0
==================

.. c:function:: enum i40iw_status_code i40iw_sc_post_wqe0(struct i40iw_sc_qp *qp, u8 opcode)

    send wqe with opcode

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param u8 opcode:
        opcode to use for wqe0

.. _`i40iw_sc_init_iw_hmc`:

i40iw_sc_init_iw_hmc
====================

.. c:function:: enum i40iw_status_code i40iw_sc_init_iw_hmc(struct i40iw_sc_dev *dev, u8 hmc_fn_id)

    queries fpm values using cqp and populates hmc_info

    :param struct i40iw_sc_dev \*dev:
        ptr to i40iw_dev struct

    :param u8 hmc_fn_id:
        hmc function id

.. _`i40iw_sc_configure_iw_fpm`:

i40iw_sc_configure_iw_fpm
=========================

.. c:function:: enum i40iw_status_code i40iw_sc_configure_iw_fpm(struct i40iw_sc_dev *dev, u8 hmc_fn_id)

    commits hmc obj cnt values using cqp command and populates fpm base address in hmc_info

    :param struct i40iw_sc_dev \*dev:
        ptr to i40iw_dev struct

    :param u8 hmc_fn_id:
        hmc function id

.. _`cqp_sds_wqe_fill`:

cqp_sds_wqe_fill
================

.. c:function:: enum i40iw_status_code cqp_sds_wqe_fill(struct i40iw_sc_cqp *cqp, struct i40iw_update_sds_info *info, u64 scratch)

    fill cqp wqe doe sd

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw
        \ ``info``\ ; sd info for wqe

    :param struct i40iw_update_sds_info \*info:
        *undescribed*

    :param u64 scratch:
        u64 saved to be used during cqp completion

.. _`i40iw_update_pe_sds`:

i40iw_update_pe_sds
===================

.. c:function:: enum i40iw_status_code i40iw_update_pe_sds(struct i40iw_sc_dev *dev, struct i40iw_update_sds_info *info, u64 scratch)

    cqp wqe for sd

    :param struct i40iw_sc_dev \*dev:
        ptr to i40iw_dev struct

    :param struct i40iw_update_sds_info \*info:
        sd info for sd's

    :param u64 scratch:
        u64 saved to be used during cqp completion

.. _`i40iw_update_sds_noccq`:

i40iw_update_sds_noccq
======================

.. c:function:: enum i40iw_status_code i40iw_update_sds_noccq(struct i40iw_sc_dev *dev, struct i40iw_update_sds_info *info)

    update sd before ccq created

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_update_sds_info \*info:
        sd info for sd's

.. _`i40iw_sc_suspend_qp`:

i40iw_sc_suspend_qp
===================

.. c:function:: enum i40iw_status_code i40iw_sc_suspend_qp(struct i40iw_sc_cqp *cqp, struct i40iw_sc_qp *qp, u64 scratch)

    suspend qp for param change

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

.. _`i40iw_sc_resume_qp`:

i40iw_sc_resume_qp
==================

.. c:function:: enum i40iw_status_code i40iw_sc_resume_qp(struct i40iw_sc_cqp *cqp, struct i40iw_sc_qp *qp, u64 scratch)

    resume qp after suspend

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param struct i40iw_sc_qp \*qp:
        sc qp struct

    :param u64 scratch:
        u64 saved to be used during cqp completion

.. _`i40iw_sc_static_hmc_pages_allocated`:

i40iw_sc_static_hmc_pages_allocated
===================================

.. c:function:: enum i40iw_status_code i40iw_sc_static_hmc_pages_allocated(struct i40iw_sc_cqp *cqp, u64 scratch, u8 hmc_fn_id, bool post_sq, bool poll_registers)

    cqp wqe to allocate hmc pages

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

    :param u64 scratch:
        u64 saved to be used during cqp completion

    :param u8 hmc_fn_id:
        hmc function id

    :param bool post_sq:
        flag for cqp db to ring

    :param bool poll_registers:
        flag to poll register for cqp completion

.. _`i40iw_ring_full`:

i40iw_ring_full
===============

.. c:function:: bool i40iw_ring_full(struct i40iw_sc_cqp *cqp)

    check if cqp ring is full

    :param struct i40iw_sc_cqp \*cqp:
        struct for cqp hw

.. _`i40iw_est_sd`:

i40iw_est_sd
============

.. c:function:: u64 i40iw_est_sd(struct i40iw_sc_dev *dev, struct i40iw_hmc_info *hmc_info)

    returns approximate number of SDs for HMC

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct i40iw_hmc_info \*hmc_info:
        hmc structure, size and count for HMC objects

.. _`i40iw_config_fpm_values`:

i40iw_config_fpm_values
=======================

.. c:function:: enum i40iw_status_code i40iw_config_fpm_values(struct i40iw_sc_dev *dev, u32 qp_count)

    configure HMC objects

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param u32 qp_count:
        desired qp count

.. _`i40iw_exec_cqp_cmd`:

i40iw_exec_cqp_cmd
==================

.. c:function:: enum i40iw_status_code i40iw_exec_cqp_cmd(struct i40iw_sc_dev *dev, struct cqp_commands_info *pcmdinfo)

    execute cqp cmd when wqe are available

    :param struct i40iw_sc_dev \*dev:
        rdma device

    :param struct cqp_commands_info \*pcmdinfo:
        cqp command info

.. _`i40iw_process_cqp_cmd`:

i40iw_process_cqp_cmd
=====================

.. c:function:: enum i40iw_status_code i40iw_process_cqp_cmd(struct i40iw_sc_dev *dev, struct cqp_commands_info *pcmdinfo)

    process all cqp commands

    :param struct i40iw_sc_dev \*dev:
        sc device struct

    :param struct cqp_commands_info \*pcmdinfo:
        cqp command info

.. _`i40iw_process_bh`:

i40iw_process_bh
================

.. c:function:: enum i40iw_status_code i40iw_process_bh(struct i40iw_sc_dev *dev)

    called from tasklet for cqp list

    :param struct i40iw_sc_dev \*dev:
        sc device struct

.. _`i40iw_iwarp_opcode`:

i40iw_iwarp_opcode
==================

.. c:function:: u32 i40iw_iwarp_opcode(struct i40iw_aeqe_info *info, u8 *pkt)

    determine if incoming is rdma layer

    :param struct i40iw_aeqe_info \*info:
        aeq info for the packet

    :param u8 \*pkt:
        packet for error

.. _`i40iw_locate_mpa`:

i40iw_locate_mpa
================

.. c:function:: u8 *i40iw_locate_mpa(u8 *pkt)

    return pointer to mpa in the pkt

    :param u8 \*pkt:
        packet with data

.. _`i40iw_setup_termhdr`:

i40iw_setup_termhdr
===================

.. c:function:: void i40iw_setup_termhdr(struct i40iw_sc_qp *qp, struct i40iw_terminate_hdr *hdr, enum i40iw_flush_opcode opcode, u8 layer_etype, u8 err)

    termhdr for terminate pkt

    :param struct i40iw_sc_qp \*qp:
        sc qp ptr for pkt

    :param struct i40iw_terminate_hdr \*hdr:
        term hdr

    :param enum i40iw_flush_opcode opcode:
        flush opcode for termhdr

    :param u8 layer_etype:
        error layer + error type

    :param u8 err:
        error cod ein the header

.. _`i40iw_bld_terminate_hdr`:

i40iw_bld_terminate_hdr
=======================

.. c:function:: int i40iw_bld_terminate_hdr(struct i40iw_sc_qp *qp, struct i40iw_aeqe_info *info)

    build terminate message header

    :param struct i40iw_sc_qp \*qp:
        qp associated with received terminate AE

    :param struct i40iw_aeqe_info \*info:
        the struct contiaing AE information

.. _`i40iw_terminate_send_fin`:

i40iw_terminate_send_fin
========================

.. c:function:: void i40iw_terminate_send_fin(struct i40iw_sc_qp *qp)

    Send fin for terminate message

    :param struct i40iw_sc_qp \*qp:
        qp associated with received terminate AE

.. _`i40iw_terminate_connection`:

i40iw_terminate_connection
==========================

.. c:function:: void i40iw_terminate_connection(struct i40iw_sc_qp *qp, struct i40iw_aeqe_info *info)

    Bad AE and send terminate to remote QP

    :param struct i40iw_sc_qp \*qp:
        qp associated with received terminate AE

    :param struct i40iw_aeqe_info \*info:
        the struct contiaing AE information

.. _`i40iw_terminate_received`:

i40iw_terminate_received
========================

.. c:function:: void i40iw_terminate_received(struct i40iw_sc_qp *qp, struct i40iw_aeqe_info *info)

    handle terminate received AE

    :param struct i40iw_sc_qp \*qp:
        qp associated with received terminate AE

    :param struct i40iw_aeqe_info \*info:
        the struct contiaing AE information

.. _`i40iw_sc_vsi_init`:

i40iw_sc_vsi_init
=================

.. c:function:: void i40iw_sc_vsi_init(struct i40iw_sc_vsi *vsi, struct i40iw_vsi_init_info *info)

    Initialize virtual device

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

    :param struct i40iw_vsi_init_info \*info:
        parameters to initialize vsi

.. _`i40iw_hw_stats_init`:

i40iw_hw_stats_init
===================

.. c:function:: void i40iw_hw_stats_init(struct i40iw_vsi_pestat *stats, u8 fcn_idx, bool is_pf)

    Initiliaze HW stats table

    :param struct i40iw_vsi_pestat \*stats:
        pestat struct

    :param u8 fcn_idx:
        PCI fn id

    :param bool is_pf:
        Is it a PF?

.. _`i40iw_hw_stats_init.description`:

Description
-----------

Populate the HW stats table with register offset addr for each
stats. And start the perioidic stats timer.

.. _`i40iw_hw_stats_read_32`:

i40iw_hw_stats_read_32
======================

.. c:function:: void i40iw_hw_stats_read_32(struct i40iw_vsi_pestat *stats, enum i40iw_hw_stats_index_32b index, u64 *value)

    Read 32-bit HW stats counters and accommodates for roll-overs.

    :param struct i40iw_vsi_pestat \*stats:
        *undescribed*

    :param enum i40iw_hw_stats_index_32b index:
        index in HW stats table which contains offset reg-addr

    :param u64 \*value:
        hw stats value

.. _`i40iw_hw_stats_read_64`:

i40iw_hw_stats_read_64
======================

.. c:function:: void i40iw_hw_stats_read_64(struct i40iw_vsi_pestat *stats, enum i40iw_hw_stats_index_64b index, u64 *value)

    Read HW stats counters (greater than 32-bit) and accommodates for roll-overs.

    :param struct i40iw_vsi_pestat \*stats:
        pestat struct

    :param enum i40iw_hw_stats_index_64b index:
        index in HW stats table which contains offset reg-addr

    :param u64 \*value:
        hw stats value

.. _`i40iw_hw_stats_read_all`:

i40iw_hw_stats_read_all
=======================

.. c:function:: void i40iw_hw_stats_read_all(struct i40iw_vsi_pestat *stats, struct i40iw_dev_hw_stats *stats_values)

    read all HW stat counters

    :param struct i40iw_vsi_pestat \*stats:
        pestat struct

    :param struct i40iw_dev_hw_stats \*stats_values:
        hw stats structure

.. _`i40iw_hw_stats_read_all.description`:

Description
-----------

Read all the HW stat counters and populates hw_stats structure
of passed-in vsi's pestat as well as copy created in stat_values.

.. _`i40iw_hw_stats_refresh_all`:

i40iw_hw_stats_refresh_all
==========================

.. c:function:: void i40iw_hw_stats_refresh_all(struct i40iw_vsi_pestat *stats)

    Update all HW stats structs

    :param struct i40iw_vsi_pestat \*stats:
        pestat struct

.. _`i40iw_hw_stats_refresh_all.description`:

Description
-----------

Read all the HW stats counters to refresh values in hw_stats structure
of passed-in dev's pestat

.. _`i40iw_get_fcn_id`:

i40iw_get_fcn_id
================

.. c:function:: u8 i40iw_get_fcn_id(struct i40iw_sc_dev *dev)

    Return the function id

    :param struct i40iw_sc_dev \*dev:
        pointer to the device

.. _`i40iw_vsi_stats_init`:

i40iw_vsi_stats_init
====================

.. c:function:: enum i40iw_status_code i40iw_vsi_stats_init(struct i40iw_sc_vsi *vsi, struct i40iw_vsi_stats_info *info)

    Initialize the vsi statistics

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

    :param struct i40iw_vsi_stats_info \*info:
        The info structure used for initialization

.. _`i40iw_vsi_stats_free`:

i40iw_vsi_stats_free
====================

.. c:function:: void i40iw_vsi_stats_free(struct i40iw_sc_vsi *vsi)

    Free the vsi stats

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

.. _`i40iw_device_init`:

i40iw_device_init
=================

.. c:function:: enum i40iw_status_code i40iw_device_init(struct i40iw_sc_dev *dev, struct i40iw_device_init_info *info)

    Initialize IWARP device

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_device_init_info \*info:
        IWARP init info

.. This file was automatic generated / don't edit.

