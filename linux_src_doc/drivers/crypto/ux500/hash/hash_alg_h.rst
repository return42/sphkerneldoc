.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ux500/hash/hash_alg.h

.. _`uint64`:

struct uint64
=============

.. c:type:: struct uint64

    Structure to handle 64 bits integers.

.. _`uint64.definition`:

Definition
----------

.. code-block:: c

    struct uint64 {
        u32 high_word;
        u32 low_word;
    }

.. _`uint64.members`:

Members
-------

high_word
    Most significant bits.

low_word
    Least significant bits.

.. _`uint64.description`:

Description
-----------

Used to handle 64 bits integers.

.. _`hash_register`:

struct hash_register
====================

.. c:type:: struct hash_register

    Contains all registers in ux500 hash hardware.

.. _`hash_register.definition`:

Definition
----------

.. code-block:: c

    struct hash_register {
        u32 cr;
        u32 din;
        u32 str;
        u32 hx;
        u32 padding0;
        u32 itcr;
        u32 itip;
        u32 itop;
        u32 padding1;
        u32 csfull;
        u32 csdatain;
        u32 csrx;
        u32 padding2;
        u32 periphid0;
        u32 periphid1;
        u32 periphid2;
        u32 periphid3;
        u32 cellid0;
        u32 cellid1;
        u32 cellid2;
        u32 cellid3;
    }

.. _`hash_register.members`:

Members
-------

cr
    HASH control register (0x000).

din
    HASH data input register (0x004).

str
    HASH start register (0x008).

hx
    HASH digest register 0..7 (0x00c-0x01C).

padding0
    Reserved (0x02C).

itcr
    Integration test control register (0x080).

itip
    Integration test input register (0x084).

itop
    Integration test output register (0x088).

padding1
    Reserved (0x08C).

csfull
    HASH context full register (0x0F8).

csdatain
    HASH context swap data input register (0x0FC).

csrx
    HASH context swap register 0..51 (0x100-0x1CC).

padding2
    Reserved (0x1D0).

periphid0
    HASH peripheral identification register 0 (0xFE0).

periphid1
    HASH peripheral identification register 1 (0xFE4).

periphid2
    HASH peripheral identification register 2 (0xFE8).

periphid3
    HASH peripheral identification register 3 (0xFEC).

cellid0
    HASH PCell identification register 0 (0xFF0).

cellid1
    HASH PCell identification register 1 (0xFF4).

cellid2
    HASH PCell identification register 2 (0xFF8).

cellid3
    HASH PCell identification register 3 (0xFFC).

.. _`hash_register.description`:

Description
-----------

The device communicates to the HASH via 32-bit-wide control registers
accessible via the 32-bit width AMBA rev. 2.0 AHB Bus. Below is a structure
with the registers used.

.. _`hash_state`:

struct hash_state
=================

.. c:type:: struct hash_state

    Hash context state.

.. _`hash_state.definition`:

Definition
----------

.. code-block:: c

    struct hash_state {
        u32 temp_cr;
        u32 str_reg;
        u32 din_reg;
        u32 csr;
        u32 csfull;
        u32 csdatain;
        u32 buffer;
        struct uint64 length;
        u8 index;
        u8 bit_index;
    }

.. _`hash_state.members`:

Members
-------

temp_cr
    Temporary HASH Control Register.

str_reg
    HASH Start Register.

din_reg
    HASH Data Input Register.

csr
    HASH Context Swap Registers 0-39.

csfull
    HASH Context Swap Registers 40 ie Status flags.

csdatain
    HASH Context Swap Registers 41 ie Input data.

buffer
    Working buffer for messages going to the hardware.

length
    Length of the part of message hashed so far (floor(N/64) \* 64).

index
    Valid number of bytes in buffer (N % 64).

bit_index
    Valid number of bits in buffer (N % 8).

.. _`hash_state.description`:

Description
-----------

This structure is used between context switches, i.e. when ongoing jobs are
interupted with new jobs. When this happens we need to store intermediate
results in software.

.. _`hash_state.warning`:

WARNING
-------

"index" is the  member of the structure, to be sure  that "buffer"
is aligned on a 4-bytes boundary. This is highly implementation dependent
and MUST be checked whenever this code is ported on new platforms.

.. _`hash_device_id`:

enum hash_device_id
===================

.. c:type:: enum hash_device_id

    HASH device ID.

.. _`hash_device_id.definition`:

Definition
----------

.. code-block:: c

    enum hash_device_id {
        HASH_DEVICE_ID_0,
        HASH_DEVICE_ID_1
    };

.. _`hash_device_id.constants`:

Constants
---------

HASH_DEVICE_ID_0
    Hash hardware with ID 0

HASH_DEVICE_ID_1
    Hash hardware with ID 1

.. _`hash_data_format`:

enum hash_data_format
=====================

.. c:type:: enum hash_data_format

    HASH data format.

.. _`hash_data_format.definition`:

Definition
----------

.. code-block:: c

    enum hash_data_format {
        HASH_DATA_32_BITS,
        HASH_DATA_16_BITS,
        HASH_DATA_8_BITS,
        HASH_DATA_1_BIT
    };

