.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_rma.c

.. _`scif_rma_ep_init`:

scif_rma_ep_init
================

.. c:function:: void scif_rma_ep_init(struct scif_endpt *ep)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

.. _`scif_rma_ep_init.description`:

Description
-----------

Initialize RMA per EP data structures.

.. _`scif_rma_ep_can_uninit`:

scif_rma_ep_can_uninit
======================

.. c:function:: int scif_rma_ep_can_uninit(struct scif_endpt *ep)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

.. _`scif_rma_ep_can_uninit.description`:

Description
-----------

Returns 1 if an endpoint can be uninitialized and 0 otherwise.

.. _`scif_create_pinned_pages`:

scif_create_pinned_pages
========================

.. c:function:: struct scif_pinned_pages *scif_create_pinned_pages(int nr_pages, int prot)

    :param nr_pages:
        number of pages in window
    :type nr_pages: int

    :param prot:
        read/write protection
    :type prot: int

.. _`scif_create_pinned_pages.description`:

Description
-----------

Allocate and prepare a set of pinned pages.

.. _`scif_destroy_pinned_pages`:

scif_destroy_pinned_pages
=========================

.. c:function:: int scif_destroy_pinned_pages(struct scif_pinned_pages *pin)

    :param pin:
        A set of pinned pages.
    :type pin: struct scif_pinned_pages \*

.. _`scif_destroy_pinned_pages.description`:

Description
-----------

Deallocate resources for pinned pages.

.. _`scif_destroy_incomplete_window`:

scif_destroy_incomplete_window
==============================

.. c:function:: void scif_destroy_incomplete_window(struct scif_endpt *ep, struct scif_window *window)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

    :param window:
        registration window
    :type window: struct scif_window \*

.. _`scif_destroy_incomplete_window.description`:

Description
-----------

Deallocate resources for self window.

.. _`scif_unmap_window`:

scif_unmap_window
=================

.. c:function:: void scif_unmap_window(struct scif_dev *remote_dev, struct scif_window *window)

    :param remote_dev:
        SCIF remote device
    :type remote_dev: struct scif_dev \*

    :param window:
        registration window
    :type window: struct scif_window \*

.. _`scif_unmap_window.description`:

Description
-----------

Delete any DMA mappings created for a registered self window

.. _`scif_destroy_window`:

scif_destroy_window
===================

.. c:function:: int scif_destroy_window(struct scif_endpt *ep, struct scif_window *window)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

    :param window:
        registration window
    :type window: struct scif_window \*

.. _`scif_destroy_window.description`:

Description
-----------

Deallocate resources for self window.

.. _`scif_create_remote_lookup`:

scif_create_remote_lookup
=========================

.. c:function:: int scif_create_remote_lookup(struct scif_dev *remote_dev, struct scif_window *window)

    :param remote_dev:
        SCIF remote device
    :type remote_dev: struct scif_dev \*

    :param window:
        remote window
    :type window: struct scif_window \*

.. _`scif_create_remote_lookup.description`:

Description
-----------

Allocate and prepare lookup entries for the remote
end to copy over the physical addresses.
Returns 0 on success and appropriate errno on failure.

.. _`scif_destroy_remote_lookup`:

scif_destroy_remote_lookup
==========================

.. c:function:: void scif_destroy_remote_lookup(struct scif_dev *remote_dev, struct scif_window *window)

    :param remote_dev:
        SCIF remote device
    :type remote_dev: struct scif_dev \*

    :param window:
        remote window
    :type window: struct scif_window \*

.. _`scif_destroy_remote_lookup.description`:

Description
-----------

Destroy lookup entries used for the remote
end to copy over the physical addresses.

.. _`scif_create_remote_window`:

scif_create_remote_window
=========================

.. c:function:: struct scif_window *scif_create_remote_window(struct scif_dev *scifdev, int nr_pages)

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param nr_pages:
        number of pages in window
    :type nr_pages: int

.. _`scif_create_remote_window.description`:

Description
-----------

Allocate and prepare a remote registration window.

.. _`scif_destroy_remote_window`:

scif_destroy_remote_window
==========================

.. c:function:: void scif_destroy_remote_window(struct scif_window *window)

    :param window:
        remote registration window
    :type window: struct scif_window \*

.. _`scif_destroy_remote_window.description`:

Description
-----------

Deallocate resources for remote window.

.. _`scif_iommu_map`:

scif_iommu_map
==============

.. c:function:: int scif_iommu_map(struct scif_dev *remote_dev, struct scif_window *window)

    create DMA mappings if the IOMMU is enabled

    :param remote_dev:
        SCIF remote device
    :type remote_dev: struct scif_dev \*

    :param window:
        remote registration window
    :type window: struct scif_window \*

.. _`scif_iommu_map.description`:

Description
-----------

Map the physical pages using dma_map_sg(..) and then detect the number
of contiguous DMA mappings allocated

.. _`scif_map_window`:

scif_map_window
===============

.. c:function:: int scif_map_window(struct scif_dev *remote_dev, struct scif_window *window)

    :param remote_dev:
        SCIF remote device
    :type remote_dev: struct scif_dev \*

    :param window:
        self registration window
    :type window: struct scif_window \*

.. _`scif_map_window.description`:

Description
-----------

Map pages of a window into the aperture/PCI.
Also determine addresses required for DMA.

.. _`scif_send_scif_unregister`:

scif_send_scif_unregister
=========================

