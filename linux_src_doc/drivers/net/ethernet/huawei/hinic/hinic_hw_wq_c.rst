.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_wq.c

.. _`queue_alloc_page`:

queue_alloc_page
================

.. c:function:: int queue_alloc_page(struct hinic_hwif *hwif, u64 **vaddr, u64 *paddr, void ***shadow_vaddr, size_t page_sz)

    allocate page for Queue

    :param struct hinic_hwif \*hwif:
        HW interface for allocating DMA

    :param u64 \*\*vaddr:
        virtual address will be returned in this address

    :param u64 \*paddr:
        physical address will be returned in this address

    :param void \*\*\*shadow_vaddr:
        VM area will be return here for holding WQ page addresses

    :param size_t page_sz:
        page size of each WQ page

.. _`queue_alloc_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`wqs_allocate_page`:

wqs_allocate_page
=================

.. c:function:: int wqs_allocate_page(struct hinic_wqs *wqs, int page_idx)

    allocate page for WQ set

    :param struct hinic_wqs \*wqs:
        Work Queue Set

    :param int page_idx:
        the page index of the page will be allocated

.. _`wqs_allocate_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`wqs_free_page`:

wqs_free_page
=============

.. c:function:: void wqs_free_page(struct hinic_wqs *wqs, int page_idx)

    free page of WQ set

    :param struct hinic_wqs \*wqs:
        Work Queue Set

    :param int page_idx:
        the page index of the page will be freed

.. _`cmdq_allocate_page`:

cmdq_allocate_page
==================

.. c:function:: int cmdq_allocate_page(struct hinic_cmdq_pages *cmdq_pages)

    allocate page for cmdq

    :param struct hinic_cmdq_pages \*cmdq_pages:
        the pages of the cmdq queue struct to hold the page

