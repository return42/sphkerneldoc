.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/s5p-sss.c

.. _`samsung_aes_variant`:

struct samsung_aes_variant
==========================

.. c:type:: struct samsung_aes_variant

    platform specific SSS driver data

.. _`samsung_aes_variant.definition`:

Definition
----------

.. code-block:: c

    struct samsung_aes_variant {
        unsigned int aes_offset;
        unsigned int hash_offset;
    }

.. _`samsung_aes_variant.members`:

Members
-------

aes_offset
    AES register offset from SSS module's base.

hash_offset
    HASH register offset from SSS module's base.

.. _`samsung_aes_variant.description`:

Description
-----------

Specifies platform specific configuration of SSS module.

.. _`samsung_aes_variant.note`:

Note
----

A structure for driver specific platform data is used for future
expansion of its usage.

.. _`s5p_aes_dev`:

struct s5p_aes_dev
==================

.. c:type:: struct s5p_aes_dev

    Crypto device state container

.. _`s5p_aes_dev.definition`:

Definition
----------

.. code-block:: c

    struct s5p_aes_dev {
        struct device *dev;
        struct clk *clk;
        void __iomem *ioaddr;
        void __iomem *aes_ioaddr;
        int irq_fc;
        struct ablkcipher_request *req;
        struct s5p_aes_ctx *ctx;
        struct scatterlist *sg_src;
        struct scatterlist *sg_dst;
        struct scatterlist *sg_src_cpy;
        struct scatterlist *sg_dst_cpy;
        struct tasklet_struct tasklet;
        struct crypto_queue queue;
        bool busy;
        spinlock_t lock;
        struct resource *res;
        void __iomem *io_hash_base;
        spinlock_t hash_lock;
        unsigned long hash_flags;
        struct crypto_queue hash_queue;
        struct tasklet_struct hash_tasklet;
        u8 xmit_buf[BUFLEN];
        struct ahash_request *hash_req;
        struct scatterlist *hash_sg_iter;
        unsigned int hash_sg_cnt;
        bool use_hash;
    }

.. _`s5p_aes_dev.members`:

Members
-------

dev
    Associated device

clk
    Clock for accessing hardware

ioaddr
    Mapped IO memory region

aes_ioaddr
    Per-varian offset for AES block IO memory

irq_fc
    Feed control interrupt line

req
    Crypto request currently handled by the device

ctx
    Configuration for currently handled crypto request

sg_src
    Scatter list with source data for currently handled block
    in device.  This is DMA-mapped into device.

sg_dst
    Scatter list with destination data for currently handled block
    in device. This is DMA-mapped into device.

sg_src_cpy
    In case of unaligned access, copied scatter list
    with source data.

sg_dst_cpy
    In case of unaligned access, copied scatter list
    with destination data.

tasklet
    New request scheduling jib

queue
    Crypto queue

busy
    Indicates whether the device is currently handling some request
    thus it uses some of the fields from this state, like:
    req, ctx, sg_src/dst (and copies).  This essentially
    protects against concurrent access to these fields.

lock
    Lock for protecting both access to device hardware registers
    and fields related to current request (including the busy field).

res
    Resources for hash.

io_hash_base
    Per-variant offset for HASH block IO memory.

hash_lock
    Lock for protecting hash_req, hash_queue and hash_flags
    variable.

hash_flags
    Flags for current HASH op.

hash_queue
    Async hash queue.

hash_tasklet
    New HASH request scheduling job.

xmit_buf
    Buffer for current HASH request transfer into SSS block.

hash_req
    Current request sending to SSS HASH block.

hash_sg_iter
    Scatterlist transferred through DMA into SSS HASH block.

hash_sg_cnt
    Counter for hash_sg_iter.

use_hash
    true if HASH algs enabled

.. _`s5p_hash_reqctx`:

struct s5p_hash_reqctx
======================

.. c:type:: struct s5p_hash_reqctx

    HASH request context

.. _`s5p_hash_reqctx.definition`:

Definition
----------

