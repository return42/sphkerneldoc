.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/android/binder_alloc_selftest.c

.. _`buf_end_align_type`:

enum buf_end_align_type
=======================

.. c:type:: enum buf_end_align_type

    Page alignment of a buffer end with regard to the end of the previous buffer.

.. _`buf_end_align_type.definition`:

Definition
----------

.. code-block:: c

    enum buf_end_align_type {
        SAME_PAGE_UNALIGNED,
        SAME_PAGE_ALIGNED,
        NEXT_PAGE_UNALIGNED,
        NEXT_PAGE_ALIGNED,
        NEXT_NEXT_UNALIGNED,
        LOOP_END
    };

.. _`buf_end_align_type.constants`:

Constants
---------

SAME_PAGE_UNALIGNED
    The end of this buffer is onthe same page as the end of the previous buffer and
    is not page aligned. Examples:
    buf1 ][ buf2 ][ ...
    buf1 ]\|[ buf2 ][ ...

SAME_PAGE_ALIGNED
    When the end of the previous bufferis not page aligned, the end of this buffer is on the
    same page as the end of the previous buffer and is page
    aligned. When the previous buffer is page aligned, the
    end of this buffer is aligned to the next page boundary.
    Examples:
    buf1 ][ buf2 ]\| ...
    buf1 ]\|[ buf2 ]\| ...

NEXT_PAGE_UNALIGNED
    The end of this buffer is onthe page next to the end of the previous buffer and
    is not page aligned. Examples:
    buf1 ][ buf2 \| buf2 ][ ...
    buf1 ]\|[ buf2 \| buf2 ][ ...

NEXT_PAGE_ALIGNED
    The end of this buffer is onthe page next to the end of the previous buffer and
    is page aligned. Examples:
    buf1 ][ buf2 \| buf2 ]\| ...
    buf1 ]\|[ buf2 \| buf2 ]\| ...

NEXT_NEXT_UNALIGNED
    The end of this buffer is onthe page that follows the page after the end of the
    previous buffer and is not page aligned. Examples:
    buf1 ][ buf2 \| buf2 \| buf2 ][ ...
    buf1 ]\|[ buf2 \| buf2 \| buf2 ][ ...

LOOP_END
    *undescribed*

.. _`buf_end_align_type.description`:

Description
-----------

In the pictures below, buf2 refers to the buffer we
are aligning. buf1 refers to previous buffer by addr.
Symbol [ means the start of a buffer, ] means the end
of a buffer, and \| means page boundaries.

.. _`binder_selftest_alloc`:

binder_selftest_alloc
=====================

.. c:function:: void binder_selftest_alloc(struct binder_alloc *alloc)

    Test alloc and free of buffer pages.

    :param struct binder_alloc \*alloc:
        Pointer to alloc struct.

.. _`binder_selftest_alloc.description`:

Description
-----------

Allocate BUFFER_NUM buffers to cover all page alignment cases,
then free them in all orders possible. Check that pages are
correctly allocated, put onto lru when buffers are freed, and
are freed when binder_alloc_free_page is called.

.. This file was automatic generated / don't edit.

