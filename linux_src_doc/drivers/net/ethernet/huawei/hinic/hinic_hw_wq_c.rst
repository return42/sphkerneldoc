.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_wq.c

.. _`queue_alloc_page`:

queue_alloc_page
================

.. c:function:: int queue_alloc_page(struct hinic_hwif *hwif, u64 **vaddr, u64 *paddr, void ***shadow_vaddr, size_t page_sz)

    allocate page for Queue

    :param hwif:
        HW interface for allocating DMA
    :type hwif: struct hinic_hwif \*

    :param vaddr:
        virtual address will be returned in this address
    :type vaddr: u64 \*\*

    :param paddr:
        physical address will be returned in this address
    :type paddr: u64 \*

    :param shadow_vaddr:
        VM area will be return here for holding WQ page addresses
    :type shadow_vaddr: void \*\*\*

    :param page_sz:
        page size of each WQ page
    :type page_sz: size_t

.. _`queue_alloc_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`wqs_allocate_page`:

wqs_allocate_page
=================

.. c:function:: int wqs_allocate_page(struct hinic_wqs *wqs, int page_idx)

    allocate page for WQ set

    :param wqs:
        Work Queue Set
    :type wqs: struct hinic_wqs \*

    :param page_idx:
        the page index of the page will be allocated
    :type page_idx: int

.. _`wqs_allocate_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`wqs_free_page`:

wqs_free_page
=============

.. c:function:: void wqs_free_page(struct hinic_wqs *wqs, int page_idx)

    free page of WQ set

    :param wqs:
        Work Queue Set
    :type wqs: struct hinic_wqs \*

    :param page_idx:
        the page index of the page will be freed
    :type page_idx: int

.. _`cmdq_allocate_page`:

cmdq_allocate_page
==================

.. c:function:: int cmdq_allocate_page(struct hinic_cmdq_pages *cmdq_pages)

    allocate page for cmdq

    :param cmdq_pages:
        the pages of the cmdq queue struct to hold the page
    :type cmdq_pages: struct hinic_cmdq_pages \*

