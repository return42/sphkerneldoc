.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_utils.c

.. _`i40iw_arp_table`:

i40iw_arp_table
===============

.. c:function:: int i40iw_arp_table(struct i40iw_device *iwdev, u32 *ip_addr, bool ipv4, u8 *mac_addr, u32 action)

    manage arp table

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param ip_addr:
        ip address for device
    :type ip_addr: u32 \*

    :param ipv4:
        *undescribed*
    :type ipv4: bool

    :param mac_addr:
        mac address ptr
    :type mac_addr: u8 \*

    :param action:
        modify, delete or add
    :type action: u32

.. _`i40iw_wr32`:

i40iw_wr32
==========

.. c:function:: void i40iw_wr32(struct i40iw_hw *hw, u32 reg, u32 value)

    write 32 bits to hw register

    :param hw:
        hardware information including registers
    :type hw: struct i40iw_hw \*

    :param reg:
        register offset
    :type reg: u32

    :param value:
        vvalue to write to register
    :type value: u32

.. _`i40iw_rd32`:

i40iw_rd32
==========

.. c:function:: u32 i40iw_rd32(struct i40iw_hw *hw, u32 reg)

    read a 32 bit hw register

    :param hw:
        hardware information including registers
    :type hw: struct i40iw_hw \*

    :param reg:
        register offset
    :type reg: u32

.. _`i40iw_rd32.description`:

Description
-----------

Return value of register content

.. _`i40iw_inetaddr_event`:

i40iw_inetaddr_event
====================

.. c:function:: int i40iw_inetaddr_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for ipv4 addr events

    :param notifier:
        *undescribed*
    :type notifier: struct notifier_block \*

    :param event:
        event for notifier
    :type event: unsigned long

    :param ptr:
        if address
    :type ptr: void \*

.. _`i40iw_inet6addr_event`:

i40iw_inet6addr_event
=====================

.. c:function:: int i40iw_inet6addr_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for ipv6 addr events

    :param notifier:
        *undescribed*
    :type notifier: struct notifier_block \*

    :param event:
        event for notifier
    :type event: unsigned long

    :param ptr:
        if address
    :type ptr: void \*

.. _`i40iw_net_event`:

i40iw_net_event
===============

.. c:function:: int i40iw_net_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for netevents

    :param notifier:
        *undescribed*
    :type notifier: struct notifier_block \*

    :param event:
        event for notifier
    :type event: unsigned long

    :param ptr:
        neighbor
    :type ptr: void \*

.. _`i40iw_netdevice_event`:

i40iw_netdevice_event
=====================

.. c:function:: int i40iw_netdevice_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    system notifier for netdev events

    :param notifier:
        *undescribed*
    :type notifier: struct notifier_block \*

    :param event:
        event for notifier
    :type event: unsigned long

    :param ptr:
        netdev
    :type ptr: void \*

.. _`i40iw_get_cqp_request`:

i40iw_get_cqp_request
=====================

.. c:function:: struct i40iw_cqp_request *i40iw_get_cqp_request(struct i40iw_cqp *cqp, bool wait)

    get cqp struct

    :param cqp:
        device cqp ptr
    :type cqp: struct i40iw_cqp \*

    :param wait:
        cqp to be used in wait mode
    :type wait: bool

.. _`i40iw_free_cqp_request`:

i40iw_free_cqp_request
======================

.. c:function:: void i40iw_free_cqp_request(struct i40iw_cqp *cqp, struct i40iw_cqp_request *cqp_request)

    free cqp request

    :param cqp:
        cqp ptr
    :type cqp: struct i40iw_cqp \*

    :param cqp_request:
        to be put back in cqp list
    :type cqp_request: struct i40iw_cqp_request \*

.. _`i40iw_put_cqp_request`:

i40iw_put_cqp_request
=====================

.. c:function:: void i40iw_put_cqp_request(struct i40iw_cqp *cqp, struct i40iw_cqp_request *cqp_request)

    dec ref count and free if 0

    :param cqp:
        cqp ptr
    :type cqp: struct i40iw_cqp \*

    :param cqp_request:
        to be put back in cqp list
    :type cqp_request: struct i40iw_cqp_request \*

.. _`i40iw_free_pending_cqp_request`:

i40iw_free_pending_cqp_request
==============================

