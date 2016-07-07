.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/uapi/ion_test.h

.. _`ion_test_rw_data`:

struct ion_test_rw_data
=======================

.. c:type:: struct ion_test_rw_data

    metadata passed to the kernel to read handle

.. _`ion_test_rw_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_test_rw_data {
        __u64 ptr;
        __u64 offset;
        __u64 size;
        int write;
        int __padding;
    }

.. _`ion_test_rw_data.members`:

Members
-------

ptr
    a pointer to an area at least as large as size

offset
    offset into the ion buffer to start reading

size
    size to read or write

write
    1 to write, 0 to read

__padding
    *undescribed*

.. This file was automatic generated / don't edit.

