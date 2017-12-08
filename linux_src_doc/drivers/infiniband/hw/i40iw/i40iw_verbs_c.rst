.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_verbs.c

.. _`i40iw_query_device`:

i40iw_query_device
==================

.. c:function:: int i40iw_query_device(struct ib_device *ibdev, struct ib_device_attr *props, struct ib_udata *udata)

    get device attributes

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param struct ib_device_attr \*props:
        returning device attributes

    :param struct ib_udata \*udata:
        user data

.. _`i40iw_query_port`:

i40iw_query_port
================

.. c:function:: int i40iw_query_port(struct ib_device *ibdev, u8 port, struct ib_port_attr *props)

    get port attrubutes

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param u8 port:
        port number for query

    :param struct ib_port_attr \*props:
        returning device attributes

.. _`i40iw_alloc_ucontext`:

i40iw_alloc_ucontext
====================

.. c:function:: struct ib_ucontext *i40iw_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    Allocate the user context data structure

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param struct ib_udata \*udata:
        user data

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

    :param struct ib_ucontext \*context:
        user context created during alloc

.. _`i40iw_mmap`:

i40iw_mmap
==========

.. c:function:: int i40iw_mmap(struct ib_ucontext *context, struct vm_area_struct *vma)

    user memory map

    :param struct ib_ucontext \*context:
        context created during alloc

    :param struct vm_area_struct \*vma:
        kernel info for user memory map

.. _`i40iw_alloc_push_page`:

i40iw_alloc_push_page
=====================

.. c:function:: void i40iw_alloc_push_page(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp)

    allocate a push page for qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

.. _`i40iw_dealloc_push_page`:

i40iw_dealloc_push_page
=======================

.. c:function:: void i40iw_dealloc_push_page(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp)

    free a push page for qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

.. _`i40iw_alloc_pd`:

i40iw_alloc_pd
==============

.. c:function:: struct ib_pd *i40iw_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    allocate protection domain

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param struct ib_ucontext \*context:
        user context created during alloc

    :param struct ib_udata \*udata:
        user data

.. _`i40iw_dealloc_pd`:

i40iw_dealloc_pd
================

.. c:function:: int i40iw_dealloc_pd(struct ib_pd *ibpd)

    deallocate pd

    :param struct ib_pd \*ibpd:
        ptr of pd to be deallocated

.. _`i40iw_get_pbl`:

i40iw_get_pbl
=============

.. c:function:: struct i40iw_pbl *i40iw_get_pbl(unsigned long va, struct list_head *pbl_list)

    Retrieve pbl from a list given a virtual address

    :param unsigned long va:
        user virtual address

    :param struct list_head \*pbl_list:
        pbl list to search in (QP's or CQ's)

.. _`i40iw_free_qp_resources`:

i40iw_free_qp_resources
=======================

.. c:function:: void i40iw_free_qp_resources(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, u32 qp_num)

    free up memory resources for qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_qp \*iwqp:
        qp ptr (user or kernel)

    :param u32 qp_num:
        qp number assigned

.. _`i40iw_clean_cqes`:

i40iw_clean_cqes
================

.. c:function:: void i40iw_clean_cqes(struct i40iw_qp *iwqp, struct i40iw_cq *iwcq)

    clean cq entries for qp

    :param struct i40iw_qp \*iwqp:
        qp ptr (user or kernel)

    :param struct i40iw_cq \*iwcq:
        cq ptr

.. _`i40iw_destroy_qp`:

i40iw_destroy_qp
================

.. c:function:: int i40iw_destroy_qp(struct ib_qp *ibqp)

    destroy qp

    :param struct ib_qp \*ibqp:
        qp's ib pointer also to get to device's qp address

.. _`i40iw_setup_virt_qp`:

i40iw_setup_virt_qp
===================

.. c:function:: int i40iw_setup_virt_qp(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, struct i40iw_qp_init_info *init_info)

    setup for allocation of virtual qp

    :param struct i40iw_device \*iwdev:
        *undescribed*

    :param struct i40iw_qp \*iwqp:
        *undescribed*

    :param struct i40iw_qp_init_info \*init_info:
        initialize info to return

.. _`i40iw_setup_kmode_qp`:

i40iw_setup_kmode_qp
====================

.. c:function:: int i40iw_setup_kmode_qp(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, struct i40iw_qp_init_info *info)

    setup initialization for kernel mode qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_qp \*iwqp:
        qp ptr (user or kernel)

    :param struct i40iw_qp_init_info \*info:
        initialize info to return

