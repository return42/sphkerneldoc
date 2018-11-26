.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_verbs.c

.. _`i40iw_query_device`:

i40iw_query_device
==================

.. c:function:: int i40iw_query_device(struct ib_device *ibdev, struct ib_device_attr *props, struct ib_udata *udata)

    get device attributes

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param props:
        returning device attributes
    :type props: struct ib_device_attr \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`i40iw_query_port`:

i40iw_query_port
================

.. c:function:: int i40iw_query_port(struct ib_device *ibdev, u8 port, struct ib_port_attr *props)

    get port attrubutes

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param port:
        port number for query
    :type port: u8

    :param props:
        returning device attributes
    :type props: struct ib_port_attr \*

.. _`i40iw_alloc_ucontext`:

i40iw_alloc_ucontext
====================

.. c:function:: struct ib_ucontext *i40iw_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    Allocate the user context data structure

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`i40iw_alloc_ucontext.description`:

Description
-----------

This keeps track of all objects associated with a particular
user-mode client.

.. _`i40iw_dealloc_ucontext`:

i40iw_dealloc_ucontext
======================

.. c:function:: int i40iw_dealloc_ucontext(struct ib_ucontext *context)

    deallocate the user context data structure

    :param context:
        user context created during alloc
    :type context: struct ib_ucontext \*

.. _`i40iw_mmap`:

i40iw_mmap
==========

.. c:function:: int i40iw_mmap(struct ib_ucontext *context, struct vm_area_struct *vma)

    user memory map

    :param context:
        context created during alloc
    :type context: struct ib_ucontext \*

    :param vma:
        kernel info for user memory map
    :type vma: struct vm_area_struct \*

.. _`i40iw_alloc_push_page`:

i40iw_alloc_push_page
=====================

.. c:function:: void i40iw_alloc_push_page(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp)

    allocate a push page for qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_dealloc_push_page`:

i40iw_dealloc_push_page
=======================

.. c:function:: void i40iw_dealloc_push_page(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp)

    free a push page for qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_alloc_pd`:

i40iw_alloc_pd
==============

.. c:function:: struct ib_pd *i40iw_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    allocate protection domain

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param context:
        user context created during alloc
    :type context: struct ib_ucontext \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`i40iw_dealloc_pd`:

i40iw_dealloc_pd
================

.. c:function:: int i40iw_dealloc_pd(struct ib_pd *ibpd)

    deallocate pd

    :param ibpd:
        ptr of pd to be deallocated
    :type ibpd: struct ib_pd \*

.. _`i40iw_get_pbl`:

i40iw_get_pbl
=============

.. c:function:: struct i40iw_pbl *i40iw_get_pbl(unsigned long va, struct list_head *pbl_list)

    Retrieve pbl from a list given a virtual address

    :param va:
        user virtual address
    :type va: unsigned long

    :param pbl_list:
        pbl list to search in (QP's or CQ's)
    :type pbl_list: struct list_head \*

.. _`i40iw_free_qp_resources`:

i40iw_free_qp_resources
=======================

.. c:function:: void i40iw_free_qp_resources(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, u32 qp_num)

    free up memory resources for qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwqp:
        qp ptr (user or kernel)
    :type iwqp: struct i40iw_qp \*

    :param qp_num:
        qp number assigned
    :type qp_num: u32

.. _`i40iw_clean_cqes`:

i40iw_clean_cqes
================

.. c:function:: void i40iw_clean_cqes(struct i40iw_qp *iwqp, struct i40iw_cq *iwcq)

    clean cq entries for qp

    :param iwqp:
        qp ptr (user or kernel)
    :type iwqp: struct i40iw_qp \*

    :param iwcq:
        cq ptr
    :type iwcq: struct i40iw_cq \*

.. _`i40iw_destroy_qp`:

i40iw_destroy_qp
================

.. c:function:: int i40iw_destroy_qp(struct ib_qp *ibqp)

    destroy qp

    :param ibqp:
        qp's ib pointer also to get to device's qp address
    :type ibqp: struct ib_qp \*

.. _`i40iw_setup_virt_qp`:

i40iw_setup_virt_qp
===================

.. c:function:: int i40iw_setup_virt_qp(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, struct i40iw_qp_init_info *init_info)

    setup for allocation of virtual qp

    :param iwdev:
        *undescribed*
    :type iwdev: struct i40iw_device \*

    :param iwqp:
        *undescribed*
    :type iwqp: struct i40iw_qp \*

    :param init_info:
        initialize info to return
    :type init_info: struct i40iw_qp_init_info \*

.. _`i40iw_setup_kmode_qp`:

i40iw_setup_kmode_qp
====================