.. c:function:: void i40iw_free_pending_cqp_request(struct i40iw_cqp *cqp, struct i40iw_cqp_request *cqp_request)

    free pending cqp request objs

    :param cqp:
        cqp ptr
    :type cqp: struct i40iw_cqp \*

    :param cqp_request:
        to be put back in cqp list
    :type cqp_request: struct i40iw_cqp_request \*

.. _`i40iw_cleanup_pending_cqp_op`:

i40iw_cleanup_pending_cqp_op
============================

.. c:function:: void i40iw_cleanup_pending_cqp_op(struct i40iw_device *iwdev)

    clean-up cqp with no completions

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_free_qp`:

i40iw_free_qp
=============

.. c:function:: void i40iw_free_qp(struct i40iw_cqp_request *cqp_request, u32 num)

    callback after destroy cqp completes

    :param cqp_request:
        cqp request for destroy qp
    :type cqp_request: struct i40iw_cqp_request \*

    :param num:
        not used
    :type num: u32

.. _`i40iw_wait_event`:

i40iw_wait_event
================

.. c:function:: int i40iw_wait_event(struct i40iw_device *iwdev, struct i40iw_cqp_request *cqp_request)

    wait for completion

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param cqp_request:
        cqp request to wait
    :type cqp_request: struct i40iw_cqp_request \*

.. _`i40iw_handle_cqp_op`:

i40iw_handle_cqp_op
===================

.. c:function:: enum i40iw_status_code i40iw_handle_cqp_op(struct i40iw_device *iwdev, struct i40iw_cqp_request *cqp_request)

    process cqp command

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param cqp_request:
        cqp request to process
    :type cqp_request: struct i40iw_cqp_request \*

.. _`i40iw_add_devusecount`:

i40iw_add_devusecount
=====================

.. c:function:: void i40iw_add_devusecount(struct i40iw_device *iwdev)

    add dev refcount

    :param iwdev:
        dev for refcount
    :type iwdev: struct i40iw_device \*

.. _`i40iw_rem_devusecount`:

i40iw_rem_devusecount
=====================

.. c:function:: void i40iw_rem_devusecount(struct i40iw_device *iwdev)

    decrement refcount for dev

    :param iwdev:
        device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_add_pdusecount`:

i40iw_add_pdusecount
====================

.. c:function:: void i40iw_add_pdusecount(struct i40iw_pd *iwpd)

    add pd refcount

    :param iwpd:
        pd for refcount
    :type iwpd: struct i40iw_pd \*

.. _`i40iw_rem_pdusecount`:

i40iw_rem_pdusecount
====================

