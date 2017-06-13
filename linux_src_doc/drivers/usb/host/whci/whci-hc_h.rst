.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/whci-hc.h

.. _`whci_page_size`:

WHCI_PAGE_SIZE
==============

.. c:function::  WHCI_PAGE_SIZE()

    page size use by WHCI

.. _`whci_page_size.description`:

Description
-----------

WHCI assumes that host system uses pages of 4096 octets.

.. _`qtd_max_xfer_size`:

QTD_MAX_XFER_SIZE
=================

.. c:function::  QTD_MAX_XFER_SIZE()

    max number of bytes to transfer with a single qtd.

.. _`qtd_max_xfer_size.description`:

Description
-----------

This is 2^20 - 1.

.. _`whc_qtd`:

struct whc_qtd
==============

.. c:type:: struct whc_qtd

    Queue Element Transfer Descriptors (qTD)

.. _`whc_qtd.definition`:

Definition
----------

.. code-block:: c

    struct whc_qtd {
        __le32 status;
        __le32 options;
        __le64 page_list_ptr;
        __u8 setup;
    }

.. _`whc_qtd.members`:

Members
-------

status
    *undescribed*

options
    *undescribed*

page_list_ptr
    *undescribed*

setup
    *undescribed*

.. _`whc_qtd.description`:

Description
-----------

This describes the data for a bulk, control or interrupt transfer.

[WHCI] section 3.2.4

.. _`whc_itd`:

struct whc_itd
==============

.. c:type:: struct whc_itd

    Isochronous Queue Element Transfer Descriptors (iTD)

.. _`whc_itd.definition`:

Definition
----------

.. code-block:: c

    struct whc_itd {
        __le16 presentation_time;
        __u8 num_segments;
        __u8 status;
        __le32 options;
        __le64 page_list_ptr;
        __le64 seg_list_ptr;
    }

.. _`whc_itd.members`:

Members
-------

presentation_time
    *undescribed*

num_segments
    *undescribed*

status
    *undescribed*

options
    *undescribed*

page_list_ptr
    *undescribed*

seg_list_ptr
    *undescribed*

.. _`whc_itd.description`:

Description
-----------

This describes the data and other parameters for an isochronous
transfer.

[WHCI] section 3.2.5

.. _`whc_seg_list_entry`:

struct whc_seg_list_entry
=========================

.. c:type:: struct whc_seg_list_entry

    Segment list entry.

.. _`whc_seg_list_entry.definition`:

Definition
----------

.. code-block:: c

    struct whc_seg_list_entry {
        __le16 len;
        __u8 idx;
        __u8 status;
        __le16 offset;
    }

.. _`whc_seg_list_entry.members`:

Members
-------

len
    *undescribed*

idx
    *undescribed*

status
    *undescribed*

offset
    *undescribed*

.. _`whc_seg_list_entry.description`:

Description
-----------

Describes a portion of the data buffer described in the containing
qTD's page list.

seg_ptr = qtd->page_list_ptr[qtd->seg_list_ptr[seg].idx].buf_ptr
+ qtd->seg_list_ptr[seg].offset;

Segments can't cross page boundries.

[WHCI] section 3.2.5.5

.. _`whc_qhead`:

struct whc_qhead
================

.. c:type:: struct whc_qhead

    endpoint and status information for a qset.

.. _`whc_qhead.definition`:

Definition
----------

.. code-block:: c

    struct whc_qhead {
        __le64 link;
        __le32 info1;
        __le32 info2;
        __le32 info3;
        __le16 status;
        __le16 err_count;
        __le32 cur_window;
        __le32 scratch;
        union overlay;
    }

.. _`whc_qhead.members`:

Members
-------

link
    *undescribed*

info1
    *undescribed*

info2
    *undescribed*

info3
    *undescribed*

status
    *undescribed*

err_count
    *undescribed*

cur_window
    *undescribed*

scratch
    *undescribed*

overlay
    *undescribed*

.. _`whc_qhead.description`:

Description
-----------

[WHCI] section 3.2.6

.. _`usb_pipe_to_qh_type`:

usb_pipe_to_qh_type
===================

.. c:function:: unsigned usb_pipe_to_qh_type(unsigned pipe)

    USB core pipe type to QH transfer type

    :param unsigned pipe:
        *undescribed*

