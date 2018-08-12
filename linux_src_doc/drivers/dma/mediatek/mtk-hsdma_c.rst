.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/mediatek/mtk-hsdma.c

.. _`mtk_hsdma_pdesc`:

struct mtk_hsdma_pdesc
======================

.. c:type:: struct mtk_hsdma_pdesc

    This is the struct holding info describing physical descriptor (PD) and its placement must be kept at 4-bytes alignment in little endian order.

.. _`mtk_hsdma_pdesc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_pdesc {
        __le32 desc1;
        __le32 desc2;
        __le32 desc3;
        __le32 desc4;
    }

.. _`mtk_hsdma_pdesc.members`:

Members
-------

desc1
    *undescribed*

desc2
    *undescribed*

desc3
    *undescribed*

desc4
    *undescribed*

.. _`mtk_hsdma_vdesc`:

struct mtk_hsdma_vdesc
======================

.. c:type:: struct mtk_hsdma_vdesc

    This is the struct holding info describing virtual descriptor (VD)

.. _`mtk_hsdma_vdesc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_vdesc {
        struct virt_dma_desc vd;
        size_t len;
        size_t residue;
        dma_addr_t dest;
        dma_addr_t src;
    }

.. _`mtk_hsdma_vdesc.members`:

Members
-------

vd
    An instance for struct virt_dma_desc

len
    The total data size device wants to move

residue
    The remaining data size device will move

dest
    The destination address device wants to move to

src
    The source address device wants to move from

.. _`mtk_hsdma_cb`:

struct mtk_hsdma_cb
===================

.. c:type:: struct mtk_hsdma_cb

    This is the struct holding extra info required for RX ring to know what relevant VD the the PD is being mapped to.

.. _`mtk_hsdma_cb.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_cb {
        struct virt_dma_desc *vd;
        enum mtk_hsdma_vdesc_flag flag;
    }

.. _`mtk_hsdma_cb.members`:

Members
-------

vd
    Pointer to the relevant VD.

flag
    Flag indicating what action should be taken when VD
    is completed.

.. _`mtk_hsdma_ring`:

struct mtk_hsdma_ring
=====================

.. c:type:: struct mtk_hsdma_ring

    This struct holds info describing underlying ring space

.. _`mtk_hsdma_ring.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_ring {
        struct mtk_hsdma_pdesc *txd;
        struct mtk_hsdma_pdesc *rxd;
        struct mtk_hsdma_cb *cb;
        dma_addr_t tphys;
        dma_addr_t rphys;
        u16 cur_tptr;
        u16 cur_rptr;
    }

.. _`mtk_hsdma_ring.members`:

Members
-------

txd
    The descriptor TX ring which describes DMA source
    information

rxd
    The descriptor RX ring which describes DMA
    destination information

cb
    The extra information pointed at by RX ring

tphys
    The physical addr of TX ring

rphys
    The physical addr of RX ring

cur_tptr
    Pointer to the next free descriptor used by the host

cur_rptr
    Pointer to the last done descriptor by the device

.. _`mtk_hsdma_pchan`:

struct mtk_hsdma_pchan
======================

.. c:type:: struct mtk_hsdma_pchan

    This is the struct holding info describing physical channel (PC)

.. _`mtk_hsdma_pchan.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_pchan {
        struct mtk_hsdma_ring ring;
        size_t sz_ring;
        atomic_t nr_free;
    }

.. _`mtk_hsdma_pchan.members`:

Members
-------

ring
    An instance for the underlying ring

sz_ring
    Total size allocated for the ring

nr_free
    Total number of free rooms in the ring. It would
    be accessed and updated frequently between IRQ
    context and user context to reflect whether ring
    can accept requests from VD.

.. _`mtk_hsdma_vchan`:

struct mtk_hsdma_vchan
======================

.. c:type:: struct mtk_hsdma_vchan

    This is the struct holding info describing virtual channel (VC)

.. _`mtk_hsdma_vchan.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_vchan {
        struct virt_dma_chan vc;
        struct completion issue_completion;
        bool issue_synchronize;
        struct list_head desc_hw_processing;
    }

.. _`mtk_hsdma_vchan.members`:

Members
-------

vc
    An instance for struct virt_dma_chan

issue_completion
    The wait for all issued descriptors completited

issue_synchronize
    Bool indicating channel synchronization starts

desc_hw_processing
    List those descriptors the hardware is processing,
    which is protected by vc.lock

.. _`mtk_hsdma_soc`:

struct mtk_hsdma_soc
====================

.. c:type:: struct mtk_hsdma_soc

    This is the struct holding differences among SoCs

.. _`mtk_hsdma_soc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_soc {
        __le32 ddone;
        __le32 ls0;
    }

.. _`mtk_hsdma_soc.members`:

Members
-------

ddone
    Bit mask for DDONE

ls0
    Bit mask for LS0

.. _`mtk_hsdma_device`:

struct mtk_hsdma_device
=======================

.. c:type:: struct mtk_hsdma_device

    This is the struct holding info describing HSDMA device

.. _`mtk_hsdma_device.definition`:

Definition
----------

.. code-block:: c

    struct mtk_hsdma_device {
        struct dma_device ddev;
        void __iomem *base;
        struct clk *clk;
        u32 irq;
        u32 dma_requests;
        struct mtk_hsdma_vchan *vc;
        struct mtk_hsdma_pchan *pc;
        refcount_t pc_refcnt;
        spinlock_t lock;
        const struct mtk_hsdma_soc *soc;
    }

.. _`mtk_hsdma_device.members`:

Members
-------

ddev
    An instance for struct dma_device

base
    The mapped register I/O base

clk
    The clock that device internal is using

irq
    The IRQ that device are using

dma_requests
    The number of VCs the device supports to

vc
    The pointer to all available VCs

pc
    The pointer to the underlying PC

pc_refcnt
    Track how many VCs are using the PC

lock
    Lock protect agaisting multiple VCs access PC

soc
    The pointer to area holding differences among
    vaious platform

.. This file was automatic generated / don't edit.

