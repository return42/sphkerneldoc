.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/maccess.c

.. _`probe_kernel_read`:

probe_kernel_read
=================

.. c:function:: long probe_kernel_read(void *dst, const void *src, size_t size)

    safely attempt to read from a location

    :param dst:
        pointer to the buffer that shall take the data
    :type dst: void \*

    :param src:
        address to read from
    :type src: const void \*

    :param size:
        size of the data chunk
    :type size: size_t

.. _`probe_kernel_read.description`:

Description
-----------

Safely read from address \ ``src``\  to the buffer at \ ``dst``\ .  If a kernel fault
happens, handle that and return -EFAULT.

We ensure that the copy_from_user is executed in atomic context so that
\ :c:func:`do_page_fault`\  doesn't attempt to take mmap_sem.  This makes
\ :c:func:`probe_kernel_read`\  suitable for use within regions where the caller
already holds mmap_sem, or other locks which nest inside mmap_sem.

.. _`probe_kernel_write`:

probe_kernel_write
==================

.. c:function:: long probe_kernel_write(void *dst, const void *src, size_t size)

    safely attempt to write to a location

    :param dst:
        address to write to
    :type dst: void \*

    :param src:
        pointer to the data that shall be written
    :type src: const void \*

    :param size:
        size of the data chunk
    :type size: size_t

.. _`probe_kernel_write.description`:

Description
-----------

Safely write to address \ ``dst``\  from the buffer at \ ``src``\ .  If a kernel fault
happens, handle that and return -EFAULT.

.. _`strncpy_from_unsafe`:

strncpy_from_unsafe
===================

.. c:function:: long strncpy_from_unsafe(char *dst, const void *unsafe_addr, long count)

    - Copy a NUL terminated string from unsafe address.

    :param dst:
        Destination address, in kernel space.  This buffer must be at
        least \ ``count``\  bytes long.
    :type dst: char \*

    :param unsafe_addr:
        Unsafe address.
    :type unsafe_addr: const void \*

    :param count:
        Maximum number of bytes to copy, including the trailing NUL.
    :type count: long

.. _`strncpy_from_unsafe.description`:

Description
-----------

Copies a NUL-terminated string from unsafe address to kernel buffer.

On success, returns the length of the string INCLUDING the trailing NUL.

If access fails, returns -EFAULT (some data may have been copied
and the trailing NUL added).

If \ ``count``\  is smaller than the length of the string, copies \ ``count``\ -1 bytes,
sets the last byte of \ ``dst``\  buffer to NUL and returns \ ``count``\ .

.. This file was automatic generated / don't edit.