.. c:function:: void i40iw_rem_pdusecount(struct i40iw_pd *iwpd, struct i40iw_device *iwdev)

    decrement refcount for pd and free if 0

    :param iwpd:
        pd for refcount
    :type iwpd: struct i40iw_pd \*

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_add_ref`:

i40iw_add_ref
=============

.. c:function:: void i40iw_add_ref(struct ib_qp *ibqp)

    add refcount for qp

    :param ibqp:
        iqarp qp
    :type ibqp: struct ib_qp \*

.. _`i40iw_rem_ref`:

i40iw_rem_ref
=============

.. c:function:: void i40iw_rem_ref(struct ib_qp *ibqp)

    rem refcount for qp and free if 0

    :param ibqp:
        iqarp qp
    :type ibqp: struct ib_qp \*

.. _`i40iw_get_qp`:

i40iw_get_qp
============

.. c:function:: struct ib_qp *i40iw_get_qp(struct ib_device *device, int qpn)

    get qp address

    :param device:
        iwarp device
    :type device: struct ib_device \*

    :param qpn:
        qp number
    :type qpn: int

.. _`i40iw_debug_buf`:

i40iw_debug_buf
===============

.. c:function:: void i40iw_debug_buf(struct i40iw_sc_dev *dev, enum i40iw_debug_flag mask, char *desc, u64 *buf, u32 size)

    print debug msg and buffer is mask set

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param mask:
        mask to compare if to print debug buffer
    :type mask: enum i40iw_debug_flag

    :param desc:
        *undescribed*
    :type desc: char \*

    :param buf:
        points buffer addr
    :type buf: u64 \*

    :param size:
        saize of buffer to print
    :type size: u32

.. _`i40iw_get_hw_addr`:

i40iw_get_hw_addr
=================

.. c:function:: u8 __iomem *i40iw_get_hw_addr(void *par)

    return hw addr

    :param par:
        points to shared dev
    :type par: void \*

.. _`i40iw_remove_head`:

i40iw_remove_head
=================

.. c:function:: void *i40iw_remove_head(struct list_head *list)

    return head entry and remove from list

    :param list:
        list for entry
    :type list: struct list_head \*

.. _`i40iw_allocate_dma_mem`:

i40iw_allocate_dma_mem
======================

.. c:function:: enum i40iw_status_code i40iw_allocate_dma_mem(struct i40iw_hw *hw, struct i40iw_dma_mem *mem, u64 size, u32 alignment)

    Memory alloc helper fn

    :param hw:
        pointer to the HW structure
    :type hw: struct i40iw_hw \*

    :param mem:
        ptr to mem struct to fill out
    :type mem: struct i40iw_dma_mem \*

    :param size:
        size of memory requested
    :type size: u64

    :param alignment:
        what to align the allocation to
    :type alignment: u32

.. _`i40iw_free_dma_mem`:

i40iw_free_dma_mem
==================

.. c:function:: void i40iw_free_dma_mem(struct i40iw_hw *hw, struct i40iw_dma_mem *mem)

    Memory free helper fn

    :param hw:
        pointer to the HW structure
    :type hw: struct i40iw_hw \*

    :param mem:
        ptr to mem struct to free
    :type mem: struct i40iw_dma_mem \*

.. _`i40iw_allocate_virt_mem`:

i40iw_allocate_virt_mem
=======================

.. c:function:: enum i40iw_status_code i40iw_allocate_virt_mem(struct i40iw_hw *hw, struct i40iw_virt_mem *mem, u32 size)

    virtual memory alloc helper fn

    :param hw:
        pointer to the HW structure
    :type hw: struct i40iw_hw \*

    :param mem:
        ptr to mem struct to fill out
    :type mem: struct i40iw_virt_mem \*

    :param size:
        size of memory requested
    :type size: u32

.. _`i40iw_free_virt_mem`:

i40iw_free_virt_mem
===================

.. c:function:: enum i40iw_status_code i40iw_free_virt_mem(struct i40iw_hw *hw, struct i40iw_virt_mem *mem)

    virtual memory free helper fn

    :param hw:
        pointer to the HW structure
    :type hw: struct i40iw_hw \*

    :param mem:
        ptr to mem struct to free
    :type mem: struct i40iw_virt_mem \*

.. _`i40iw_cqp_sds_cmd`:

i40iw_cqp_sds_cmd
=================

.. c:function:: enum i40iw_status_code i40iw_cqp_sds_cmd(struct i40iw_sc_dev *dev, struct i40iw_update_sds_info *sdinfo)

    create cqp command for sd

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param sdinfo:
        *undescribed*
    :type sdinfo: struct i40iw_update_sds_info \*

.. _`i40iw_qp_suspend_resume`:

i40iw_qp_suspend_resume
=======================

.. c:function:: void i40iw_qp_suspend_resume(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp, bool suspend)

    cqp command for suspend/resume

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

    :param suspend:
        flag if suspend or resume
    :type suspend: bool

.. _`i40iw_term_modify_qp`:

i40iw_term_modify_qp
====================

.. c:function:: void i40iw_term_modify_qp(struct i40iw_sc_qp *qp, u8 next_state, u8 term, u8 term_len)

    modify qp for term message

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

    :param next_state:
        qp's next state
    :type next_state: u8

    :param term:
        terminate code
    :type term: u8

    :param term_len:
        length
    :type term_len: u8

.. _`i40iw_terminate_done`:

i40iw_terminate_done
====================

.. c:function:: void i40iw_terminate_done(struct i40iw_sc_qp *qp, int timeout_occurred)

    after terminate is completed

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

    :param timeout_occurred:
        indicates if terminate timer expired
    :type timeout_occurred: int

.. _`i40iw_terminate_timeout`:

i40iw_terminate_timeout
=======================

.. c:function:: void i40iw_terminate_timeout(struct timer_list *t)

    timeout happened

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`i40iw_terminate_start_timer`:

i40iw_terminate_start_timer
===========================

.. c:function:: void i40iw_terminate_start_timer(struct i40iw_sc_qp *qp)

    start terminate timeout

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_terminate_del_timer`:

i40iw_terminate_del_timer
=========================

