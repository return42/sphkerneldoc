.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/marvell/cesa.h

.. _`mv_cesa_sec_accel_desc`:

struct mv_cesa_sec_accel_desc
=============================

.. c:type:: struct mv_cesa_sec_accel_desc

    security accelerator descriptor

.. _`mv_cesa_sec_accel_desc.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_sec_accel_desc {
        __le32 config;
        __le32 enc_p;
        __le32 enc_len;
        __le32 enc_key_p;
        __le32 enc_iv;
        __le32 mac_src_p;
        __le32 mac_digest;
        __le32 mac_iv;
    }

.. _`mv_cesa_sec_accel_desc.members`:

Members
-------

config
    engine config

enc_p
    input and output data pointers for a cipher operation

enc_len
    cipher operation length

enc_key_p
    cipher key pointer

enc_iv
    cipher IV pointers

mac_src_p
    input pointer and total hash length

mac_digest
    digest pointer and hash operation length

mac_iv
    hmac IV pointers

.. _`mv_cesa_sec_accel_desc.description`:

Description
-----------

Structure passed to the CESA engine to describe the crypto operation
to be executed.

.. _`mv_cesa_blkcipher_op_ctx`:

struct mv_cesa_blkcipher_op_ctx
===============================

.. c:type:: struct mv_cesa_blkcipher_op_ctx

    cipher operation context

.. _`mv_cesa_blkcipher_op_ctx.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_blkcipher_op_ctx {
        u32 key[8];
        u32 iv[4];
    }

.. _`mv_cesa_blkcipher_op_ctx.members`:

Members
-------

key
    cipher key

iv
    cipher IV

.. _`mv_cesa_blkcipher_op_ctx.description`:

Description
-----------

Context associated to a cipher operation.

.. _`mv_cesa_hash_op_ctx`:

struct mv_cesa_hash_op_ctx
==========================

.. c:type:: struct mv_cesa_hash_op_ctx

    hash or hmac operation context

.. _`mv_cesa_hash_op_ctx.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_hash_op_ctx {
        u32 iv[16];
        u32 hash[8];
    }

.. _`mv_cesa_hash_op_ctx.members`:

Members
-------

iv
    cipher IV

.. _`mv_cesa_hash_op_ctx.description`:

Description
-----------

Context associated to an hash or hmac operation.

.. _`mv_cesa_op_ctx`:

struct mv_cesa_op_ctx
=====================

.. c:type:: struct mv_cesa_op_ctx

    crypto operation context

.. _`mv_cesa_op_ctx.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_op_ctx {
        struct mv_cesa_sec_accel_desc desc;
        union ctx;
    }

.. _`mv_cesa_op_ctx.members`:

Members
-------

desc
    CESA descriptor

ctx
    context associated to the crypto operation

.. _`mv_cesa_op_ctx.description`:

Description
-----------

Context associated to a crypto operation.

.. _`mv_cesa_tdma_desc`:

struct mv_cesa_tdma_desc
========================

.. c:type:: struct mv_cesa_tdma_desc

    TDMA descriptor

.. _`mv_cesa_tdma_desc.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_tdma_desc {
        __le32 byte_cnt;
        __le32 src;
        __le32 dst;
        __le32 next_dma;
        dma_addr_t cur_dma;
        struct mv_cesa_tdma_desc *next;
        union {unnamed_union};
        u32 flags;
    }

.. _`mv_cesa_tdma_desc.members`:

Members
-------

byte_cnt
    number of bytes to transfer

src
    DMA address of the source

dst
    DMA address of the destination

next_dma
    DMA address of the next TDMA descriptor

cur_dma
    DMA address of this TDMA descriptor

next
    pointer to the next TDMA descriptor

{unnamed_union}
    anonymous


flags
    flags describing the TDMA transfer. See the
    "TDMA descriptor flags" section above

.. _`mv_cesa_tdma_desc.description`:

Description
-----------

TDMA descriptor used to create a transfer chain describing a crypto
operation.

.. _`mv_cesa_sg_dma_iter`:

struct mv_cesa_sg_dma_iter
==========================

.. c:type:: struct mv_cesa_sg_dma_iter

    scatter-gather iterator

.. _`mv_cesa_sg_dma_iter.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_sg_dma_iter {
        enum dma_data_direction dir;
        struct scatterlist *sg;
        unsigned int offset;
        unsigned int op_offset;
    }

