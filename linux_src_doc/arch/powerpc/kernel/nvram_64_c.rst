.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/nvram_64.c

.. _`nvram_pstore_write`:

nvram_pstore_write
==================

.. c:function:: int nvram_pstore_write(struct pstore_record *record)

    pstore write callback for nvram

    :param record:
        pstore record to write, with \ ``id``\  to be set
    :type record: struct pstore_record \*

.. _`nvram_pstore_write.description`:

Description
-----------

Called by \ :c:func:`pstore_dump`\  when an oops or panic report is logged in the
printk buffer.
Returns 0 on successful write.

.. _`nvram_remove_partition`:

nvram_remove_partition
======================

.. c:function:: int nvram_remove_partition(const char *name, int sig, const char  *exceptions)

    Remove one or more partitions in nvram

    :param name:
        name of the partition to remove, or NULL for a
        signature only match
    :type name: const char \*

    :param sig:
        signature of the partition(s) to remove
    :type sig: int

    :param exceptions:
        When removing all partitions with a matching signature,
        leave these alone.
    :type exceptions: const char  \*

.. _`nvram_create_partition`:

nvram_create_partition
======================

.. c:function:: loff_t nvram_create_partition(const char *name, int sig, int req_size, int min_size)

    Create a partition in nvram

    :param name:
        name of the partition to create
    :type name: const char \*

    :param sig:
        signature of the partition to create
    :type sig: int

    :param req_size:
        size of data to allocate in bytes
    :type req_size: int

    :param min_size:
        minimum acceptable size (0 means req_size)
    :type min_size: int

.. _`nvram_create_partition.description`:

Description
-----------

Returns a negative error code or a positive nvram index
of the beginning of the data area of the newly created
partition. If you provided a min_size smaller than req_size
you need to query for the actual size yourself after the
call using \ :c:func:`nvram_partition_get_size`\ .

.. _`nvram_get_partition_size`:

nvram_get_partition_size
========================

.. c:function:: int nvram_get_partition_size(loff_t data_index)

    Get the data size of an nvram partition

    :param data_index:
        This is the offset of the start of the data of
        the partition. The same value that is returned by
        \ :c:func:`nvram_create_partition`\ .
    :type data_index: loff_t

.. _`nvram_find_partition`:

nvram_find_partition
====================

.. c:function:: loff_t nvram_find_partition(const char *name, int sig, int *out_size)

    Find an nvram partition by signature and name

    :param name:
        Name of the partition or NULL for any name
    :type name: const char \*

    :param sig:
        Signature to test against
    :type sig: int

    :param out_size:
        if non-NULL, returns the size of the data part of the partition
    :type out_size: int \*

.. This file was automatic generated / don't edit.