.. c:function:: void i40iw_terminate_del_timer(struct i40iw_sc_qp *qp)

    delete terminate timeout

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_cqp_generic_worker`:

i40iw_cqp_generic_worker
========================

.. c:function:: void i40iw_cqp_generic_worker(struct work_struct *work)

    generic worker for cqp

    :param work:
        work pointer
    :type work: struct work_struct \*

.. _`i40iw_cqp_spawn_worker`:

i40iw_cqp_spawn_worker
======================

.. c:function:: void i40iw_cqp_spawn_worker(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_work_info *work_info, u32 iw_vf_idx)

    spawn worket thread

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param work_info:
        work request info
    :type work_info: struct i40iw_virtchnl_work_info \*

    :param iw_vf_idx:
        virtual function index
    :type iw_vf_idx: u32

.. _`i40iw_cqp_manage_hmc_fcn_worker`:

i40iw_cqp_manage_hmc_fcn_worker
===============================

.. c:function:: void i40iw_cqp_manage_hmc_fcn_worker(struct work_struct *work)

    :param work:
        work pointer for hmc info
    :type work: struct work_struct \*

.. _`i40iw_cqp_manage_hmc_fcn_callback`:

i40iw_cqp_manage_hmc_fcn_callback
=================================

.. c:function:: void i40iw_cqp_manage_hmc_fcn_callback(struct i40iw_cqp_request *cqp_request, u32 unused)

    called function after cqp completion

    :param cqp_request:
        cqp request info struct for hmc fun
    :type cqp_request: struct i40iw_cqp_request \*

    :param unused:
        unused param of callback
    :type unused: u32

.. _`i40iw_cqp_manage_hmc_fcn_cmd`:

i40iw_cqp_manage_hmc_fcn_cmd
============================

.. c:function:: enum i40iw_status_code i40iw_cqp_manage_hmc_fcn_cmd(struct i40iw_sc_dev *dev, struct i40iw_hmc_fcn_info *hmcfcninfo)

    issue cqp command to manage hmc

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param hmcfcninfo:
        info for hmc
    :type hmcfcninfo: struct i40iw_hmc_fcn_info \*

.. _`i40iw_cqp_query_fpm_values_cmd`:

i40iw_cqp_query_fpm_values_cmd
==============================

.. c:function:: enum i40iw_status_code i40iw_cqp_query_fpm_values_cmd(struct i40iw_sc_dev *dev, struct i40iw_dma_mem *values_mem, u8 hmc_fn_id)

    send cqp command for fpm

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param values_mem:
        buffer for fpm
    :type values_mem: struct i40iw_dma_mem \*

    :param hmc_fn_id:
        function id for fpm
    :type hmc_fn_id: u8

.. _`i40iw_cqp_commit_fpm_values_cmd`:

i40iw_cqp_commit_fpm_values_cmd
===============================

.. c:function:: enum i40iw_status_code i40iw_cqp_commit_fpm_values_cmd(struct i40iw_sc_dev *dev, struct i40iw_dma_mem *values_mem, u8 hmc_fn_id)

    commit fpm values in hw

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param values_mem:
        buffer with fpm values
    :type values_mem: struct i40iw_dma_mem \*

    :param hmc_fn_id:
        function id for fpm
    :type hmc_fn_id: u8

.. _`i40iw_vf_wait_vchnl_resp`:

i40iw_vf_wait_vchnl_resp
========================

.. c:function:: enum i40iw_status_code i40iw_vf_wait_vchnl_resp(struct i40iw_sc_dev *dev)

    wait for channel msg

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

.. _`i40iw_cqp_cq_create_cmd`:

i40iw_cqp_cq_create_cmd
=======================

.. c:function:: enum i40iw_status_code i40iw_cqp_cq_create_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq)

    create a cq for the cqp

    :param dev:
        device pointer
    :type dev: struct i40iw_sc_dev \*

    :param cq:
        pointer to created cq
    :type cq: struct i40iw_sc_cq \*

.. _`i40iw_cqp_qp_create_cmd`:

i40iw_cqp_qp_create_cmd
=======================

.. c:function:: enum i40iw_status_code i40iw_cqp_qp_create_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    create a qp for the cqp

    :param dev:
        device pointer
    :type dev: struct i40iw_sc_dev \*

    :param qp:
        pointer to created qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_cqp_cq_destroy_cmd`:

i40iw_cqp_cq_destroy_cmd
========================

.. c:function:: void i40iw_cqp_cq_destroy_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq)

    destroy the cqp cq

    :param dev:
        device pointer
    :type dev: struct i40iw_sc_dev \*

    :param cq:
        pointer to cq
    :type cq: struct i40iw_sc_cq \*