.. c:function:: int i40iw_setup_kmode_qp(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, struct i40iw_qp_init_info *info)

    setup initialization for kernel mode qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwqp:
        qp ptr (user or kernel)
    :type iwqp: struct i40iw_qp \*

    :param info:
        initialize info to return
    :type info: struct i40iw_qp_init_info \*

.. _`i40iw_create_qp`:

i40iw_create_qp
===============

.. c:function:: struct ib_qp *i40iw_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create qp

    :param ibpd:
        ptr of pd
    :type ibpd: struct ib_pd \*

    :param init_attr:
        attributes for qp
    :type init_attr: struct ib_qp_init_attr \*

    :param udata:
        user data for create qp
    :type udata: struct ib_udata \*

.. _`i40iw_query_qp`:

i40iw_query_qp
==============

.. c:function:: int i40iw_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    query qp attributes

    :param ibqp:
        qp pointer
    :type ibqp: struct ib_qp \*

    :param attr:
        attributes pointer
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        Not used
    :type attr_mask: int

    :param init_attr:
        qp attributes to return
    :type init_attr: struct ib_qp_init_attr \*

.. _`i40iw_hw_modify_qp`:

i40iw_hw_modify_qp
==================

.. c:function:: void i40iw_hw_modify_qp(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, struct i40iw_modify_qp_info *info, bool wait)

    setup cqp for modify qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwqp:
        qp ptr (user or kernel)
    :type iwqp: struct i40iw_qp \*

    :param info:
        info for modify qp
    :type info: struct i40iw_modify_qp_info \*

    :param wait:
        flag to wait or not for modify qp completion
    :type wait: bool

.. _`i40iw_modify_qp`:

i40iw_modify_qp
===============

.. c:function:: int i40iw_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    modify qp request

    :param ibqp:
        qp's pointer for modify
    :type ibqp: struct ib_qp \*

    :param attr:
        access attributes
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        state mask
    :type attr_mask: int

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`cq_free_resources`:

cq_free_resources
=================

.. c:function:: void cq_free_resources(struct i40iw_device *iwdev, struct i40iw_cq *iwcq)

    free up recources for cq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwcq:
        cq ptr
    :type iwcq: struct i40iw_cq \*

.. _`i40iw_cq_wq_destroy`:

i40iw_cq_wq_destroy
===================

.. c:function:: void i40iw_cq_wq_destroy(struct i40iw_device *iwdev, struct i40iw_sc_cq *cq)

    send cq destroy cqp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param cq:
        hardware control cq
    :type cq: struct i40iw_sc_cq \*

.. _`i40iw_destroy_cq`:

i40iw_destroy_cq
================

.. c:function:: int i40iw_destroy_cq(struct ib_cq *ib_cq)

    destroy cq

    :param ib_cq:
        cq pointer
    :type ib_cq: struct ib_cq \*

.. _`i40iw_create_cq`:

i40iw_create_cq
===============

.. c:function:: struct ib_cq *i40iw_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    create cq

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param attr:
        attributes for cq
    :type attr: const struct ib_cq_init_attr \*

    :param context:
        user context created during alloc
    :type context: struct ib_ucontext \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`i40iw_get_user_access`:

i40iw_get_user_access
=====================

.. c:function:: u16 i40iw_get_user_access(int acc)

    get hw access from IB access

    :param acc:
        IB access to return hw access
    :type acc: int

.. _`i40iw_free_stag`:

i40iw_free_stag
===============

.. c:function:: void i40iw_free_stag(struct i40iw_device *iwdev, u32 stag)

    free stag resource

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param stag:
        stag to free
    :type stag: u32

.. _`i40iw_create_stag`:

i40iw_create_stag
=================