.. _`i40iw_create_qp`:

i40iw_create_qp
===============

.. c:function:: struct ib_qp *i40iw_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create qp

    :param struct ib_pd \*ibpd:
        ptr of pd

    :param struct ib_qp_init_attr \*init_attr:
        attributes for qp

    :param struct ib_udata \*udata:
        user data for create qp

.. _`i40iw_query_qp`:

i40iw_query_qp
==============

.. c:function:: int i40iw_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    query qp attributes

    :param struct ib_qp \*ibqp:
        qp pointer

    :param struct ib_qp_attr \*attr:
        attributes pointer

    :param int attr_mask:
        Not used

    :param struct ib_qp_init_attr \*init_attr:
        qp attributes to return

.. _`i40iw_hw_modify_qp`:

i40iw_hw_modify_qp
==================

.. c:function:: void i40iw_hw_modify_qp(struct i40iw_device *iwdev, struct i40iw_qp *iwqp, struct i40iw_modify_qp_info *info, bool wait)

    setup cqp for modify qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_qp \*iwqp:
        qp ptr (user or kernel)

    :param struct i40iw_modify_qp_info \*info:
        info for modify qp

    :param bool wait:
        flag to wait or not for modify qp completion

.. _`i40iw_modify_qp`:

i40iw_modify_qp
===============

.. c:function:: int i40iw_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    modify qp request

    :param struct ib_qp \*ibqp:
        qp's pointer for modify

    :param struct ib_qp_attr \*attr:
        access attributes

    :param int attr_mask:
        state mask

    :param struct ib_udata \*udata:
        user data

.. _`cq_free_resources`:

cq_free_resources
=================

.. c:function:: void cq_free_resources(struct i40iw_device *iwdev, struct i40iw_cq *iwcq)

    free up recources for cq

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_cq \*iwcq:
        cq ptr

.. _`i40iw_cq_wq_destroy`:

i40iw_cq_wq_destroy
===================

.. c:function:: void i40iw_cq_wq_destroy(struct i40iw_device *iwdev, struct i40iw_sc_cq *cq)

    send cq destroy cqp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_cq \*cq:
        hardware control cq

.. _`i40iw_destroy_cq`:

i40iw_destroy_cq
================

.. c:function:: int i40iw_destroy_cq(struct ib_cq *ib_cq)

    destroy cq

    :param struct ib_cq \*ib_cq:
        cq pointer

.. _`i40iw_create_cq`:

i40iw_create_cq
===============

.. c:function:: struct ib_cq *i40iw_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    create cq

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param const struct ib_cq_init_attr \*attr:
        attributes for cq

    :param struct ib_ucontext \*context:
        user context created during alloc

    :param struct ib_udata \*udata:
        user data

.. _`i40iw_get_user_access`:

i40iw_get_user_access
=====================

.. c:function:: u16 i40iw_get_user_access(int acc)

    get hw access from IB access

    :param int acc:
        IB access to return hw access

.. _`i40iw_free_stag`:

i40iw_free_stag
===============

.. c:function:: void i40iw_free_stag(struct i40iw_device *iwdev, u32 stag)

    free stag resource

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u32 stag:
        stag to free

.. _`i40iw_create_stag`:

i40iw_create_stag
=================

