.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/ima_kexec.c

.. _`ima_get_kexec_buffer`:

ima_get_kexec_buffer
====================

.. c:function:: int ima_get_kexec_buffer(void **addr, size_t *size)

    get IMA buffer from the previous kernel

    :param void \*\*addr:
        On successful return, set to point to the buffer contents.

    :param size_t \*size:
        On successful return, set to the buffer size.

.. _`ima_get_kexec_buffer.return`:

Return
------

0 on success, negative errno on error.

.. _`ima_free_kexec_buffer`:

ima_free_kexec_buffer
=====================

.. c:function:: int ima_free_kexec_buffer( void)

    free memory used by the IMA buffer

    :param  void:
        no arguments

.. _`remove_ima_buffer`:

remove_ima_buffer
=================

.. c:function:: void remove_ima_buffer(void *fdt, int chosen_node)

    remove the IMA buffer property and reservation from \ ``fdt``\ 

    :param void \*fdt:
        *undescribed*

    :param int chosen_node:
        *undescribed*

.. _`remove_ima_buffer.description`:

Description
-----------

The IMA measurement buffer is of no use to a subsequent kernel, so we always
remove it from the device tree.

.. _`arch_ima_add_kexec_buffer`:

arch_ima_add_kexec_buffer
=========================

.. c:function:: int arch_ima_add_kexec_buffer(struct kimage *image, unsigned long load_addr, size_t size)

    do arch-specific steps to add the IMA buffer

    :param struct kimage \*image:
        *undescribed*

    :param unsigned long load_addr:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`arch_ima_add_kexec_buffer.description`:

Description
-----------

Architectures should use this function to pass on the IMA buffer
information to the next kernel.

.. _`arch_ima_add_kexec_buffer.return`:

Return
------

0 on success, negative errno on error.

.. _`setup_ima_buffer`:

setup_ima_buffer
================

.. c:function:: int setup_ima_buffer(const struct kimage *image, void *fdt, int chosen_node)

    add IMA buffer information to the fdt

    :param const struct kimage \*image:
        kexec image being loaded.

    :param void \*fdt:
        Flattened device tree for the next kernel.

    :param int chosen_node:
        Offset to the chosen node.

.. _`setup_ima_buffer.return`:

Return
------

0 on success, or negative errno on error.

.. This file was automatic generated / don't edit.

