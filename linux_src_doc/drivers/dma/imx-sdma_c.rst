.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/imx-sdma.c

.. _`sdma_channel_control`:

struct sdma_channel_control
===========================

.. c:type:: struct sdma_channel_control

    Channel control Block

.. _`sdma_channel_control.definition`:

Definition
----------

.. code-block:: c

    struct sdma_channel_control {
        u32 current_bd_ptr;
        u32 base_bd_ptr;
        u32 unused[2];
    }

.. _`sdma_channel_control.members`:

Members
-------

current_bd_ptr
    current buffer descriptor processed

base_bd_ptr
    first element of buffer descriptor array

unused
    padding. The SDMA engine expects an array of 128 byte
    control blocks

.. _`sdma_state_registers`:

struct sdma_state_registers
===========================

.. c:type:: struct sdma_state_registers

    SDMA context for a channel

.. _`sdma_state_registers.definition`:

Definition
----------

.. code-block:: c

    struct sdma_state_registers {
        u32 pc :14;
        u32 unused1: 1;
        u32 t : 1;
        u32 rpc :14;
        u32 unused0: 1;
        u32 sf : 1;
        u32 spc :14;
        u32 unused2: 1;
        u32 df : 1;
        u32 epc :14;
        u32 lm : 2;
    }

.. _`sdma_state_registers.members`:

Members
-------

pc
    program counter

unused1
    unused

t
    test bit: status of arithmetic & test instruction

rpc
    return program counter

unused0
    unused

sf
    source fault while loading data

spc
    loop start program counter

unused2
    unused

df
    destination fault while storing data

epc
    loop end program counter

lm
    loop mode

.. _`sdma_context_data`:

struct sdma_context_data
========================

.. c:type:: struct sdma_context_data

    sdma context specific to a channel

.. _`sdma_context_data.definition`:

Definition
----------

.. code-block:: c

    struct sdma_context_data {
        struct sdma_state_registers channel_state;
        u32 gReg[8];
        u32 mda;
        u32 msa;
        u32 ms;
        u32 md;
        u32 pda;
        u32 psa;
        u32 ps;
        u32 pd;
        u32 ca;
        u32 cs;
        u32 dda;
        u32 dsa;
        u32 ds;
        u32 dd;
        u32 scratch0;
        u32 scratch1;
        u32 scratch2;
        u32 scratch3;
        u32 scratch4;
        u32 scratch5;
        u32 scratch6;
        u32 scratch7;
    }

.. _`sdma_context_data.members`:

Members
-------

channel_state
    channel state bits

gReg
    general registers

mda
    burst dma destination address register

msa
    burst dma source address register

ms
    burst dma status register

md
    burst dma data register

pda
    peripheral dma destination address register

psa
    peripheral dma source address register

ps
    peripheral dma status register

pd
    peripheral dma data register

ca
    CRC polynomial register

cs
    CRC accumulator register

dda
    dedicated core destination address register

dsa
    dedicated core source address register

ds
    dedicated core status register

dd
    dedicated core data register

scratch0
    1st word of dedicated ram for context switch

scratch1
    2nd word of dedicated ram for context switch

scratch2
    3rd word of dedicated ram for context switch

scratch3
    4th word of dedicated ram for context switch

scratch4
    5th word of dedicated ram for context switch

scratch5
    6th word of dedicated ram for context switch

scratch6
    7th word of dedicated ram for context switch

scratch7
    8th word of dedicated ram for context switch

.. _`sdma_desc`:

struct sdma_desc
================

.. c:type:: struct sdma_desc

    descriptor structor for one transfer

.. _`sdma_desc.definition`:

Definition
----------

.. code-block:: c

    struct sdma_desc {
        struct virt_dma_desc vd;
        unsigned int num_bd;
        dma_addr_t bd_phys;
        unsigned int buf_tail;
        unsigned int buf_ptail;
        unsigned int period_len;
        unsigned int chn_real_count;
        unsigned int chn_count;
        struct sdma_channel *sdmac;
        struct sdma_buffer_descriptor *bd;
    }

.. _`sdma_desc.members`:

Members
-------

vd
    descriptor for virt dma

num_bd
    number of descriptors currently handling

bd_phys
    physical address of bd

buf_tail
    ID of the buffer that was processed

buf_ptail
    ID of the previous buffer that was processed

period_len
    period length, used in cyclic.

chn_real_count
    the real count updated from bd->mode.count

chn_count
    the transfer count set

sdmac
    sdma_channel pointer

bd
    pointer of allocate bd

.. _`sdma_channel`:

struct sdma_channel
===================

.. c:type:: struct sdma_channel

    housekeeping for a SDMA channel

.. _`sdma_channel.definition`:

Definition
----------

.. code-block:: c

    struct sdma_channel {
        struct virt_dma_chan vc;
        struct sdma_desc *desc;
        struct sdma_engine *sdma;
        unsigned int channel;
        enum dma_transfer_direction direction;
        enum sdma_peripheral_type peripheral_type;
        unsigned int event_id0;
        unsigned int event_id1;
        enum dma_slave_buswidth word_size;
        unsigned int pc_from_device, pc_to_device;
        unsigned int device_to_device;
        unsigned int pc_to_pc;
        unsigned long flags;
        dma_addr_t per_address, per_address2;
        unsigned long event_mask[2];
        unsigned long watermark_level;
        u32 shp_addr, per_addr;
        enum dma_status status;
        struct imx_dma_data data;
        struct dma_pool *bd_pool;
    }

.. _`sdma_channel.members`:

Members
-------

vc
    virt_dma base structure

desc
    sdma description including vd and other special member

sdma
    pointer to the SDMA engine for this channel

channel
    the channel number, matches dmaengine chan_id + 1

direction
    transfer type. Needed for setting SDMA script

peripheral_type
    Peripheral type. Needed for setting SDMA script

event_id0
    aka dma request line

event_id1
    for channels that use 2 events

word_size
    peripheral access size

pc_from_device
    script address for those device_2_memory

pc_to_device
    script address for those memory_2_device

device_to_device
    script address for those device_2_device

pc_to_pc
    script address for those memory_2_memory

flags
    loop mode or not

per_address
    peripheral source or destination address in common case
    destination address in p_2_p case

per_address2
    peripheral source address in p_2_p case

event_mask
    event mask used in p_2_p script

watermark_level
    value for gReg[7], some script will extend it from
    basic watermark such as p_2_p

shp_addr
    value for gReg[6]

per_addr
    value for gReg[2]

status
    status of dma channel

data
    specific sdma interface structure

bd_pool
    dma_pool for bd

.. _`sdma_firmware_header`:

struct sdma_firmware_header
===========================

.. c:type:: struct sdma_firmware_header

    Layout of the firmware image

.. _`sdma_firmware_header.definition`:

Definition
----------

.. code-block:: c

    struct sdma_firmware_header {
        u32 magic;
        u32 version_major;
        u32 version_minor;
        u32 script_addrs_start;
        u32 num_script_addrs;
        u32 ram_code_start;
        u32 ram_code_size;
    }

.. _`sdma_firmware_header.members`:

Members
-------

magic
    "SDMA"

version_major
    increased whenever layout of struct
    sdma_script_start_addrs changes.

version_minor
    firmware minor version (for binary compatible changes)

script_addrs_start
    offset of struct sdma_script_start_addrs in this image

num_script_addrs
    Number of script addresses in this image

ram_code_start
    offset of SDMA ram image in this firmware image

ram_code_size
    size of SDMA ram image

.. This file was automatic generated / don't edit.