.. _`usb_pipe_to_qh_type.description`:

Description
-----------

Returns the QH type field for a USB core pipe type.

.. _`whci_qset_td_max`:

WHCI_QSET_TD_MAX
================

.. c:function::  WHCI_QSET_TD_MAX()

.. _`whc_qset`:

struct whc_qset
===============

.. c:type:: struct whc_qset

    WUSB data transfers to a specific endpoint

.. _`whc_qset.definition`:

Definition
----------

.. code-block:: c

    struct whc_qset {
        struct whc_qhead qh;
        union {unnamed_union};
        dma_addr_t qset_dma;
        struct whc *whc;
        struct usb_host_endpoint *ep;
        struct list_head stds;
        int ntds;
        int td_start;
        int td_end;
        struct list_head list_node;
        unsigned in_sw_list:1;
        unsigned in_hw_list:1;
        unsigned remove:1;
        unsigned reset:1;
        struct urb *pause_after_urb;
        struct completion remove_complete;
        uint16_t max_packet;
        uint8_t max_burst;
        uint8_t max_seq;
    }

.. _`whc_qset.members`:

Members
-------

qh
    the QHead of this qset

{unnamed_union}
    anonymous


qset_dma
    DMA address for this qset

whc
    WHCI HC this qset is for

ep
    endpoint

stds
    list of sTDs queued to this qset

ntds
    number of qTDs queued (not necessarily the same as nTDs
    field in the QH)

td_start
    index of the first qTD in the list

td_end
    index of next free qTD in the list (provided
    ntds < WHCI_QSET_TD_MAX)

list_node
    *undescribed*

in_sw_list
    *undescribed*

in_hw_list
    *undescribed*

remove
    *undescribed*

reset
    *undescribed*

pause_after_urb
    *undescribed*

remove_complete
    *undescribed*

max_packet
    *undescribed*

max_burst
    *undescribed*

max_seq
    *undescribed*

.. _`whc_qset.description`:

Description
-----------

Queue Sets (qsets) are added to the asynchronous schedule list
(ASL) or the periodic zone list (PZL).

qsets may contain up to 8 TDs (either qTDs or iTDs as appropriate).
Each TD may refer to at most 1 MiB of data. If a single transfer
has > 8MiB of data, TDs can be reused as they are completed since
the TD list is used as a circular buffer.  Similarly, several
(smaller) transfers may be queued in a qset.

WHCI controllers may cache portions of the qsets in the ASL and
PZL, requiring the WHCD to inform the WHC that the lists have been
updated (fields changed or qsets inserted or removed).  For safe
insertion and removal of qsets from the lists the schedule must be
stopped to avoid races in updating the QH link pointers.

Since the HC is free to execute qsets in any order, all transfers
to an endpoint should use the same qset to ensure transfers are
executed in the order they're submitted.

[WHCI] section 3.2.3

.. _`di_buf_entry`:

struct di_buf_entry
===================

.. c:type:: struct di_buf_entry

    Device Information (DI) buffer entry.

.. _`di_buf_entry.definition`:

Definition
----------

.. code-block:: c

    struct di_buf_entry {
        __le32 availability_info;
        __le32 addr_sec_info;
        __le32 reserved;
    }

.. _`di_buf_entry.members`:

Members
-------

availability_info
    *undescribed*

addr_sec_info
    *undescribed*

reserved
    *undescribed*

.. _`di_buf_entry.description`:

Description
-----------

There's one of these per connected device.

.. _`dn_buf_entry`:

struct dn_buf_entry
===================

.. c:type:: struct dn_buf_entry

    Device Notification (DN) buffer entry.

.. _`dn_buf_entry.definition`:

Definition
----------

.. code-block:: c

    struct dn_buf_entry {
        __u8 msg_size;
        __u8 reserved1;
        __u8 src_addr;
        __u8 status;
        __le32 tkid;
        __u8 dn_data;
    }

.. _`dn_buf_entry.members`:

Members
-------

msg_size
    *undescribed*

reserved1
    *undescribed*

src_addr
    *undescribed*

status
    *undescribed*

tkid
    *undescribed*

dn_data
    *undescribed*

.. _`dn_buf_entry.description`:

Description
-----------

[WHCI] section 3.2.8

.. This file was automatic generated / don't edit.

