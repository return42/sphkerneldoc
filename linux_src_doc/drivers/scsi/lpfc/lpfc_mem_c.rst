.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_mem.c

.. _`lpfc_mem_alloc`:

lpfc_mem_alloc
==============

.. c:function:: int lpfc_mem_alloc(struct lpfc_hba *phba, int align)

    create and allocate all PCI and memory pools

    :param phba:
        HBA to allocate pools for
    :type phba: struct lpfc_hba \*

    :param align:
        *undescribed*
    :type align: int

.. _`lpfc_mem_alloc.description`:

Description
-----------

Creates and allocates PCI pools lpfc_sg_dma_buf_pool,
lpfc_mbuf_pool, lpfc_hrb_pool.  Creates and allocates kmalloc-backed mempools
for LPFC_MBOXQ_t and lpfc_nodelist.  Also allocates the VPI bitmask.

.. _`lpfc_mem_alloc.notes`:

Notes
-----

Not interrupt-safe.  Must be called with no locks held.  If any
allocation fails, frees all successfully allocated memory before returning.

.. _`lpfc_mem_alloc.return`:

Return
------

0 on success
-ENOMEM on failure (if any memory allocations fail)

.. _`lpfc_mem_free`:

lpfc_mem_free
=============

.. c:function:: void lpfc_mem_free(struct lpfc_hba *phba)

    Frees memory allocated by lpfc_mem_alloc

    :param phba:
        HBA to free memory for
    :type phba: struct lpfc_hba \*

.. _`lpfc_mem_free.description`:

Description
-----------

Free the memory allocated by lpfc_mem_alloc routine. This
routine is a the counterpart of lpfc_mem_alloc.

.. _`lpfc_mem_free.return`:

Return
------

None

.. _`lpfc_mem_free_all`:

lpfc_mem_free_all
=================

.. c:function:: void lpfc_mem_free_all(struct lpfc_hba *phba)

    Frees all PCI and driver memory

    :param phba:
        HBA to free memory for
    :type phba: struct lpfc_hba \*

.. _`lpfc_mem_free_all.description`:

Description
-----------

Free memory from PCI and driver memory pools and also those
used : lpfc_sg_dma_buf_pool, lpfc_mbuf_pool, lpfc_hrb_pool. Frees
kmalloc-backed mempools for LPFC_MBOXQ_t and lpfc_nodelist. Also frees
the VPI bitmask.

.. _`lpfc_mem_free_all.return`:

Return
------

None

.. _`lpfc_mbuf_alloc`:

lpfc_mbuf_alloc
===============

.. c:function:: void *lpfc_mbuf_alloc(struct lpfc_hba *phba, int mem_flags, dma_addr_t *handle)

    Allocate an mbuf from the lpfc_mbuf_pool PCI pool

    :param phba:
        HBA which owns the pool to allocate from
    :type phba: struct lpfc_hba \*

    :param mem_flags:
        indicates if this is a priority (MEM_PRI) allocation
    :type mem_flags: int

    :param handle:
        used to return the DMA-mapped address of the mbuf
    :type handle: dma_addr_t \*

.. _`lpfc_mbuf_alloc.description`:

Description
-----------

Allocates a DMA-mapped buffer from the lpfc_mbuf_pool PCI pool.
Allocates from generic dma_pool_alloc function first and if that fails and
mem_flags has MEM_PRI set (the only defined flag), returns an mbuf from the
HBA's pool.

.. _`lpfc_mbuf_alloc.notes`:

Notes
-----

Not interrupt-safe.  Must be called with no locks held.  Takes
phba->hbalock.

.. _`lpfc_mbuf_alloc.return`:

Return
------

pointer to the allocated mbuf on success
NULL on failure

.. _`__lpfc_mbuf_free`:

\__lpfc_mbuf_free
=================

.. c:function:: void __lpfc_mbuf_free(struct lpfc_hba *phba, void *virt, dma_addr_t dma)

    Free an mbuf from the lpfc_mbuf_pool PCI pool (locked)

    :param phba:
        HBA which owns the pool to return to
    :type phba: struct lpfc_hba \*

    :param virt:
        mbuf to free
    :type virt: void \*

    :param dma:
        the DMA-mapped address of the lpfc_mbuf_pool to be freed
    :type dma: dma_addr_t

.. _`__lpfc_mbuf_free.description`:

Description
-----------

Returns an mbuf lpfc_mbuf_pool to the lpfc_mbuf_safety_pool if
it is below its max_count, frees the mbuf otherwise.

.. _`__lpfc_mbuf_free.notes`:

Notes
-----

Must be called with phba->hbalock held to synchronize access to
lpfc_mbuf_safety_pool.

.. _`__lpfc_mbuf_free.return`:

