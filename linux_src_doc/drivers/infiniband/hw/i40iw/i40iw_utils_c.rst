.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_utils.c

.. _`i40iw_arp_table`:

i40iw_arp_table
===============

.. c:function:: int i40iw_arp_table(struct i40iw_device *iwdev, u32 *ip_addr, bool ipv4, u8 *mac_addr, u32 action)

    manage arp table

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u32 \*ip_addr:
        ip address for device

    :param bool ipv4:
        *undescribed*

    :param u8 \*mac_addr:
        mac address ptr

    :param u32 action:
        modify, delete or add

.. _`i40iw_wr32`:

i40iw_wr32
==========

.. c:function:: void i40iw_wr32(struct i40iw_hw *hw, u32 reg, u32 value)

    write 32 bits to hw register

    :param struct i40iw_hw \*hw:
        hardware information including registers

    :param u32 reg:
        register offset

    :param u32 value:
        vvalue to write to register

.. _`i40iw_rd32`:

i40iw_rd32
==========

.. c:function:: u32 i40iw_rd32(struct i40iw_hw *hw, u32 reg)

    read a 32 bit hw register

    :param struct i40iw_hw \*hw:
        hardware information including registers

    :param u32 reg:
        register offset

.. _`i40iw_rd32.description`:

Description
-----------

Return value of register content

.. _`i40iw_inetaddr_event`:

i40iw_inetaddr_event
====================

.. c:function:: int i40iw_inetaddr_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for netdev events

    :param struct notifier_block \*notifier:
        *undescribed*

    :param unsigned long event:
        event for notifier

    :param void \*ptr:
        if address

.. _`i40iw_inet6addr_event`:

i40iw_inet6addr_event
=====================

.. c:function:: int i40iw_inet6addr_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for ipv6 netdev events

    :param struct notifier_block \*notifier:
        *undescribed*

    :param unsigned long event:
        event for notifier

    :param void \*ptr:
        if address

.. _`i40iw_net_event`:

i40iw_net_event
===============

.. c:function:: int i40iw_net_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for net events

    :param struct notifier_block \*notifier:
        *undescribed*

    :param unsigned long event:
        event for notifier

    :param void \*ptr:
        neighbor

.. _`i40iw_get_cqp_request`:

i40iw_get_cqp_request
=====================

.. c:function:: struct i40iw_cqp_request *i40iw_get_cqp_request(struct i40iw_cqp *cqp, bool wait)

    get cqp struct

    :param struct i40iw_cqp \*cqp:
        device cqp ptr

    :param bool wait:
        cqp to be used in wait mode

.. _`i40iw_free_cqp_request`:

i40iw_free_cqp_request
======================

.. c:function:: void i40iw_free_cqp_request(struct i40iw_cqp *cqp, struct i40iw_cqp_request *cqp_request)

    free cqp request

    :param struct i40iw_cqp \*cqp:
        cqp ptr

    :param struct i40iw_cqp_request \*cqp_request:
        to be put back in cqp list

.. _`i40iw_put_cqp_request`:

i40iw_put_cqp_request
=====================

.. c:function:: void i40iw_put_cqp_request(struct i40iw_cqp *cqp, struct i40iw_cqp_request *cqp_request)

    dec ref count and free if 0

    :param struct i40iw_cqp \*cqp:
        cqp ptr

    :param struct i40iw_cqp_request \*cqp_request:
        to be put back in cqp list

.. _`i40iw_free_pending_cqp_request`:

i40iw_free_pending_cqp_request
==============================

.. c:function:: void i40iw_free_pending_cqp_request(struct i40iw_cqp *cqp, struct i40iw_cqp_request *cqp_request)

    free pending cqp request objs

    :param struct i40iw_cqp \*cqp:
        cqp ptr

    :param struct i40iw_cqp_request \*cqp_request:
        to be put back in cqp list

.. _`i40iw_cleanup_pending_cqp_op`:

i40iw_cleanup_pending_cqp_op
============================