.. _`hash_data_format.constants`:

Constants
---------

HASH_DATA_32_BITS
    32 bits data format

HASH_DATA_16_BITS
    16 bits data format

HASH_DATA_8_BITS
    8 bits data format.

HASH_DATA_1_BIT
    *undescribed*

.. _`hash_algo`:

enum hash_algo
==============

.. c:type:: enum hash_algo

    Enumeration for selecting between SHA1 or SHA2 algorithm.

.. _`hash_algo.definition`:

Definition
----------

.. code-block:: c

    enum hash_algo {
        HASH_ALGO_SHA1,
        HASH_ALGO_SHA256
    };

.. _`hash_algo.constants`:

Constants
---------

HASH_ALGO_SHA1
    Indicates that SHA1 is used.

HASH_ALGO_SHA256
    *undescribed*

.. _`hash_op`:

enum hash_op
============

.. c:type:: enum hash_op

    Enumeration for selecting between HASH or HMAC mode.

.. _`hash_op.definition`:

Definition
----------

.. code-block:: c

    enum hash_op {
        HASH_OPER_MODE_HASH,
        HASH_OPER_MODE_HMAC
    };

.. _`hash_op.constants`:

Constants
---------

HASH_OPER_MODE_HASH
    Indicates usage of normal HASH mode.

HASH_OPER_MODE_HMAC
    Indicates usage of HMAC.

.. _`hash_config`:

struct hash_config
==================

.. c:type:: struct hash_config

    Configuration data for the hardware.

.. _`hash_config.definition`:

Definition
----------

.. code-block:: c

    struct hash_config {
        int data_format;
        int algorithm;
        int oper_mode;
    }

.. _`hash_config.members`:

Members
-------

data_format
    Format of data entered into the hash data in register.

algorithm
    Algorithm selection bit.

oper_mode
    Operating mode selection bit.

.. _`hash_dma`:

struct hash_dma
===============

.. c:type:: struct hash_dma

    Structure used for dma.

.. _`hash_dma.definition`:

Definition
----------

.. code-block:: c

    struct hash_dma {
        dma_cap_mask_t mask;
        struct completion complete;
        struct dma_chan *chan_mem2hash;
        void *cfg_mem2hash;
        int sg_len;
        struct scatterlist *sg;
        int nents;
    }

.. _`hash_dma.members`:

Members
-------

mask
    DMA capabilities bitmap mask.

complete
    Used to maintain state for a "completion".

chan_mem2hash
    DMA channel.

cfg_mem2hash
    DMA channel configuration.

sg_len
    Scatterlist length.

sg
    Scatterlist.

nents
    Number of sg entries.

.. _`hash_ctx`:

struct hash_ctx
===============

.. c:type:: struct hash_ctx

    The context used for hash calculations.

.. _`hash_ctx.definition`:

Definition
----------

.. code-block:: c

    struct hash_ctx {
        u8 *key;
        u32 keylen;
        struct hash_config config;
        int digestsize;
        struct hash_device_data *device;
    }

.. _`hash_ctx.members`:

Members
-------

key
    The key used in the operation.

keylen
    The length of the key.

config
    The current configuration.

digestsize
    The size of current digest.

device
    Pointer to the device structure.

.. _`hash_req_ctx`:

struct hash_req_ctx
===================

.. c:type:: struct hash_req_ctx

    The request context used for hash calculations.

.. _`hash_req_ctx.definition`:

Definition
----------

.. code-block:: c

    struct hash_req_ctx {
        struct hash_state state;
        bool dma_mode;
        u8 updated;
    }

.. _`hash_req_ctx.members`:

Members
-------

state
    The state of the current calculations.

dma_mode
    Used in special cases (workaround), e.g. need to change to
    cpu mode, if not supported/working in dma mode.

updated
    Indicates if hardware is initialized for new operations.

.. _`hash_device_data`:

struct hash_device_data
=======================

.. c:type:: struct hash_device_data

    structure for a hash device.

.. _`hash_device_data.definition`:

Definition
----------

.. code-block:: c

    struct hash_device_data {
        struct hash_register __iomem *base;
        phys_addr_t phybase;
        struct klist_node list_node;
        struct device *dev;
        struct spinlock ctx_lock;
        struct hash_ctx *current_ctx;
        bool power_state;
        struct spinlock power_state_lock;
        struct regulator *regulator;
        struct clk *clk;
        bool restore_dev_state;
        struct hash_state state;
        struct hash_dma dma;
    }

.. _`hash_device_data.members`:

Members
-------

base
    Pointer to virtual base address of the hash device.

phybase
    Pointer to physical memory location of the hash device.

list_node
    For inclusion in klist.

dev
    Pointer to the device dev structure.

ctx_lock
    Spinlock for current_ctx.

current_ctx
    Pointer to the currently allocated context.

power_state
    TRUE = power state on, FALSE = power state off.

power_state_lock
    Spinlock for power_state.

regulator
    Pointer to the device's power control.

clk
    Pointer to the device's clock control.

restore_dev_state
    TRUE = saved state, FALSE = no saved state.

state
    *undescribed*

dma
    Structure used for dma.

.. This file was automatic generated / don't edit.

