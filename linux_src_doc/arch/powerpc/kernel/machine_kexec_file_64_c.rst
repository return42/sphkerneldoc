.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/machine_kexec_file_64.c

.. _`arch_kexec_walk_mem`:

arch_kexec_walk_mem
===================

.. c:function:: int arch_kexec_walk_mem(struct kexec_buf *kbuf, int (*func)(struct resource *, void *))

    call func(data) for each unreserved memory block

    :param kbuf:
        Context info for the search. Also passed to \ ``func``\ .
    :type kbuf: struct kexec_buf \*

    :param int (\*func)(struct resource \*, void \*):
        Function to call for each memory block.

.. _`arch_kexec_walk_mem.description`:

Description
-----------

This function is used by kexec_add_buffer and kexec_locate_mem_hole
to find unreserved memory to load kexec segments into.

.. _`arch_kexec_walk_mem.return`:

Return
------

The memory walk will stop when func returns a non-zero value
and that value will be returned. If all free regions are visited without
func returning non-zero, then zero will be returned.

.. _`setup_purgatory`:

setup_purgatory
===============

.. c:function:: int setup_purgatory(struct kimage *image, const void *slave_code, const void *fdt, unsigned long kernel_load_addr, unsigned long fdt_load_addr)

    initialize the purgatory's global variables

    :param image:
        kexec image.
    :type image: struct kimage \*

    :param slave_code:
        Slave code for the purgatory.
    :type slave_code: const void \*

    :param fdt:
        Flattened device tree for the next kernel.
    :type fdt: const void \*

    :param kernel_load_addr:
        Address where the kernel is loaded.
    :type kernel_load_addr: unsigned long

    :param fdt_load_addr:
        Address where the flattened device tree is loaded.
    :type fdt_load_addr: unsigned long

.. _`setup_purgatory.return`:

Return
------

0 on success, or negative errno on error.

.. _`delete_fdt_mem_rsv`:

delete_fdt_mem_rsv
==================

.. c:function:: int delete_fdt_mem_rsv(void *fdt, unsigned long start, unsigned long size)

    delete memory reservation with given address and size

    :param fdt:
        *undescribed*
    :type fdt: void \*

    :param start:
        *undescribed*
    :type start: unsigned long

    :param size:
        *undescribed*
    :type size: unsigned long

.. _`delete_fdt_mem_rsv.return`:

Return
------

0 on success, or negative errno on error.

.. This file was automatic generated / don't edit.

