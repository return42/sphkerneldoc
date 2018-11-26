.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_memcpy.c

.. _`i915_memcpy_from_wc`:

i915_memcpy_from_wc
===================

.. c:function:: bool i915_memcpy_from_wc(void *dst, const void *src, unsigned long len)

    perform an accelerated \*aligned\* read from WC

    :param dst:
        destination pointer
    :type dst: void \*

    :param src:
        source pointer
    :type src: const void \*

    :param len:
        how many bytes to copy
    :type len: unsigned long

.. _`i915_memcpy_from_wc.description`:

Description
-----------

i915_memcpy_from_wc copies \ ``len``\  bytes from \ ``src``\  to \ ``dst``\  using
non-temporal instructions where available. Note that all arguments
(@src, \ ``dst``\ ) must be aligned to 16 bytes and \ ``len``\  must be a multiple
of 16.

To test whether accelerated reads from WC are supported, use
i915_memcpy_from_wc(NULL, NULL, 0);

Returns true if the copy was successful, false if the preconditions
are not met.

.. This file was automatic generated / don't edit.