.. _`i40iw_cqp_qp_destroy_cmd`:

i40iw_cqp_qp_destroy_cmd
========================

.. c:function:: void i40iw_cqp_qp_destroy_cmd(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    destroy the cqp

    :param dev:
        device pointer
    :type dev: struct i40iw_sc_dev \*

    :param qp:
        pointer to qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_ieq_mpa_crc_ae`:

i40iw_ieq_mpa_crc_ae
====================

.. c:function:: void i40iw_ieq_mpa_crc_ae(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    generate AE for crc error

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_init_hash_desc`:

i40iw_init_hash_desc
====================

.. c:function:: enum i40iw_status_code i40iw_init_hash_desc(struct shash_desc **desc)

    initialize hash for crc calculation

    :param desc:
        cryption type
    :type desc: struct shash_desc \*\*

.. _`i40iw_free_hash_desc`:

i40iw_free_hash_desc
====================

.. c:function:: void i40iw_free_hash_desc(struct shash_desc *desc)

    free hash desc

    :param desc:
        to be freed
    :type desc: struct shash_desc \*

.. _`i40iw_alloc_query_fpm_buf`:

i40iw_alloc_query_fpm_buf
=========================

.. c:function:: enum i40iw_status_code i40iw_alloc_query_fpm_buf(struct i40iw_sc_dev *dev, struct i40iw_dma_mem *mem)

    allocate buffer for fpm

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param mem:
        buffer ptr for fpm to be allocated
    :type mem: struct i40iw_dma_mem \*

.. _`i40iw_ieq_check_mpacrc`:

i40iw_ieq_check_mpacrc
======================

.. c:function:: enum i40iw_status_code i40iw_ieq_check_mpacrc(struct shash_desc *desc, void *addr, u32 length, u32 value)

    check if mpa crc is OK

    :param desc:
        desc for hash
    :type desc: struct shash_desc \*

    :param addr:
        address of buffer for crc
    :type addr: void \*

    :param length:
        length of buffer
    :type length: u32

    :param value:
        value to be compared
    :type value: u32

.. _`i40iw_ieq_get_qp`:

i40iw_ieq_get_qp
================

.. c:function:: struct i40iw_sc_qp *i40iw_ieq_get_qp(struct i40iw_sc_dev *dev, struct i40iw_puda_buf *buf)

    get qp based on quad in puda buffer

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param buf:
        receive puda buffer on exception q
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_ieq_update_tcpip_info`:

i40iw_ieq_update_tcpip_info
===========================

.. c:function:: void i40iw_ieq_update_tcpip_info(struct i40iw_puda_buf *buf, u16 length, u32 seqnum)

    update tcpip in the buffer

    :param buf:
        puda to update
    :type buf: struct i40iw_puda_buf \*

    :param length:
        length of buffer
    :type length: u16

    :param seqnum:
        seq number for tcp
    :type seqnum: u32

.. _`i40iw_puda_get_tcpip_info`:

i40iw_puda_get_tcpip_info
=========================

.. c:function:: enum i40iw_status_code i40iw_puda_get_tcpip_info(struct i40iw_puda_completion_info *info, struct i40iw_puda_buf *buf)

    get tcpip info from puda buffer

    :param info:
        to get information
    :type info: struct i40iw_puda_completion_info \*

    :param buf:
        puda buffer
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_hw_stats_timeout`:

i40iw_hw_stats_timeout
======================

.. c:function:: void i40iw_hw_stats_timeout(struct timer_list *t)

    Stats timer-handler which updates all HW stats

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`i40iw_hw_stats_start_timer`:

i40iw_hw_stats_start_timer
==========================

.. c:function:: void i40iw_hw_stats_start_timer(struct i40iw_sc_vsi *vsi)

    Start periodic stats timer

    :param vsi:
        pointer to the vsi structure
    :type vsi: struct i40iw_sc_vsi \*

.. _`i40iw_hw_stats_stop_timer`:

i40iw_hw_stats_stop_timer
=========================

.. c:function:: void i40iw_hw_stats_stop_timer(struct i40iw_sc_vsi *vsi)

    Delete periodic stats timer

    :param vsi:
        pointer to the vsi structure
    :type vsi: struct i40iw_sc_vsi \*

.. This file was automatic generated / don't edit.

