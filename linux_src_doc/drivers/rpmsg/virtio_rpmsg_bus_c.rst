.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rpmsg/virtio_rpmsg_bus.c

.. _`virtproc_info`:

struct virtproc_info
====================

.. c:type:: struct virtproc_info

    virtual remote processor state

.. _`virtproc_info.definition`:

Definition
----------

.. code-block:: c

    struct virtproc_info {
        struct virtio_device *vdev;
        struct virtqueue *rvq, *svq;
        void *rbufs, *sbufs;
        unsigned int num_bufs;
        unsigned int buf_size;
        int last_sbuf;
        dma_addr_t bufs_dma;
        struct mutex tx_lock;
        struct idr endpoints;
        struct mutex endpoints_lock;
        wait_queue_head_t sendq;
        atomic_t sleepers;
        struct rpmsg_endpoint *ns_ept;
    }

.. _`virtproc_info.members`:

Members
-------

vdev
    the virtio device

rvq
    rx virtqueue

svq
    tx virtqueue

rbufs
    kernel address of rx buffers

sbufs
    kernel address of tx buffers

num_bufs
    total number of buffers for rx and tx

buf_size
    size of one rx or tx buffer

last_sbuf
    index of last tx buffer used

bufs_dma
    dma base addr of the buffers

tx_lock
    protects svq, sbufs and sleepers, to allow concurrent senders.
    sending a message might require waking up a dozing remote
    processor, which involves sleeping, hence the mutex.

endpoints
    idr of local endpoints, allows fast retrieval

endpoints_lock
    lock of the endpoints set

sendq
    wait queue of sending contexts waiting for a tx buffers

sleepers
    number of senders that are waiting for a tx buffer

ns_ept
    the bus's name service endpoint

.. _`virtproc_info.description`:

Description
-----------

This structure stores the rpmsg state of a given virtio remote processor
device (there might be several virtio proc devices for each physical
remote processor).

.. _`rpmsg_hdr`:

struct rpmsg_hdr
================

.. c:type:: struct rpmsg_hdr

    common header for all rpmsg messages

.. _`rpmsg_hdr.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_hdr {
        u32 src;
        u32 dst;
        u32 reserved;
        u16 len;
        u16 flags;
        u8 data[0];
    }

.. _`rpmsg_hdr.members`:

Members
-------

src
    source address

dst
    destination address

reserved
    reserved for future use

len
    length of payload (in bytes)

flags
    message flags

data
    \ ``len``\  bytes of message payload data

.. _`rpmsg_hdr.description`:

Description
-----------

Every message sent(/received) on the rpmsg bus begins with this header.

.. _`rpmsg_ns_msg`:

struct rpmsg_ns_msg
===================

.. c:type:: struct rpmsg_ns_msg

    dynamic name service announcement message

.. _`rpmsg_ns_msg.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_ns_msg {
        char name[RPMSG_NAME_SIZE];
        u32 addr;
        u32 flags;
    }

.. _`rpmsg_ns_msg.members`:

Members
-------

name
    name of remote service that is published

addr
    address of remote service that is published

flags
    indicates whether service is created or destroyed

.. _`rpmsg_ns_msg.description`:

Description
-----------

This message is sent across to publish a new service, or announce
about its removal. When we receive these messages, an appropriate
rpmsg channel (i.e device) is created/destroyed. In turn, the ->probe()
or ->remove() handler of the appropriate rpmsg driver will be invoked
(if/as-soon-as one is registered).

.. _`rpmsg_ns_flags`:

enum rpmsg_ns_flags
===================

.. c:type:: enum rpmsg_ns_flags

    dynamic name service announcement flags

.. _`rpmsg_ns_flags.definition`:

Definition
----------

.. code-block:: c

    enum rpmsg_ns_flags {
        RPMSG_NS_CREATE,
        RPMSG_NS_DESTROY
    };

.. _`rpmsg_ns_flags.constants`:

Constants
---------

RPMSG_NS_CREATE
    a new remote service was just created

RPMSG_NS_DESTROY
    a known remote service was just destroyed

.. _`rpmsg_sg_init`:

rpmsg_sg_init
=============

.. c:function:: void rpmsg_sg_init(struct scatterlist *sg, void *cpu_addr, unsigned int len)

    initialize scatterlist according to cpu address location

    :param struct scatterlist \*sg:
        scatterlist to fill

    :param void \*cpu_addr:
        virtual address of the buffer

    :param unsigned int len:
        buffer length

