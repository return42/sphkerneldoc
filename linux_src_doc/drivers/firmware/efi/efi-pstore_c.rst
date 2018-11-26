.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/efi-pstore.c

.. _`efi_pstore_scan_sysfs_enter`:

efi_pstore_scan_sysfs_enter
===========================

.. c:function:: void efi_pstore_scan_sysfs_enter(struct efivar_entry *pos, struct efivar_entry *next, struct list_head *head)

    :param pos:
        scanning entry
    :type pos: struct efivar_entry \*

    :param next:
        next entry
    :type next: struct efivar_entry \*

    :param head:
        list head
    :type head: struct list_head \*

.. _`__efi_pstore_scan_sysfs_exit`:

\__efi_pstore_scan_sysfs_exit
=============================

.. c:function:: int __efi_pstore_scan_sysfs_exit(struct efivar_entry *entry, bool turn_off_scanning)

    :param entry:
        deleting entry
    :type entry: struct efivar_entry \*

    :param turn_off_scanning:
        Check if a scanning flag should be turned off
    :type turn_off_scanning: bool

.. _`efi_pstore_scan_sysfs_exit`:

efi_pstore_scan_sysfs_exit
==========================

.. c:function:: int efi_pstore_scan_sysfs_exit(struct efivar_entry *pos, struct efivar_entry *next, struct list_head *head, bool stop)

    :param pos:
        scanning entry
    :type pos: struct efivar_entry \*

    :param next:
        next entry
    :type next: struct efivar_entry \*

    :param head:
        list head
    :type head: struct list_head \*

    :param stop:
        a flag checking if scanning will stop
    :type stop: bool

.. _`efi_pstore_sysfs_entry_iter`:

efi_pstore_sysfs_entry_iter
===========================

.. c:function:: int efi_pstore_sysfs_entry_iter(struct pstore_record *record)

    :param record:
        pstore record to pass to callback
    :type record: struct pstore_record \*

.. _`efi_pstore_sysfs_entry_iter.description`:

Description
-----------

You MUST call \ :c:func:`efivar_enter_iter_begin`\  before this function, and
\ :c:func:`efivar_entry_iter_end`\  afterwards.

.. _`efi_pstore_read`:

efi_pstore_read
===============

.. c:function:: ssize_t efi_pstore_read(struct pstore_record *record)

    :param record:
        *undescribed*
    :type record: struct pstore_record \*

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