.. _`cmdq_allocate_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`cmdq_free_page`:

cmdq_free_page
==============

.. c:function:: void cmdq_free_page(struct hinic_cmdq_pages *cmdq_pages)

    free page from cmdq

    :param cmdq_pages:
        the pages of the cmdq queue struct that hold the page
    :type cmdq_pages: struct hinic_cmdq_pages \*

.. _`cmdq_free_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wqs_alloc`:

hinic_wqs_alloc
===============

.. c:function:: int hinic_wqs_alloc(struct hinic_wqs *wqs, int max_wqs, struct hinic_hwif *hwif)

    allocate Work Queues set

    :param wqs:
        Work Queue Set
    :type wqs: struct hinic_wqs \*

    :param max_wqs:
        maximum wqs to allocate
    :type max_wqs: int

    :param hwif:
        HW interface for use for the allocation
    :type hwif: struct hinic_hwif \*

.. _`hinic_wqs_alloc.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wqs_free`:

hinic_wqs_free
==============

.. c:function:: void hinic_wqs_free(struct hinic_wqs *wqs)

    free Work Queues set

    :param wqs:
        Work Queue Set
    :type wqs: struct hinic_wqs \*

.. _`alloc_wqes_shadow`:

alloc_wqes_shadow
=================

.. c:function:: int alloc_wqes_shadow(struct hinic_wq *wq)

    allocate WQE shadows for WQ

    :param wq:
        WQ to allocate shadows for
    :type wq: struct hinic_wq \*

.. _`alloc_wqes_shadow.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_wqes_shadow`:

free_wqes_shadow
================

.. c:function:: void free_wqes_shadow(struct hinic_wq *wq)

    free WQE shadows of WQ

    :param wq:
        WQ to free shadows from
    :type wq: struct hinic_wq \*

.. _`free_wq_pages`:

free_wq_pages
=============

.. c:function:: void free_wq_pages(struct hinic_wq *wq, struct hinic_hwif *hwif, int num_q_pages)

    free pages of WQ

    :param wq:
        WQ to free pages from
    :type wq: struct hinic_wq \*

    :param hwif:
        HW interface for releasing dma addresses
    :type hwif: struct hinic_hwif \*

    :param num_q_pages:
        number pages to free
    :type num_q_pages: int

.. _`alloc_wq_pages`:

alloc_wq_pages
==============

.. c:function:: int alloc_wq_pages(struct hinic_wq *wq, struct hinic_hwif *hwif, int max_pages)

    alloc pages for WQ

    :param wq:
        WQ to allocate pages for
    :type wq: struct hinic_wq \*

    :param hwif:
        HW interface for allocating dma addresses
    :type hwif: struct hinic_hwif \*

    :param max_pages:
        maximum pages allowed
    :type max_pages: int

.. _`alloc_wq_pages.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wq_allocate`:

hinic_wq_allocate
=================

.. c:function:: int hinic_wq_allocate(struct hinic_wqs *wqs, struct hinic_wq *wq, u16 wqebb_size, u16 wq_page_size, u16 q_depth, u16 max_wqe_size)

    Allocate the WQ resources from the WQS

    :param wqs:
        WQ set from which to allocate the WQ resources
    :type wqs: struct hinic_wqs \*

    :param wq:
        WQ to allocate resources for it from the WQ set
    :type wq: struct hinic_wq \*

    :param wqebb_size:
        Work Queue Block Byte Size
    :type wqebb_size: u16

    :param wq_page_size:
        the page size in the Work Queue
    :type wq_page_size: u16

    :param q_depth:
        number of wqebbs in WQ
    :type q_depth: u16

    :param max_wqe_size:
        maximum WQE size that will be used in the WQ
    :type max_wqe_size: u16

.. _`hinic_wq_allocate.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wq_free`:

hinic_wq_free
=============

.. c:function:: void hinic_wq_free(struct hinic_wqs *wqs, struct hinic_wq *wq)

    Free the WQ resources to the WQS

    :param wqs:
        WQ set to free the WQ resources to it
    :type wqs: struct hinic_wqs \*

    :param wq:
        WQ to free its resources to the WQ set resources
    :type wq: struct hinic_wq \*

.. _`hinic_wqs_cmdq_alloc`:

hinic_wqs_cmdq_alloc
====================

.. c:function:: int hinic_wqs_cmdq_alloc(struct hinic_cmdq_pages *cmdq_pages, struct hinic_wq *wq, struct hinic_hwif *hwif, int cmdq_blocks, u16 wqebb_size, u16 wq_page_size, u16 q_depth, u16 max_wqe_size)

    Allocate wqs for cmdqs

    :param cmdq_pages:
        will hold the pages of the cmdq
    :type cmdq_pages: struct hinic_cmdq_pages \*

    :param wq:
        returned wqs
    :type wq: struct hinic_wq \*

    :param hwif:
        HW interface
    :type hwif: struct hinic_hwif \*

    :param cmdq_blocks:
        number of cmdq blocks/wq to allocate
    :type cmdq_blocks: int

    :param wqebb_size:
        Work Queue Block Byte Size
    :type wqebb_size: u16

    :param wq_page_size:
        the page size in the Work Queue
    :type wq_page_size: u16

    :param q_depth:
        number of wqebbs in WQ
    :type q_depth: u16

    :param max_wqe_size:
        maximum WQE size that will be used in the WQ
    :type max_wqe_size: u16

.. _`hinic_wqs_cmdq_alloc.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wqs_cmdq_free`:

hinic_wqs_cmdq_free
===================

.. c:function:: void hinic_wqs_cmdq_free(struct hinic_cmdq_pages *cmdq_pages, struct hinic_wq *wq, int cmdq_blocks)

    Free wqs from cmdqs

    :param cmdq_pages:
        hold the pages of the cmdq
    :type cmdq_pages: struct hinic_cmdq_pages \*

    :param wq:
        wqs to free
    :type wq: struct hinic_wq \*

    :param cmdq_blocks:
        number of wqs to free
    :type cmdq_blocks: int

.. _`hinic_get_wqe`:

hinic_get_wqe
=============

.. c:function:: struct hinic_hw_wqe *hinic_get_wqe(struct hinic_wq *wq, unsigned int wqe_size, u16 *prod_idx)

    get wqe ptr in the current pi and update the pi

    :param wq:
        wq to get wqe from
    :type wq: struct hinic_wq \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

    :param prod_idx:
        returned pi
    :type prod_idx: u16 \*

.. _`hinic_get_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_return_wqe`:

hinic_return_wqe
================

.. c:function:: void hinic_return_wqe(struct hinic_wq *wq, unsigned int wqe_size)

    return the wqe when transmit failed

    :param wq:
        wq to return wqe
    :type wq: struct hinic_wq \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

.. _`hinic_put_wqe`:

hinic_put_wqe
=============

.. c:function:: void hinic_put_wqe(struct hinic_wq *wq, unsigned int wqe_size)

    return the wqe place to use for a new wqe

    :param wq:
        wq to return wqe
    :type wq: struct hinic_wq \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

.. _`hinic_read_wqe`:

hinic_read_wqe
==============

.. c:function:: struct hinic_hw_wqe *hinic_read_wqe(struct hinic_wq *wq, unsigned int wqe_size, u16 *cons_idx)

    read wqe ptr in the current ci

    :param wq:
        wq to get read from
    :type wq: struct hinic_wq \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

    :param cons_idx:
        returned ci
    :type cons_idx: u16 \*

.. _`hinic_read_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_read_wqe_direct`:

hinic_read_wqe_direct
=====================

.. c:function:: struct hinic_hw_wqe *hinic_read_wqe_direct(struct hinic_wq *wq, u16 cons_idx)

    read wqe directly from ci position

    :param wq:
        wq
    :type wq: struct hinic_wq \*

    :param cons_idx:
        ci position
    :type cons_idx: u16

.. _`hinic_read_wqe_direct.description`:

Description
-----------

Return wqe

.. _`wqe_shadow`:

wqe_shadow
==========

.. c:function:: bool wqe_shadow(struct hinic_wq *wq, struct hinic_hw_wqe *wqe)

    check if a wqe is shadow

    :param wq:
        wq of the wqe
    :type wq: struct hinic_wq \*

    :param wqe:
        the wqe for shadow checking
    :type wqe: struct hinic_hw_wqe \*

.. _`wqe_shadow.description`:

Description
-----------

Return true - shadow, false - Not shadow

.. _`hinic_write_wqe`:

hinic_write_wqe
===============

.. c:function:: void hinic_write_wqe(struct hinic_wq *wq, struct hinic_hw_wqe *wqe, unsigned int wqe_size)

    write the wqe to the wq

    :param wq:
        wq to write wqe to
    :type wq: struct hinic_wq \*

    :param wqe:
        wqe to write
    :type wqe: struct hinic_hw_wqe \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

.. This file was automatic generated / don't edit.

