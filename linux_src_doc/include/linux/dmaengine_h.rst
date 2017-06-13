.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dmaengine.h

.. _`dma_cookie_t`:

typedef dma_cookie_t
====================

.. c:type:: typedef dma_cookie_t

    an opaque DMA cookie

.. _`dma_cookie_t.description`:

Description
-----------

if dma_cookie_t is >0 it's a DMA request cookie, <0 it's an error code

.. _`dma_status`:

enum dma_status
===============

.. c:type:: enum dma_status

    DMA transaction status

.. _`dma_status.definition`:

Definition
----------

.. code-block:: c

    enum dma_status {
        DMA_COMPLETE,
        DMA_IN_PROGRESS,
        DMA_PAUSED,
        DMA_ERROR
    };

.. _`dma_status.constants`:

Constants
---------

DMA_COMPLETE
    transaction completed

DMA_IN_PROGRESS
    transaction not yet processed

DMA_PAUSED
    transaction is paused

DMA_ERROR
    transaction failed

.. _`dma_transaction_type`:

enum dma_transaction_type
=========================

.. c:type:: enum dma_transaction_type

    DMA transaction types/indexes

.. _`dma_transaction_type.definition`:

Definition
----------

.. code-block:: c

    enum dma_transaction_type {
        DMA_MEMCPY,
        DMA_XOR,
        DMA_PQ,
        DMA_XOR_VAL,
        DMA_PQ_VAL,
        DMA_MEMSET,
        DMA_MEMSET_SG,
        DMA_INTERRUPT,
        DMA_SG,
        DMA_PRIVATE,
        DMA_ASYNC_TX,
        DMA_SLAVE,
        DMA_CYCLIC,
        DMA_INTERLEAVE,
        DMA_TX_TYPE_END
    };

.. _`dma_transaction_type.constants`:

Constants
---------

DMA_MEMCPY
    *undescribed*

DMA_XOR
    *undescribed*

DMA_PQ
    *undescribed*

DMA_XOR_VAL
    *undescribed*

DMA_PQ_VAL
    *undescribed*

DMA_MEMSET
    *undescribed*

DMA_MEMSET_SG
    *undescribed*

DMA_INTERRUPT
    *undescribed*

DMA_SG
    *undescribed*

DMA_PRIVATE
    *undescribed*

DMA_ASYNC_TX
    *undescribed*

DMA_SLAVE
    *undescribed*

DMA_CYCLIC
    *undescribed*

DMA_INTERLEAVE
    *undescribed*

DMA_TX_TYPE_END
    *undescribed*

.. _`dma_transaction_type.note`:

Note
----

The DMA_ASYNC_TX capability is not to be set by drivers.  It is
automatically set as dma devices are registered.

.. _`dma_transfer_direction`:

enum dma_transfer_direction
===========================

.. c:type:: enum dma_transfer_direction

    dma transfer mode and direction indicator

.. _`dma_transfer_direction.definition`:

Definition
----------

.. code-block:: c

    enum dma_transfer_direction {
        DMA_MEM_TO_MEM,
        DMA_MEM_TO_DEV,
        DMA_DEV_TO_MEM,
        DMA_DEV_TO_DEV,
        DMA_TRANS_NONE
    };

.. _`dma_transfer_direction.constants`:

Constants
---------

DMA_MEM_TO_MEM
    Async/Memcpy mode

DMA_MEM_TO_DEV
    Slave mode & From Memory to Device

DMA_DEV_TO_MEM
    Slave mode & From Device to Memory

DMA_DEV_TO_DEV
    Slave mode & From Device to Device

DMA_TRANS_NONE
    *undescribed*

.. _`dma_interleaved_template`:

struct dma_interleaved_template
===============================

.. c:type:: struct dma_interleaved_template

    Template to convey DMAC the transfer pattern and attributes.

.. _`dma_interleaved_template.definition`:

Definition
----------

.. code-block:: c

    struct dma_interleaved_template {
        dma_addr_t src_start;
        dma_addr_t dst_start;
        enum dma_transfer_direction dir;
        bool src_inc;
        bool dst_inc;
        bool src_sgl;
        bool dst_sgl;
        size_t numf;
        size_t frame_size;
        struct data_chunk sgl;
    }

.. _`dma_interleaved_template.members`:

Members
-------

src_start
    Bus address of source for the first chunk.

