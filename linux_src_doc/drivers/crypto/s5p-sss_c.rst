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
    }

.. _`samsung_aes_variant.members`:

Members
-------

aes_offset
    AES register offset from SSS module's base.

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

.. This file was automatic generated / don't edit.

