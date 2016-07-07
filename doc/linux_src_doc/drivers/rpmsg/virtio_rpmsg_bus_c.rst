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
        struct virtqueue *rvq;
        struct virtqueue * *svq;
        void *rbufs;
        void * *sbufs;
        unsigned int num_bufs;
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

.. _`rpmsg_channel_info`:

struct rpmsg_channel_info
=========================

.. c:type:: struct rpmsg_channel_info

    internal channel info representation

.. _`rpmsg_channel_info.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_channel_info {
        char name[RPMSG_NAME_SIZE];
        u32 src;
        u32 dst;
    }

.. _`rpmsg_channel_info.members`:

Members
-------

name
    name of service

src
    local address

dst
    destination address

.. _`__ept_release`:

__ept_release
=============

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

.. _`rpmsg_create_ept`:

rpmsg_create_ept
================

.. c:function:: struct rpmsg_endpoint *rpmsg_create_ept(struct rpmsg_channel *rpdev, rpmsg_rx_cb_t cb, void *priv, u32 addr)

    create a new rpmsg_endpoint

    :param struct rpmsg_channel \*rpdev:
        rpmsg channel device

    :param rpmsg_rx_cb_t cb:
        rx callback handler

    :param void \*priv:
        private data for the driver's use

    :param u32 addr:
        local rpmsg address to bind with \ ``cb``\ 

.. _`rpmsg_create_ept.description`:

Description
-----------

Every rpmsg address in the system is bound to an rx callback (so when
inbound messages arrive, they are dispatched by the rpmsg bus using the
appropriate callback handler) by means of an rpmsg_endpoint struct.

This function allows drivers to create such an endpoint, and by that,
bind a callback, and possibly some private data too, to an rpmsg address
(either one that is known in advance, or one that will be dynamically
assigned for them).

Simple rpmsg drivers need not call rpmsg_create_ept, because an endpoint
is already created for them when they are probed by the rpmsg bus
(using the rx callback provided when they registered to the rpmsg bus).

.. _`rpmsg_create_ept.so-things-should-just-work-for-simple-drivers`:

So things should just work for simple drivers
---------------------------------------------

they already have an
endpoint, their rx callback is bound to their rpmsg address, and when
relevant inbound messages arrive (i.e. messages which their dst address
equals to the src address of their rpmsg channel), the driver's handler
is invoked to process it.

That said, more complicated drivers might do need to allocate
additional rpmsg addresses, and bind them to different rx callbacks.
To accomplish that, those drivers need to call this function.

Drivers should provide their \ ``rpdev``\  channel (so the new endpoint would belong
to the same remote processor their channel belongs to), an rx callback
function, an optional private data (which is provided back when the
rx callback is invoked), and an address they want to bind with the
callback. If \ ``addr``\  is RPMSG_ADDR_ANY, then rpmsg_create_ept will
dynamically assign them an available rpmsg address (drivers should have
a very good reason why not to always use RPMSG_ADDR_ANY here).

Returns a pointer to the endpoint on success, or NULL on error.

.. _`__rpmsg_destroy_ept`:

__rpmsg_destroy_ept
===================

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
See also \\ :c:func:`__rpmsg_create_ept`\ .

.. _`rpmsg_destroy_ept`:

rpmsg_destroy_ept
=================

.. c:function:: void rpmsg_destroy_ept(struct rpmsg_endpoint *ept)

    destroy an existing rpmsg endpoint

    :param struct rpmsg_endpoint \*ept:
        endpoing to destroy

.. _`rpmsg_destroy_ept.description`:

Description
-----------

Should be used by drivers to destroy an rpmsg endpoint previously
created with \ :c:func:`rpmsg_create_ept`\ .

.. _`__register_rpmsg_driver`:

__register_rpmsg_driver
=======================

.. c:function:: int __register_rpmsg_driver(struct rpmsg_driver *rpdrv, struct module *owner)

    register an rpmsg driver with the rpmsg bus

    :param struct rpmsg_driver \*rpdrv:
        pointer to a struct rpmsg_driver

    :param struct module \*owner:
        owning module/driver

.. _`__register_rpmsg_driver.description`:

Description
-----------

Returns 0 on success, and an appropriate error value on failure.

.. _`unregister_rpmsg_driver`:

unregister_rpmsg_driver
=======================

.. c:function:: void unregister_rpmsg_driver(struct rpmsg_driver *rpdrv)

    unregister an rpmsg driver from the rpmsg bus

    :param struct rpmsg_driver \*rpdrv:
        pointer to a struct rpmsg_driver

.. _`unregister_rpmsg_driver.description`:

Description
-----------

Returns 0 on success, and an appropriate error value on failure.

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

.. c:function:: int rpmsg_send_offchannel_raw(struct rpmsg_channel *rpdev, u32 src, u32 dst, void *data, int len, bool wait)

    send a message across to the remote processor

    :param struct rpmsg_channel \*rpdev:
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