Return
------

None

.. _`lpfc_mbuf_free`:

lpfc_mbuf_free
==============

.. c:function:: void lpfc_mbuf_free(struct lpfc_hba *phba, void *virt, dma_addr_t dma)

    Free an mbuf from the lpfc_mbuf_pool PCI pool (unlocked)

    :param phba:
        HBA which owns the pool to return to
    :type phba: struct lpfc_hba \*

    :param virt:
        mbuf to free
    :type virt: void \*

    :param dma:
        the DMA-mapped address of the lpfc_mbuf_pool to be freed
    :type dma: dma_addr_t

.. _`lpfc_mbuf_free.description`:

Description
-----------

Returns an mbuf lpfc_mbuf_pool to the lpfc_mbuf_safety_pool if
it is below its max_count, frees the mbuf otherwise.

.. _`lpfc_mbuf_free.notes`:

Notes
-----

Takes phba->hbalock.  Can be called with or without other locks held.

.. _`lpfc_mbuf_free.return`:

Return
------

None

.. _`lpfc_nvmet_buf_alloc`:

lpfc_nvmet_buf_alloc
====================

.. c:function:: void *lpfc_nvmet_buf_alloc(struct lpfc_hba *phba, int mem_flags, dma_addr_t *handle)

    Allocate an nvmet_buf from the lpfc_sg_dma_buf_pool PCI pool

    :param phba:
        HBA which owns the pool to allocate from
    :type phba: struct lpfc_hba \*

    :param mem_flags:
        indicates if this is a priority (MEM_PRI) allocation
    :type mem_flags: int

    :param handle:
        used to return the DMA-mapped address of the nvmet_buf
    :type handle: dma_addr_t \*

.. _`lpfc_nvmet_buf_alloc.description`:

Description
-----------

Allocates a DMA-mapped buffer from the lpfc_sg_dma_buf_pool
PCI pool.  Allocates from generic dma_pool_alloc function.

.. _`lpfc_nvmet_buf_alloc.return`:

Return
------

pointer to the allocated nvmet_buf on success
NULL on failure

.. _`lpfc_nvmet_buf_free`:

lpfc_nvmet_buf_free
===================

.. c:function:: void lpfc_nvmet_buf_free(struct lpfc_hba *phba, void *virt, dma_addr_t dma)

    Free an nvmet_buf from the lpfc_sg_dma_buf_pool PCI pool

    :param phba:
        HBA which owns the pool to return to
    :type phba: struct lpfc_hba \*

    :param virt:
        nvmet_buf to free
    :type virt: void \*

    :param dma:
        the DMA-mapped address of the lpfc_sg_dma_buf_pool to be freed
    :type dma: dma_addr_t

.. _`lpfc_nvmet_buf_free.return`:

Return
------

None

.. _`lpfc_els_hbq_alloc`:

lpfc_els_hbq_alloc
==================

.. c:function:: struct hbq_dmabuf *lpfc_els_hbq_alloc(struct lpfc_hba *phba)

    Allocate an HBQ buffer

    :param phba:
        HBA to allocate HBQ buffer for
    :type phba: struct lpfc_hba \*

.. _`lpfc_els_hbq_alloc.description`:

Description
-----------

Allocates a DMA-mapped HBQ buffer from the lpfc_hrb_pool PCI
pool along a non-DMA-mapped container for it.

.. _`lpfc_els_hbq_alloc.notes`:

Notes
-----

Not interrupt-safe.  Must be called with no locks held.

.. _`lpfc_els_hbq_alloc.return`:

Return
------

pointer to HBQ on success
NULL on failure

.. _`lpfc_els_hbq_free`:

lpfc_els_hbq_free
=================

.. c:function:: void lpfc_els_hbq_free(struct lpfc_hba *phba, struct hbq_dmabuf *hbqbp)

    Frees an HBQ buffer allocated with lpfc_els_hbq_alloc

    :param phba:
        HBA buffer was allocated for
    :type phba: struct lpfc_hba \*

    :param hbqbp:
        HBQ container returned by lpfc_els_hbq_alloc
    :type hbqbp: struct hbq_dmabuf \*

.. _`lpfc_els_hbq_free.description`:

Description
-----------

Frees both the container and the DMA-mapped buffer returned by
lpfc_els_hbq_alloc.

.. _`lpfc_els_hbq_free.notes`:

Notes
-----

Can be called with or without locks held.

.. _`lpfc_els_hbq_free.return`:

Return
------

None

.. _`lpfc_sli4_rb_alloc`:

lpfc_sli4_rb_alloc
==================

