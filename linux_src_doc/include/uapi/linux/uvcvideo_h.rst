.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/uvcvideo.h

.. _`uvc_meta_buf`:

struct uvc_meta_buf
===================

.. c:type:: struct uvc_meta_buf

    metadata buffer building block \ ``ns``\           - system timestamp of the payload in nanoseconds \ ``sof``\          - USB Frame Number \ ``length``\       - length of the payload header \ ``flags``\        - payload header flags \ ``buf``\          - optional device-specific header data

.. _`uvc_meta_buf.definition`:

Definition
----------

.. code-block:: c

    struct uvc_meta_buf {
        __u64 ns;
        __u16 sof;
        __u8 length;
        __u8 flags;
        __u8 buf[];
    }

.. _`uvc_meta_buf.members`:

Members
-------

ns
    *undescribed*

sof
    *undescribed*

length
    *undescribed*

flags
    *undescribed*

buf
    *undescribed*

.. _`uvc_meta_buf.description`:

Description
-----------

UVC metadata nodes fill buffers with possibly multiple instances of this
struct. The first two fields are added by the driver, they can be used for
clock synchronisation. The rest is an exact copy of a UVC payload header.
Only complete objects with complete buffers are included. Therefore it's
always sizeof(meta->ts) + sizeof(meta->sof) + meta->length bytes large.

.. This file was automatic generated / don't edit.

