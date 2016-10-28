.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/memmap.c

.. _`firmware_map_add_entry`:

firmware_map_add_entry
======================

.. c:function:: int firmware_map_add_entry(u64 start, u64 end, const char *type, struct firmware_map_entry *entry)

    Does the real work to add a firmware memmap entry.

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range (exclusive).

    :param const char \*type:
        Type of the memory range.

    :param struct firmware_map_entry \*entry:
        Pre-allocated (either \ :c:func:`kmalloc`\  or bootmem allocator), uninitialised
        entry.

.. _`firmware_map_add_entry.description`:

Description
-----------

Common implementation of \ :c:func:`firmware_map_add`\  and \ :c:func:`firmware_map_add_early`\ 
which expects a pre-allocated struct firmware_map_entry.

.. _`firmware_map_add_entry.return`:

Return
------

0 always

.. _`firmware_map_remove_entry`:

firmware_map_remove_entry
=========================

.. c:function:: void firmware_map_remove_entry(struct firmware_map_entry *entry)

    Does the real work to remove a firmware memmap entry.

    :param struct firmware_map_entry \*entry:
        removed entry.

.. _`firmware_map_remove_entry.description`:

Description
-----------

The caller must hold map_entries_lock, and release it properly.

.. _`firmware_map_find_entry_in_list`:

firmware_map_find_entry_in_list
===============================

.. c:function:: struct firmware_map_entry *firmware_map_find_entry_in_list(u64 start, u64 end, const char *type, struct list_head *list)

    Search memmap entry in a given list.

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range (exclusive).

    :param const char \*type:
        Type of the memory range.

    :param struct list_head \*list:
        In which to find the entry.

.. _`firmware_map_find_entry_in_list.description`:

Description
-----------

This function is to find the memmap entey of a given memory range in a
given list. The caller must hold map_entries_lock, and must not release
the lock until the processing of the returned entry has completed.

.. _`firmware_map_find_entry_in_list.return`:

Return
------

Pointer to the entry to be found on success, or NULL on failure.

.. _`firmware_map_find_entry`:

firmware_map_find_entry
=======================

.. c:function:: struct firmware_map_entry *firmware_map_find_entry(u64 start, u64 end, const char *type)

    Search memmap entry in map_entries.

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range (exclusive).

    :param const char \*type:
        Type of the memory range.

.. _`firmware_map_find_entry.description`:

Description
-----------

This function is to find the memmap entey of a given memory range.
The caller must hold map_entries_lock, and must not release the lock
until the processing of the returned entry has completed.

.. _`firmware_map_find_entry.return`:

Return
------

Pointer to the entry to be found on success, or NULL on failure.

.. _`firmware_map_find_entry_bootmem`:

firmware_map_find_entry_bootmem
===============================

.. c:function:: struct firmware_map_entry *firmware_map_find_entry_bootmem(u64 start, u64 end, const char *type)

    Search memmap entry in map_entries_bootmem.

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range (exclusive).

    :param const char \*type:
        Type of the memory range.

.. _`firmware_map_find_entry_bootmem.description`:

Description
-----------

This function is similar to firmware_map_find_entry except that it find the
given entry in map_entries_bootmem.

.. _`firmware_map_find_entry_bootmem.return`:

Return
------

Pointer to the entry to be found on success, or NULL on failure.

.. _`firmware_map_add_hotplug`:

firmware_map_add_hotplug
========================

.. c:function:: int firmware_map_add_hotplug(u64 start, u64 end, const char *type)

    Adds a firmware mapping entry when we do memory hotplug.

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range (exclusive)

    :param const char \*type:
        Type of the memory range.

.. _`firmware_map_add_hotplug.description`:

Description
-----------

Adds a firmware mapping entry. This function is for memory hotplug, it is
similar to function \ :c:func:`firmware_map_add_early`\ . The only difference is that
it will create the syfs entry dynamically.

.. _`firmware_map_add_hotplug.return`:

Return
------

0 on success, or -ENOMEM if no memory could be allocated.

.. _`firmware_map_add_early`:

firmware_map_add_early
======================

.. c:function:: int firmware_map_add_early(u64 start, u64 end, const char *type)

    Adds a firmware mapping entry.

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range.

    :param const char \*type:
        Type of the memory range.

.. _`firmware_map_add_early.description`:

Description
-----------

Adds a firmware mapping entry. This function uses the bootmem allocator
for memory allocation.

That function must be called before late_initcall.

.. _`firmware_map_add_early.return`:

Return
------

0 on success, or -ENOMEM if no memory could be allocated.

.. _`firmware_map_remove`:

firmware_map_remove
===================

.. c:function:: int firmware_map_remove(u64 start, u64 end, const char *type)

    remove a firmware mapping entry

    :param u64 start:
        Start of the memory range.

    :param u64 end:
        End of the memory range.

    :param const char \*type:
        Type of the memory range.

.. _`firmware_map_remove.description`:

Description
-----------

removes a firmware mapping entry.

.. _`firmware_map_remove.return`:

Return
------

0 on success, or -EINVAL if no entry.

.. This file was automatic generated / don't edit.