.. c:function:: u32 i40iw_create_stag(struct i40iw_device *iwdev)

    create random stag

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_next_pbl_addr`:

i40iw_next_pbl_addr
===================

.. c:function:: u64 *i40iw_next_pbl_addr(u64 *pbl, struct i40iw_pble_info **pinfo, u32 *idx)

    Get next pbl address

    :param u64 \*pbl:
        pointer to a pble

    :param struct i40iw_pble_info \*\*pinfo:
        info pointer

    :param u32 \*idx:
        index

.. _`i40iw_copy_user_pgaddrs`:

i40iw_copy_user_pgaddrs
=======================

.. c:function:: void i40iw_copy_user_pgaddrs(struct i40iw_mr *iwmr, u64 *pbl, enum i40iw_pble_level level)

    copy user page address to pble's os locally

    :param struct i40iw_mr \*iwmr:
        iwmr for IB's user page addresses

    :param u64 \*pbl:
        ple pointer to save 1 level or 0 level pble

    :param enum i40iw_pble_level level:
        indicated level 0, 1 or 2

.. _`i40iw_set_hugetlb_values`:

i40iw_set_hugetlb_values
========================

.. c:function:: void i40iw_set_hugetlb_values(u64 addr, struct i40iw_mr *iwmr)

    set MR pg size and mask to huge pg values.

    :param u64 addr:
        virtual address

    :param struct i40iw_mr \*iwmr:
        mr pointer for this memory registration

.. _`i40iw_check_mem_contiguous`:

i40iw_check_mem_contiguous
==========================

.. c:function:: bool i40iw_check_mem_contiguous(u64 *arr, u32 npages, u32 pg_size)

    check if pbls stored in arr are contiguous

    :param u64 \*arr:
        lvl1 pbl array

    :param u32 npages:
        page count

    :param u32 pg_size:
        *undescribed*

.. _`i40iw_check_mem_contiguous.pg_size`:

pg_size
-------

page size

.. _`i40iw_check_mr_contiguous`:

i40iw_check_mr_contiguous
=========================

.. c:function:: bool i40iw_check_mr_contiguous(struct i40iw_pble_alloc *palloc, u32 pg_size)

    check if MR is physically contiguous

    :param struct i40iw_pble_alloc \*palloc:
        pbl allocation struct

    :param u32 pg_size:
        *undescribed*

.. _`i40iw_check_mr_contiguous.pg_size`:

pg_size
-------

page size

.. _`i40iw_setup_pbles`:

i40iw_setup_pbles
=================

.. c:function:: int i40iw_setup_pbles(struct i40iw_device *iwdev, struct i40iw_mr *iwmr, bool use_pbles)

    copy user pg address to pble's

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_mr \*iwmr:
        mr pointer for this memory registration

    :param bool use_pbles:
        flag if to use pble's

.. _`i40iw_handle_q_mem`:

i40iw_handle_q_mem
==================

.. c:function:: int i40iw_handle_q_mem(struct i40iw_device *iwdev, struct i40iw_mem_reg_req *req, struct i40iw_pbl *iwpbl, bool use_pbles)

    handle memory for qp and cq

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_mem_reg_req \*req:
        information for q memory management

    :param struct i40iw_pbl \*iwpbl:
        pble struct

    :param bool use_pbles:
        flag to use pble

.. _`i40iw_hw_alloc_stag`:

i40iw_hw_alloc_stag
===================

.. c:function:: int i40iw_hw_alloc_stag(struct i40iw_device *iwdev, struct i40iw_mr *iwmr)

    cqp command to allocate stag

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_mr \*iwmr:
        iwarp mr pointer

.. _`i40iw_alloc_mr`:

i40iw_alloc_mr
==============

.. c:function:: struct ib_mr *i40iw_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    register stag for fast memory registration

    :param struct ib_pd \*pd:
        ibpd pointer

    :param enum ib_mr_type mr_type:
        memory for stag registrion

    :param u32 max_num_sg:
        man number of pages

.. _`i40iw_set_page`:

i40iw_set_page
==============

.. c:function:: int i40iw_set_page(struct ib_mr *ibmr, u64 addr)

    populate pbl list for fmr

    :param struct ib_mr \*ibmr:
        ib mem to access iwarp mr pointer

    :param u64 addr:
        page dma address fro pbl list

.. _`i40iw_map_mr_sg`:

i40iw_map_mr_sg
===============

.. c:function:: int i40iw_map_mr_sg(struct ib_mr *ibmr, struct scatterlist *sg, int sg_nents, unsigned int *sg_offset)

    map of sg list for fmr

    :param struct ib_mr \*ibmr:
        ib mem to access iwarp mr pointer

    :param struct scatterlist \*sg:
        scatter gather list for fmr

    :param int sg_nents:
        number of sg pages

    :param unsigned int \*sg_offset:
        *undescribed*

.. _`i40iw_drain_sq`:

i40iw_drain_sq
==============

.. c:function:: void i40iw_drain_sq(struct ib_qp *ibqp)

    drain the send queue

    :param struct ib_qp \*ibqp:
        ib qp pointer

.. _`i40iw_drain_rq`:

i40iw_drain_rq
==============

.. c:function:: void i40iw_drain_rq(struct ib_qp *ibqp)

    drain the receive queue

    :param struct ib_qp \*ibqp:
        ib qp pointer

.. _`i40iw_hwreg_mr`:

i40iw_hwreg_mr
==============

.. c:function:: int i40iw_hwreg_mr(struct i40iw_device *iwdev, struct i40iw_mr *iwmr, u16 access)

    send cqp command for memory registration

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_mr \*iwmr:
        iwarp mr pointer

    :param u16 access:
        access for MR

.. _`i40iw_reg_user_mr`:

i40iw_reg_user_mr
=================

.. c:function:: struct ib_mr *i40iw_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt, int acc, struct ib_udata *udata)

    Register a user memory region

    :param struct ib_pd \*pd:
        ptr of pd

    :param u64 start:
        virtual start address

    :param u64 length:
        length of mr

    :param u64 virt:
        virtual address

    :param int acc:
        access of mr

    :param struct ib_udata \*udata:
        user data

.. _`i40iw_reg_phys_mr`:

i40iw_reg_phys_mr
=================

.. c:function:: struct ib_mr *i40iw_reg_phys_mr(struct ib_pd *pd, u64 addr, u64 size, int acc, u64 *iova_start)

    register kernel physical memory

    :param struct ib_pd \*pd:
        ibpd pointer

    :param u64 addr:
        physical address of memory to register

    :param u64 size:
        size of memory to register

    :param int acc:
        Access rights

    :param u64 \*iova_start:
        start of virtual address for physical buffers

.. _`i40iw_get_dma_mr`:

i40iw_get_dma_mr
================

.. c:function:: struct ib_mr *i40iw_get_dma_mr(struct ib_pd *pd, int acc)

    register physical mem

    :param struct ib_pd \*pd:
        ptr of pd

    :param int acc:
        access for memory

.. _`i40iw_del_memlist`:

i40iw_del_memlist
=================

.. c:function:: void i40iw_del_memlist(struct i40iw_mr *iwmr, struct i40iw_ucontext *ucontext)

    Deleting pbl list entries for CQ/QP

    :param struct i40iw_mr \*iwmr:
        iwmr for IB's user page addresses

    :param struct i40iw_ucontext \*ucontext:
        ptr to user context

.. _`i40iw_dereg_mr`:

i40iw_dereg_mr
==============

.. c:function:: int i40iw_dereg_mr(struct ib_mr *ib_mr)

    deregister mr

    :param struct ib_mr \*ib_mr:
        mr ptr for dereg

.. _`i40iw_show_rev`:

i40iw_show_rev
==============

.. c:function:: ssize_t i40iw_show_rev(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`i40iw_show_hca`:

i40iw_show_hca
==============

.. c:function:: ssize_t i40iw_show_hca(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`i40iw_show_board`:

i40iw_show_board
================

.. c:function:: ssize_t i40iw_show_board(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`i40iw_copy_sg_list`:

i40iw_copy_sg_list
==================

.. c:function:: void i40iw_copy_sg_list(struct i40iw_sge *sg_list, struct ib_sge *sgl, int num_sges)

    copy sg list for qp

    :param struct i40iw_sge \*sg_list:
        copied into sg_list

    :param struct ib_sge \*sgl:
        copy from sgl

    :param int num_sges:
        count of sg entries

.. _`i40iw_post_send`:

i40iw_post_send
===============

.. c:function:: int i40iw_post_send(struct ib_qp *ibqp, struct ib_send_wr *ib_wr, struct ib_send_wr **bad_wr)

    kernel application wr

    :param struct ib_qp \*ibqp:
        qp ptr for wr

    :param struct ib_send_wr \*ib_wr:
        work request ptr

    :param struct ib_send_wr \*\*bad_wr:
        return of bad wr if err

.. _`i40iw_post_recv`:

i40iw_post_recv
===============

.. c:function:: int i40iw_post_recv(struct ib_qp *ibqp, struct ib_recv_wr *ib_wr, struct ib_recv_wr **bad_wr)

    post receive wr for kernel application

    :param struct ib_qp \*ibqp:
        ib qp pointer

    :param struct ib_recv_wr \*ib_wr:
        work request for receive

    :param struct ib_recv_wr \*\*bad_wr:
        bad wr caused an error

.. _`i40iw_poll_cq`:

i40iw_poll_cq
=============

.. c:function:: int i40iw_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *entry)

    poll cq for completion (kernel apps)

    :param struct ib_cq \*ibcq:
        cq to poll

    :param int num_entries:
        number of entries to poll

    :param struct ib_wc \*entry:
        wr of entry completed

.. _`i40iw_req_notify_cq`:

i40iw_req_notify_cq
===================

.. c:function:: int i40iw_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    arm cq kernel application

    :param struct ib_cq \*ibcq:
        cq to arm

    :param enum ib_cq_notify_flags notify_flags:
        notofication flags

.. _`i40iw_port_immutable`:

i40iw_port_immutable
====================

.. c:function:: int i40iw_port_immutable(struct ib_device *ibdev, u8 port_num, struct ib_port_immutable *immutable)

    return port's immutable data

    :param struct ib_device \*ibdev:
        ib dev struct

    :param u8 port_num:
        port number

    :param struct ib_port_immutable \*immutable:
        immutable data for the port return

.. _`i40iw_alloc_hw_stats`:

i40iw_alloc_hw_stats
====================

.. c:function:: struct rdma_hw_stats *i40iw_alloc_hw_stats(struct ib_device *ibdev, u8 port_num)

    Allocate a hw stats structure

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param u8 port_num:
        port number

.. _`i40iw_get_hw_stats`:

i40iw_get_hw_stats
==================

.. c:function:: int i40iw_get_hw_stats(struct ib_device *ibdev, struct rdma_hw_stats *stats, u8 port_num, int index)

    Populates the rdma_hw_stats structure

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param struct rdma_hw_stats \*stats:
        stats pointer from stack

    :param u8 port_num:
        port number

    :param int index:
        which hw counter the stack is requesting we update

.. _`i40iw_query_gid`:

i40iw_query_gid
===============

.. c:function:: int i40iw_query_gid(struct ib_device *ibdev, u8 port, int index, union ib_gid *gid)

    Query port GID

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param u8 port:
        port number

    :param int index:
        Entry index

    :param union ib_gid \*gid:
        Global ID

.. _`i40iw_modify_port`:

i40iw_modify_port
=================

.. c:function:: int i40iw_modify_port(struct ib_device *ibdev, u8 port, int port_modify_mask, struct ib_port_modify *props)

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param u8 port:
        port number

    :param int port_modify_mask:
        mask for port modifications

    :param struct ib_port_modify \*props:
        port properties

.. _`i40iw_query_pkey`:

i40iw_query_pkey
================

.. c:function:: int i40iw_query_pkey(struct ib_device *ibdev, u8 port, u16 index, u16 *pkey)

    Query partition key

    :param struct ib_device \*ibdev:
        device pointer from stack

    :param u8 port:
        port number

    :param u16 index:
        index of pkey

    :param u16 \*pkey:
        pointer to store the pkey

.. _`i40iw_create_ah`:

i40iw_create_ah
===============

.. c:function:: struct ib_ah *i40iw_create_ah(struct ib_pd *ibpd, struct rdma_ah_attr *attr, struct ib_udata *udata)

    create address handle

    :param struct ib_pd \*ibpd:
        ptr of pd

    :param struct rdma_ah_attr \*attr:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`i40iw_destroy_ah`:

i40iw_destroy_ah
================

.. c:function:: int i40iw_destroy_ah(struct ib_ah *ah)

    Destroy address handle

    :param struct ib_ah \*ah:
        pointer to address handle

.. _`i40iw_init_rdma_device`:

i40iw_init_rdma_device
======================

.. c:function:: struct i40iw_ib_device *i40iw_init_rdma_device(struct i40iw_device *iwdev)

    initialization of iwarp device

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_port_ibevent`:

i40iw_port_ibevent
==================

.. c:function:: void i40iw_port_ibevent(struct i40iw_device *iwdev)

    indicate port event

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_unregister_rdma_device`:

i40iw_unregister_rdma_device
============================

.. c:function:: void i40iw_unregister_rdma_device(struct i40iw_ib_device *iwibdev)

    unregister of iwarp from IB

    :param struct i40iw_ib_device \*iwibdev:
        rdma device ptr

.. _`i40iw_destroy_rdma_device`:

i40iw_destroy_rdma_device
=========================

.. c:function:: void i40iw_destroy_rdma_device(struct i40iw_ib_device *iwibdev)

    destroy rdma device and free resources

    :param struct i40iw_ib_device \*iwibdev:
        IB device ptr

.. _`i40iw_register_rdma_device`:

i40iw_register_rdma_device
==========================

.. c:function:: int i40iw_register_rdma_device(struct i40iw_device *iwdev)

    register iwarp device to IB

    :param struct i40iw_device \*iwdev:
        iwarp device

.. This file was automatic generated / don't edit.