dst_start
    Bus address of destination for the first chunk.

dir
    Specifies the type of Source and Destination.

src_inc
    If the source address increments after reading from it.

dst_inc
    If the destination address increments after writing to it.

src_sgl
    If the 'icg' of sgl[] applies to Source (scattered read).
    Otherwise, source is read contiguously (icg ignored).
    Ignored if src_inc is false.

dst_sgl
    If the 'icg' of sgl[] applies to Destination (scattered write).
    Otherwise, destination is filled contiguously (icg ignored).
    Ignored if dst_inc is false.

numf
    Number of frames in this template.

frame_size
    Number of chunks in a frame i.e, size of sgl[].

sgl
    Array of {chunk,icg} pairs that make up a frame.

.. _`dma_ctrl_flags`:

enum dma_ctrl_flags
===================

.. c:type:: enum dma_ctrl_flags

    DMA flags to augment operation preparation, control completion, and communicate status. \ ``DMA_PREP_INTERRUPT``\  - trigger an interrupt (callback) upon completion of this transaction \ ``DMA_CTRL_ACK``\  - if clear, the descriptor cannot be reused until the client acknowledges receipt, i.e. has has a chance to establish any dependency chains \ ``DMA_PREP_PQ_DISABLE_P``\  - prevent generation of P while generating Q \ ``DMA_PREP_PQ_DISABLE_Q``\  - prevent generation of Q while generating P \ ``DMA_PREP_CONTINUE``\  - indicate to a driver that it is reusing buffers as sources that were the result of a previous operation, in the case of a PQ operation it continues the calculation with new sources \ ``DMA_PREP_FENCE``\  - tell the driver that subsequent operations depend on the result of this operation

.. _`dma_ctrl_flags.definition`:

Definition
----------

.. code-block:: c

    enum dma_ctrl_flags {
        DMA_PREP_INTERRUPT,
        DMA_CTRL_ACK,
        DMA_PREP_PQ_DISABLE_P,
        DMA_PREP_PQ_DISABLE_Q,
        DMA_PREP_CONTINUE,
        DMA_PREP_FENCE,
        DMA_CTRL_REUSE
    };

.. _`dma_ctrl_flags.constants`:

Constants
---------

DMA_PREP_INTERRUPT
    *undescribed*

DMA_CTRL_ACK
    *undescribed*

DMA_PREP_PQ_DISABLE_P
    *undescribed*

DMA_PREP_PQ_DISABLE_Q
    *undescribed*

DMA_PREP_CONTINUE
    *undescribed*

DMA_PREP_FENCE
    *undescribed*

DMA_CTRL_REUSE
    client can reuse the descriptor and submit again till
    cleared or freed

.. _`sum_check_bits`:

enum sum_check_bits
===================

.. c:type:: enum sum_check_bits

    bit position of pq_check_flags

.. _`sum_check_bits.definition`:

Definition
----------

.. code-block:: c

    enum sum_check_bits {
        SUM_CHECK_P,
        SUM_CHECK_Q
    };

.. _`sum_check_bits.constants`:

Constants
---------

SUM_CHECK_P
    *undescribed*

SUM_CHECK_Q
    *undescribed*

.. _`sum_check_flags`:

enum sum_check_flags
====================

.. c:type:: enum sum_check_flags

    result of async_{xor,pq}_zero_sum operations \ ``SUM_CHECK_P_RESULT``\  - 1 if xor zero sum error, 0 otherwise \ ``SUM_CHECK_Q_RESULT``\  - 1 if reed-solomon zero sum error, 0 otherwise

.. _`sum_check_flags.definition`:

Definition
----------

.. code-block:: c

    enum sum_check_flags {
        SUM_CHECK_P_RESULT,
        SUM_CHECK_Q_RESULT
    };

.. _`sum_check_flags.constants`:

Constants
---------

SUM_CHECK_P_RESULT
    *undescribed*

SUM_CHECK_Q_RESULT
    *undescribed*

.. _`dma_cap_mask_t`:

typedef dma_cap_mask_t
======================

.. c:type:: typedef dma_cap_mask_t

    capabilities bitmap modeled after cpumask_t. See linux/cpumask.h

.. _`dma_chan_percpu`:

struct dma_chan_percpu
======================

.. c:type:: struct dma_chan_percpu

    the per-CPU part of struct dma_chan

.. _`dma_chan_percpu.definition`:

Definition
----------

.. code-block:: c

    struct dma_chan_percpu {
        unsigned long memcpy_count;
        unsigned long bytes_transferred;
    }

.. _`dma_chan_percpu.members`:

Members
-------

memcpy_count
    transaction counter

bytes_transferred
    byte counter

.. _`dma_router`:

struct dma_router
=================

.. c:type:: struct dma_router

    DMA router structure

.. _`dma_router.definition`:

Definition
----------

.. code-block:: c

    struct dma_router {
        struct device *dev;
        void (*route_free)(struct device *dev, void *route_data);
    }

.. _`dma_router.members`:

Members
-------

dev
    pointer to the DMA router device

route_free
    function to be called when the route can be disconnected

.. _`dma_chan`:

struct dma_chan
===============

.. c:type:: struct dma_chan

    devices supply DMA channels, clients use them

.. _`dma_chan.definition`:

Definition
----------

.. code-block:: c

    struct dma_chan {
        struct dma_device *device;
        dma_cookie_t cookie;
        dma_cookie_t completed_cookie;
        int chan_id;
        struct dma_chan_dev *dev;
        struct list_head device_node;
        struct dma_chan_percpu __percpu *local;
        int client_count;
        int table_count;
        struct dma_router *router;
        void *route_data;
        void *private;
    }

.. _`dma_chan.members`:

Members
-------

device
    ptr to the dma device who supplies this channel, always !%NULL

cookie
    last cookie value returned to client

completed_cookie
    last completed cookie for this channel

chan_id
    channel ID for sysfs

dev
    class device for sysfs

device_node
    used to add this to the device chan list

local
    per-cpu pointer to a struct dma_chan_percpu

client_count
    how many clients are using this channel

table_count
    number of appearances in the mem-to-mem allocation table

router
    pointer to the DMA router structure

route_data
    channel specific data for the router

private
    private data for certain client-channel associations

.. _`dma_chan_dev`:

struct dma_chan_dev
===================

.. c:type:: struct dma_chan_dev

    relate sysfs device node to backing channel device

.. _`dma_chan_dev.definition`:

Definition
----------

.. code-block:: c

    struct dma_chan_dev {
        struct dma_chan *chan;
        struct device device;
        int dev_id;
        atomic_t *idr_ref;
    }

.. _`dma_chan_dev.members`:

Members
-------

chan
    driver channel device

device
    sysfs device

dev_id
    parent dma_device dev_id

idr_ref
    reference count to gate release of dma_device dev_id

.. _`dma_slave_buswidth`:

enum dma_slave_buswidth
=======================

.. c:type:: enum dma_slave_buswidth

    defines bus width of the DMA slave device, source or target buses

.. _`dma_slave_buswidth.definition`:

Definition
----------

.. code-block:: c

    enum dma_slave_buswidth {
        DMA_SLAVE_BUSWIDTH_UNDEFINED,
        DMA_SLAVE_BUSWIDTH_1_BYTE,
        DMA_SLAVE_BUSWIDTH_2_BYTES,
        DMA_SLAVE_BUSWIDTH_3_BYTES,
        DMA_SLAVE_BUSWIDTH_4_BYTES,
        DMA_SLAVE_BUSWIDTH_8_BYTES,
        DMA_SLAVE_BUSWIDTH_16_BYTES,
        DMA_SLAVE_BUSWIDTH_32_BYTES,
        DMA_SLAVE_BUSWIDTH_64_BYTES
    };

.. _`dma_slave_buswidth.constants`:

Constants
---------

DMA_SLAVE_BUSWIDTH_UNDEFINED
    *undescribed*

DMA_SLAVE_BUSWIDTH_1_BYTE
    *undescribed*

DMA_SLAVE_BUSWIDTH_2_BYTES
    *undescribed*

DMA_SLAVE_BUSWIDTH_3_BYTES
    *undescribed*

DMA_SLAVE_BUSWIDTH_4_BYTES
    *undescribed*

DMA_SLAVE_BUSWIDTH_8_BYTES
    *undescribed*

DMA_SLAVE_BUSWIDTH_16_BYTES
    *undescribed*

DMA_SLAVE_BUSWIDTH_32_BYTES
    *undescribed*

DMA_SLAVE_BUSWIDTH_64_BYTES
    *undescribed*

.. _`dma_slave_config`:

struct dma_slave_config
=======================

