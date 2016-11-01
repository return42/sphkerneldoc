.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_receiver.c

.. _`drbd_alloc_pages`:

drbd_alloc_pages
================

.. c:function:: struct page *drbd_alloc_pages(struct drbd_peer_device *peer_device, unsigned int number, bool retry)

    Returns \ ``number``\  pages, retries forever (or until signalled)

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

    :param unsigned int number:
        number of pages requested

    :param bool retry:
        whether to retry, if not enough pages are available right now

.. _`drbd_alloc_pages.description`:

Description
-----------

Tries to allocate number pages, first from our own page pool, then from
the kernel.
Possibly retry until DRBD frees sufficient pages somewhere else.

If this allocation would exceed the max_buffers setting, we throttle
allocation (schedule_timeout) to give the system some room to breathe.

We do not use max-buffers as hard limit, because it could lead to
congestion and further to a distributed deadlock during online-verify or
(checksum based) resync, if the max-buffers, socket buffer sizes and
resync-rate settings are mis-configured.

Returns a page chain linked via page->private.

.. _`drbd_socket_okay`:

drbd_socket_okay
================

.. c:function:: bool drbd_socket_okay(struct socket **sock)

    Free the socket if its connection is not okay

    :param struct socket \*\*sock:
        pointer to the pointer to the socket.

.. _`drbd_may_finish_epoch`:

drbd_may_finish_epoch
=====================

.. c:function:: enum finish_epoch drbd_may_finish_epoch(struct drbd_connection *connection, struct drbd_epoch *epoch, enum epoch_event ev)

    Applies an epoch_event to the epoch's state, eventually finishes it.

    :param struct drbd_connection \*connection:
        *undescribed*

    :param struct drbd_epoch \*epoch:
        Epoch object.

    :param enum epoch_event ev:
        Epoch event.

.. _`drbd_bump_write_ordering`:

drbd_bump_write_ordering
========================

.. c:function:: void drbd_bump_write_ordering(struct drbd_resource *resource, struct drbd_backing_dev *bdev, enum write_ordering_e wo)

    Fall back to an other write ordering method

    :param struct drbd_resource \*resource:
        *undescribed*

    :param struct drbd_backing_dev \*bdev:
        *undescribed*

    :param enum write_ordering_e wo:
        Write ordering method to try.

.. _`drbd_submit_peer_request`:

drbd_submit_peer_request
========================

.. c:function:: int drbd_submit_peer_request(struct drbd_device *device, struct drbd_peer_request *peer_req, const unsigned op, const unsigned op_flags, const int fault_type)

    :param struct drbd_device \*device:
        DRBD device.

    :param struct drbd_peer_request \*peer_req:
        peer request

    :param const unsigned op:
        *undescribed*

    :param const unsigned op_flags:
        *undescribed*

    :param const int fault_type:
        *undescribed*

.. _`drbd_submit_peer_request.description`:

Description
-----------

May spread the pages to multiple bios,
depending on bio_add_page restrictions.

Returns 0 if all bios have been submitted,
-ENOMEM if we could not allocate enough bios,
-ENOSPC (any better suggestion?) if we have not been able to bio_add_page a
single page to an empty bio (which should never happen and likely indicates
that the lower level IO stack is in some way broken). This has been observed
on certain Xen deployments.

.. _`drbd_asb_recover_0p`:

drbd_asb_recover_0p
===================

.. c:function:: int drbd_asb_recover_0p(struct drbd_peer_device *peer_device)

    Recover after split-brain with no remaining primaries

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

.. _`drbd_asb_recover_1p`:

drbd_asb_recover_1p
===================

.. c:function:: int drbd_asb_recover_1p(struct drbd_peer_device *peer_device)

    Recover after split-brain with one remaining primary

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

.. _`drbd_asb_recover_2p`:

drbd_asb_recover_2p
===================

.. c:function:: int drbd_asb_recover_2p(struct drbd_peer_device *peer_device)

    Recover after split-brain with two remaining primaries

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

.. _`convert_state`:

convert_state
=============

.. c:function:: union drbd_state convert_state(union drbd_state ps)

    Converts the peer's view of the cluster state to our point of view

    :param union drbd_state ps:
        The state as seen by the peer.

.. _`receive_bitmap_plain`:

receive_bitmap_plain
====================

.. c:function:: int receive_bitmap_plain(struct drbd_peer_device *peer_device, unsigned int size, unsigned long *p, struct bm_xfer_ctx *c)

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

    :param unsigned int size:
        *undescribed*

    :param unsigned long \*p:
        *undescribed*

    :param struct bm_xfer_ctx \*c:
        *undescribed*

.. _`receive_bitmap_plain.description`:

Description
-----------

Return 0 when done, 1 when another iteration is needed, and a negative error
code upon failure.

.. _`recv_bm_rle_bits`:

recv_bm_rle_bits
================

.. c:function:: int recv_bm_rle_bits(struct drbd_peer_device *peer_device, struct p_compressed_bm *p, struct bm_xfer_ctx *c, unsigned int len)

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

    :param struct p_compressed_bm \*p:
        *undescribed*

    :param struct bm_xfer_ctx \*c:
        *undescribed*

    :param unsigned int len:
        *undescribed*

.. _`recv_bm_rle_bits.description`:

Description
-----------

Return 0 when done, 1 when another iteration is needed, and a negative error
code upon failure.

.. _`decode_bitmap_c`:

decode_bitmap_c
===============

.. c:function:: int decode_bitmap_c(struct drbd_peer_device *peer_device, struct p_compressed_bm *p, struct bm_xfer_ctx *c, unsigned int len)

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

    :param struct p_compressed_bm \*p:
        *undescribed*

    :param struct bm_xfer_ctx \*c:
        *undescribed*

    :param unsigned int len:
        *undescribed*

.. _`decode_bitmap_c.description`:

Description
-----------

Return 0 when done, 1 when another iteration is needed, and a negative error
code upon failure.

.. This file was automatic generated / don't edit.