.. c:function:: u32 i40iw_create_stag(struct i40iw_device *iwdev)

    create random stag

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_next_pbl_addr`:

i40iw_next_pbl_addr
===================

.. c:function:: u64 *i40iw_next_pbl_addr(u64 *pbl, struct i40iw_pble_info **pinfo, u32 *idx)

    Get next pbl address

    :param pbl:
        pointer to a pble
    :type pbl: u64 \*

    :param pinfo:
        info pointer
    :type pinfo: struct i40iw_pble_info \*\*

    :param idx:
        index
    :type idx: u32 \*

.. _`i40iw_copy_user_pgaddrs`:

i40iw_copy_user_pgaddrs
=======================

.. c:function:: void i40iw_copy_user_pgaddrs(struct i40iw_mr *iwmr, u64 *pbl, enum i40iw_pble_level level)

    copy user page address to pble's os locally

    :param iwmr:
        iwmr for IB's user page addresses
    :type iwmr: struct i40iw_mr \*

    :param pbl:
        ple pointer to save 1 level or 0 level pble
    :type pbl: u64 \*

    :param level:
        indicated level 0, 1 or 2
    :type level: enum i40iw_pble_level

.. _`i40iw_set_hugetlb_values`:

i40iw_set_hugetlb_values
========================

.. c:function:: void i40iw_set_hugetlb_values(u64 addr, struct i40iw_mr *iwmr)

    set MR pg size and mask to huge pg values.

    :param addr:
        virtual address
    :type addr: u64

    :param iwmr:
        mr pointer for this memory registration
    :type iwmr: struct i40iw_mr \*

.. _`i40iw_check_mem_contiguous`:

i40iw_check_mem_contiguous
==========================

.. c:function:: bool i40iw_check_mem_contiguous(u64 *arr, u32 npages, u32 pg_size)

    check if pbls stored in arr are contiguous

    :param arr:
        lvl1 pbl array
    :type arr: u64 \*

    :param npages:
        page count
    :type npages: u32

    :param pg_size:
        *undescribed*
    :type pg_size: u32

.. _`i40iw_check_mem_contiguous.pg_size`:

pg_size
-------

page size

.. _`i40iw_check_mr_contiguous`:

i40iw_check_mr_contiguous
=========================

.. c:function:: bool i40iw_check_mr_contiguous(struct i40iw_pble_alloc *palloc, u32 pg_size)

    check if MR is physically contiguous

    :param palloc:
        pbl allocation struct
    :type palloc: struct i40iw_pble_alloc \*

    :param pg_size:
        *undescribed*
    :type pg_size: u32

.. _`i40iw_check_mr_contiguous.pg_size`:

pg_size
-------

page size

.. _`i40iw_setup_pbles`:

i40iw_setup_pbles
=================

.. c:function:: int i40iw_setup_pbles(struct i40iw_device *iwdev, struct i40iw_mr *iwmr, bool use_pbles)

    copy user pg address to pble's

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwmr:
        mr pointer for this memory registration
    :type iwmr: struct i40iw_mr \*

    :param use_pbles:
        flag if to use pble's
    :type use_pbles: bool

.. _`i40iw_handle_q_mem`:

i40iw_handle_q_mem
==================

.. c:function:: int i40iw_handle_q_mem(struct i40iw_device *iwdev, struct i40iw_mem_reg_req *req, struct i40iw_pbl *iwpbl, bool use_pbles)

    handle memory for qp and cq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param req:
        information for q memory management
    :type req: struct i40iw_mem_reg_req \*

    :param iwpbl:
        pble struct
    :type iwpbl: struct i40iw_pbl \*

    :param use_pbles:
        flag to use pble
    :type use_pbles: bool

.. _`i40iw_hw_alloc_stag`:

i40iw_hw_alloc_stag
===================

.. c:function:: int i40iw_hw_alloc_stag(struct i40iw_device *iwdev, struct i40iw_mr *iwmr)

    cqp command to allocate stag

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwmr:
        iwarp mr pointer
    :type iwmr: struct i40iw_mr \*

.. _`i40iw_alloc_mr`:

i40iw_alloc_mr
==============

.. c:function:: struct ib_mr *i40iw_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    register stag for fast memory registration

    :param pd:
        ibpd pointer
    :type pd: struct ib_pd \*

    :param mr_type:
        memory for stag registrion
    :type mr_type: enum ib_mr_type

    :param max_num_sg:
        man number of pages
    :type max_num_sg: u32

.. _`i40iw_set_page`:

i40iw_set_page
==============

.. c:function:: int i40iw_set_page(struct ib_mr *ibmr, u64 addr)

    populate pbl list for fmr

    :param ibmr:
        ib mem to access iwarp mr pointer
    :type ibmr: struct ib_mr \*

    :param addr:
        page dma address fro pbl list
    :type addr: u64

.. _`i40iw_map_mr_sg`:

i40iw_map_mr_sg
===============

.. c:function:: int i40iw_map_mr_sg(struct ib_mr *ibmr, struct scatterlist *sg, int sg_nents, unsigned int *sg_offset)

    map of sg list for fmr

    :param ibmr:
        ib mem to access iwarp mr pointer
    :type ibmr: struct ib_mr \*

    :param sg:
        scatter gather list for fmr
    :type sg: struct scatterlist \*

    :param sg_nents:
        number of sg pages
    :type sg_nents: int

    :param sg_offset:
        *undescribed*
    :type sg_offset: unsigned int \*

.. _`i40iw_drain_sq`:

i40iw_drain_sq
==============

.. c:function:: void i40iw_drain_sq(struct ib_qp *ibqp)

    drain the send queue

    :param ibqp:
        ib qp pointer
    :type ibqp: struct ib_qp \*

.. _`i40iw_drain_rq`:

i40iw_drain_rq
==============

.. c:function:: void i40iw_drain_rq(struct ib_qp *ibqp)

    drain the receive queue

    :param ibqp:
        ib qp pointer
    :type ibqp: struct ib_qp \*

.. _`i40iw_hwreg_mr`:

i40iw_hwreg_mr
==============

.. c:function:: int i40iw_hwreg_mr(struct i40iw_device *iwdev, struct i40iw_mr *iwmr, u16 access)

    send cqp command for memory registration

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwmr:
        iwarp mr pointer
    :type iwmr: struct i40iw_mr \*

    :param access:
        access for MR
    :type access: u16

.. _`i40iw_reg_user_mr`:

i40iw_reg_user_mr
=================

.. c:function:: struct ib_mr *i40iw_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt, int acc, struct ib_udata *udata)

    Register a user memory region

    :param pd:
        ptr of pd
    :type pd: struct ib_pd \*

    :param start:
        virtual start address
    :type start: u64

    :param length:
        length of mr
    :type length: u64

    :param virt:
        virtual address
    :type virt: u64

    :param acc:
        access of mr
    :type acc: int

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`i40iw_reg_phys_mr`:

i40iw_reg_phys_mr
=================

.. c:function:: struct ib_mr *i40iw_reg_phys_mr(struct ib_pd *pd, u64 addr, u64 size, int acc, u64 *iova_start)

    register kernel physical memory

    :param pd:
        ibpd pointer
    :type pd: struct ib_pd \*

    :param addr:
        physical address of memory to register
    :type addr: u64

    :param size:
        size of memory to register
    :type size: u64

    :param acc:
        Access rights
    :type acc: int

    :param iova_start:
        start of virtual address for physical buffers
    :type iova_start: u64 \*

.. _`i40iw_get_dma_mr`:

i40iw_get_dma_mr
================

.. c:function:: struct ib_mr *i40iw_get_dma_mr(struct ib_pd *pd, int acc)

    register physical mem

    :param pd:
        ptr of pd
    :type pd: struct ib_pd \*

    :param acc:
        access for memory
    :type acc: int

.. _`i40iw_del_memlist`:

i40iw_del_memlist
=================

.. c:function:: void i40iw_del_memlist(struct i40iw_mr *iwmr, struct i40iw_ucontext *ucontext)

    Deleting pbl list entries for CQ/QP

    :param iwmr:
        iwmr for IB's user page addresses
    :type iwmr: struct i40iw_mr \*

    :param ucontext:
        ptr to user context
    :type ucontext: struct i40iw_ucontext \*

.. _`i40iw_dereg_mr`:

i40iw_dereg_mr
==============

.. c:function:: int i40iw_dereg_mr(struct ib_mr *ib_mr)

    deregister mr

    :param ib_mr:
        mr ptr for dereg
    :type ib_mr: struct ib_mr \*

.. _`hw_rev_show`:

hw_rev_show
===========

.. c:function:: ssize_t hw_rev_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`hca_type_show`:

hca_type_show
=============

.. c:function:: ssize_t hca_type_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`board_id_show`:

board_id_show
=============

.. c:function:: ssize_t board_id_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`i40iw_copy_sg_list`:

i40iw_copy_sg_list
==================

.. c:function:: void i40iw_copy_sg_list(struct i40iw_sge *sg_list, struct ib_sge *sgl, int num_sges)

    copy sg list for qp

    :param sg_list:
        copied into sg_list
    :type sg_list: struct i40iw_sge \*

    :param sgl:
        copy from sgl
    :type sgl: struct ib_sge \*

    :param num_sges:
        count of sg entries
    :type num_sges: int

.. _`i40iw_post_send`:

i40iw_post_send
===============

.. c:function:: int i40iw_post_send(struct ib_qp *ibqp, const struct ib_send_wr *ib_wr, const struct ib_send_wr **bad_wr)

    kernel application wr

    :param ibqp:
        qp ptr for wr
    :type ibqp: struct ib_qp \*

    :param ib_wr:
        work request ptr
    :type ib_wr: const struct ib_send_wr \*

    :param bad_wr:
        return of bad wr if err
    :type bad_wr: const struct ib_send_wr \*\*

.. _`i40iw_post_recv`:

i40iw_post_recv
===============

.. c:function:: int i40iw_post_recv(struct ib_qp *ibqp, const struct ib_recv_wr *ib_wr, const struct ib_recv_wr **bad_wr)

    post receive wr for kernel application

    :param ibqp:
        ib qp pointer
    :type ibqp: struct ib_qp \*

    :param ib_wr:
        work request for receive
    :type ib_wr: const struct ib_recv_wr \*

    :param bad_wr:
        bad wr caused an error
    :type bad_wr: const struct ib_recv_wr \*\*

.. _`i40iw_poll_cq`:

i40iw_poll_cq
=============

.. c:function:: int i40iw_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *entry)

    poll cq for completion (kernel apps)

    :param ibcq:
        cq to poll
    :type ibcq: struct ib_cq \*

    :param num_entries:
        number of entries to poll
    :type num_entries: int

    :param entry:
        wr of entry completed
    :type entry: struct ib_wc \*

.. _`i40iw_req_notify_cq`:

i40iw_req_notify_cq
===================

.. c:function:: int i40iw_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    arm cq kernel application

    :param ibcq:
        cq to arm
    :type ibcq: struct ib_cq \*

    :param notify_flags:
        notofication flags
    :type notify_flags: enum ib_cq_notify_flags

.. _`i40iw_port_immutable`:

i40iw_port_immutable
====================

.. c:function:: int i40iw_port_immutable(struct ib_device *ibdev, u8 port_num, struct ib_port_immutable *immutable)

    return port's immutable data

    :param ibdev:
        ib dev struct
    :type ibdev: struct ib_device \*

    :param port_num:
        port number
    :type port_num: u8

    :param immutable:
        immutable data for the port return
    :type immutable: struct ib_port_immutable \*

.. _`i40iw_alloc_hw_stats`:

i40iw_alloc_hw_stats
====================

.. c:function:: struct rdma_hw_stats *i40iw_alloc_hw_stats(struct ib_device *ibdev, u8 port_num)

    Allocate a hw stats structure

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param port_num:
        port number
    :type port_num: u8

.. _`i40iw_get_hw_stats`:

i40iw_get_hw_stats
==================

.. c:function:: int i40iw_get_hw_stats(struct ib_device *ibdev, struct rdma_hw_stats *stats, u8 port_num, int index)

    Populates the rdma_hw_stats structure

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param stats:
        stats pointer from stack
    :type stats: struct rdma_hw_stats \*

    :param port_num:
        port number
    :type port_num: u8

    :param index:
        which hw counter the stack is requesting we update
    :type index: int

.. _`i40iw_query_gid`:

i40iw_query_gid
===============

.. c:function:: int i40iw_query_gid(struct ib_device *ibdev, u8 port, int index, union ib_gid *gid)

    Query port GID

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param port:
        port number
    :type port: u8

    :param index:
        Entry index
    :type index: int

    :param gid:
        Global ID
    :type gid: union ib_gid \*

.. _`i40iw_query_pkey`:

i40iw_query_pkey
================

.. c:function:: int i40iw_query_pkey(struct ib_device *ibdev, u8 port, u16 index, u16 *pkey)

    Query partition key

    :param ibdev:
        device pointer from stack
    :type ibdev: struct ib_device \*

    :param port:
        port number
    :type port: u8

    :param index:
        index of pkey
    :type index: u16

    :param pkey:
        pointer to store the pkey
    :type pkey: u16 \*

.. _`i40iw_get_vector_affinity`:

i40iw_get_vector_affinity
=========================

.. c:function:: const struct cpumask *i40iw_get_vector_affinity(struct ib_device *ibdev, int comp_vector)

    report IRQ affinity mask

    :param ibdev:
        IB device
    :type ibdev: struct ib_device \*

    :param comp_vector:
        completion vector index
    :type comp_vector: int

.. _`i40iw_init_rdma_device`:

i40iw_init_rdma_device
======================

.. c:function:: struct i40iw_ib_device *i40iw_init_rdma_device(struct i40iw_device *iwdev)

    initialization of iwarp device

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_port_ibevent`:

i40iw_port_ibevent
==================

.. c:function:: void i40iw_port_ibevent(struct i40iw_device *iwdev)

    indicate port event

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_destroy_rdma_device`:

i40iw_destroy_rdma_device
=========================

.. c:function:: void i40iw_destroy_rdma_device(struct i40iw_ib_device *iwibdev)

    destroy rdma device and free resources

    :param iwibdev:
        IB device ptr
    :type iwibdev: struct i40iw_ib_device \*

.. _`i40iw_register_rdma_device`:

i40iw_register_rdma_device
==========================

.. c:function:: int i40iw_register_rdma_device(struct i40iw_device *iwdev)

    register iwarp device to IB

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. This file was automatic generated / don't edit.

