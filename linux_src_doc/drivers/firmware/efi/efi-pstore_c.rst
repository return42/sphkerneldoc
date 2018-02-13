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

\__efi_pstore_scan_sysfs_exit
=============================

.. c:function:: int __efi_pstore_scan_sysfs_exit(struct efivar_entry *entry, bool turn_off_scanning)

    :param struct efivar_entry \*entry:
        deleting entry

    :param bool turn_off_scanning:
        Check if a scanning flag should be turned off

.. _`efi_pstore_scan_sysfs_exit`:

efi_pstore_scan_sysfs_exit
==========================

.. c:function:: int efi_pstore_scan_sysfs_exit(struct efivar_entry *pos, struct efivar_entry *next, struct list_head *head, bool stop)

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

.. c:function:: int efi_pstore_sysfs_entry_iter(struct pstore_record *record)

    :param struct pstore_record \*record:
        pstore record to pass to callback

.. _`efi_pstore_sysfs_entry_iter.description`:

Description
-----------

You MUST call \ :c:func:`efivar_enter_iter_begin`\  before this function, and
\ :c:func:`efivar_entry_iter_end`\  afterwards.

.. _`efi_pstore_read`:

efi_pstore_read
===============

.. c:function:: ssize_t efi_pstore_read(struct pstore_record *record)

    :param struct pstore_record \*record:
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