.. _`mv_cesa_sg_dma_iter.members`:

Members
-------

dir
    transfer direction

sg
    scatter list

offset
    current position in the scatter list

op_offset
    current position in the crypto operation

.. _`mv_cesa_sg_dma_iter.description`:

Description
-----------

Iterator used to iterate over a scatterlist while creating a TDMA chain for
a crypto operation.

.. _`mv_cesa_dma_iter`:

struct mv_cesa_dma_iter
=======================

.. c:type:: struct mv_cesa_dma_iter

    crypto operation iterator

.. _`mv_cesa_dma_iter.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_dma_iter {
        unsigned int len;
        unsigned int offset;
        unsigned int op_len;
    }

.. _`mv_cesa_dma_iter.members`:

Members
-------

len
    the crypto operation length

offset
    current position in the crypto operation

op_len
    sub-operation length (the crypto engine can only act on 2kb
    chunks)

.. _`mv_cesa_dma_iter.description`:

Description
-----------

Iterator used to create a TDMA chain for a given crypto operation.

.. _`mv_cesa_tdma_chain`:

struct mv_cesa_tdma_chain
=========================

.. c:type:: struct mv_cesa_tdma_chain

    TDMA chain

.. _`mv_cesa_tdma_chain.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_tdma_chain {
        struct mv_cesa_tdma_desc *first;
        struct mv_cesa_tdma_desc *last;
    }

.. _`mv_cesa_tdma_chain.members`:

Members
-------

first
    first entry in the TDMA chain

last
    last entry in the TDMA chain

.. _`mv_cesa_tdma_chain.description`:

Description
-----------

Stores a TDMA chain for a specific crypto operation.

.. _`mv_cesa_caps`:

struct mv_cesa_caps
===================

.. c:type:: struct mv_cesa_caps

    CESA device capabilities

.. _`mv_cesa_caps.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_caps {
        int nengines;
        bool has_tdma;
        struct crypto_alg **cipher_algs;
        int ncipher_algs;
        struct ahash_alg **ahash_algs;
        int nahash_algs;
    }

.. _`mv_cesa_caps.members`:

Members
-------

nengines
    *undescribed*

has_tdma
    whether this device has a TDMA block

cipher_algs
    supported cipher algorithms

ncipher_algs
    number of supported cipher algorithms

ahash_algs
    supported hash algorithms

nahash_algs
    number of supported hash algorithms

.. _`mv_cesa_caps.description`:

Description
-----------

Structure used to describe CESA device capabilities.

.. _`mv_cesa_dev_dma`:

struct mv_cesa_dev_dma
======================

.. c:type:: struct mv_cesa_dev_dma

    DMA pools

.. _`mv_cesa_dev_dma.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_dev_dma {
        struct dma_pool *tdma_desc_pool;
        struct dma_pool *op_pool;
        struct dma_pool *cache_pool;
        struct dma_pool *padding_pool;
    }

.. _`mv_cesa_dev_dma.members`:

Members
-------

tdma_desc_pool
    TDMA desc pool

op_pool
    crypto operation pool

cache_pool
    data cache pool (used by hash implementation when the
    hash request is smaller than the hash block size)

padding_pool
    padding pool (used by hash implementation when hardware
    padding cannot be used)

.. _`mv_cesa_dev_dma.description`:

Description
-----------

Structure containing the different DMA pools used by this driver.

.. _`mv_cesa_dev`:

struct mv_cesa_dev
==================

.. c:type:: struct mv_cesa_dev

    CESA device

