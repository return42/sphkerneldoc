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

    :param client:
        client instance
    :type client: struct p9_client \*

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

    :param vq:
        virtio queue activity was received on
    :type vq: struct virtqueue \*

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

    :param sg:
        scatter/gather list to pack into
    :type sg: struct scatterlist \*

    :param start:
        which segment of the sg_list to start at
    :type start: int

    :param limit:
        maximum segment to pack data to
    :type limit: int

    :param data:
        data to pack into scatter/gather list
    :type data: char \*

    :param count:
        amount of data to pack into the scatter/gather list
    :type count: int

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

    :param sg:
        scatter/gather list to pack into
    :type sg: struct scatterlist \*

    :param start:
        which segment of the sg_list to start at
    :type start: int

    :param limit:
        *undescribed*
    :type limit: int

    :param pdata:
        a list of pages to add into sg.
    :type pdata: struct page \*\*

    :param nr_pages:
        number of pages to pack into the scatter/gather list
    :type nr_pages: int

    :param offs:
        amount of data in the beginning of first page \_not\_ to pack
    :type offs: size_t

    :param count:
        amount of data to pack into the scatter/gather list
    :type count: int

.. _`p9_virtio_request`:

p9_virtio_request
=================

.. c:function:: int p9_virtio_request(struct p9_client *client, struct p9_req_t *req)

    issue a request

    :param client:
        client instance issuing the request
    :type client: struct p9_client \*

    :param req:
        request to be issued
    :type req: struct p9_req_t \*

.. _`p9_virtio_zc_request`:

p9_virtio_zc_request
====================

.. c:function:: int p9_virtio_zc_request(struct p9_client *client, struct p9_req_t *req, struct iov_iter *uidata, struct iov_iter *uodata, int inlen, int outlen, int in_hdr_len)

    issue a zero copy request

    :param client:
        client instance issuing the request
    :type client: struct p9_client \*

    :param req:
        request to be issued
    :type req: struct p9_req_t \*

    :param uidata:
        user buffer that should be used for zero copy read
    :type uidata: struct iov_iter \*

    :param uodata:
        user buffer that should be used for zero copy write
    :type uodata: struct iov_iter \*

    :param inlen:
        read buffer size
    :type inlen: int

    :param outlen:
        write buffer size
    :type outlen: int

    :param in_hdr_len:
        reader header size, This is the size of response protocol data
    :type in_hdr_len: int

.. _`p9_virtio_probe`:

p9_virtio_probe
===============

.. c:function:: int p9_virtio_probe(struct virtio_device *vdev)

    probe for existence of 9P virtio channels

    :param vdev:
        virtio device to probe
    :type vdev: struct virtio_device \*

.. _`p9_virtio_probe.description`:

Description
-----------

This probes for existing virtio channels.

.. _`p9_virtio_create`:

p9_virtio_create
================

.. c:function:: int p9_virtio_create(struct p9_client *client, const char *devname, char *args)

    allocate a new virtio channel

    :param client:
        client instance invoking this transport
    :type client: struct p9_client \*

    :param devname:
        string identifying the channel to connect to (unused)
    :type devname: const char \*

    :param args:
        args passed from \ :c:func:`sys_mount`\  for per-transport options (unused)
    :type args: char \*

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

    :param vdev:
        virtio device to remove
    :type vdev: struct virtio_device \*

.. This file was automatic generated / don't edit.

