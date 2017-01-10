.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_mc.c

.. _`edac_align_ptr`:

edac_align_ptr
==============

.. c:function:: void *edac_align_ptr(void **p, unsigned size, int n_elems)

    Prepares the pointer offsets for a single-shot allocation

    :param void \*\*p:
        pointer to a pointer with the memory offset to be used. At
        return, this will be incremented to point to the next offset

    :param unsigned size:
        Size of the data structure to be reserved

    :param int n_elems:
        Number of elements that should be reserved

.. _`edac_align_ptr.description`:

Description
-----------

If 'size' is a constant, the compiler will optimize this whole function
down to either a no-op or the addition of a constant to the value of '\*p'.

The 'p' pointer is absolutely needed to keep the proper advancing
further in memory to the proper offsets when allocating the struct along
with its embedded structs, as \ :c:func:`edac_device_alloc_ctl_info`\  does it
above, for example.

At return, the pointer 'p' will be incremented to be used on a next call
to this function.

.. _`find_mci_by_dev`:

find_mci_by_dev
===============

.. c:function:: struct mem_ctl_info *find_mci_by_dev(struct device *dev)

    :param struct device \*dev:
        pointer to a struct device related with the MCI

.. _`find_mci_by_dev.description`:

Description
-----------

scan list of controllers looking for the one that manages
the 'dev' device

.. This file was automatic generated / don't edit.