.. _`mv_cesa_dev.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_dev {
        const struct mv_cesa_caps *caps;
        void __iomem *regs;
        struct device *dev;
        unsigned int sram_size;
        spinlock_t lock;
        struct mv_cesa_engine *engines;
        struct mv_cesa_dev_dma *dma;
    }

.. _`mv_cesa_dev.members`:

Members
-------

caps
    device capabilities

regs
    device registers

dev
    *undescribed*

sram_size
    usable SRAM size

lock
    device lock

engines
    array of engines

dma
    dma pools

.. _`mv_cesa_dev.description`:

Description
-----------

Structure storing CESA device information.

.. _`mv_cesa_engine`:

struct mv_cesa_engine
=====================

.. c:type:: struct mv_cesa_engine

    CESA engine

.. _`mv_cesa_engine.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_engine {
        int id;
        void __iomem *regs;
        void __iomem *sram;
        dma_addr_t sram_dma;
        spinlock_t lock;
        struct crypto_async_request *req;
        struct clk *clk;
        struct clk *zclk;
        size_t max_req_len;
        u32 int_mask;
        struct gen_pool *pool;
        struct crypto_queue queue;
        atomic_t load;
        struct mv_cesa_tdma_chain chain;
        struct list_head complete_queue;
    }

.. _`mv_cesa_engine.members`:

Members
-------

id
    engine id

regs
    engine registers

sram
    SRAM memory region

sram_dma
    DMA address of the SRAM memory region

lock
    engine lock

req
    current crypto request

clk
    engine clk

zclk
    engine zclk

max_req_len
    maximum chunk length (useful to create the TDMA chain)

int_mask
    interrupt mask cache

pool
    memory pool pointing to the memory region reserved in
    SRAM

queue
    fifo of the pending crypto requests

load
    engine load counter, useful for load balancing

chain
    list of the current tdma descriptors being processed
    by this engine.

complete_queue
    fifo of the processed requests by the engine

.. _`mv_cesa_engine.description`:

Description
-----------

Structure storing CESA engine information.

.. _`mv_cesa_req_ops`:

struct mv_cesa_req_ops
======================

.. c:type:: struct mv_cesa_req_ops

    CESA request operations

.. _`mv_cesa_req_ops.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_req_ops {
        int (*process)(struct crypto_async_request *req, u32 status);
        void (*step)(struct crypto_async_request *req);
        void (*cleanup)(struct crypto_async_request *req);
        void (*complete)(struct crypto_async_request *req);
    }

.. _`mv_cesa_req_ops.members`:

Members
-------

process
    process a request chunk result (should return 0 if the
    operation, -EINPROGRESS if it needs more steps or an error
    code)

step
    launch the crypto operation on the next chunk

cleanup
    cleanup the crypto request (release associated data)

complete
    complete the request, i.e copy result or context from sram when
    needed.

.. _`mv_cesa_ctx`:

struct mv_cesa_ctx
==================

.. c:type:: struct mv_cesa_ctx

    CESA operation context

.. _`mv_cesa_ctx.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_ctx {
        const struct mv_cesa_req_ops *ops;
    }

.. _`mv_cesa_ctx.members`:

Members
-------

ops
    crypto operations

.. _`mv_cesa_ctx.description`:

Description
-----------

Base context structure inherited by operation specific ones.

.. _`mv_cesa_hash_ctx`:

struct mv_cesa_hash_ctx
=======================

.. c:type:: struct mv_cesa_hash_ctx

    CESA hash operation context

.. _`mv_cesa_hash_ctx.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_hash_ctx {
        struct mv_cesa_ctx base;
    }

.. _`mv_cesa_hash_ctx.members`:

Members
-------

base
    base context structure

.. _`mv_cesa_hash_ctx.description`:

Description
-----------

Hash context structure.

.. _`mv_cesa_hmac_ctx`:

struct mv_cesa_hmac_ctx
=======================

.. c:type:: struct mv_cesa_hmac_ctx

    CESA hmac operation context

.. _`mv_cesa_hmac_ctx.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_hmac_ctx {
        struct mv_cesa_ctx base;
        u32 iv[16];
    }

.. _`mv_cesa_hmac_ctx.members`:

Members
-------

base
    base context structure

iv
    initialization vectors

.. _`mv_cesa_hmac_ctx.description`:

Description
-----------

HMAC context structure.

.. _`mv_cesa_req_type`:

enum mv_cesa_req_type
=====================

.. c:type:: enum mv_cesa_req_type

    request type definitions

.. _`mv_cesa_req_type.definition`:

Definition
----------

.. code-block:: c

    enum mv_cesa_req_type {
        CESA_STD_REQ,
        CESA_DMA_REQ
    };

.. _`mv_cesa_req_type.constants`:

Constants
---------

CESA_STD_REQ
    standard request

CESA_DMA_REQ
    DMA request