.. _`cmdq_allocate_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`cmdq_free_page`:

cmdq_free_page
==============

.. c:function:: void cmdq_free_page(struct hinic_cmdq_pages *cmdq_pages)

    free page from cmdq

    :param struct hinic_cmdq_pages \*cmdq_pages:
        the pages of the cmdq queue struct that hold the page

.. _`cmdq_free_page.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wqs_alloc`:

hinic_wqs_alloc
===============

.. c:function:: int hinic_wqs_alloc(struct hinic_wqs *wqs, int max_wqs, struct hinic_hwif *hwif)

    allocate Work Queues set

    :param struct hinic_wqs \*wqs:
        Work Queue Set

    :param int max_wqs:
        maximum wqs to allocate

    :param struct hinic_hwif \*hwif:
        HW interface for use for the allocation

.. _`hinic_wqs_alloc.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wqs_free`:

hinic_wqs_free
==============

.. c:function:: void hinic_wqs_free(struct hinic_wqs *wqs)

    free Work Queues set

    :param struct hinic_wqs \*wqs:
        Work Queue Set

.. _`alloc_wqes_shadow`:

alloc_wqes_shadow
=================

.. c:function:: int alloc_wqes_shadow(struct hinic_wq *wq)

    allocate WQE shadows for WQ

    :param struct hinic_wq \*wq:
        WQ to allocate shadows for

.. _`alloc_wqes_shadow.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_wqes_shadow`:

free_wqes_shadow
================

.. c:function:: void free_wqes_shadow(struct hinic_wq *wq)

    free WQE shadows of WQ

    :param struct hinic_wq \*wq:
        WQ to free shadows from

.. _`free_wq_pages`:

free_wq_pages
=============

.. c:function:: void free_wq_pages(struct hinic_wq *wq, struct hinic_hwif *hwif, int num_q_pages)

    free pages of WQ

    :param struct hinic_wq \*wq:
        WQ to free pages from

    :param struct hinic_hwif \*hwif:
        HW interface for releasing dma addresses

    :param int num_q_pages:
        number pages to free

.. _`alloc_wq_pages`:

alloc_wq_pages
==============

.. c:function:: int alloc_wq_pages(struct hinic_wq *wq, struct hinic_hwif *hwif, int max_pages)

    alloc pages for WQ

    :param struct hinic_wq \*wq:
        WQ to allocate pages for

    :param struct hinic_hwif \*hwif:
        HW interface for allocating dma addresses

    :param int max_pages:
        maximum pages allowed

.. _`alloc_wq_pages.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wq_allocate`:

hinic_wq_allocate
=================

.. c:function:: int hinic_wq_allocate(struct hinic_wqs *wqs, struct hinic_wq *wq, u16 wqebb_size, u16 wq_page_size, u16 q_depth, u16 max_wqe_size)

    Allocate the WQ resources from the WQS

    :param struct hinic_wqs \*wqs:
        WQ set from which to allocate the WQ resources

    :param struct hinic_wq \*wq:
        WQ to allocate resources for it from the WQ set

    :param u16 wqebb_size:
        Work Queue Block Byte Size

    :param u16 wq_page_size:
        the page size in the Work Queue

    :param u16 q_depth:
        number of wqebbs in WQ

    :param u16 max_wqe_size:
        maximum WQE size that will be used in the WQ

.. _`hinic_wq_allocate.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wq_free`:

hinic_wq_free
=============

.. c:function:: void hinic_wq_free(struct hinic_wqs *wqs, struct hinic_wq *wq)

    Free the WQ resources to the WQS

    :param struct hinic_wqs \*wqs:
        WQ set to free the WQ resources to it

    :param struct hinic_wq \*wq:
        WQ to free its resources to the WQ set resources

.. _`hinic_wqs_cmdq_alloc`:

hinic_wqs_cmdq_alloc
====================

.. c:function:: int hinic_wqs_cmdq_alloc(struct hinic_cmdq_pages *cmdq_pages, struct hinic_wq *wq, struct hinic_hwif *hwif, int cmdq_blocks, u16 wqebb_size, u16 wq_page_size, u16 q_depth, u16 max_wqe_size)

    Allocate wqs for cmdqs

    :param struct hinic_cmdq_pages \*cmdq_pages:
        will hold the pages of the cmdq

    :param struct hinic_wq \*wq:
        returned wqs

    :param struct hinic_hwif \*hwif:
        HW interface

    :param int cmdq_blocks:
        number of cmdq blocks/wq to allocate

    :param u16 wqebb_size:
        Work Queue Block Byte Size

    :param u16 wq_page_size:
        the page size in the Work Queue

    :param u16 q_depth:
        number of wqebbs in WQ

    :param u16 max_wqe_size:
        maximum WQE size that will be used in the WQ

.. _`hinic_wqs_cmdq_alloc.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_wqs_cmdq_free`:

hinic_wqs_cmdq_free
===================

.. c:function:: void hinic_wqs_cmdq_free(struct hinic_cmdq_pages *cmdq_pages, struct hinic_wq *wq, int cmdq_blocks)

    Free wqs from cmdqs

    :param struct hinic_cmdq_pages \*cmdq_pages:
        hold the pages of the cmdq

    :param struct hinic_wq \*wq:
        wqs to free

    :param int cmdq_blocks:
        number of wqs to free

.. _`hinic_get_wqe`:

hinic_get_wqe
=============

.. c:function:: struct hinic_hw_wqe *hinic_get_wqe(struct hinic_wq *wq, unsigned int wqe_size, u16 *prod_idx)

    get wqe ptr in the current pi and update the pi

    :param struct hinic_wq \*wq:
        wq to get wqe from

    :param unsigned int wqe_size:
        wqe size

    :param u16 \*prod_idx:
        returned pi

.. _`hinic_get_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_put_wqe`:

hinic_put_wqe
=============

.. c:function:: void hinic_put_wqe(struct hinic_wq *wq, unsigned int wqe_size)

    return the wqe place to use for a new wqe

    :param struct hinic_wq \*wq:
        wq to return wqe

    :param unsigned int wqe_size:
        wqe size

.. _`hinic_read_wqe`:

hinic_read_wqe
==============

.. c:function:: struct hinic_hw_wqe *hinic_read_wqe(struct hinic_wq *wq, unsigned int wqe_size, u16 *cons_idx)

    read wqe ptr in the current ci

    :param struct hinic_wq \*wq:
        wq to get read from

    :param unsigned int wqe_size:
        wqe size

    :param u16 \*cons_idx:
        returned ci

.. _`hinic_read_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_read_wqe_direct`:

hinic_read_wqe_direct
=====================

.. c:function:: struct hinic_hw_wqe *hinic_read_wqe_direct(struct hinic_wq *wq, u16 cons_idx)

    read wqe directly from ci position

    :param struct hinic_wq \*wq:
        wq

    :param u16 cons_idx:
        ci position

.. _`hinic_read_wqe_direct.description`:

Description
-----------

Return wqe

.. _`wqe_shadow`:

wqe_shadow
==========

.. c:function:: bool wqe_shadow(struct hinic_wq *wq, struct hinic_hw_wqe *wqe)

    check if a wqe is shadow

    :param struct hinic_wq \*wq:
        wq of the wqe

    :param struct hinic_hw_wqe \*wqe:
        the wqe for shadow checking

.. _`wqe_shadow.description`:

Description
-----------

Return true - shadow, false - Not shadow

.. _`hinic_write_wqe`:

hinic_write_wqe
===============

.. c:function:: void hinic_write_wqe(struct hinic_wq *wq, struct hinic_hw_wqe *wqe, unsigned int wqe_size)

    write the wqe to the wq

    :param struct hinic_wq \*wq:
        wq to write wqe to

    :param struct hinic_hw_wqe \*wqe:
        wqe to write

    :param unsigned int wqe_size:
        wqe size

.. This file was automatic generated / don't edit.