.. _`rpmsg_sg_init.description`:

Description
-----------

An internal function filling scatterlist according to virtual address
location (in vmalloc or in kernel).

.. _`__ept_release`:

\__ept_release
==============

.. c:function:: void __ept_release(struct kref *kref)

    deallocate an rpmsg endpoint

    :param struct kref \*kref:
        the ept's reference count

.. _`__ept_release.description`:

Description
-----------

This function deallocates an ept, and is invoked when its \ ``kref``\  refcount
drops to zero.

Never invoke this function directly!

.. _`__rpmsg_destroy_ept`:

\__rpmsg_destroy_ept
====================

.. c:function:: void __rpmsg_destroy_ept(struct virtproc_info *vrp, struct rpmsg_endpoint *ept)

    destroy an existing rpmsg endpoint

    :param struct virtproc_info \*vrp:
        virtproc which owns this ept

    :param struct rpmsg_endpoint \*ept:
        endpoing to destroy

.. _`__rpmsg_destroy_ept.description`:

Description
-----------

An internal function which destroy an ept without assuming it is
bound to an rpmsg channel. This is needed for handling the internal
name service endpoint, which isn't bound to an rpmsg channel.
See also \__rpmsg_create_ept().

.. _`rpmsg_upref_sleepers`:

rpmsg_upref_sleepers
====================

.. c:function:: void rpmsg_upref_sleepers(struct virtproc_info *vrp)

    enable "tx-complete" interrupts, if needed

    :param struct virtproc_info \*vrp:
        virtual remote processor state

.. _`rpmsg_upref_sleepers.description`:

Description
-----------

This function is called before a sender is blocked, waiting for
a tx buffer to become available.

If we already have blocking senders, this function merely increases
the "sleepers" reference count, and exits.

Otherwise, if this is the first sender to block, we also enable
virtio's tx callbacks, so we'd be immediately notified when a tx
buffer is consumed (we rely on virtio's tx callback in order
to wake up sleeping senders as soon as a tx buffer is used by the
remote processor).

.. _`rpmsg_downref_sleepers`:

rpmsg_downref_sleepers
======================

.. c:function:: void rpmsg_downref_sleepers(struct virtproc_info *vrp)

    disable "tx-complete" interrupts, if needed

    :param struct virtproc_info \*vrp:
        virtual remote processor state

.. _`rpmsg_downref_sleepers.description`:

Description
-----------

This function is called after a sender, that waited for a tx buffer
to become available, is unblocked.

If we still have blocking senders, this function merely decreases
the "sleepers" reference count, and exits.

Otherwise, if there are no more blocking senders, we also disable
virtio's tx callbacks, to avoid the overhead incurred with handling
those (now redundant) interrupts.

.. _`rpmsg_send_offchannel_raw`:

rpmsg_send_offchannel_raw
=========================

.. c:function:: int rpmsg_send_offchannel_raw(struct rpmsg_device *rpdev, u32 src, u32 dst, void *data, int len, bool wait)

    send a message across to the remote processor

    :param struct rpmsg_device \*rpdev:
        the rpmsg channel

    :param u32 src:
        source address

    :param u32 dst:
        destination address

    :param void \*data:
        payload of message

    :param int len:
        length of payload

    :param bool wait:
        indicates whether caller should block in case no TX buffers available

.. _`rpmsg_send_offchannel_raw.description`:

Description
-----------

This function is the base implementation for all of the rpmsg sending API.

It will send \ ``data``\  of length \ ``len``\  to \ ``dst``\ , and say it's from \ ``src``\ . The
message will be sent to the remote processor which the \ ``rpdev``\  channel
belongs to.

The message is sent using one of the TX buffers that are available for
communication with this remote processor.

If \ ``wait``\  is true, the caller will be blocked until either a TX buffer is
available, or 15 seconds elapses (we don't want callers to
sleep indefinitely due to misbehaving remote processors), and in that
case -ERESTARTSYS is returned. The number '15' itself was picked
arbitrarily; there's little point in asking drivers to provide a timeout
value themselves.

Otherwise, if \ ``wait``\  is false, and there are no TX buffers available,
the function will immediately fail, and -ENOMEM will be returned.

Normally drivers shouldn't use this function directly; instead, drivers
should use the appropriate rpmsg_{try}send{to, \_offchannel} API
(see include/linux/rpmsg.h).

Returns 0 on success and an appropriate error value on failure.

.. This file was automatic generated / don't edit.