.. code-block:: c

    struct s5p_hash_reqctx {
        struct s5p_aes_dev *dd;
        bool op_update;
        u64 digcnt;
        u8 digest[SHA256_DIGEST_SIZE];
        unsigned int nregs;
        u32 engine;
        struct scatterlist *sg;
        unsigned int sg_len;
        struct scatterlist sgl[2];
        unsigned int skip;
        unsigned int total;
        bool finup;
        bool error;
        u32 bufcnt;
        u8 buffer[0];
    }

.. _`s5p_hash_reqctx.members`:

Members
-------

dd
    Associated device

op_update
    Current request operation (OP_UPDATE or OP_FINAL)

digcnt
    Number of bytes processed by HW (without buffer[] ones)

digest
    Digest message or IV for partial result

nregs
    Number of HW registers for digest or IV read/write

engine
    Bits for selecting type of HASH in SSS block

sg
    sg for DMA transfer

sg_len
    Length of sg for DMA transfer

sgl
    sg for joining buffer and req->src scatterlist

skip
    Skip offset in req->src for current op

total
    Total number of bytes for current request

finup
    Keep state for finup or final.

error
    Keep track of error.

bufcnt
    Number of bytes holded in buffer[]

buffer
    For byte(s) from end of req->src in UPDATE op

.. _`s5p_hash_ctx`:

struct s5p_hash_ctx
===================

.. c:type:: struct s5p_hash_ctx

    HASH transformation context

.. _`s5p_hash_ctx.definition`:

Definition
----------

.. code-block:: c

    struct s5p_hash_ctx {
        struct s5p_aes_dev *dd;
        unsigned long flags;
        struct crypto_shash *fallback;
    }

.. _`s5p_hash_ctx.members`:

Members
-------

dd
    Associated device

flags
    Bits for algorithm HASH.

fallback
    Software transformation for zero message or size < BUFLEN.

.. _`s5p_set_dma_hashdata`:

s5p_set_dma_hashdata
====================

.. c:function:: void s5p_set_dma_hashdata(struct s5p_aes_dev *dev, const struct scatterlist *sg)

    start DMA with sg

    :param struct s5p_aes_dev \*dev:
        device

    :param const struct scatterlist \*sg:
        scatterlist ready to DMA transmit

.. _`s5p_hash_rx`:

s5p_hash_rx
===========

.. c:function:: int s5p_hash_rx(struct s5p_aes_dev *dev)

    get next hash_sg_iter

    :param struct s5p_aes_dev \*dev:
        device

.. _`s5p_hash_rx.return`:

Return
------

2    if there is no more data and it is UPDATE op
1    if new receiving (input) data is ready and can be written to device
0    if there is no more data and it is FINAL op

.. _`s5p_hash_read_msg`:

s5p_hash_read_msg
=================

.. c:function:: void s5p_hash_read_msg(struct ahash_request *req)

    read message or IV from HW

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_write_ctx_iv`:

s5p_hash_write_ctx_iv
=====================

.. c:function:: void s5p_hash_write_ctx_iv(struct s5p_aes_dev *dd, const struct s5p_hash_reqctx *ctx)

    write IV for next partial/finup op.

    :param struct s5p_aes_dev \*dd:
        device

    :param const struct s5p_hash_reqctx \*ctx:
        request context

.. _`s5p_hash_write_iv`:

s5p_hash_write_iv
=================

.. c:function:: void s5p_hash_write_iv(struct ahash_request *req)

    write IV for next partial/finup op.

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_copy_result`:

s5p_hash_copy_result
====================