.. c:function:: void i40iw_cleanup_pending_cqp_op(struct i40iw_device *iwdev)

    clean-up cqp with no completions

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_free_qp`:

i40iw_free_qp
=============

.. c:function:: void i40iw_free_qp(struct i40iw_cqp_request *cqp_request, u32 num)

    callback after destroy cqp completes

    :param struct i40iw_cqp_request \*cqp_request:
        cqp request for destroy qp

    :param u32 num:
        not used

.. _`i40iw_wait_event`:

i40iw_wait_event
================

.. c:function:: int i40iw_wait_event(struct i40iw_device *iwdev, struct i40iw_cqp_request *cqp_request)

    wait for completion

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_cqp_request \*cqp_request:
        cqp request to wait

.. _`i40iw_handle_cqp_op`:

i40iw_handle_cqp_op
===================

.. c:function:: enum i40iw_status_code i40iw_handle_cqp_op(struct i40iw_device *iwdev, struct i40iw_cqp_request *cqp_request)

    process cqp command

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_cqp_request \*cqp_request:
        cqp request to process

.. _`i40iw_add_devusecount`:

i40iw_add_devusecount
=====================

.. c:function:: void i40iw_add_devusecount(struct i40iw_device *iwdev)

    add dev refcount

    :param struct i40iw_device \*iwdev:
        dev for refcount

.. _`i40iw_rem_devusecount`:

i40iw_rem_devusecount
=====================

.. c:function:: void i40iw_rem_devusecount(struct i40iw_device *iwdev)

    decrement refcount for dev

    :param struct i40iw_device \*iwdev:
        device

.. _`i40iw_add_pdusecount`:

i40iw_add_pdusecount
====================

.. c:function:: void i40iw_add_pdusecount(struct i40iw_pd *iwpd)

    add pd refcount

    :param struct i40iw_pd \*iwpd:
        pd for refcount

.. _`i40iw_rem_pdusecount`:

i40iw_rem_pdusecount
====================

.. c:function:: void i40iw_rem_pdusecount(struct i40iw_pd *iwpd, struct i40iw_device *iwdev)

    decrement refcount for pd and free if 0

    :param struct i40iw_pd \*iwpd:
        pd for refcount

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_add_ref`:

i40iw_add_ref
=============

.. c:function:: void i40iw_add_ref(struct ib_qp *ibqp)

    add refcount for qp

    :param struct ib_qp \*ibqp:
        iqarp qp

.. _`i40iw_rem_ref`:

i40iw_rem_ref
=============

.. c:function:: void i40iw_rem_ref(struct ib_qp *ibqp)

    rem refcount for qp and free if 0

    :param struct ib_qp \*ibqp:
        iqarp qp

.. _`i40iw_get_qp`:

i40iw_get_qp
============

.. c:function:: struct ib_qp *i40iw_get_qp(struct ib_device *device, int qpn)

    get qp address

    :param struct ib_device \*device:
        iwarp device

    :param int qpn:
        qp number

.. _`i40iw_debug_buf`:

i40iw_debug_buf
===============

.. c:function:: void i40iw_debug_buf(struct i40iw_sc_dev *dev, enum i40iw_debug_flag mask, char *desc, u64 *buf, u32 size)

    print debug msg and buffer is mask set

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param enum i40iw_debug_flag mask:
        mask to compare if to print debug buffer

    :param char \*desc:
        *undescribed*

    :param u64 \*buf:
        points buffer addr

    :param u32 size:
        saize of buffer to print

.. _`i40iw_get_hw_addr`:

i40iw_get_hw_addr
=================

.. c:function:: u8 __iomem *i40iw_get_hw_addr(void *par)

    return hw addr

    :param void \*par:
        points to shared dev

.. _`i40iw_remove_head`:

i40iw_remove_head
=================

.. c:function:: void *i40iw_remove_head(struct list_head *list)

    return head entry and remove from list

    :param struct list_head \*list:
        list for entry

.. _`i40iw_allocate_dma_mem`:

i40iw_allocate_dma_mem
======================