.. _`mv_cesa_req`:

struct mv_cesa_req
==================

.. c:type:: struct mv_cesa_req

    CESA request

.. _`mv_cesa_req.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_req {
        struct mv_cesa_engine *engine;
        struct mv_cesa_tdma_chain chain;
    }

.. _`mv_cesa_req.members`:

Members
-------

engine
    engine associated with this request

chain
    list of tdma descriptors associated  with this request

.. _`mv_cesa_sg_std_iter`:

struct mv_cesa_sg_std_iter
==========================

.. c:type:: struct mv_cesa_sg_std_iter

    CESA scatter-gather iterator for standard requests

.. _`mv_cesa_sg_std_iter.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_sg_std_iter {
        struct sg_mapping_iter iter;
        unsigned int offset;
    }

.. _`mv_cesa_sg_std_iter.members`:

Members
-------

iter
    sg mapping iterator

offset
    current offset in the SG entry mapped in memory

.. _`mv_cesa_ablkcipher_std_req`:

struct mv_cesa_ablkcipher_std_req
=================================

.. c:type:: struct mv_cesa_ablkcipher_std_req

    cipher standard request

.. _`mv_cesa_ablkcipher_std_req.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_ablkcipher_std_req {
        struct mv_cesa_op_ctx op;
        unsigned int offset;
        unsigned int size;
        bool skip_ctx;
    }

.. _`mv_cesa_ablkcipher_std_req.members`:

Members
-------

op
    operation context

offset
    current operation offset

size
    size of the crypto operation

skip_ctx
    *undescribed*

.. _`mv_cesa_ablkcipher_req`:

struct mv_cesa_ablkcipher_req
=============================

.. c:type:: struct mv_cesa_ablkcipher_req

    cipher request

.. _`mv_cesa_ablkcipher_req.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_ablkcipher_req {
        struct mv_cesa_req base;
        struct mv_cesa_ablkcipher_std_req std;
        int src_nents;
        int dst_nents;
    }

.. _`mv_cesa_ablkcipher_req.members`:

Members
-------

base
    *undescribed*

std
    *undescribed*

src_nents
    number of entries in the src sg list

dst_nents
    number of entries in the dest sg list

.. _`mv_cesa_ahash_std_req`:

struct mv_cesa_ahash_std_req
============================

.. c:type:: struct mv_cesa_ahash_std_req

    standard hash request

.. _`mv_cesa_ahash_std_req.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_ahash_std_req {
        unsigned int offset;
    }

.. _`mv_cesa_ahash_std_req.members`:

Members
-------

offset
    current operation offset

.. _`mv_cesa_ahash_dma_req`:

struct mv_cesa_ahash_dma_req
============================

.. c:type:: struct mv_cesa_ahash_dma_req

    DMA hash request

.. _`mv_cesa_ahash_dma_req.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_ahash_dma_req {
        u8 *padding;
        dma_addr_t padding_dma;
        u8 *cache;
        dma_addr_t cache_dma;
    }

.. _`mv_cesa_ahash_dma_req.members`:

Members
-------

padding
    padding buffer

padding_dma
    DMA address of the padding buffer

cache
    *undescribed*

cache_dma
    DMA address of the cache buffer

.. _`mv_cesa_ahash_req`:

struct mv_cesa_ahash_req
========================

.. c:type:: struct mv_cesa_ahash_req

    hash request

.. _`mv_cesa_ahash_req.definition`:

Definition
----------

.. code-block:: c

    struct mv_cesa_ahash_req {
        struct mv_cesa_req base;
        union req;
        struct mv_cesa_op_ctx op_tmpl;
        u8 cache[CESA_MAX_HASH_BLOCK_SIZE];
        unsigned int cache_ptr;
        u64 len;
        int src_nents;
        bool last_req;
        bool algo_le;
        u32 state[8];
    }

.. _`mv_cesa_ahash_req.members`:

Members
-------

base
    *undescribed*

req
    type specific request information

op_tmpl
    *undescribed*

cache
    cache buffer

cache_ptr
    write pointer in the cache buffer

len
    hash total length

src_nents
    number of entries in the scatterlist

last_req
    define whether the current operation is the last one
    or not

algo_le
    *undescribed*

state
    hash state

.. This file was automatic generated / don't edit.

