.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/virt-dma.h

.. _`vchan_tx_prep`:

vchan_tx_prep
=============

.. c:function:: struct dma_async_tx_descriptor *vchan_tx_prep(struct virt_dma_chan *vc, struct virt_dma_desc *vd, unsigned long tx_flags)

    prepare a descriptor

    :param struct virt_dma_chan \*vc:
        virtual channel allocating this descriptor

    :param struct virt_dma_desc \*vd:
        virtual descriptor to prepare

    :param unsigned long tx_flags:
        flags argument passed in to prepare function

.. _`vchan_issue_pending`:

vchan_issue_pending
===================

.. c:function:: bool vchan_issue_pending(struct virt_dma_chan *vc)

    move submitted descriptors to issued list

    :param struct virt_dma_chan \*vc:
        virtual channel to update

.. _`vchan_issue_pending.description`:

Description
-----------

vc.lock must be held by caller

.. _`vchan_cookie_complete`:

vchan_cookie_complete
=====================

.. c:function:: void vchan_cookie_complete(struct virt_dma_desc *vd)

    report completion of a descriptor

    :param struct virt_dma_desc \*vd:
        virtual descriptor to update

.. _`vchan_cookie_complete.description`:

Description
-----------

vc.lock must be held by caller

.. _`vchan_cyclic_callback`:

vchan_cyclic_callback
=====================

.. c:function:: void vchan_cyclic_callback(struct virt_dma_desc *vd)

    report the completion of a period

    :param struct virt_dma_desc \*vd:
        virtual descriptor

.. _`vchan_next_desc`:

vchan_next_desc
===============

.. c:function:: struct virt_dma_desc *vchan_next_desc(struct virt_dma_chan *vc)

    peek at the next descriptor to be processed

    :param struct virt_dma_chan \*vc:
        virtual channel to obtain descriptor from

.. _`vchan_next_desc.description`:

Description
-----------

vc.lock must be held by caller

.. _`vchan_get_all_descriptors`:

vchan_get_all_descriptors
=========================

.. c:function:: void vchan_get_all_descriptors(struct virt_dma_chan *vc, struct list_head *head)

    obtain all submitted and issued descriptors

    :param struct virt_dma_chan \*vc:
        virtual channel to get descriptors from

    :param struct list_head \*head:
        list of descriptors found

.. _`vchan_get_all_descriptors.description`:

Description
-----------

vc.lock must be held by caller

Removes all submitted and issued descriptors from internal lists, and
provides a list of all descriptors found

.. _`vchan_synchronize`:

vchan_synchronize
=================

.. c:function:: void vchan_synchronize(struct virt_dma_chan *vc)

    synchronize callback execution to the current context

    :param struct virt_dma_chan \*vc:
        virtual channel to synchronize

.. _`vchan_synchronize.description`:

Description
-----------

Makes sure that all scheduled or active callbacks have finished running. For
proper operation the caller has to ensure that no new callbacks are scheduled
after the invocation of this function started.

.. This file was automatic generated / don't edit.