.. c:function:: void s5p_hash_copy_result(struct ahash_request *req)

    copy digest into req->result

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_dma_flush`:

s5p_hash_dma_flush
==================

.. c:function:: void s5p_hash_dma_flush(struct s5p_aes_dev *dev)

    flush HASH DMA

    :param struct s5p_aes_dev \*dev:
        secss device

.. _`s5p_hash_dma_enable`:

s5p_hash_dma_enable
===================

.. c:function:: void s5p_hash_dma_enable(struct s5p_aes_dev *dev)

    enable DMA mode for HASH

    :param struct s5p_aes_dev \*dev:
        secss device

.. _`s5p_hash_dma_enable.description`:

Description
-----------

enable DMA mode for HASH

.. _`s5p_hash_irq_disable`:

s5p_hash_irq_disable
====================

.. c:function:: void s5p_hash_irq_disable(struct s5p_aes_dev *dev, u32 flags)

    disable irq HASH signals

    :param struct s5p_aes_dev \*dev:
        secss device

    :param u32 flags:
        bitfield with irq's to be disabled

.. _`s5p_hash_irq_enable`:

s5p_hash_irq_enable
===================

.. c:function:: void s5p_hash_irq_enable(struct s5p_aes_dev *dev, int flags)

    enable irq signals

    :param struct s5p_aes_dev \*dev:
        secss device

    :param int flags:
        bitfield with irq's to be enabled

.. _`s5p_hash_set_flow`:

s5p_hash_set_flow
=================

.. c:function:: void s5p_hash_set_flow(struct s5p_aes_dev *dev, u32 hashflow)

    set flow inside SecSS AES/DES with/without HASH

    :param struct s5p_aes_dev \*dev:
        secss device

    :param u32 hashflow:
        HASH stream flow with/without crypto AES/DES

.. _`s5p_ahash_dma_init`:

s5p_ahash_dma_init
==================

.. c:function:: void s5p_ahash_dma_init(struct s5p_aes_dev *dev, u32 hashflow)

    enable DMA and set HASH flow inside SecSS

    :param struct s5p_aes_dev \*dev:
        secss device

    :param u32 hashflow:
        HASH stream flow with/without AES/DES

.. _`s5p_ahash_dma_init.description`:

Description
-----------

flush HASH DMA and enable DMA, set HASH stream flow inside SecSS HW,
enable HASH irq's HRDMA, HDONE, HPART

.. _`s5p_hash_write_ctrl`:

s5p_hash_write_ctrl
===================

.. c:function:: void s5p_hash_write_ctrl(struct s5p_aes_dev *dd, size_t length, bool final)

    prepare HASH block in SecSS for processing

    :param struct s5p_aes_dev \*dd:
        secss device

    :param size_t length:
        length for request

    :param bool final:
        true if final op

.. _`s5p_hash_write_ctrl.description`:

Description
-----------

Prepare SSS HASH block for processing bytes in DMA mode. If it is called
after previous updates, fill up IV words. For final, calculate and set
lengths for HASH so SecSS can finalize hash. For partial, set SSS HASH
length as 2^63 so it will be never reached and set to zero prelow and
prehigh.

This function does not start DMA transfer.

.. _`s5p_hash_xmit_dma`:

s5p_hash_xmit_dma
=================

.. c:function:: int s5p_hash_xmit_dma(struct s5p_aes_dev *dd, size_t length, bool final)

    start DMA hash processing

    :param struct s5p_aes_dev \*dd:
        secss device

    :param size_t length:
        length for request

    :param bool final:
        true if final op

.. _`s5p_hash_xmit_dma.description`:

Description
-----------

Update digcnt here, as it is needed for finup/final op.

.. _`s5p_hash_copy_sgs`:

s5p_hash_copy_sgs
=================

.. c:function:: int s5p_hash_copy_sgs(struct s5p_hash_reqctx *ctx, struct scatterlist *sg, unsigned int new_len)

    copy request's bytes into new buffer

    :param struct s5p_hash_reqctx \*ctx:
        request context

    :param struct scatterlist \*sg:
        source scatterlist request

    :param unsigned int new_len:
        number of bytes to process from sg

.. _`s5p_hash_copy_sgs.description`:

Description
-----------

Allocate new buffer, copy data for HASH into it. If there was xmit_buf
filled, copy it first, then copy data from sg into it. Prepare one sgl[0]
with allocated buffer.

Set bit in dd->hash_flag so we can free it after irq ends processing.

.. _`s5p_hash_copy_sg_lists`:

s5p_hash_copy_sg_lists
======================

.. c:function:: int s5p_hash_copy_sg_lists(struct s5p_hash_reqctx *ctx, struct scatterlist *sg, unsigned int new_len)

    copy sg list and make fixes in copy

    :param struct s5p_hash_reqctx \*ctx:
        request context

    :param struct scatterlist \*sg:
        source scatterlist request

    :param unsigned int new_len:
        number of bytes to process from sg

.. _`s5p_hash_copy_sg_lists.description`:

Description
-----------

Allocate new scatterlist table, copy data for HASH into it. If there was
xmit_buf filled, prepare it first, then copy page, length and offset from
source sg into it, adjusting begin and/or end for skip offset and
hash_later value.

Resulting sg table will be assigned to ctx->sg. Set flag so we can free
it after irq ends processing.

.. _`s5p_hash_prepare_sgs`:

s5p_hash_prepare_sgs
====================

.. c:function:: int s5p_hash_prepare_sgs(struct s5p_hash_reqctx *ctx, struct scatterlist *sg, unsigned int new_len, bool final)

    prepare sg for processing

    :param struct s5p_hash_reqctx \*ctx:
        request context

    :param struct scatterlist \*sg:
        source scatterlist request

    :param unsigned int new_len:
        *undescribed*

    :param bool final:
        final flag

.. _`s5p_hash_prepare_sgs.check-two-conditions`:

Check two conditions
--------------------

(1) if buffers in sg have len aligned data, and (2)
sg table have good aligned elements (list_ok). If one of this checks fails,
then either (1) allocates new buffer for data with s5p_hash_copy_sgs, copy
data into this buffer and prepare request in sgl, or (2) allocates new sg
table and prepare sg elements.

For digest or finup all conditions can be good, and we may not need any
fixes.

.. _`s5p_hash_prepare_request`:

s5p_hash_prepare_request
========================

.. c:function:: int s5p_hash_prepare_request(struct ahash_request *req, bool update)

    prepare request for processing

    :param struct ahash_request \*req:
        AHASH request

    :param bool update:
        true if UPDATE op

.. _`s5p_hash_prepare_request.note-1`:

Note 1
------

we can have update flag \_and\_ final flag at the same time.

.. _`s5p_hash_prepare_request.note-2`:

Note 2
------

we enter here when digcnt > BUFLEN (=HASH_BLOCK_SIZE) or
either req->nbytes or ctx->bufcnt + req->nbytes is > BUFLEN or
we have final op

.. _`s5p_hash_update_dma_stop`:

s5p_hash_update_dma_stop
========================

.. c:function:: void s5p_hash_update_dma_stop(struct s5p_aes_dev *dd)

    unmap DMA

    :param struct s5p_aes_dev \*dd:
        secss device

.. _`s5p_hash_update_dma_stop.description`:

Description
-----------

Unmap scatterlist ctx->sg.

.. _`s5p_hash_finish`:

s5p_hash_finish
===============

.. c:function:: void s5p_hash_finish(struct ahash_request *req)

    copy calculated digest to crypto layer

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_finish_req`:

s5p_hash_finish_req
===================

.. c:function:: void s5p_hash_finish_req(struct ahash_request *req, int err)

    finish request

    :param struct ahash_request \*req:
        AHASH request

    :param int err:
        error

.. _`s5p_hash_handle_queue`:

s5p_hash_handle_queue
=====================

.. c:function:: int s5p_hash_handle_queue(struct s5p_aes_dev *dd, struct ahash_request *req)

    handle hash queue

    :param struct s5p_aes_dev \*dd:
        device s5p_aes_dev

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_handle_queue.description`:

Description
-----------

If req!=NULL enqueue it on dd->queue, if FLAGS_BUSY is not set on the
device then processes the first request from the dd->queue

.. _`s5p_hash_handle_queue.return`:

Return
------

see s5p_hash_final below.

.. _`s5p_hash_tasklet_cb`:

s5p_hash_tasklet_cb
===================

.. c:function:: void s5p_hash_tasklet_cb(unsigned long data)

    hash tasklet

    :param unsigned long data:
        ptr to s5p_aes_dev

.. _`s5p_hash_enqueue`:

s5p_hash_enqueue
================

.. c:function:: int s5p_hash_enqueue(struct ahash_request *req, bool op)

    enqueue request

    :param struct ahash_request \*req:
        AHASH request

    :param bool op:
        operation UPDATE (true) or FINAL (false)

.. _`s5p_hash_enqueue.return`:

Return
------

see s5p_hash_final below.

.. _`s5p_hash_update`:

s5p_hash_update
===============

.. c:function:: int s5p_hash_update(struct ahash_request *req)

    process the hash input data

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_update.description`:

