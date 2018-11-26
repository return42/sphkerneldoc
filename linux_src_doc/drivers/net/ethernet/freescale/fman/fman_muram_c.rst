.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fman/fman_muram.c

.. _`fman_muram_init`:

fman_muram_init
===============

.. c:function:: struct muram_info *fman_muram_init(phys_addr_t base, size_t size)

    :param base:
        Pointer to base of memory mapped FM-MURAM.
    :type base: phys_addr_t

    :param size:
        Size of the FM-MURAM partition.
    :type size: size_t

.. _`fman_muram_init.description`:

Description
-----------

Creates partition in the MURAM.
The routine returns a pointer to the MURAM partition.
This pointer must be passed as to all other FM-MURAM function calls.
No actual initialization or configuration of FM_MURAM hardware is done by
this routine.

.. _`fman_muram_init.return`:

Return
------

pointer to FM-MURAM object, or NULL for Failure.

.. _`fman_muram_offset_to_vbase`:

fman_muram_offset_to_vbase
==========================

.. c:function:: unsigned long fman_muram_offset_to_vbase(struct muram_info *muram, unsigned long offset)

    :param muram:
        FM-MURAM module pointer.
    :type muram: struct muram_info \*

    :param offset:
        the offset of the memory block
    :type offset: unsigned long

.. _`fman_muram_offset_to_vbase.description`:

Description
-----------

Gives the address of the memory region from specific offset

.. _`fman_muram_offset_to_vbase.return`:

Return
------

The address of the memory block

.. _`fman_muram_alloc`:

fman_muram_alloc
================

.. c:function:: unsigned long fman_muram_alloc(struct muram_info *muram, size_t size)

    :param muram:
        FM-MURAM module pointer.
    :type muram: struct muram_info \*

    :param size:
        Size of the memory to be allocated.
    :type size: size_t

.. _`fman_muram_alloc.description`:

Description
-----------

Allocate some memory from FM-MURAM partition.

.. _`fman_muram_alloc.return`:

Return
------

address of the allocated memory; NULL otherwise.

.. _`fman_muram_free_mem`:

fman_muram_free_mem
===================

.. c:function:: void fman_muram_free_mem(struct muram_info *muram, unsigned long offset, size_t size)

    :param muram:
        *undescribed*
    :type muram: struct muram_info \*

    :param offset:
        *undescribed*
    :type offset: unsigned long

    :param size:
        *undescribed*
    :type size: size_t

.. _`fman_muram_free_mem.muram`:

muram
-----

FM-MURAM module pointer.

.. _`fman_muram_free_mem.offset`:

offset
------

offset of the memory region to be freed.

.. _`fman_muram_free_mem.size`:

size
----

size of the memory to be freed.

Free an allocated memory from FM-MURAM partition.

.. This file was automatic generated / don't edit.