.. c:function:: int scif_send_scif_unregister(struct scif_endpt *ep, struct scif_window *window)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

    :param window:
        self registration window
    :type window: struct scif_window \*

.. _`scif_send_scif_unregister.description`:

Description
-----------

Send a SCIF_UNREGISTER message.

.. _`scif_unregister_window`:

scif_unregister_window
======================

.. c:function:: int scif_unregister_window(struct scif_window *window)

    :param window:
        self registration window
    :type window: struct scif_window \*

.. _`scif_unregister_window.description`:

Description
-----------

Send an unregistration request and wait for a response.

.. _`scif_send_alloc_request`:

scif_send_alloc_request
=======================

.. c:function:: int scif_send_alloc_request(struct scif_endpt *ep, struct scif_window *window)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

    :param window:
        self registration window
    :type window: struct scif_window \*

.. _`scif_send_alloc_request.description`:

Description
-----------

Send a remote window allocation request

.. _`scif_prep_remote_window`:

scif_prep_remote_window
=======================

.. c:function:: int scif_prep_remote_window(struct scif_endpt *ep, struct scif_window *window)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

    :param window:
        self registration window
    :type window: struct scif_window \*

.. _`scif_prep_remote_window.description`:

Description
-----------

Send a remote window allocation request, wait for an allocation response,
and prepares the remote window by copying over the page lists

.. _`scif_send_scif_register`:

scif_send_scif_register
=======================

.. c:function:: int scif_send_scif_register(struct scif_endpt *ep, struct scif_window *window)

    :param ep:
        end point
    :type ep: struct scif_endpt \*

    :param window:
        self registration window
    :type window: struct scif_window \*

.. _`scif_send_scif_register.description`:

Description
-----------

Send a SCIF_REGISTER message if EP is connected and wait for a
SCIF_REGISTER_(N)ACK message else send a SCIF_FREE_VIRT
message so that the peer can free its remote window allocated earlier.

.. _`scif_get_window_offset`:

scif_get_window_offset
======================

.. c:function:: int scif_get_window_offset(struct scif_endpt *ep, int flags, s64 offset, int num_pages, s64 *out_offset)

    :param ep:
        end point descriptor
    :type ep: struct scif_endpt \*

    :param flags:
        flags
    :type flags: int

    :param offset:
        offset hint
    :type offset: s64

    :param num_pages:
        number of pages
    :type num_pages: int

    :param out_offset:
        computed offset returned by reference.
    :type out_offset: s64 \*

.. _`scif_get_window_offset.description`:

Description
-----------

Compute/Claim a new offset for this EP.

.. _`scif_free_window_offset`:

scif_free_window_offset
=======================

.. c:function:: void scif_free_window_offset(struct scif_endpt *ep, struct scif_window *window, s64 offset)

    :param ep:
        end point descriptor
    :type ep: struct scif_endpt \*

    :param window:
        registration window
    :type window: struct scif_window \*

    :param offset:
        Offset to be freed
    :type offset: s64

.. _`scif_free_window_offset.description`:

Description
-----------

Free offset for this EP. The callee is supposed to grab
the RMA mutex before calling this API.

.. _`scif_alloc_req`:

scif_alloc_req
==============

.. c:function:: void scif_alloc_req(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_ALLOC_REQ interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_alloc_req.description`:

Description
-----------

Remote side is requesting a memory allocation.

.. _`scif_alloc_gnt_rej`:

scif_alloc_gnt_rej
==================

.. c:function:: void scif_alloc_gnt_rej(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_ALLOC_GNT/REJ interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_alloc_gnt_rej.description`:

Description
-----------

Remote side responded to a memory allocation.

.. _`scif_free_virt`:

scif_free_virt
==============

.. c:function:: void scif_free_virt(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_FREE_VIRT interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_free_virt.description`:

Description
-----------

Free up memory kmalloc'd earlier.

.. _`scif_recv_reg`:

scif_recv_reg
=============

.. c:function:: void scif_recv_reg(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_REGISTER interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_reg.description`:

Description
-----------

Update remote window list with a new registered window.

.. _`scif_recv_unreg`:

scif_recv_unreg
===============

.. c:function:: void scif_recv_unreg(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_UNREGISTER interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_unreg.description`:

Description
-----------

Remove window from remote registration list;

.. _`scif_recv_reg_ack`:

scif_recv_reg_ack
=================

.. c:function:: void scif_recv_reg_ack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_REGISTER_ACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_reg_ack.description`:

Description
-----------

Wake up the window waiting to complete registration.

.. _`scif_recv_reg_nack`:

scif_recv_reg_nack
==================

.. c:function:: void scif_recv_reg_nack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_REGISTER_NACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_reg_nack.description`:

Description
-----------

Wake up the window waiting to inform it that registration
cannot be completed.

.. _`scif_recv_unreg_ack`:

scif_recv_unreg_ack
===================

.. c:function:: void scif_recv_unreg_ack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_UNREGISTER_ACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_unreg_ack.description`:

Description
-----------

Wake up the window waiting to complete unregistration.

.. _`scif_recv_unreg_nack`:

scif_recv_unreg_nack
====================

.. c:function:: void scif_recv_unreg_nack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_UNREGISTER_NACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_unreg_nack.description`:

Description
-----------

Wake up the window waiting to inform it that unregistration
cannot be completed immediately.

.. This file was automatic generated / don't edit.

