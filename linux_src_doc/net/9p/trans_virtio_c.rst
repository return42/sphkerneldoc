.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/trans_virtio.c

.. _`virtio_chan`:

struct virtio_chan
==================

.. c:type:: struct virtio_chan

    per-instance transport information

.. _`virtio_chan.definition`:

Definition
----------

.. code-block:: c

    struct virtio_chan {
        bool inuse;
        spinlock_t lock;
        struct p9_client *client;
        struct virtio_device *vdev;
        struct virtqueue *vq;
        int ring_bufs_avail;
        wait_queue_head_t *vc_wq;
        unsigned long p9_max_pages;
        struct scatterlist sg[VIRTQUEUE_NUM];
        int tag_len;
        char *tag;
        struct list_head chan_list;
    }

.. _`virtio_chan.members`:

Members
-------

inuse
    whether the channel is in use

lock
    protects multiple elements within this structure

client
    client instance

vdev
    virtio dev associated with this channel

vq
    virtio queue associated with this channel

ring_bufs_avail
    *undescribed*

vc_wq
    *undescribed*

p9_max_pages
    *undescribed*

sg
    scatter gather list which is used to pack a request (protected?)

tag_len
    *undescribed*

tag
    *undescribed*

chan_list
    *undescribed*

.. _`virtio_chan.description`:

Description
-----------

We keep all per-channel information in a structure.
This structure is allocated within the devices dev->mem space.
A pointer to the structure will get put in the transport private.

.. _`p9_virtio_close`:

p9_virtio_close
===============

.. c:function:: void p9_virtio_close(struct p9_client *client)

    reclaim resources of a channel

    :param struct p9_client \*client:
        client instance

.. _`p9_virtio_close.description`:

Description
-----------

This reclaims a channel by freeing its resources and
reseting its inuse flag.

.. _`req_done`:

req_done
========

.. c:function:: void req_done(struct virtqueue *vq)

    callback which signals activity from the server

    :param struct virtqueue \*vq:
        virtio queue activity was received on

.. _`req_done.description`:

Description
-----------

This notifies us that the server has triggered some activity
on the virtio channel - most likely a response to request we
sent.  Figure out which requests now have responses and wake up
those threads.

.. _`req_done.bugs`:

Bugs
----

could do with some additional sanity checking, but appears to work.

.. _`pack_sg_list`:

pack_sg_list
============

.. c:function:: int pack_sg_list(struct scatterlist *sg, int start, int limit, char *data, int count)

    pack a scatter gather list from a linear buffer

    :param struct scatterlist \*sg:
        scatter/gather list to pack into

    :param int start:
        which segment of the sg_list to start at

    :param int limit:
        maximum segment to pack data to

    :param char \*data:
        data to pack into scatter/gather list

    :param int count:
        amount of data to pack into the scatter/gather list

.. _`pack_sg_list.description`:

Description
-----------

sg_lists have multiple segments of various sizes.  This will pack
arbitrary data into an existing scatter gather list, segmenting the
data as necessary within constraints.

.. _`pack_sg_list_p`:

pack_sg_list_p
==============

.. c:function:: int pack_sg_list_p(struct scatterlist *sg, int start, int limit, struct page **pdata, int nr_pages, size_t offs, int count)

    Just like pack_sg_list. Instead of taking a buffer, this takes a list of pages.

    :param struct scatterlist \*sg:
        scatter/gather list to pack into

    :param int start:
        which segment of the sg_list to start at

    :param int limit:
        *undescribed*

    :param struct page \*\*pdata:
        a list of pages to add into sg.

    :param int nr_pages:
        number of pages to pack into the scatter/gather list

    :param size_t offs:
        amount of data in the beginning of first page \_not\_ to pack

    :param int count:
        amount of data to pack into the scatter/gather list

.. _`p9_virtio_request`:

p9_virtio_request
=================

.. c:function:: int p9_virtio_request(struct p9_client *client, struct p9_req_t *req)

    issue a request

    :param struct p9_client \*client:
        client instance issuing the request

    :param struct p9_req_t \*req:
        request to be issued

.. _`p9_virtio_zc_request`:

p9_virtio_zc_request
====================

.. c:function:: int p9_virtio_zc_request(struct p9_client *client, struct p9_req_t *req, struct iov_iter *uidata, struct iov_iter *uodata, int inlen, int outlen, int in_hdr_len)

    issue a zero copy request

    :param struct p9_client \*client:
        client instance issuing the request

    :param struct p9_req_t \*req:
        request to be issued

    :param struct iov_iter \*uidata:
        user bffer that should be ued for zero copy read

    :param struct iov_iter \*uodata:
        user buffer that shoud be user for zero copy write

    :param int inlen:
        read buffer size

    :param int outlen:
        write buffer size

    :param int in_hdr_len:
        reader header size, This is the size of response protocol data

.. _`p9_virtio_probe`:

p9_virtio_probe
===============

.. c:function:: int p9_virtio_probe(struct virtio_device *vdev)

    probe for existence of 9P virtio channels

    :param struct virtio_device \*vdev:
        virtio device to probe

.. _`p9_virtio_probe.description`:

Description
-----------

This probes for existing virtio channels.

.. _`p9_virtio_create`:

p9_virtio_create
================

.. c:function:: int p9_virtio_create(struct p9_client *client, const char *devname, char *args)

    allocate a new virtio channel

    :param struct p9_client \*client:
        client instance invoking this transport

    :param const char \*devname:
        string identifying the channel to connect to (unused)

    :param char \*args:
        args passed from \ :c:func:`sys_mount`\  for per-transport options (unused)

.. _`p9_virtio_create.description`:

Description
-----------

This sets up a transport channel for 9p communication.  Right now
we only match the first available channel, but eventually we couldlook up
alternate channels by matching devname versus a virtio_config entry.
We use a simple reference count mechanism to ensure that only a single
mount has a channel open at a time.

.. _`p9_virtio_remove`:

p9_virtio_remove
================

.. c:function:: void p9_virtio_remove(struct virtio_device *vdev)

    clean up resources associated with a virtio device

    :param struct virtio_device \*vdev:
        virtio device to remove

.. This file was automatic generated / don't edit.

