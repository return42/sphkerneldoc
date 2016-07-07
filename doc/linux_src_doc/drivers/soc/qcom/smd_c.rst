.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/smd.c

.. _`qcom_smd_edge`:

struct qcom_smd_edge
====================

.. c:type:: struct qcom_smd_edge

    representing a remote processor

.. _`qcom_smd_edge.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smd_edge {
        struct qcom_smd *smd;
        struct device_node *of_node;
        unsigned edge_id;
        unsigned remote_pid;
        int irq;
        struct regmap *ipc_regmap;
        int ipc_offset;
        int ipc_bit;
        struct list_head channels;
        spinlock_t channels_lock;
        unsigned long allocated[SMD_ALLOC_TBL_COUNT]\[BITS_TO_LONGS(SMD_ALLOC_TBL_SIZE)\];
        unsigned smem_available;
        wait_queue_head_t new_channel_event;
        struct work_struct scan_work;
        struct work_struct state_work;
    }

.. _`qcom_smd_edge.members`:

Members
-------

smd
    handle to qcom_smd

of_node
    of_node handle for information related to this edge

edge_id
    identifier of this edge

remote_pid
    identifier of remote processor

irq
    interrupt for signals on this edge

ipc_regmap
    regmap handle holding the outgoing ipc register

ipc_offset
    offset within \ ``ipc_regmap``\  of the register for ipc

ipc_bit
    bit in the register at \ ``ipc_offset``\  of \ ``ipc_regmap``\ 

channels
    list of all channels detected on this edge

channels_lock
    guard for modifications of \ ``channels``\ 

allocated
    array of bitmaps representing already allocated channels

smem_available
    last available amount of smem triggering a channel scan

new_channel_event
    *undescribed*

scan_work
    work item for discovering new channels

state_work
    work item for edge state changes

.. _`qcom_smd_channel`:

struct qcom_smd_channel
=======================

.. c:type:: struct qcom_smd_channel

    smd channel struct

.. _`qcom_smd_channel.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smd_channel {
        struct qcom_smd_edge *edge;
        struct qcom_smd_device *qsdev;
        char *name;
        enum smd_channel_state state;
        enum smd_channel_state remote_state;
        struct smd_channel_info_pair *info;
        struct smd_channel_info_word_pair *info_word;
        struct mutex tx_lock;
        wait_queue_head_t fblockread_event;
        void *tx_fifo;
        void *rx_fifo;
        int fifo_size;
        void *bounce_buffer;
        qcom_smd_cb_t cb;
        spinlock_t recv_lock;
        int pkt_size;
        void *drvdata;
        struct list_head list;
        struct list_head dev_list;
    }

.. _`qcom_smd_channel.members`:

Members
-------

edge
    qcom_smd_edge this channel is living on

qsdev
    reference to a associated smd client device

name
    name of the channel

state
    local state of the channel

remote_state
    remote state of the channel

info
    byte aligned outgoing/incoming channel info

info_word
    word aligned outgoing/incoming channel info

tx_lock
    lock to make writes to the channel mutually exclusive

fblockread_event
    wakeup event tied to tx fBLOCKREADINTR

tx_fifo
    pointer to the outgoing ring buffer

rx_fifo
    pointer to the incoming ring buffer

fifo_size
    size of each ring buffer

bounce_buffer
    bounce buffer for reading wrapped packets

cb
    callback function registered for this channel

recv_lock
    guard for rx info modifications and cb pointer

pkt_size
    size of the currently handled packet

drvdata
    *undescribed*

list
    lite entry for \ ``channels``\  in qcom_smd_edge

dev_list
    *undescribed*

.. _`qcom_smd`:

struct qcom_smd
===============

.. c:type:: struct qcom_smd

    smd struct

.. _`qcom_smd.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smd {
        struct device *dev;
        unsigned num_edges;
        struct qcom_smd_edge edges[0];
    }

.. _`qcom_smd.members`:

Members
-------

dev
    device struct

num_edges
    number of entries in \ ``edges``\ 

edges
    array of edges to be handled

.. _`qcom_smd_alloc_entry`:

struct qcom_smd_alloc_entry
===========================

.. c:type:: struct qcom_smd_alloc_entry

    channel allocation entry

.. _`qcom_smd_alloc_entry.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smd_alloc_entry {
        u8 name[20];
        __le32 cid;
        __le32 flags;
        __le32 ref_count;
    }

.. _`qcom_smd_alloc_entry.members`:

Members
-------

name
    channel name

cid
    channel index

flags
    channel flags and edge id

ref_count
    reference count of the channel

.. _`qcom_smd_send`:

qcom_smd_send
=============

.. c:function:: int qcom_smd_send(struct qcom_smd_channel *channel, const void *data, int len)

    write data to smd channel

    :param struct qcom_smd_channel \*channel:
        channel handle

    :param const void \*data:
        buffer of data to write

    :param int len:
        number of bytes to write

.. _`qcom_smd_send.description`:

Description
-----------

This is a blocking write of len bytes into the channel's tx ring buffer and
signal the remote end. It will sleep until there is enough space available
in the tx buffer, utilizing the fBLOCKREADINTR signaling mechanism to avoid
polling.

.. _`qcom_smd_driver_register`:

qcom_smd_driver_register
========================

.. c:function:: int qcom_smd_driver_register(struct qcom_smd_driver *qsdrv)

    register a smd driver

    :param struct qcom_smd_driver \*qsdrv:
        qcom_smd_driver struct

.. _`qcom_smd_driver_unregister`:

qcom_smd_driver_unregister
==========================

.. c:function:: void qcom_smd_driver_unregister(struct qcom_smd_driver *qsdrv)

    unregister a smd driver

    :param struct qcom_smd_driver \*qsdrv:
        qcom_smd_driver struct

.. _`qcom_smd_open_channel`:

qcom_smd_open_channel
=====================

.. c:function:: struct qcom_smd_channel *qcom_smd_open_channel(struct qcom_smd_channel *parent, const char *name, qcom_smd_cb_t cb)

    claim additional channels on the same edge

    :param struct qcom_smd_channel \*parent:
        *undescribed*

    :param const char \*name:
        channel name

    :param qcom_smd_cb_t cb:
        callback method to use for incoming data

.. _`qcom_smd_open_channel.description`:

Description
-----------

Returns a channel handle on success, or -EPROBE_DEFER if the channel isn't
ready.

.. This file was automatic generated / don't edit.

