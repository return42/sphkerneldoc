.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/kexec_file.c

.. _`arch_kexec_walk_mem`:

arch_kexec_walk_mem
===================

.. c:function:: int arch_kexec_walk_mem(struct kexec_buf *kbuf, int (*func)(struct resource *, void *))

    call func(data) on free memory regions

    :param kbuf:
        Context info for the search. Also passed to \ ``func``\ .
    :type kbuf: struct kexec_buf \*

    :param int (\*func)(struct resource \*, void \*):
        Function to call for each memory region.

.. _`arch_kexec_walk_mem.return`:

Return
------

The memory walk will stop when func returns a non-zero value
and that value will be returned. If all free regions are visited without
func returning non-zero, then zero will be returned.

.. _`kexec_locate_mem_hole`:

kexec_locate_mem_hole
=====================

.. c:function:: int kexec_locate_mem_hole(struct kexec_buf *kbuf)

    find free memory for the purgatory or the next kernel

    :param kbuf:
        Parameters for the memory search.
    :type kbuf: struct kexec_buf \*

.. _`kexec_locate_mem_hole.description`:

Description
-----------

On success, kbuf->mem will have the start address of the memory region found.

.. _`kexec_locate_mem_hole.return`:

Return
------

0 on success, negative errno on error.

.. _`kexec_add_buffer`:

kexec_add_buffer
================

.. c:function:: int kexec_add_buffer(struct kexec_buf *kbuf)

    place a buffer in a kexec segment

    :param kbuf:
        Buffer contents and memory parameters.
    :type kbuf: struct kexec_buf \*

.. _`kexec_add_buffer.description`:

Description
-----------

This function assumes that kexec_mutex is held.
On successful return, \ ``kbuf->mem``\  will have the physical address of
the buffer in memory.

.. _`kexec_add_buffer.return`:

Return
------

0 on success, negative errno on error.

.. This file was automatic generated / don't edit.