.. c:function:: enum i40iw_status_code i40iw_allocate_dma_mem(struct i40iw_hw *hw, struct i40iw_dma_mem *mem, u64 size, u32 alignment)

    Memory alloc helper fn

    :param struct i40iw_hw \*hw:
        pointer to the HW structure

    :param struct i40iw_dma_mem \*mem:
        ptr to mem struct to fill out

    :param u64 size:
        size of memory requested

    :param u32 alignment:
        what to align the allocation to

.. _`i40iw_free_dma_mem`:

i40iw_free_dma_mem
==================

.. c:function:: void i40iw_free_dma_mem(struct i40iw_hw *hw, struct i40iw_dma_mem *mem)

    Memory free helper fn

    :param struct i40iw_hw \*hw:
        pointer to the HW structure

    :param struct i40iw_dma_mem \*mem:
        ptr to mem struct to free

.. _`i40iw_allocate_virt_mem`:

i40iw_allocate_virt_mem
=======================

.. c:function:: enum i40iw_status_code i40iw_allocate_virt_mem(struct i40iw_hw *hw, struct i40iw_virt_mem *mem, u32 size)

    virtual memory alloc helper fn

    :param struct i40iw_hw \*hw:
        pointer to the HW structure

    :param struct i40iw_virt_mem \*mem:
        ptr to mem struct to fill out

    :param u32 size:
        size of memory requested

.. _`i40iw_free_virt_mem`:

i40iw_free_virt_mem
===================

.. c:function:: enum i40iw_status_code i40iw_free_virt_mem(struct i40iw_hw *hw, struct i40iw_virt_mem *mem)

    virtual memory free helper fn

    :param struct i40iw_hw \*hw:
        pointer to the HW structure

    :param struct i40iw_virt_mem \*mem:
        ptr to mem struct to free

.. _`i40iw_cqp_sds_cmd`:

i40iw_cqp_sds_cmd
=================

.. c:function:: enum i40iw_status_code i40iw_cqp_sds_cmd(struct i40iw_sc_dev *dev, struct i40iw_update_sds_info *sdinfo)

    create cqp command for sd

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_update_sds_info \*sdinfo:
        *undescribed*

.. _`i40iw_qp_suspend_resume`:

i40iw_qp_suspend_resume
=======================

.. c:function:: void i40iw_qp_suspend_resume(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp, bool suspend)

    cqp command for suspend/resume

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

    :param bool suspend:
        flag if suspend or resume

.. _`i40iw_term_modify_qp`:

i40iw_term_modify_qp
====================

.. c:function:: void i40iw_term_modify_qp(struct i40iw_sc_qp *qp, u8 next_state, u8 term, u8 term_len)

    modify qp for term message

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

    :param u8 next_state:
        qp's next state

    :param u8 term:
        terminate code

    :param u8 term_len:
        length

.. _`i40iw_terminate_done`:

i40iw_terminate_done
====================

.. c:function:: void i40iw_terminate_done(struct i40iw_sc_qp *qp, int timeout_occurred)

    after terminate is completed

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

    :param int timeout_occurred:
        indicates if terminate timer expired

.. _`i40iw_terminate_timeout`:

i40iw_terminate_timeout
=======================

.. c:function:: void i40iw_terminate_timeout(unsigned long context)

    timeout happened

    :param unsigned long context:
        points to iwarp qp

.. _`i40iw_terminate_start_timer`:

i40iw_terminate_start_timer
===========================

.. c:function:: void i40iw_terminate_start_timer(struct i40iw_sc_qp *qp)

    start terminate timeout

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

.. _`i40iw_terminate_del_timer`:

i40iw_terminate_del_timer
=========================

.. c:function:: void i40iw_terminate_del_timer(struct i40iw_sc_qp *qp)

    delete terminate timeout

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

.. _`i40iw_cqp_generic_worker`:

i40iw_cqp_generic_worker
========================

.. c:function:: void i40iw_cqp_generic_worker(struct work_struct *work)

    generic worker for cqp

    :param struct work_struct \*work:
        work pointer

.. _`i40iw_cqp_spawn_worker`:

i40iw_cqp_spawn_worker
======================

.. c:function:: void i40iw_cqp_spawn_worker(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_work_info *work_info, u32 iw_vf_idx)

    spawn worket thread

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param struct i40iw_virtchnl_work_info \*work_info:
        work request info

    :param u32 iw_vf_idx:
        virtual function index

.. _`i40iw_cqp_manage_hmc_fcn_worker`:

i40iw_cqp_manage_hmc_fcn_worker
===============================

.. c:function:: void i40iw_cqp_manage_hmc_fcn_worker(struct work_struct *work)

    :param struct work_struct \*work:
        work pointer for hmc info

.. _`i40iw_cqp_manage_hmc_fcn_callback`:

i40iw_cqp_manage_hmc_fcn_callback
=================================

.. c:function:: void i40iw_cqp_manage_hmc_fcn_callback(struct i40iw_cqp_request *cqp_request, u32 unused)

    called function after cqp completion

    :param struct i40iw_cqp_request \*cqp_request:
        cqp request info struct for hmc fun

    :param u32 unused:
        unused param of callback

.. _`i40iw_cqp_manage_hmc_fcn_cmd`:

i40iw_cqp_manage_hmc_fcn_cmd
============================

.. c:function:: enum i40iw_status_code i40iw_cqp_manage_hmc_fcn_cmd(struct i40iw_sc_dev *dev, struct i40iw_hmc_fcn_info *hmcfcninfo)

    issue cqp command to manage hmc

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_hmc_fcn_info \*hmcfcninfo:
        info for hmc

.. _`i40iw_cqp_query_fpm_values_cmd`:

i40iw_cqp_query_fpm_values_cmd
==============================

.. c:function:: enum i40iw_status_code i40iw_cqp_query_fpm_values_cmd(struct i40iw_sc_dev *dev, struct i40iw_dma_mem *values_mem, u8 hmc_fn_id)

    send cqp command for fpm

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param struct i40iw_dma_mem \*values_mem:
        buffer for fpm

    :param u8 hmc_fn_id:
        function id for fpm

.. _`i40iw_cqp_commit_fpm_values_cmd`:

i40iw_cqp_commit_fpm_values_cmd
===============================

.. c:function:: enum i40iw_status_code i40iw_cqp_commit_fpm_values_cmd(struct i40iw_sc_dev *dev, struct i40iw_dma_mem *values_mem, u8 hmc_fn_id)

    commit fpm values in hw

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_dma_mem \*values_mem:
        buffer with fpm values

    :param u8 hmc_fn_id:
        function id for fpm

.. _`i40iw_vf_wait_vchnl_resp`:

i40iw_vf_wait_vchnl_resp
========================

.. c:function:: enum i40iw_status_code i40iw_vf_wait_vchnl_resp(struct i40iw_sc_dev *dev)

    wait for channel msg

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

.. _`i40iw_cqp_cq_create_cmd`:

i40iw_cqp_cq_create_cmd
=======================

.. c:function:: enum i40iw_status_code i40iw_cqp_cq_create_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq)

    create a cq for the cqp

    :param struct i40iw_sc_dev \*dev:
        device pointer

    :param struct i40iw_sc_cq \*cq:
        pointer to created cq

.. _`i40iw_cqp_qp_create_cmd`:

i40iw_cqp_qp_create_cmd
=======================

.. c:function:: enum i40iw_status_code i40iw_cqp_qp_create_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    create a qp for the cqp

    :param struct i40iw_sc_dev \*dev:
        device pointer

    :param struct i40iw_sc_qp \*qp:
        pointer to created qp

.. _`i40iw_cqp_cq_destroy_cmd`:

i40iw_cqp_cq_destroy_cmd
========================

.. c:function:: void i40iw_cqp_cq_destroy_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq)

    destroy the cqp cq

    :param struct i40iw_sc_dev \*dev:
        device pointer

    :param struct i40iw_sc_cq \*cq:
        pointer to cq

.. _`i40iw_cqp_qp_destroy_cmd`:

i40iw_cqp_qp_destroy_cmd
========================

.. c:function:: void i40iw_cqp_qp_destroy_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    destroy the cqp

    :param struct i40iw_sc_dev \*dev:
        device pointer

    :param struct i40iw_sc_qp \*qp:
        pointer to qp

.. _`i40iw_ieq_mpa_crc_ae`:

i40iw_ieq_mpa_crc_ae
====================

.. c:function:: void i40iw_ieq_mpa_crc_ae(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    generate AE for crc error

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

.. _`i40iw_init_hash_desc`:

i40iw_init_hash_desc
====================

.. c:function:: enum i40iw_status_code i40iw_init_hash_desc(struct shash_desc **desc)

    initialize hash for crc calculation

    :param struct shash_desc \*\*desc:
        cryption type

.. _`i40iw_free_hash_desc`:

i40iw_free_hash_desc
====================

.. c:function:: void i40iw_free_hash_desc(struct shash_desc *desc)

    free hash desc

    :param struct shash_desc \*desc:
        to be freed

.. _`i40iw_alloc_query_fpm_buf`:

i40iw_alloc_query_fpm_buf
=========================

.. c:function:: enum i40iw_status_code i40iw_alloc_query_fpm_buf(struct i40iw_sc_dev *dev, struct i40iw_dma_mem *mem)

    allocate buffer for fpm

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_dma_mem \*mem:
        buffer ptr for fpm to be allocated

.. _`i40iw_ieq_check_mpacrc`:

i40iw_ieq_check_mpacrc
======================

.. c:function:: enum i40iw_status_code i40iw_ieq_check_mpacrc(struct shash_desc *desc, void *addr, u32 length, u32 value)

    check if mpa crc is OK

    :param struct shash_desc \*desc:
        desc for hash

    :param void \*addr:
        address of buffer for crc

    :param u32 length:
        length of buffer

    :param u32 value:
        value to be compared

.. _`i40iw_ieq_get_qp`:

i40iw_ieq_get_qp
================

.. c:function:: struct i40iw_sc_qp *i40iw_ieq_get_qp(struct i40iw_sc_dev *dev, struct i40iw_puda_buf *buf)

    get qp based on quad in puda buffer

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_puda_buf \*buf:
        receive puda buffer on exception q

.. _`i40iw_ieq_update_tcpip_info`:

i40iw_ieq_update_tcpip_info
===========================

.. c:function:: void i40iw_ieq_update_tcpip_info(struct i40iw_puda_buf *buf, u16 length, u32 seqnum)

    update tcpip in the buffer

    :param struct i40iw_puda_buf \*buf:
        puda to update

    :param u16 length:
        length of buffer

    :param u32 seqnum:
        seq number for tcp

.. _`i40iw_puda_get_tcpip_info`:

i40iw_puda_get_tcpip_info
=========================

.. c:function:: enum i40iw_status_code i40iw_puda_get_tcpip_info(struct i40iw_puda_completion_info *info, struct i40iw_puda_buf *buf)

    get tcpip info from puda buffer

    :param struct i40iw_puda_completion_info \*info:
        to get information

    :param struct i40iw_puda_buf \*buf:
        puda buffer

.. _`i40iw_hw_stats_timeout`:

i40iw_hw_stats_timeout
======================

.. c:function:: void i40iw_hw_stats_timeout(unsigned long vsi)

    Stats timer-handler which updates all HW stats

    :param unsigned long vsi:
        pointer to the vsi structure

.. _`i40iw_hw_stats_start_timer`:

i40iw_hw_stats_start_timer
==========================

.. c:function:: void i40iw_hw_stats_start_timer(struct i40iw_sc_vsi *vsi)

    Start periodic stats timer

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

.. _`i40iw_hw_stats_stop_timer`:

i40iw_hw_stats_stop_timer
=========================

.. c:function:: void i40iw_hw_stats_stop_timer(struct i40iw_sc_vsi *vsi)

    Delete periodic stats timer

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

.. This file was automatic generated / don't edit.