.. c:type:: struct dma_slave_config

    dma slave channel runtime config

.. _`dma_slave_config.definition`:

Definition
----------

.. code-block:: c

    struct dma_slave_config {
        enum dma_transfer_direction direction;
        phys_addr_t src_addr;
        phys_addr_t dst_addr;
        enum dma_slave_buswidth src_addr_width;
        enum dma_slave_buswidth dst_addr_width;
        u32 src_maxburst;
        u32 dst_maxburst;
        u32 src_port_window_size;
        u32 dst_port_window_size;
        bool device_fc;
        unsigned int slave_id;
    }

.. _`dma_slave_config.members`:

Members
-------

direction
    whether the data shall go in or out on this slave
    channel, right now. DMA_MEM_TO_DEV and DMA_DEV_TO_MEM are
    legal values. DEPRECATED, drivers should use the direction argument
    to the device_prep_slave_sg and device_prep_dma_cyclic functions or
    the dir field in the dma_interleaved_template structure.

src_addr
    this is the physical address where DMA slave data
    should be read (RX), if the source is memory this argument is
    ignored.

dst_addr
    this is the physical address where DMA slave data
    should be written (TX), if the source is memory this argument
    is ignored.

src_addr_width
    this is the width in bytes of the source (RX)
    register where DMA data shall be read. If the source
    is memory this may be ignored depending on architecture.

dst_addr_width
    same as src_addr_width but for destination
    target (TX) mutatis mutandis.

src_maxburst
    the maximum number of words (note: words, as in
    units of the src_addr_width member, not bytes) that can be sent
    in one burst to the device. Typically something like half the
    FIFO depth on I/O peripherals so you don't overflow it. This
    may or may not be applicable on memory sources.

dst_maxburst
    same as src_maxburst but for destination target
    mutatis mutandis.

src_port_window_size
    The length of the register area in words the data need
    to be accessed on the device side. It is only used for devices which is using
    an area instead of a single register to receive the data. Typically the DMA
    loops in this area in order to transfer the data.

dst_port_window_size
    same as src_port_window_size but for the destination
    port.

device_fc
    Flow Controller Settings. Only valid for slave channels. Fill
    with 'true' if peripheral should be flow controller. Direction will be
    selected at Runtime.

slave_id
    Slave requester id. Only valid for slave channels. The dma
    slave peripheral will have unique id as dma requester which need to be
    pass as slave config.

.. _`dma_slave_config.legal-values`:

Legal values
------------

1, 2, 4, 8.

.. _`dma_slave_config.description`:

Description
-----------

This struct is passed in as configuration data to a DMA engine
in order to set up a certain channel for DMA transport at runtime.
The DMA device/engine has to provide support for an additional
callback in the dma_device structure, device_config and this struct
will then be passed in as an argument to the function.

The rationale for adding configuration information to this struct is as

.. _`dma_slave_config.follows`:

follows
-------

if it is likely that more than one DMA slave controllers in
the world will support the configuration option, then make it generic.

.. _`dma_slave_config.if-not`:

If not
------

if it is fixed so that it be sent in static from the platform
data, then prefer to do that.

.. _`dma_residue_granularity`:

enum dma_residue_granularity
============================

.. c:type:: enum dma_residue_granularity

    Granularity of the reported transfer residue

.. _`dma_residue_granularity.definition`:

Definition
----------

.. code-block:: c

    enum dma_residue_granularity {
        DMA_RESIDUE_GRANULARITY_DESCRIPTOR,
        DMA_RESIDUE_GRANULARITY_SEGMENT,
        DMA_RESIDUE_GRANULARITY_BURST
    };

.. _`dma_residue_granularity.constants`:

Constants
---------

DMA_RESIDUE_GRANULARITY_DESCRIPTOR
    Residue reporting is not support. The
    DMA channel is only able to tell whether a descriptor has been completed or
    not, which means residue reporting is not supported by this channel. The
    residue field of the dma_tx_state field will always be 0.

DMA_RESIDUE_GRANULARITY_SEGMENT
    Residue is updated after each successfully
    completed segment of the transfer (For cyclic transfers this is after each
    period). This is typically implemented by having the hardware generate an
    interrupt after each transferred segment and then the drivers updates the
    outstanding residue by the size of the segment. Another possibility is if
    the hardware supports scatter-gather and the segment descriptor has a field
    which gets set after the segment has been completed. The driver then counts
    the number of segments without the flag set to compute the residue.

