.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/mediatek/mtk-platform.h

.. _`mtk_desc`:

struct mtk_desc
===============

.. c:type:: struct mtk_desc

    DMA descriptor

.. _`mtk_desc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_desc {
        __le32 hdr;
        __le32 buf;
        __le32 ct;
        __le32 ct_hdr;
        __le32 tag;
        __le32 tfm;
        __le32 bound;
    }

.. _`mtk_desc.members`:

Members
-------

hdr
    the descriptor control header

buf
    DMA address of input buffer segment

ct
    DMA address of command token that control operation flow

ct_hdr
    the command token control header

tag
    the user-defined field

tfm
    DMA address of transform state

bound
    align descriptors offset boundary

.. _`mtk_desc.description`:

Description
-----------

Structure passed to the crypto engine to describe where source
data needs to be fetched and how it needs to be processed.

.. _`mtk_ring`:

struct mtk_ring
===============

.. c:type:: struct mtk_ring

    Descriptor ring

.. _`mtk_ring.definition`:

Definition
----------

.. code-block:: c

    struct mtk_ring {
        struct mtk_desc *cmd_base;
        struct mtk_desc *cmd_next;
        dma_addr_t cmd_dma;
        struct mtk_desc *res_base;
        struct mtk_desc *res_next;
        struct mtk_desc *res_prev;
        dma_addr_t res_dma;
    }

.. _`mtk_ring.members`:

Members
-------

cmd_base
    pointer to command descriptor ring base

cmd_next
    pointer to the next command descriptor

cmd_dma
    DMA address of command descriptor ring

res_base
    pointer to result descriptor ring base

res_next
    pointer to the next result descriptor

res_prev
    pointer to the previous result descriptor

res_dma
    DMA address of result descriptor ring

.. _`mtk_ring.description`:

Description
-----------

A descriptor ring is a circular buffer that is used to manage
one or more descriptors. There are two type of descriptor rings;
the command descriptor ring and result descriptor ring.

.. _`mtk_aes_dma`:

struct mtk_aes_dma
==================

.. c:type:: struct mtk_aes_dma

    Structure that holds sg list info

.. _`mtk_aes_dma.definition`:

Definition
----------

.. code-block:: c

    struct mtk_aes_dma {
        struct scatterlist *sg;
        int nents;
        u32 remainder;
        u32 sg_len;
    }

.. _`mtk_aes_dma.members`:

Members
-------

sg
    pointer to scatter-gather list

nents
    number of entries in the sg list

remainder
    remainder of sg list

sg_len
    number of entries in the sg mapped list

.. _`mtk_aes_rec`:

struct mtk_aes_rec
==================

.. c:type:: struct mtk_aes_rec

    AES operation record

.. _`mtk_aes_rec.definition`:

Definition
----------

.. code-block:: c

    struct mtk_aes_rec {
        struct mtk_cryp *cryp;
        struct crypto_queue queue;
        struct crypto_async_request *areq;
        struct tasklet_struct done_task;
        struct tasklet_struct queue_task;
        struct mtk_aes_base_ctx *ctx;
        struct mtk_aes_dma src;
        struct mtk_aes_dma dst;
        struct scatterlist aligned_sg;
        struct scatterlist *real_dst;
        mtk_aes_fn resume;
        size_t total;
        void *buf;
        u8 id;
        unsigned long flags;
        spinlock_t lock;
    }

.. _`mtk_aes_rec.members`:

Members
-------

cryp
    pointer to Cryptographic device

queue
    crypto request queue

areq
    pointer to async request

done_task
    the tasklet is use in AES interrupt

queue_task
    the tasklet is used to dequeue request

ctx
    pointer to current context

src
    the structure that holds source sg list info

dst
    the structure that holds destination sg list info

aligned_sg
    the scatter list is use to alignment

real_dst
    pointer to the destination sg list

resume
    pointer to resume function

total
    request buffer length

buf
    pointer to page buffer

id
    the current use of ring

flags
    it's describing AES operation state

lock
    the async queue lock

.. _`mtk_aes_rec.description`:

Description
-----------

Structure used to record AES execution state.

.. _`mtk_sha_rec`:

struct mtk_sha_rec
==================

.. c:type:: struct mtk_sha_rec

    SHA operation record

.. _`mtk_sha_rec.definition`:

Definition
----------

.. code-block:: c

    struct mtk_sha_rec {
        struct mtk_cryp *cryp;
        struct crypto_queue queue;
        struct ahash_request *req;
        struct tasklet_struct done_task;
        struct tasklet_struct queue_task;
        u8 id;
        unsigned long flags;
        spinlock_t lock;
    }

.. _`mtk_sha_rec.members`:

Members
-------

cryp
    pointer to Cryptographic device

queue
    crypto request queue

req
    pointer to ahash request

done_task
    the tasklet is use in SHA interrupt

queue_task
    the tasklet is used to dequeue request

id
    the current use of ring

flags
    it's describing SHA operation state

lock
    the async queue lock

.. _`mtk_sha_rec.description`:

Description
-----------

Structure used to record SHA execution state.

.. _`mtk_cryp`:

struct mtk_cryp
===============

.. c:type:: struct mtk_cryp

    Cryptographic device

.. _`mtk_cryp.definition`:

Definition
----------

.. code-block:: c

    struct mtk_cryp {
        void __iomem *base;
        struct device *dev;
        struct clk *clk_ethif;
        struct clk *clk_cryp;
        int irq;
        struct mtk_ring  *ring;
        struct mtk_aes_rec  *aes;
        struct mtk_sha_rec  *sha;
        struct list_head aes_list;
        struct list_head sha_list;
        bool rec;
    }

.. _`mtk_cryp.members`:

Members
-------

base
    pointer to mapped register I/O base

dev
    pointer to device

clk_ethif
    pointer to ethif clock

clk_cryp
    pointer to crypto clock

irq
    global system and rings IRQ

ring
    pointer to descriptor rings

aes
    pointer to operation record of AES

sha
    pointer to operation record of SHA

aes_list
    device list of AES

sha_list
    device list of SHA

rec
    it's used to select SHA record for tfm

.. _`mtk_cryp.description`:

Description
-----------

Structure storing cryptographic device information.

.. This file was automatic generated / don't edit.

