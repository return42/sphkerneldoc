.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/efi-pstore.c

.. _`efi_pstore_scan_sysfs_enter`:

efi_pstore_scan_sysfs_enter
===========================

.. c:function:: void efi_pstore_scan_sysfs_enter(struct efivar_entry *pos, struct efivar_entry *next, struct list_head *head)

    :param struct efivar_entry \*pos:
        scanning entry

    :param struct efivar_entry \*next:
        next entry

    :param struct list_head \*head:
        list head

.. _`__efi_pstore_scan_sysfs_exit`:

__efi_pstore_scan_sysfs_exit
============================

.. c:function:: void __efi_pstore_scan_sysfs_exit(struct efivar_entry *entry, bool turn_off_scanning)

    :param struct efivar_entry \*entry:
        deleting entry

    :param bool turn_off_scanning:
        Check if a scanning flag should be turned off

.. _`efi_pstore_scan_sysfs_exit`:

efi_pstore_scan_sysfs_exit
==========================

.. c:function:: void efi_pstore_scan_sysfs_exit(struct efivar_entry *pos, struct efivar_entry *next, struct list_head *head, bool stop)

    :param struct efivar_entry \*pos:
        scanning entry

    :param struct efivar_entry \*next:
        next entry

    :param struct list_head \*head:
        list head

    :param bool stop:
        a flag checking if scanning will stop

.. _`efi_pstore_sysfs_entry_iter`:

efi_pstore_sysfs_entry_iter
===========================

.. c:function:: int efi_pstore_sysfs_entry_iter(void *data, struct efivar_entry **pos)

    :param void \*data:
        function-specific data to pass to callback

    :param struct efivar_entry \*\*pos:
        entry to begin iterating from

.. _`efi_pstore_sysfs_entry_iter.description`:

Description
-----------

You MUST call \ :c:func:`efivar_enter_iter_begin`\  before this function, and
\ :c:func:`efivar_entry_iter_end`\  afterwards.

It is possible to begin iteration from an arbitrary entry within
the list by passing \ ``pos``\ . \ ``pos``\  is updated on return to point to
the next entry of the last one passed to \ :c:func:`efi_pstore_read_func`\ .
To begin iterating from the beginning of the list \ ``pos``\  must be \ ``NULL``\ .

.. _`efi_pstore_read`:

efi_pstore_read
===============

.. c:function:: ssize_t efi_pstore_read(u64 *id, enum pstore_type_id *type, int *count, struct timespec *timespec, char **buf, bool *compressed, struct pstore_info *psi)

    :param u64 \*id:
        *undescribed*

    :param enum pstore_type_id \*type:
        *undescribed*

    :param int \*count:
        *undescribed*

    :param struct timespec \*timespec:
        *undescribed*

    :param char \*\*buf:
        *undescribed*

    :param bool \*compressed:
        *undescribed*

    :param struct pstore_info \*psi:
        *undescribed*

.. _`efi_pstore_read.description`:

Description
-----------

This function returns a size of NVRAM entry logged via \ :c:func:`efi_pstore_write`\ .
The meaning and behavior of efi_pstore/pstore are as below.

size > 0: Got data of an entry logged via \ :c:func:`efi_pstore_write`\  successfully,
and pstore filesystem will continue reading subsequent entries.
size == 0: Entry was not logged via \ :c:func:`efi_pstore_write`\ ,
and efi_pstore driver will continue reading subsequent entries.
size < 0: Failed to get data of entry logging via \ :c:func:`efi_pstore_write`\ ,
and pstore will stop reading entry.

.. This file was automatic generated / don't edit.

