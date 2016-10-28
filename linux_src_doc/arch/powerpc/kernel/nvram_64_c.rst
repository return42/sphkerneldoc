.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/nvram_64.c

.. _`nvram_pstore_write`:

nvram_pstore_write
==================

.. c:function:: int nvram_pstore_write(enum pstore_type_id type, enum kmsg_dump_reason reason, u64 *id, unsigned int part, int count, bool compressed, size_t size, struct pstore_info *psi)

    pstore write callback for nvram

    :param enum pstore_type_id type:
        Type of message logged

    :param enum kmsg_dump_reason reason:
        reason behind dump (oops/panic)

    :param u64 \*id:
        identifier to indicate the write performed

    :param unsigned int part:
        pstore writes data to registered buffer in parts,
        part number will indicate the same.

    :param int count:
        Indicates oops count

    :param bool compressed:
        Flag to indicate the log is compressed

    :param size_t size:
        number of bytes written to the registered buffer

    :param struct pstore_info \*psi:
        registered pstore_info structure

.. _`nvram_pstore_write.description`:

Description
-----------

Called by \ :c:func:`pstore_dump`\  when an oops or panic report is logged in the
printk buffer.
Returns 0 on successful write.

.. _`nvram_remove_partition`:

nvram_remove_partition
======================

.. c:function:: int nvram_remove_partition(const char *name, int sig, const char  *exceptions[])

    Remove one or more partitions in nvram

    :param const char \*name:
        name of the partition to remove, or NULL for a
        signature only match

    :param int sig:
        signature of the partition(s) to remove

    :param const char  \*exceptions:
        When removing all partitions with a matching signature,
        leave these alone.

.. _`nvram_create_partition`:

nvram_create_partition
======================

.. c:function:: loff_t nvram_create_partition(const char *name, int sig, int req_size, int min_size)

    Create a partition in nvram

    :param const char \*name:
        name of the partition to create

    :param int sig:
        signature of the partition to create

    :param int req_size:
        size of data to allocate in bytes

    :param int min_size:
        minimum acceptable size (0 means req_size)

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

    :param loff_t data_index:
        This is the offset of the start of the data of
        the partition. The same value that is returned by
        \ :c:func:`nvram_create_partition`\ .

.. _`nvram_find_partition`:

nvram_find_partition
====================

.. c:function:: loff_t nvram_find_partition(const char *name, int sig, int *out_size)

    Find an nvram partition by signature and name

    :param const char \*name:
        Name of the partition or NULL for any name

    :param int sig:
        Signature to test against

    :param int \*out_size:
        if non-NULL, returns the size of the data part of the partition

.. This file was automatic generated / don't edit.