Description
-----------

If request will fit in buffer, copy it and return immediately
else enqueue it with OP_UPDATE.

.. _`s5p_hash_update.return`:

Return
------

see s5p_hash_final below.

.. _`s5p_hash_shash_digest`:

s5p_hash_shash_digest
=====================

.. c:function:: int s5p_hash_shash_digest(struct crypto_shash *tfm, u32 flags, const u8 *data, unsigned int len, u8 *out)

    calculate shash digest

    :param struct crypto_shash \*tfm:
        crypto transformation

    :param u32 flags:
        tfm flags

    :param const u8 \*data:
        input data

    :param unsigned int len:
        length of data

    :param u8 \*out:
        output buffer

.. _`s5p_hash_final_shash`:

s5p_hash_final_shash
====================

.. c:function:: int s5p_hash_final_shash(struct ahash_request *req)

    calculate shash digest

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_final`:

s5p_hash_final
==============

.. c:function:: int s5p_hash_final(struct ahash_request *req)

    close up hash and calculate digest

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_final.note`:

Note
----

in final req->src do not have any data, and req->nbytes can be
non-zero.

If there were no input data processed yet and the buffered hash data is
less than BUFLEN (64) then calculate the final hash immediately by using
SW algorithm fallback.

Otherwise enqueues the current AHASH request with OP_FINAL operation op
and finalize hash message in HW. Note that if digcnt!=0 then there were
previous update op, so there are always some buffered bytes in ctx->buffer,
which means that ctx->bufcnt!=0

.. _`s5p_hash_final.return`:

Return
------

0 if the request has been processed immediately,
-EINPROGRESS if the operation has been queued for later execution or is set
to processing by HW,
-EBUSY if queue is full and request should be resubmitted later,
other negative values denotes an error.

.. _`s5p_hash_finup`:

s5p_hash_finup
==============

.. c:function:: int s5p_hash_finup(struct ahash_request *req)

    process last req->src and calculate digest

    :param struct ahash_request \*req:
        AHASH request containing the last update data

.. _`s5p_hash_finup.return-values`:

Return values
-------------

see s5p_hash_final above.

.. _`s5p_hash_init`:

s5p_hash_init
=============

.. c:function:: int s5p_hash_init(struct ahash_request *req)

    initialize AHASH request contex

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_init.description`:

Description
-----------

Init async hash request context.

.. _`s5p_hash_digest`:

s5p_hash_digest
===============

.. c:function:: int s5p_hash_digest(struct ahash_request *req)

    calculate digest from req->src

    :param struct ahash_request \*req:
        AHASH request

.. _`s5p_hash_digest.return-values`:

Return values
-------------

see s5p_hash_final above.

.. _`s5p_hash_cra_init_alg`:

s5p_hash_cra_init_alg
=====================

.. c:function:: int s5p_hash_cra_init_alg(struct crypto_tfm *tfm)

    init crypto alg transformation

    :param struct crypto_tfm \*tfm:
        crypto transformation

.. _`s5p_hash_cra_init`:

s5p_hash_cra_init
=================

.. c:function:: int s5p_hash_cra_init(struct crypto_tfm *tfm)

    init crypto tfm

    :param struct crypto_tfm \*tfm:
        crypto transformation

.. _`s5p_hash_cra_exit`:

s5p_hash_cra_exit
=================

.. c:function:: void s5p_hash_cra_exit(struct crypto_tfm *tfm)

    exit crypto tfm

    :param struct crypto_tfm \*tfm:
        crypto transformation

.. _`s5p_hash_cra_exit.description`:

Description
-----------

free allocated fallback

.. _`s5p_hash_export`:

s5p_hash_export
===============

.. c:function:: int s5p_hash_export(struct ahash_request *req, void *out)

    export hash state

    :param struct ahash_request \*req:
        AHASH request

    :param void \*out:
        buffer for exported state

.. _`s5p_hash_import`:

s5p_hash_import
===============

.. c:function:: int s5p_hash_import(struct ahash_request *req, const void *in)

    import hash state

    :param struct ahash_request \*req:
        AHASH request

    :param const void \*in:
        buffer with state to be imported from

.. This file was automatic generated / don't edit.

