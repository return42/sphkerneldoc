.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/hisilicon/sec/sec_drv.h

.. _`sec_queue_ring_cmd`:

struct sec_queue_ring_cmd
=========================

.. c:type:: struct sec_queue_ring_cmd

    store information about a SEC HW cmd ring

.. _`sec_queue_ring_cmd.definition`:

Definition
----------

.. code-block:: c

    struct sec_queue_ring_cmd {
        atomic_t used;
        struct mutex lock;
        struct sec_bd_info *vaddr;
        dma_addr_t paddr;
        void (*callback)(struct sec_bd_info *resp, void *ctx);
    }

.. _`sec_queue_ring_cmd.members`:

Members
-------

used
    Local counter used to cheaply establish if the ring is empty.

lock
    Protect against simultaneous adjusting of the read and write pointers.

vaddr
    Virtual address for the ram pages used for the ring.

paddr
    Physical address of the dma mapped region of ram used for the ring.

callback
    Callback function called on a ring element completing.

.. _`sec_alg_tfm_ctx`:

struct sec_alg_tfm_ctx
======================

.. c:type:: struct sec_alg_tfm_ctx

    hardware specific tranformation context

.. _`sec_alg_tfm_ctx.definition`:

Definition
----------

.. code-block:: c

    struct sec_alg_tfm_ctx {
        enum sec_cipher_alg cipher_alg;
        u8 *key;
        dma_addr_t pkey;
        struct sec_bd_info req_template;
        struct sec_queue *queue;
        struct mutex lock;
        u8 *auth_buf;
        struct list_head backlog;
    }

.. _`sec_alg_tfm_ctx.members`:

Members
-------

cipher_alg
    Cipher algorithm enabled include encryption mode.

key
    Key storage if required.

pkey
    DMA address for the key storage.

req_template
    Request template to save time on setup.

queue
    The hardware queue associated with this tfm context.

lock
    Protect key and pkey to ensure they are consistent

auth_buf
    Current context buffer for auth operations.

backlog
    The backlog queue used for cases where our buffers aren't
    large enough.

.. _`sec_request`:

struct sec_request
==================

.. c:type:: struct sec_request

    data associate with a single crypto request

.. _`sec_request.definition`:

Definition
----------

.. code-block:: c

    struct sec_request {
        struct list_head elements;
        int num_elements;
        struct mutex lock;
        struct sec_alg_tfm_ctx *tfm_ctx;
        int len_in;
        int len_out;
        dma_addr_t dma_iv;
        int err;
        struct crypto_async_request *req_base;
        void (*cb)(struct sec_bd_info *resp, struct crypto_async_request *req);
        struct list_head backlog_head;
    }

.. _`sec_request.members`:

Members
-------

elements
    List of subparts of this request (hardware size restriction)

num_elements
    The number of subparts (used as an optimization)

lock
    Protect elements of this structure against concurrent change.

tfm_ctx
    hardware specific context.

len_in
    length of in sgl from upper layers

len_out
    length of out sgl from upper layers

dma_iv
    initialization vector - phsyical address

err
    store used to track errors across subelements of this request.

req_base
    pointer to base element of associate crypto context.
    This is needed to allow shared handling skcipher, ahash etc.

cb
    completion callback.

backlog_head
    list head to allow backlog maintenance.

.. _`sec_request.description`:

Description
-----------

The hardware is limited in the maximum size of data that it can
process from a single BD.  Typically this is fairly large (32MB)
but still requires the complexity of splitting the incoming
skreq up into a number of elements complete with appropriate
iv chaining.

.. _`sec_request_el`:

struct sec_request_el
=====================

.. c:type:: struct sec_request_el

    A subpart of a request.

.. _`sec_request_el.definition`:

Definition
----------

.. code-block:: c

    struct sec_request_el {
        struct list_head head;
        struct sec_bd_info req;
        struct sec_hw_sgl *in;
        dma_addr_t dma_in;
        struct scatterlist *sgl_in;
        struct sec_hw_sgl *out;
        dma_addr_t dma_out;
        struct scatterlist *sgl_out;
        struct sec_request *sec_req;
        size_t el_length;
    }

.. _`sec_request_el.members`:

Members
-------

head
    allow us to attach this to the list in the sec_request

req
    hardware block descriptor corresponding to this request subpart

in
    hardware sgl for input - virtual address

dma_in
    hardware sgl for input - physical address

sgl_in
    scatterlist for this request subpart

out
    hardware sgl for output - virtual address

dma_out
    hardware sgl for output - physical address

sgl_out
    scatterlist for this request subpart

sec_req
    The request which this subpart forms a part of

el_length
    Number of bytes in this subpart. Needed to locate
    last ivsize chunk for iv chaining.

.. _`sec_queue`:

struct sec_queue
================