DMA_RESIDUE_GRANULARITY_BURST
    Residue is updated after each transferred
    burst. This is typically only supported if the hardware has a progress
    register of some sort (E.g. a register with the current read/write address
    or a register with the amount of bursts/beats/bytes that have been
    transferred or still need to be transferred).

.. _`dma_filter_fn`:

dma_filter_fn
=============

.. c:function:: bool dma_filter_fn(struct dma_chan *chan, void *filter_param)

    callback filter for dma_request_channel

    :param struct dma_chan \*chan:
        channel to be reviewed

    :param void \*filter_param:
        opaque parameter passed through dma_request_channel

.. _`dma_filter_fn.description`:

Description
-----------

When this optional parameter is specified in a call to dma_request_channel a
suitable channel is passed to this routine for further dispositioning before
being returned.  Where 'suitable' indicates a non-busy channel that
satisfies the given capability mask.  It returns 'true' to indicate that the
channel is suitable.

.. _`dma_async_tx_descriptor`:

struct dma_async_tx_descriptor
==============================

.. c:type:: struct dma_async_tx_descriptor

    async transaction descriptor ---dma generic offload fields---

.. _`dma_async_tx_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct dma_async_tx_descriptor {
        dma_cookie_t cookie;
        enum dma_ctrl_flags flags;
        dma_addr_t phys;
        struct dma_chan *chan;
        dma_cookie_t (*tx_submit)(struct dma_async_tx_descriptor *tx);
        int (*desc_free)(struct dma_async_tx_descriptor *tx);
        dma_async_tx_callback callback;
        dma_async_tx_callback_result callback_result;
        void *callback_param;
        struct dmaengine_unmap_data *unmap;
    #ifdef CONFIG_ASYNC_TX_ENABLE_CHANNEL_SWITCH
        struct dma_async_tx_descriptor *next;
        struct dma_async_tx_descriptor *parent;
        spinlock_t lock;
    #endif
    }

.. _`dma_async_tx_descriptor.members`:

Members
-------

cookie
    tracking cookie for this transaction, set to -EBUSY if
    this tx is sitting on a dependency list

flags
    flags to augment operation preparation, control completion, and
    communicate status

phys
    physical address of the descriptor

chan
    target channel for this operation

tx_submit
    accept the descriptor, assign ordered cookie and mark the
    descriptor pending. To be pushed on .issue_pending() call

desc_free
    *undescribed*

callback
    routine to call after this operation is complete

callback_result
    *undescribed*

callback_param
    general parameter to pass to the callback routine
    ---async_tx api specific fields---

unmap
    *undescribed*

next
    at completion submit this descriptor

parent
    pointer to the next level up in the dependency chain

lock
    protect the parent and next pointers

.. _`dma_tx_state`:

struct dma_tx_state
===================

.. c:type:: struct dma_tx_state

    filled in to report the status of a transfer.

.. _`dma_tx_state.definition`:

Definition
----------

.. code-block:: c

    struct dma_tx_state {
        dma_cookie_t last;
        dma_cookie_t used;
        u32 residue;
    }

.. _`dma_tx_state.members`:

Members
-------

last
    last completed DMA cookie

used
    last issued DMA cookie (i.e. the one in progress)

residue
    the remaining number of bytes left to transmit
    on the selected transfer for states DMA_IN_PROGRESS and
    DMA_PAUSED if this is implemented in the driver, else 0

.. _`dmaengine_alignment`:

enum dmaengine_alignment
========================

.. c:type:: enum dmaengine_alignment

    defines alignment of the DMA async tx buffers

.. _`dmaengine_alignment.definition`:

Definition
----------

.. code-block:: c

    enum dmaengine_alignment {
        DMAENGINE_ALIGN_1_BYTE,
        DMAENGINE_ALIGN_2_BYTES,
        DMAENGINE_ALIGN_4_BYTES,
        DMAENGINE_ALIGN_8_BYTES,
        DMAENGINE_ALIGN_16_BYTES,
        DMAENGINE_ALIGN_32_BYTES,
        DMAENGINE_ALIGN_64_BYTES
    };

.. _`dmaengine_alignment.constants`:

Constants
---------

DMAENGINE_ALIGN_1_BYTE
    *undescribed*

DMAENGINE_ALIGN_2_BYTES
    *undescribed*

DMAENGINE_ALIGN_4_BYTES
    *undescribed*

DMAENGINE_ALIGN_8_BYTES
    *undescribed*

DMAENGINE_ALIGN_16_BYTES
    *undescribed*

DMAENGINE_ALIGN_32_BYTES
    *undescribed*

DMAENGINE_ALIGN_64_BYTES
    *undescribed*

.. _`dma_slave_map`:

struct dma_slave_map
====================

.. c:type:: struct dma_slave_map

    associates slave device and it's slave channel with parameter to be used by a filter function

.. _`dma_slave_map.definition`:

Definition
----------

.. code-block:: c

    struct dma_slave_map {
        const char *devname;
        const char *slave;
        void *param;
    }

.. _`dma_slave_map.members`:

Members
-------

devname
    name of the device

slave
    slave channel name

param
    opaque parameter to pass to struct dma_filter.fn

.. _`dma_filter`:

struct dma_filter
=================

.. c:type:: struct dma_filter

    information for slave device/channel to filter_fn/param mapping

.. _`dma_filter.definition`:

Definition
----------

.. code-block:: c

    struct dma_filter {
        dma_filter_fn fn;
        int mapcnt;
        const struct dma_slave_map *map;
    }

.. _`dma_filter.members`:

Members
-------

fn
    filter function callback

mapcnt
    number of slave device/channel in the map

map
    array of channel to filter mapping data

.. _`dma_device`:

struct dma_device
=================

.. c:type:: struct dma_device

    info on the entity supplying DMA services

.. _`dma_device.definition`:

Definition
----------

.. code-block:: c

    struct dma_device {
        unsigned int chancnt;
        unsigned int privatecnt;
        struct list_head channels;
        struct list_head global_node;
        struct dma_filter filter;
        dma_cap_mask_t cap_mask;
        unsigned short max_xor;
        unsigned short max_pq;
        enum dmaengine_alignment copy_align;
        enum dmaengine_alignment xor_align;
        enum dmaengine_alignment pq_align;
        enum dmaengine_alignment fill_align;
    #define DMA_HAS_PQ_CONTINUE (1 << 15)
        int dev_id;
        struct device *dev;
        u32 src_addr_widths;
        u32 dst_addr_widths;
        u32 directions;
        u32 max_burst;
        bool descriptor_reuse;
        enum dma_residue_granularity residue_granularity;
        int (*device_alloc_chan_resources)(struct dma_chan *chan);
        void (*device_free_chan_resources)(struct dma_chan *chan);
        struct dma_async_tx_descriptor *(*device_prep_dma_memcpy)(struct dma_chan *chan, dma_addr_t dst, dma_addr_t src,size_t len, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_xor)(struct dma_chan *chan, dma_addr_t dst, dma_addr_t *src,unsigned int src_cnt, size_t len, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_xor_val)(struct dma_chan *chan, dma_addr_t *src, unsigned int src_cnt,size_t len, enum sum_check_flags *result, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_pq)(struct dma_chan *chan, dma_addr_t *dst, dma_addr_t *src,unsigned int src_cnt, const unsigned char *scf,size_t len, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_pq_val)(struct dma_chan *chan, dma_addr_t *pq, dma_addr_t *src,unsigned int src_cnt, const unsigned char *scf, size_t len,enum sum_check_flags *pqres, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_memset)(struct dma_chan *chan, dma_addr_t dest, int value, size_t len,unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_memset_sg)(struct dma_chan *chan, struct scatterlist *sg,unsigned int nents, int value, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_interrupt)(struct dma_chan *chan, unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_sg)(struct dma_chan *chan,struct scatterlist *dst_sg, unsigned int dst_nents,struct scatterlist *src_sg, unsigned int src_nents,unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_slave_sg)(struct dma_chan *chan, struct scatterlist *sgl,unsigned int sg_len, enum dma_transfer_direction direction,unsigned long flags, void *context);
        struct dma_async_tx_descriptor *(*device_prep_dma_cyclic)(struct dma_chan *chan, dma_addr_t buf_addr, size_t buf_len,size_t period_len, enum dma_transfer_direction direction,unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_interleaved_dma)(struct dma_chan *chan, struct dma_interleaved_template *xt,unsigned long flags);
        struct dma_async_tx_descriptor *(*device_prep_dma_imm_data)(struct dma_chan *chan, dma_addr_t dst, u64 data,unsigned long flags);
        int (*device_config)(struct dma_chan *chan,struct dma_slave_config *config);
        int (*device_pause)(struct dma_chan *chan);
        int (*device_resume)(struct dma_chan *chan);
        int (*device_terminate_all)(struct dma_chan *chan);
        void (*device_synchronize)(struct dma_chan *chan);
        enum dma_status (*device_tx_status)(struct dma_chan *chan,dma_cookie_t cookie,struct dma_tx_state *txstate);
        void (*device_issue_pending)(struct dma_chan *chan);
    }

.. _`dma_device.members`:

Members
-------

chancnt
    how many DMA channels are supported

privatecnt
    how many DMA channels are requested by dma_request_channel

channels
    the list of struct dma_chan

global_node
    list_head for global dma_device_list

filter
    information for device/slave to filter function/param mapping

cap_mask
    one or more dma_capability flags

max_xor
    maximum number of xor sources, 0 if no capability

max_pq
    maximum number of PQ sources and PQ-continue capability

copy_align
    alignment shift for memcpy operations

xor_align
    alignment shift for xor operations

pq_align
    alignment shift for pq operations

fill_align
    alignment shift for memset operations

dev_id
    unique device ID

dev
    struct device reference for dma mapping api

src_addr_widths
    bit mask of src addr widths the device supports

dst_addr_widths
    bit mask of dst addr widths the device supports

directions
    bit mask of slave direction the device supports since
    the enum dma_transfer_direction is not defined as bits for
    each type of direction, the dma controller should fill (1 <<
    <TYPE>) and same should be checked by controller as well

max_burst
    max burst capability per-transfer

descriptor_reuse
    a submitted transfer can be resubmitted after completion

residue_granularity
    granularity of the transfer residue reported
    by tx_status

device_alloc_chan_resources
    allocate resources and return the
    number of allocated descriptors

device_free_chan_resources
    release DMA channel's resources

device_prep_dma_memcpy
    prepares a memcpy operation

device_prep_dma_xor
    prepares a xor operation

device_prep_dma_xor_val
    prepares a xor validation operation

device_prep_dma_pq
    prepares a pq operation

device_prep_dma_pq_val
    prepares a pqzero_sum operation

device_prep_dma_memset
    prepares a memset operation

device_prep_dma_memset_sg
    prepares a memset operation over a scatter list

device_prep_dma_interrupt
    prepares an end of chain interrupt operation

device_prep_dma_sg
    *undescribed*

device_prep_slave_sg
    prepares a slave dma operation

device_prep_dma_cyclic
    prepare a cyclic dma operation suitable for audio.
    The function takes a buffer of size buf_len. The callback function will
    be called after period_len bytes have been transferred.

device_prep_interleaved_dma
    Transfer expression in a generic way.

device_prep_dma_imm_data
    DMA's 8 byte immediate data to the dst address

device_config
    Pushes a new configuration to a channel, return 0 or an error
    code

device_pause
    Pauses any transfer happening on a channel. Returns
    0 or an error code

device_resume
    Resumes any transfer on a channel previously
    paused. Returns 0 or an error code

device_terminate_all
    Aborts all transfers on a channel. Returns 0
    or an error code

device_synchronize
    Synchronizes the termination of a transfers to the
    current context.

device_tx_status
    poll for transaction completion, the optional
    txstate parameter can be supplied with a pointer to get a
    struct with auxiliary transfer status information, otherwise the call
    will just return a simple status code

device_issue_pending
    push pending transactions to hardware

.. _`dmaengine_terminate_all`:

dmaengine_terminate_all
=======================

.. c:function:: int dmaengine_terminate_all(struct dma_chan *chan)

    Terminate all active DMA transfers

    :param struct dma_chan \*chan:
        The channel for which to terminate the transfers

.. _`dmaengine_terminate_all.description`:

Description
-----------

This function is DEPRECATED use either \ :c:func:`dmaengine_terminate_sync`\  or
\ :c:func:`dmaengine_terminate_async`\  instead.

.. _`dmaengine_terminate_async`:

dmaengine_terminate_async
=========================

.. c:function:: int dmaengine_terminate_async(struct dma_chan *chan)

    Terminate all active DMA transfers

    :param struct dma_chan \*chan:
        The channel for which to terminate the transfers

.. _`dmaengine_terminate_async.description`:

Description
-----------

Calling this function will terminate all active and pending descriptors
that have previously been submitted to the channel. It is not guaranteed
though that the transfer for the active descriptor has stopped when the
function returns. Furthermore it is possible the complete callback of a
submitted transfer is still running when this function returns.

\ :c:func:`dmaengine_synchronize`\  needs to be called before it is safe to free
any memory that is accessed by previously submitted descriptors or before
freeing any resources accessed from within the completion callback of any
perviously submitted descriptors.

This function can be called from atomic context as well as from within a
complete callback of a descriptor submitted on the same channel.

If none of the two conditions above apply consider using
\ :c:func:`dmaengine_terminate_sync`\  instead.

.. _`dmaengine_synchronize`:

dmaengine_synchronize
=====================

.. c:function:: void dmaengine_synchronize(struct dma_chan *chan)

    Synchronize DMA channel termination

    :param struct dma_chan \*chan:
        The channel to synchronize

.. _`dmaengine_synchronize.description`:

Description
-----------

Synchronizes to the DMA channel termination to the current context. When this
function returns it is guaranteed that all transfers for previously issued
descriptors have stopped and and it is safe to free the memory assoicated
with them. Furthermore it is guaranteed that all complete callback functions
for a previously submitted descriptor have finished running and it is safe to
free resources accessed from within the complete callbacks.

The behavior of this function is undefined if \ :c:func:`dma_async_issue_pending`\  has
been called between \ :c:func:`dmaengine_terminate_async`\  and this function.

This function must only be called from non-atomic context and must not be
called from within a complete callback of a descriptor submitted on the same
channel.

.. _`dmaengine_terminate_sync`:

dmaengine_terminate_sync
========================

.. c:function:: int dmaengine_terminate_sync(struct dma_chan *chan)

    Terminate all active DMA transfers

    :param struct dma_chan \*chan:
        The channel for which to terminate the transfers

.. _`dmaengine_terminate_sync.description`:

Description
-----------

Calling this function will terminate all active and pending transfers
that have previously been submitted to the channel. It is similar to
\ :c:func:`dmaengine_terminate_async`\  but guarantees that the DMA transfer has actually
stopped and that all complete callbacks have finished running when the
function returns.

This function must only be called from non-atomic context and must not be
called from within a complete callback of a descriptor submitted on the same
channel.

.. _`dma_async_issue_pending`:

dma_async_issue_pending
=======================

.. c:function:: void dma_async_issue_pending(struct dma_chan *chan)

    flush pending transactions to HW

    :param struct dma_chan \*chan:
        target DMA channel

.. _`dma_async_issue_pending.description`:

Description
-----------

This allows drivers to push copies to HW in batches,
reducing MMIO writes where possible.

.. _`dma_async_is_tx_complete`:

dma_async_is_tx_complete
========================

.. c:function:: enum dma_status dma_async_is_tx_complete(struct dma_chan *chan, dma_cookie_t cookie, dma_cookie_t *last, dma_cookie_t *used)

    poll for transaction completion

    :param struct dma_chan \*chan:
        DMA channel

    :param dma_cookie_t cookie:
        transaction identifier to check status of

    :param dma_cookie_t \*last:
        returns last completed cookie, can be NULL

    :param dma_cookie_t \*used:
        returns last issued cookie, can be NULL

.. _`dma_async_is_tx_complete.description`:

Description
-----------

If \ ``last``\  and \ ``used``\  are passed in, upon return they reflect the driver
internal state and can be used with \ :c:func:`dma_async_is_complete`\  to check
the status of multiple cookies without re-checking hardware state.

.. _`dma_async_is_complete`:

dma_async_is_complete
=====================

.. c:function:: enum dma_status dma_async_is_complete(dma_cookie_t cookie, dma_cookie_t last_complete, dma_cookie_t last_used)

    test a cookie against chan state

    :param dma_cookie_t cookie:
        transaction identifier to test status of

    :param dma_cookie_t last_complete:
        last know completed transaction

    :param dma_cookie_t last_used:
        last cookie value handed out

.. _`dma_async_is_complete.description`:

Description
-----------

dma_async_is_complete() is used in \ :c:func:`dma_async_is_tx_complete`\ 
the test logic is separated for lightweight testing of multiple cookies

.. This file was automatic generated / don't edit.

