.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/vars.c

.. _`efivar_init`:

efivar_init
===========

.. c:function:: int efivar_init(int (*) func (efi_char16_t *, efi_guid_t, unsigned long, void *, void *data, bool duplicates, struct list_head *head)

    build the initial list of EFI variables

    :param (int (\*) func (efi_char16_t \*, efi_guid_t, unsigned long, void \*):
        callback function to invoke for every variable

    :param void \*data:
        function-specific data to pass to \ ``func``\ 

    :param bool duplicates:
        error if we encounter duplicates on \ ``head``\ ?

    :param struct list_head \*head:
        initialised head of variable list

.. _`efivar_init.description`:

Description
-----------

Get every EFI variable from the firmware and invoke \ ``func``\ . \ ``func``\ 
should call \ :c:func:`efivar_entry_add`\  to build the list of variables.

Returns 0 on success, or a kernel error code on failure.

.. _`efivar_entry_add`:

efivar_entry_add
================

.. c:function:: void efivar_entry_add(struct efivar_entry *entry, struct list_head *head)

    add entry to variable list

    :param struct efivar_entry \*entry:
        entry to add to list

    :param struct list_head \*head:
        list head

.. _`efivar_entry_remove`:

efivar_entry_remove
===================

.. c:function:: void efivar_entry_remove(struct efivar_entry *entry)

    remove entry from variable list

    :param struct efivar_entry \*entry:
        entry to remove from list

.. _`__efivar_entry_delete`:

__efivar_entry_delete
=====================

.. c:function:: int __efivar_entry_delete(struct efivar_entry *entry)

    delete an EFI variable

    :param struct efivar_entry \*entry:
        entry containing EFI variable to delete

.. _`__efivar_entry_delete.description`:

Description
-----------

Delete the variable from the firmware but leave \ ``entry``\  on the
variable list.

This function differs from \ :c:func:`efivar_entry_delete`\  because it does
not remove \ ``entry``\  from the variable list. Also, it is safe to be
called from within a \ :c:func:`efivar_entry_iter_begin`\  and
\ :c:func:`efivar_entry_iter_end`\  region, unlike \ :c:func:`efivar_entry_delete`\ .

Returns 0 on success, or a converted EFI status code if
\ :c:func:`set_variable`\  fails.

.. _`efivar_entry_delete`:

efivar_entry_delete
===================

.. c:function:: int efivar_entry_delete(struct efivar_entry *entry)

    delete variable and remove entry from list

    :param struct efivar_entry \*entry:
        entry containing variable to delete

.. _`efivar_entry_delete.description`:

Description
-----------

Delete the variable from the firmware and remove \ ``entry``\  from the
variable list. It is the caller's responsibility to free \ ``entry``\ 
once we return.

Returns 0 on success, or a converted EFI status code if
\ :c:func:`set_variable`\  fails.

.. _`efivar_entry_set`:

efivar_entry_set
================

.. c:function:: int efivar_entry_set(struct efivar_entry *entry, u32 attributes, unsigned long size, void *data, struct list_head *head)

    call \ :c:func:`set_variable`\ 

    :param struct efivar_entry \*entry:
        entry containing the EFI variable to write

    :param u32 attributes:
        variable attributes

    :param unsigned long size:
        size of \ ``data``\  buffer

    :param void \*data:
        buffer containing variable data

    :param struct list_head \*head:
        head of variable list

.. _`efivar_entry_set.description`:

Description
-----------

Calls \ :c:func:`set_variable`\  for an EFI variable. If creating a new EFI
variable, this function is usually followed by \ :c:func:`efivar_entry_add`\ .

Before writing the variable, the remaining EFI variable storage
space is checked to ensure there is enough room available.

If \ ``head``\  is not NULL a lookup is performed to determine whether
the entry is already on the list.

Returns 0 on success, -EEXIST if a lookup is performed and the entry
already exists on the list, or a converted EFI status code if
\ :c:func:`set_variable`\  fails.

.. _`efivar_entry_set_safe`:

efivar_entry_set_safe
=====================

.. c:function:: int efivar_entry_set_safe(efi_char16_t *name, efi_guid_t vendor, u32 attributes, bool block, unsigned long size, void *data)

    call \ :c:func:`set_variable`\  if enough space in firmware

    :param efi_char16_t \*name:
        buffer containing the variable name

    :param efi_guid_t vendor:
        variable vendor guid

    :param u32 attributes:
        variable attributes

    :param bool block:
        can we block in this context?

    :param unsigned long size:
        size of \ ``data``\  buffer

    :param void \*data:
        buffer containing variable data

.. _`efivar_entry_set_safe.description`:

Description
-----------

Ensures there is enough free storage in the firmware for this variable, and
if so, calls \ :c:func:`set_variable`\ . If creating a new EFI variable, this function
is usually followed by \ :c:func:`efivar_entry_add`\ .

Returns 0 on success, -ENOSPC if the firmware does not have enough
space for \ :c:func:`set_variable`\  to succeed, or a converted EFI status code
if \ :c:func:`set_variable`\  fails.

.. _`efivar_entry_find`:

efivar_entry_find
=================

.. c:function:: struct efivar_entry *efivar_entry_find(efi_char16_t *name, efi_guid_t guid, struct list_head *head, bool remove)

    search for an entry

    :param efi_char16_t \*name:
        the EFI variable name

    :param efi_guid_t guid:
        the EFI variable vendor's guid

    :param struct list_head \*head:
        head of the variable list

    :param bool remove:
        should we remove the entry from the list?

.. _`efivar_entry_find.description`:

Description
-----------

Search for an entry on the variable list that has the EFI variable
name \ ``name``\  and vendor guid \ ``guid``\ . If an entry is found on the list
and \ ``remove``\  is true, the entry is removed from the list.

The caller MUST call \ :c:func:`efivar_entry_iter_begin`\  and
\ :c:func:`efivar_entry_iter_end`\  before and after the invocation of this
function, respectively.

Returns the entry if found on the list, \ ``NULL``\  otherwise.

.. _`efivar_entry_size`:

efivar_entry_size
=================

.. c:function:: int efivar_entry_size(struct efivar_entry *entry, unsigned long *size)

    obtain the size of a variable

    :param struct efivar_entry \*entry:
        entry for this variable

    :param unsigned long \*size:
        location to store the variable's size

.. _`__efivar_entry_get`:

__efivar_entry_get
==================

.. c:function:: int __efivar_entry_get(struct efivar_entry *entry, u32 *attributes, unsigned long *size, void *data)

    call \ :c:func:`get_variable`\ 

    :param struct efivar_entry \*entry:
        read data for this variable

    :param u32 \*attributes:
        variable attributes

    :param unsigned long \*size:
        size of \ ``data``\  buffer

    :param void \*data:
        buffer to store variable data

.. _`__efivar_entry_get.description`:

Description
-----------

The caller MUST call \ :c:func:`efivar_entry_iter_begin`\  and
\ :c:func:`efivar_entry_iter_end`\  before and after the invocation of this
function, respectively.

.. _`efivar_entry_get`:

efivar_entry_get
================

.. c:function:: int efivar_entry_get(struct efivar_entry *entry, u32 *attributes, unsigned long *size, void *data)

    call \ :c:func:`get_variable`\ 

    :param struct efivar_entry \*entry:
        read data for this variable

    :param u32 \*attributes:
        variable attributes

    :param unsigned long \*size:
        size of \ ``data``\  buffer

    :param void \*data:
        buffer to store variable data

.. _`efivar_entry_set_get_size`:

efivar_entry_set_get_size
=========================

.. c:function:: int efivar_entry_set_get_size(struct efivar_entry *entry, u32 attributes, unsigned long *size, void *data, bool *set)

    call \ :c:func:`set_variable`\  and get new size (atomic)

    :param struct efivar_entry \*entry:
        entry containing variable to set and get

    :param u32 attributes:
        attributes of variable to be written

    :param unsigned long \*size:
        size of data buffer

    :param void \*data:
        buffer containing data to write

    :param bool \*set:
        did the \ :c:func:`set_variable`\  call succeed?

.. _`efivar_entry_set_get_size.description`:

Description
-----------

This is a pretty special (complex) function. See \ :c:func:`efivarfs_file_write`\ .

Atomically call \ :c:func:`set_variable`\  for \ ``entry``\  and if the call is
successful, return the new size of the variable from \ :c:func:`get_variable`\ 
in \ ``size``\ . The success of \ :c:func:`set_variable`\  is indicated by \ ``set``\ .

Returns 0 on success, -EINVAL if the variable data is invalid,
-ENOSPC if the firmware does not have enough available space, or a
converted EFI status code if either of \ :c:func:`set_variable`\  or
\ :c:func:`get_variable`\  fail.

If the EFI variable does not exist when calling \ :c:func:`set_variable`\ 
(EFI_NOT_FOUND), \ ``entry``\  is removed from the variable list.

.. _`efivar_entry_iter_begin`:

efivar_entry_iter_begin
=======================

.. c:function:: void efivar_entry_iter_begin( void)

    begin iterating the variable list

    :param  void:
        no arguments

.. _`efivar_entry_iter_begin.description`:

Description
-----------

Lock the variable list to prevent entry insertion and removal until
\ :c:func:`efivar_entry_iter_end`\  is called. This function is usually used in
conjunction with \\ :c:func:`__efivar_entry_iter`\  or \ :c:func:`efivar_entry_iter`\ .

.. _`efivar_entry_iter_end`:

efivar_entry_iter_end
=====================

.. c:function:: void efivar_entry_iter_end( void)

    finish iterating the variable list

    :param  void:
        no arguments

.. _`efivar_entry_iter_end.description`:

Description
-----------

Unlock the variable list and allow modifications to the list again.

.. _`__efivar_entry_iter`:

__efivar_entry_iter
===================

.. c:function:: int __efivar_entry_iter(int (*) func (struct efivar_entry *, void *, struct list_head *head, void *data, struct efivar_entry **prev)

    iterate over variable list

    :param (int (\*) func (struct efivar_entry \*, void \*):
        callback function

    :param struct list_head \*head:
        head of the variable list

    :param void \*data:
        function-specific data to pass to callback

    :param struct efivar_entry \*\*prev:
        entry to begin iterating from

.. _`__efivar_entry_iter.description`:

Description
-----------

Iterate over the list of EFI variables and call \ ``func``\  with every
entry on the list. It is safe for \ ``func``\  to remove entries in the
list via \ :c:func:`efivar_entry_delete`\ .

You MUST call \ :c:func:`efivar_enter_iter_begin`\  before this function, and
\ :c:func:`efivar_entry_iter_end`\  afterwards.

It is possible to begin iteration from an arbitrary entry within
the list by passing \ ``prev``\ . \ ``prev``\  is updated on return to point to
the last entry passed to \ ``func``\ . To begin iterating from the
beginning of the list \ ``prev``\  must be \ ``NULL``\ .

The restrictions for \ ``func``\  are the same as documented for
\ :c:func:`efivar_entry_iter`\ .

.. _`efivar_entry_iter`:

efivar_entry_iter
=================

.. c:function:: int efivar_entry_iter(int (*) func (struct efivar_entry *, void *, struct list_head *head, void *data)

    iterate over variable list

    :param (int (\*) func (struct efivar_entry \*, void \*):
        callback function

    :param struct list_head \*head:
        head of variable list

    :param void \*data:
        function-specific data to pass to callback

.. _`efivar_entry_iter.description`:

Description
-----------

Iterate over the list of EFI variables and call \ ``func``\  with every
entry on the list. It is safe for \ ``func``\  to remove entries in the
list via \ :c:func:`efivar_entry_delete`\  while iterating.

.. _`efivar_entry_iter.some-notes-for-the-callback-function`:

Some notes for the callback function
------------------------------------

- a non-zero return value indicates an error and terminates the loop
- \ ``func``\  is called from atomic context

.. _`efivars_kobject`:

efivars_kobject
===============

.. c:function:: struct kobject *efivars_kobject( void)

    get the kobject for the registered efivars

    :param  void:
        no arguments

.. _`efivars_kobject.description`:

Description
-----------

If \ :c:func:`efivars_register`\  has not been called we return NULL,
otherwise return the kobject used at registration time.

.. _`efivar_run_worker`:

efivar_run_worker
=================

.. c:function:: void efivar_run_worker( void)

    schedule the efivar worker thread

    :param  void:
        no arguments

.. _`efivars_register`:

efivars_register
================

.. c:function:: int efivars_register(struct efivars *efivars, const struct efivar_operations *ops, struct kobject *kobject)

    register an efivars

    :param struct efivars \*efivars:
        efivars to register

    :param const struct efivar_operations \*ops:
        efivars operations

    :param struct kobject \*kobject:
        \ ``efivars``\ -specific kobject

.. _`efivars_register.description`:

Description
-----------

Only a single efivars can be registered at any time.

.. _`efivars_unregister`:

efivars_unregister
==================

.. c:function:: int efivars_unregister(struct efivars *efivars)

    unregister an efivars

    :param struct efivars \*efivars:
        efivars to unregister

.. _`efivars_unregister.description`:

Description
-----------

The caller must have already removed every entry from the list,
failure to do so is an error.

.. This file was automatic generated / don't edit.

