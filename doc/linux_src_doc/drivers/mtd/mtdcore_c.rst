.. -*- coding: utf-8; mode: rst -*-

=========
mtdcore.c
=========


.. _`add_mtd_device`:

add_mtd_device
==============

.. c:function:: int add_mtd_device (struct mtd_info *mtd)

    register an MTD device

    :param struct mtd_info \*mtd:
        pointer to new MTD device info structure



.. _`add_mtd_device.description`:

Description
-----------

Add a device to the list of MTD devices present in the system, and
notify each currently active MTD 'user' of its arrival. Returns
zero on success or non-zero on failure.



.. _`del_mtd_device`:

del_mtd_device
==============

.. c:function:: int del_mtd_device (struct mtd_info *mtd)

    unregister an MTD device

    :param struct mtd_info \*mtd:
        pointer to MTD device info structure



.. _`del_mtd_device.description`:

Description
-----------

Remove a device from the list of MTD devices present in the system,
and notify each currently active MTD 'user' of its departure.
Returns zero on success or 1 on failure, which currently will happen
if the requested device does not appear to be present in the list.



.. _`mtd_device_parse_register`:

mtd_device_parse_register
=========================

.. c:function:: int mtd_device_parse_register (struct mtd_info *mtd, const char *const *types, struct mtd_part_parser_data *parser_data, const struct mtd_partition *parts, int nr_parts)

    parse partitions and register an MTD device.

    :param struct mtd_info \*mtd:
        the MTD device to register

    :param const \*types:
        the list of MTD partition probes to try, see
        ':c:func:`parse_mtd_partitions`' for more information

    :param struct mtd_part_parser_data \*parser_data:
        MTD partition parser-specific data

    :param const struct mtd_partition \*parts:
        fallback partition information to register, if parsing fails;
        only valid if ``nr_parts`` > ``0``

    :param int nr_parts:
        the number of partitions in parts, if zero then the full
        MTD device is registered if no partition info is found



.. _`mtd_device_parse_register.description`:

Description
-----------

This function aggregates MTD partitions parsing (done by
':c:func:`parse_mtd_partitions`') and MTD device and partitions registering. It



.. _`mtd_device_parse_register.basically-follows-the-most-common-pattern-found-in-many-mtd-drivers`:

basically follows the most common pattern found in many MTD drivers
-------------------------------------------------------------------


* It first tries to probe partitions on MTD device ``mtd`` using parsers

  specified in ``types`` (if ``types`` is ``NULL``\ , then the default list of parsers
  is used, see ':c:func:`parse_mtd_partitions`' for more information). If none are
  found this functions tries to fallback to information specified in
  ``parts``\ /\ ``nr_parts``\ .

* If any partitioning info was found, this function registers the found

  partitions. If the MTD_PARTITIONED_MASTER option is set, then the device
  as a whole is registered first.

* If no partitions were found this function just registers the MTD device

  ``mtd`` and exits.

Returns zero in case of success and a negative error code in case of failure.



.. _`mtd_device_unregister`:

mtd_device_unregister
=====================

.. c:function:: int mtd_device_unregister (struct mtd_info *master)

    unregister an existing MTD device.

    :param struct mtd_info \*master:
        the MTD device to unregister.  This will unregister both the master
        and any partitions if registered.



.. _`register_mtd_user`:

register_mtd_user
=================

.. c:function:: void register_mtd_user (struct mtd_notifier *new)

    register a 'user' of MTD devices.

    :param struct mtd_notifier \*new:
        pointer to notifier info structure



.. _`register_mtd_user.description`:

Description
-----------

Registers a pair of callbacks function to be called upon addition
or removal of MTD devices. Causes the 'add' callback to be immediately
invoked for each MTD device currently present in the system.



.. _`unregister_mtd_user`:

unregister_mtd_user
===================

.. c:function:: int unregister_mtd_user (struct mtd_notifier *old)

    unregister a 'user' of MTD devices.

    :param struct mtd_notifier \*old:
        pointer to notifier info structure



.. _`unregister_mtd_user.description`:

Description
-----------

Removes a callback function pair from the list of 'users' to be
notified upon addition or removal of MTD devices. Causes the
'remove' callback to be immediately invoked for each MTD device
currently present in the system.



.. _`get_mtd_device`:

get_mtd_device
==============

.. c:function:: struct mtd_info *get_mtd_device (struct mtd_info *mtd, int num)

    obtain a validated handle for an MTD device

    :param struct mtd_info \*mtd:
        last known address of the required MTD device

    :param int num:
        internal device number of the required MTD device



.. _`get_mtd_device.description`:

Description
-----------

Given a number and NULL address, return the num'th entry in the device
table, if any.        Given an address and num == -1, search the device table
for a device with that address and return if it's still present. Given
both, return the num'th driver only if its address matches. Return
error code if not.



.. _`get_mtd_device_nm`:

get_mtd_device_nm
=================

.. c:function:: struct mtd_info *get_mtd_device_nm (const char *name)

    obtain a validated handle for an MTD device by device name

    :param const char \*name:
        MTD device name to open



.. _`get_mtd_device_nm.description`:

Description
-----------

This function returns MTD device description structure in case of
success and an error code in case of failure.



.. _`mtd_kmalloc_up_to`:

mtd_kmalloc_up_to
=================

.. c:function:: void *mtd_kmalloc_up_to (const struct mtd_info *mtd, size_t *size)

    allocate a contiguous buffer up to the specified size

    :param const struct mtd_info \*mtd:
        mtd device description object pointer

    :param size_t \*size:
        a pointer to the ideal or maximum size of the allocation, points
        to the actual allocation size on success.



.. _`mtd_kmalloc_up_to.description`:

Description
-----------

This routine attempts to allocate a contiguous kernel buffer up to
the specified size, backing off the size of the request exponentially
until the request succeeds or until the allocation size falls below
the system page size. This attempts to make sure it does not adversely
impact system performance, so when allocating more than one page, we
ask the memory allocator to avoid re-trying, swapping, writing back
or performing I/O.

Note, this function also makes sure that the allocated buffer is aligned to
the MTD device's min. I/O unit, i.e. the "mtd->writesize" value.

This is called, for example by mtd_{read,write} and jffs2_scan_medium,
to handle smaller (i.e. degraded) buffer allocations under low- or
fragmented-memory situations where such reduced allocations, from a
requested ideal, are allowed.

Returns a pointer to the allocated buffer on success; otherwise, NULL.

