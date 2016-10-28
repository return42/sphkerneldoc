.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/whcd.h

.. _`whc_std`:

struct whc_std
==============

.. c:type:: struct whc_std

    a software TD.

.. _`whc_std.definition`:

Definition
----------

.. code-block:: c

    struct whc_std {
        struct urb *urb;
        size_t len;
        int ntds_remaining;
        struct whc_qtd *qtd;
        struct list_head list_node;
        int num_pointers;
        dma_addr_t dma_addr;
        struct whc_page_list_entry *pl_virt;
        void *bounce_buf;
        struct scatterlist *bounce_sg;
        unsigned bounce_offset;
    }

.. _`whc_std.members`:

Members
-------

urb
    the URB this sTD is for.

len
    the length of data in the associated TD.

ntds_remaining
    number of TDs (starting from this one) in this transfer.

qtd
    *undescribed*

list_node
    *undescribed*

num_pointers
    *undescribed*

dma_addr
    *undescribed*

pl_virt
    *undescribed*

bounce_buf
    a bounce buffer if the std was from an urb with a sg
    list that could not be mapped to qTDs directly.

bounce_sg
    the first scatterlist element bounce_buf is for.

bounce_offset
    the offset into bounce_sg for the start of bounce_buf.

.. _`whc_std.description`:

Description
-----------

Queued URBs may require more TDs than are available in a qset so we
use a list of these "software TDs" (sTDs) to hold per-TD data.

.. _`whc_urb`:

struct whc_urb
==============

.. c:type:: struct whc_urb

    per URB host controller structure.

.. _`whc_urb.definition`:

Definition
----------

.. code-block:: c

    struct whc_urb {
        struct urb *urb;
        struct whc_qset *qset;
        struct work_struct dequeue_work;
        bool is_async;
        int status;
    }

.. _`whc_urb.members`:

Members
-------

urb
    the URB this struct is for.

qset
    the qset associated to the URB.

dequeue_work
    the work to remove the URB when dequeued.

is_async
    the URB belongs to async sheduler or not.

status
    the status to be returned when calling wusbhc_giveback_urb.

.. _`whc_std_last`:

whc_std_last
============

.. c:function:: bool whc_std_last(struct whc_std *std)

    is this sTD the URB's last?

    :param struct whc_std \*std:
        the sTD to check.

.. This file was automatic generated / don't edit.

