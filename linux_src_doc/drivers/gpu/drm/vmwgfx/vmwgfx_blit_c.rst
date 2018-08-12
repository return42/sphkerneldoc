.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_blit.c

.. _`vmw_find_first_diff`:

vmw_find_first_diff
===================

.. c:function:: size_t vmw_find_first_diff(const u8 *dst, const u8 *src, size_t size, size_t granularity)

    find the first difference between dst and src

    :param const u8 \*dst:
        The destination address

    :param const u8 \*src:
        The source address

    :param size_t size:
        Number of bytes to compare

    :param size_t granularity:
        The granularity needed for the return value in bytes.

.. _`vmw_find_first_diff.return`:

Return
------

The offset from find start where the first difference was
encountered in bytes. If no difference was found, the function returns
a value >= \ ``size``\ .

.. _`vmw_find_last_diff`:

vmw_find_last_diff
==================

.. c:function:: ssize_t vmw_find_last_diff(const u8 *dst, const u8 *src, size_t size, size_t granularity)

    find the last difference between dst and src

    :param const u8 \*dst:
        The destination address

    :param const u8 \*src:
        The source address

    :param size_t size:
        Number of bytes to compare

    :param size_t granularity:
        The granularity needed for the return value in bytes.

.. _`vmw_find_last_diff.return`:

Return
------

The offset from find start where the last difference was
encountered in bytes, or a negative value if no difference was found.

.. _`vmw_memcpy`:

vmw_memcpy
==========

.. c:function:: void vmw_memcpy(struct vmw_diff_cpy *diff, u8 *dest, const u8 *src, size_t n)

    A wrapper around kernel memcpy with allowing to plug it into a struct vmw_diff_cpy.

    :param struct vmw_diff_cpy \*diff:
        The struct vmw_diff_cpy closure argument (unused).

    :param u8 \*dest:
        The copy destination.

    :param const u8 \*src:
        The copy source.

    :param size_t n:
        Number of bytes to copy.

.. _`vmw_adjust_rect`:

vmw_adjust_rect
===============

.. c:function:: void vmw_adjust_rect(struct vmw_diff_cpy *diff, size_t diff_offs)

    Adjust rectangle coordinates for newly found difference

    :param struct vmw_diff_cpy \*diff:
        The struct vmw_diff_cpy used to track the modified bounding box.

    :param size_t diff_offs:
        The offset from \ ``diff``\ ->line_offset where the difference was
        found.

.. _`vmw_diff_memcpy`:

vmw_diff_memcpy
===============

.. c:function:: void vmw_diff_memcpy(struct vmw_diff_cpy *diff, u8 *dest, const u8 *src, size_t n)

    memcpy that creates a bounding box of modified content.

    :param struct vmw_diff_cpy \*diff:
        The struct vmw_diff_cpy used to track the modified bounding box.

    :param u8 \*dest:
        The copy destination.

    :param const u8 \*src:
        The copy source.

    :param size_t n:
        Number of bytes to copy.

.. _`vmw_diff_memcpy.description`:

Description
-----------

In order to correctly track the modified content, the field \ ``diff``\ ->line must
be pre-loaded with the current line number, the field \ ``diff``\ ->line_offset must
be pre-loaded with the line offset in bytes where the copy starts, and
finally the field \ ``diff``\ ->cpp need to be preloaded with the number of bytes
per unit in the horizontal direction of the area we're examining.
Typically bytes per pixel.
This is needed to know the needed granularity of the difference computing
operations. A higher cpp generally leads to faster execution at the cost of
bounding box width precision.

.. _`vmw_bo_blit_line_data`:

struct vmw_bo_blit_line_data
============================

.. c:type:: struct vmw_bo_blit_line_data

    Convenience argument to vmw_bo_cpu_blit_line

.. _`vmw_bo_blit_line_data.definition`:

Definition
----------

.. code-block:: c

    struct vmw_bo_blit_line_data {
        u32 mapped_dst;
        u8 *dst_addr;
        struct page **dst_pages;
        u32 dst_num_pages;
        pgprot_t dst_prot;
        u32 mapped_src;
        u8 *src_addr;
        struct page **src_pages;
        u32 src_num_pages;
        pgprot_t src_prot;
        struct vmw_diff_cpy *diff;
    }

.. _`vmw_bo_blit_line_data.members`:

Members
-------

mapped_dst
    Already mapped destination page index in \ ``dst_pages``\ .

dst_addr
    Kernel virtual address of mapped destination page.

dst_pages
    Array of destination bo pages.

dst_num_pages
    Number of destination bo pages.

dst_prot
    Destination bo page protection.

mapped_src
    Already mapped source page index in \ ``dst_pages``\ .

src_addr
    Kernel virtual address of mapped source page.

src_pages
    Array of source bo pages.

src_num_pages
    Number of source bo pages.

src_prot
    Source bo page protection.

diff
    Struct vmw_diff_cpy, in the end forwarded to the memcpy routine.

.. _`vmw_bo_cpu_blit_line`:

vmw_bo_cpu_blit_line
====================

.. c:function:: int vmw_bo_cpu_blit_line(struct vmw_bo_blit_line_data *d, u32 dst_offset, u32 src_offset, u32 bytes_to_copy)

    Blit part of a line from one bo to another.

    :param struct vmw_bo_blit_line_data \*d:
        Blit data as described above.

    :param u32 dst_offset:
        Destination copy start offset from start of bo.

    :param u32 src_offset:
        Source copy start offset from start of bo.

    :param u32 bytes_to_copy:
        Number of bytes to copy in this line.

.. _`vmw_bo_cpu_blit`:

vmw_bo_cpu_blit
===============

.. c:function:: int vmw_bo_cpu_blit(struct ttm_buffer_object *dst, u32 dst_offset, u32 dst_stride, struct ttm_buffer_object *src, u32 src_offset, u32 src_stride, u32 w, u32 h, struct vmw_diff_cpy *diff)

    in-kernel cpu blit.

    :param struct ttm_buffer_object \*dst:
        Destination buffer object.

    :param u32 dst_offset:
        Destination offset of blit start in bytes.

    :param u32 dst_stride:
        Destination stride in bytes.

    :param struct ttm_buffer_object \*src:
        Source buffer object.

    :param u32 src_offset:
        Source offset of blit start in bytes.

    :param u32 src_stride:
        Source stride in bytes.

    :param u32 w:
        Width of blit.

    :param u32 h:
        Height of blit.

    :param struct vmw_diff_cpy \*diff:
        *undescribed*

.. _`vmw_bo_cpu_blit.return`:

Return
------

Zero on success. Negative error value on failure. Will print out
kernel warnings on caller bugs.

Performs a CPU blit from one buffer object to another avoiding a full
bo vmap which may exhaust- or fragment vmalloc space.
On supported architectures (x86), we're using kmap_atomic which avoids
cross-processor TLB- and cache flushes and may, on non-HIGHMEM systems
reference already set-up mappings.

Neither of the buffer objects may be placed in PCI memory
(Fixed memory in TTM terminology) when using this function.

.. This file was automatic generated / don't edit.