.. c:type:: struct sec_queue

    All the information about a HW queue

.. _`sec_queue.definition`:

Definition
----------

.. code-block:: c

    struct sec_queue {
        struct sec_dev_info *dev_info;
        int task_irq;
        char name[SEC_NAME_SIZE];
        struct sec_queue_ring_cmd ring_cmd;
        struct sec_queue_ring_cq ring_cq;
        struct sec_queue_ring_db ring_db;
        void __iomem *regs;
        u32 queue_id;
        bool in_use;
        int expected;
        DECLARE_BITMAP(unprocessed, SEC_QUEUE_LEN);
        DECLARE_KFIFO_PTR(softqueue, typeof(struct sec_request_el *));
        bool havesoftqueue;
        struct mutex queuelock;
        void *shadow[SEC_QUEUE_LEN];
    }

.. _`sec_queue.members`:

Members
-------

dev_info
    The parent SEC device to which this queue belongs.

task_irq
    Completion interrupt for the queue.

name
    Human readable queue description also used as irq name.

ring_cmd
    *undescribed*

ring_cq
    *undescribed*

ring_db
    *undescribed*

regs
    The iomapped device registers

queue_id
    Index of the queue used for naming and resource selection.

in_use
    Flag to say if the queue is in use.

expected
    The next expected element to finish assuming we were in order.

unprocessed
    *undescribed*

softqueue
    A software queue used when chaining requirements prevent direct
    use of the hardware queues.

havesoftqueue
    A flag to say we have a queues - as we may need one for the
    current mode.

queuelock
    Protect the soft queue from concurrent changes to avoid some
    potential loss of data races.

shadow
    Pointers back to the shadow copy of the hardware ring element
    need because we can't store any context reference in the bd element.

.. _`sec_hw_sge`:

struct sec_hw_sge
=================

.. c:type:: struct sec_hw_sge

    Track each of the 64 element SEC HW SGL entries

.. _`sec_hw_sge.definition`:

Definition
----------

.. code-block:: c

    struct sec_hw_sge {
        dma_addr_t buf;
        unsigned int len;
        unsigned int pad;
    }

.. _`sec_hw_sge.members`:

Members
-------

buf
    The IOV dma address for this entry.

len
    Length of this IOV.

pad
    Reserved space.

.. _`sec_hw_sgl`:

struct sec_hw_sgl
=================

.. c:type:: struct sec_hw_sgl

    One hardware SGL entry.

.. _`sec_hw_sgl.definition`:

Definition
----------

.. code-block:: c

    struct sec_hw_sgl {
        dma_addr_t next_sgl;
        u16 entry_sum_in_chain;
        u16 entry_sum_in_sgl;
        u32 flag;
        u64 serial_num;
        u32 cpuid;
        u32 data_bytes_in_sgl;
        struct sec_hw_sgl *next;
        u64 reserved;
        struct sec_hw_sge sge_entries[SEC_MAX_SGE_NUM];
        u8 node[16];
    }

.. _`sec_hw_sgl.members`:

Members
-------

next_sgl
    The next entry if we need to chain dma address. Null if last.

entry_sum_in_chain
    The full count of SGEs - only matters for first SGL.

entry_sum_in_sgl
    The number of SGEs in this SGL element.

flag
    Unused in skciphers.

serial_num
    Unsued in skciphers.

cpuid
    Currently unused.

data_bytes_in_sgl
    Count of bytes from all SGEs in this SGL.

next
    Virtual address used to stash the next sgl - useful in completion.

reserved
    A reserved field not currently used.

sge_entries
    The (up to) 64 Scatter Gather Entries, representing IOVs.

node
    Currently unused.

.. _`sec_dev_info`:

struct sec_dev_info
===================

.. c:type:: struct sec_dev_info

    The full SEC unit comprising queues and processors.

.. _`sec_dev_info.definition`:

Definition
----------

.. code-block:: c

    struct sec_dev_info {
        int sec_id;
        int num_saas;
        void __iomem *regs[SEC_NUM_ADDR_REGIONS];
        struct mutex dev_lock;
        int queues_in_use;
        struct sec_queue queues[SEC_Q_NUM];
        struct device *dev;
        struct dma_pool *hw_sgl_pool;
    }

.. _`sec_dev_info.members`:

Members
-------

sec_id
    Index used to track which SEC this is when more than one is present.

num_saas
    The number of backed processors enabled.

regs
    iomapped register regions shared by whole SEC unit.

dev_lock
    Protects concurrent queue allocation / freeing for the SEC.

queues_in_use
    *undescribed*

queues
    The 16 queues that this SEC instance provides.

dev
    Device pointer.

hw_sgl_pool
    DMA pool used to mimise mapping for the scatter gather lists.

.. This file was automatic generated / don't edit.