.. c:function:: struct hbq_dmabuf *lpfc_sli4_rb_alloc(struct lpfc_hba *phba)

    Allocate an SLI4 Receive buffer

    :param phba:
        HBA to allocate a receive buffer for
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_rb_alloc.description`:

Description
-----------

Allocates a DMA-mapped receive buffer from the lpfc_hrb_pool PCI
pool along a non-DMA-mapped container for it.

.. _`lpfc_sli4_rb_alloc.notes`:

Notes
-----

Not interrupt-safe.  Must be called with no locks held.

.. _`lpfc_sli4_rb_alloc.return`:

Return
------

pointer to HBQ on success
NULL on failure

.. _`lpfc_sli4_rb_free`:

lpfc_sli4_rb_free
=================

.. c:function:: void lpfc_sli4_rb_free(struct lpfc_hba *phba, struct hbq_dmabuf *dmab)

    Frees a receive buffer

    :param phba:
        HBA buffer was allocated for
    :type phba: struct lpfc_hba \*

    :param dmab:
        DMA Buffer container returned by lpfc_sli4_hbq_alloc
    :type dmab: struct hbq_dmabuf \*

.. _`lpfc_sli4_rb_free.description`:

Description
-----------

Frees both the container and the DMA-mapped buffers returned by
lpfc_sli4_rb_alloc.

.. _`lpfc_sli4_rb_free.notes`:

Notes
-----

Can be called with or without locks held.

.. _`lpfc_sli4_rb_free.return`:

Return
------

None

.. _`lpfc_sli4_nvmet_alloc`:

lpfc_sli4_nvmet_alloc
=====================

.. c:function:: struct rqb_dmabuf *lpfc_sli4_nvmet_alloc(struct lpfc_hba *phba)

    Allocate an SLI4 Receive buffer

    :param phba:
        HBA to allocate a receive buffer for
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_nvmet_alloc.description`:

Description
-----------

Allocates a DMA-mapped receive buffer from the lpfc_hrb_pool PCI
pool along a non-DMA-mapped container for it.

.. _`lpfc_sli4_nvmet_alloc.notes`:

Notes
-----

Not interrupt-safe.  Must be called with no locks held.

.. _`lpfc_sli4_nvmet_alloc.return`:

Return
------

pointer to HBQ on success
NULL on failure

.. _`lpfc_sli4_nvmet_free`:

lpfc_sli4_nvmet_free
====================

.. c:function:: void lpfc_sli4_nvmet_free(struct lpfc_hba *phba, struct rqb_dmabuf *dmab)

    Frees a receive buffer

    :param phba:
        HBA buffer was allocated for
    :type phba: struct lpfc_hba \*

    :param dmab:
        DMA Buffer container returned by lpfc_sli4_rbq_alloc
    :type dmab: struct rqb_dmabuf \*

.. _`lpfc_sli4_nvmet_free.description`:

Description
-----------

Frees both the container and the DMA-mapped buffers returned by
lpfc_sli4_nvmet_alloc.

.. _`lpfc_sli4_nvmet_free.notes`:

Notes
-----

Can be called with or without locks held.

.. _`lpfc_sli4_nvmet_free.return`:

Return
------

None

.. _`lpfc_in_buf_free`:

lpfc_in_buf_free
================

.. c:function:: void lpfc_in_buf_free(struct lpfc_hba *phba, struct lpfc_dmabuf *mp)

    Free a DMA buffer

    :param phba:
        HBA buffer is associated with
    :type phba: struct lpfc_hba \*

    :param mp:
        Buffer to free
    :type mp: struct lpfc_dmabuf \*

.. _`lpfc_in_buf_free.description`:

Description
-----------

Frees the given DMA buffer in the appropriate way given if the
HBA is running in SLI3 mode with HBQs enabled.

.. _`lpfc_in_buf_free.notes`:

Notes
-----

Takes phba->hbalock.  Can be called with or without other locks held.

.. _`lpfc_in_buf_free.return`:

Return
------

None

.. _`lpfc_rq_buf_free`:

lpfc_rq_buf_free
================

.. c:function:: void lpfc_rq_buf_free(struct lpfc_hba *phba, struct lpfc_dmabuf *mp)

    Free a RQ DMA buffer

    :param phba:
        HBA buffer is associated with
    :type phba: struct lpfc_hba \*

    :param mp:
        Buffer to free
    :type mp: struct lpfc_dmabuf \*

.. _`lpfc_rq_buf_free.description`:

Description
-----------

Frees the given DMA buffer in the appropriate way given by
reposting it to its associated RQ so it can be reused.

.. _`lpfc_rq_buf_free.notes`:

Notes
-----

Takes phba->hbalock.  Can be called with or without other locks held.

.. _`lpfc_rq_buf_free.return`:

Return
------

None

.. This file was automatic generated / don't edit.

