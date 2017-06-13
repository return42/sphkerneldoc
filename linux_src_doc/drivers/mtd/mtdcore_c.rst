.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/mtdcore.c

.. _`mtd_wunit_to_pairing_info`:

mtd_wunit_to_pairing_info
=========================

.. c:function:: int mtd_wunit_to_pairing_info(struct mtd_info *mtd, int wunit, struct mtd_pairing_info *info)

    get pairing information of a wunit

    :param struct mtd_info \*mtd:
        pointer to new MTD device info structure

    :param int wunit:
        *undescribed*

    :param struct mtd_pairing_info \*info:
        returned pairing information

.. _`mtd_wunit_to_pairing_info.description`:

Description
-----------

Retrieve pairing information associated to the wunit.
This is mainly useful when dealing with MLC/TLC NANDs where pages can be
paired together, and where programming a page may influence the page it is
paired with.
The notion of page is replaced by the term wunit (write-unit) to stay
consistent with the ->writesize field.

The \ ``wunit``\  argument can be extracted from an absolute offset using
\ :c:func:`mtd_offset_to_wunit`\ . \ ``info``\  is filled with the pairing information attached
to \ ``wunit``\ .

From the pairing info the MTD user can find all the wunits paired with

for (i = 0; i < mtd_pairing_groups(mtd); i++) {
info.pair = i;
mtd_pairing_info_to_wunit(mtd, \ :c:type:`struct info <info>`\ );
...
}

.. _`mtd_pairing_info_to_wunit`:

mtd_pairing_info_to_wunit
=========================

.. c:function:: int mtd_pairing_info_to_wunit(struct mtd_info *mtd, const struct mtd_pairing_info *info)

    get wunit from pairing information

    :param struct mtd_info \*mtd:
        pointer to new MTD device info structure

    :param const struct mtd_pairing_info \*info:
        pairing information struct

.. _`mtd_pairing_info_to_wunit.description`:

Description
-----------

Returns a positive number representing the wunit associated to the info
struct, or a negative error code.

This is the reverse of \ :c:func:`mtd_wunit_to_pairing_info`\ , and can help one to
iterate over all wunits of a given pair (see \ :c:func:`mtd_wunit_to_pairing_info`\ 
doc).

It can also be used to only program the first page of each pair (i.e.
page attached to group 0), which allows one to use an MLC NAND in
software-emulated SLC mode:

info.group = 0;
npairs = mtd_wunit_per_eb(mtd) / mtd_pairing_groups(mtd);
for (info.pair = 0; info.pair < npairs; info.pair++) {
wunit = mtd_pairing_info_to_wunit(mtd, \ :c:type:`struct info <info>`\ );
mtd_write(mtd, mtd_wunit_to_offset(mtd, blkoffs, wunit),
mtd->writesize, \ :c:type:`struct retlen <retlen>`\ , buf + (i \* mtd->writesize));
}

.. _`mtd_pairing_groups`:

mtd_pairing_groups
==================

.. c:function:: int mtd_pairing_groups(struct mtd_info *mtd)

    get the number of pairing groups

    :param struct mtd_info \*mtd:
        pointer to new MTD device info structure

.. _`mtd_pairing_groups.description`:

Description
-----------

Returns the number of pairing groups.

This number is usually equal to the number of bits exposed by a single
cell, and can be used in conjunction with \ :c:func:`mtd_pairing_info_to_wunit`\ 
to iterate over all pages of a given pair.

.. _`add_mtd_device`:

add_mtd_device
==============

.. c:function:: int add_mtd_device(struct mtd_info *mtd)

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

.. c:function:: int del_mtd_device(struct mtd_info *mtd)

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

.. c:function:: int mtd_device_parse_register(struct mtd_info *mtd, const char * const *types, struct mtd_part_parser_data *parser_data, const struct mtd_partition *parts, int nr_parts)

    parse partitions and register an MTD device.

    :param struct mtd_info \*mtd:
        the MTD device to register

    :param const char \* const \*types:
        the list of MTD partition probes to try, see
        'parse_mtd_partitions()' for more information

    :param struct mtd_part_parser_data \*parser_data:
        MTD partition parser-specific data

    :param const struct mtd_partition \*parts:
        fallback partition information to register, if parsing fails;
        only valid if \ ``nr_parts``\  > \ ``0``\ 

    :param int nr_parts:
        the number of partitions in parts, if zero then the full
        MTD device is registered if no partition info is found

.. _`mtd_device_parse_register.description`:

Description
-----------

This function aggregates MTD partitions parsing (done by
'parse_mtd_partitions()') and MTD device and partitions registering. It

.. _`mtd_device_parse_register.basically-follows-the-most-common-pattern-found-in-many-mtd-drivers`:

basically follows the most common pattern found in many MTD drivers
-------------------------------------------------------------------


\* It first tries to probe partitions on MTD device \ ``mtd``\  using parsers
specified in \ ``types``\  (if \ ``types``\  is \ ``NULL``\ , then the default list of parsers
is used, see 'parse_mtd_partitions()' for more information). If none are
found this functions tries to fallback to information specified in
\ ``parts``\ /@nr_parts.
\* If any partitioning info was found, this function registers the found
partitions. If the MTD_PARTITIONED_MASTER option is set, then the device
as a whole is registered first.
\* If no partitions were found this function just registers the MTD device
\ ``mtd``\  and exits.

Returns zero in case of success and a negative error code in case of failure.

.. _`mtd_device_unregister`:

mtd_device_unregister
=====================

.. c:function:: int mtd_device_unregister(struct mtd_info *master)

    unregister an existing MTD device.

    :param struct mtd_info \*master:
        the MTD device to unregister.  This will unregister both the master
        and any partitions if registered.

.. _`register_mtd_user`:

register_mtd_user
=================

.. c:function:: void register_mtd_user(struct mtd_notifier *new)

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

.. c:function:: int unregister_mtd_user(struct mtd_notifier *old)

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

.. c:function:: struct mtd_info *get_mtd_device(struct mtd_info *mtd, int num)

    obtain a validated handle for an MTD device

    :param struct mtd_info \*mtd:
        last known address of the required MTD device

    :param int num:
        internal device number of the required MTD device

.. _`get_mtd_device.description`:

Description
-----------

Given a number and NULL address, return the num'th entry in the device
table, if any.  Given an address and num == -1, search the device table
for a device with that address and return if it's still present. Given
both, return the num'th driver only if its address matches. Return
error code if not.

.. _`get_mtd_device_nm`:

get_mtd_device_nm
=================

.. c:function:: struct mtd_info *get_mtd_device_nm(const char *name)

    obtain a validated handle for an MTD device by device name

    :param const char \*name:
        MTD device name to open

.. _`get_mtd_device_nm.description`:

Description
-----------

This function returns MTD device description structure in case of
success and an error code in case of failure.

.. _`mtd_ooblayout_ecc`:

mtd_ooblayout_ecc
=================

.. c:function:: int mtd_ooblayout_ecc(struct mtd_info *mtd, int section, struct mtd_oob_region *oobecc)

    Get the OOB region definition of a specific ECC section

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int section:
        ECC section. Depending on the layout you may have all the ECC
        bytes stored in a single contiguous section, or one section
        per ECC chunk (and sometime several sections for a single ECC
        ECC chunk)

    :param struct mtd_oob_region \*oobecc:
        OOB region struct filled with the appropriate ECC position
        information

.. _`mtd_ooblayout_ecc.description`:

Description
-----------

This function returns ECC section information in the OOB area. If you want
to get all the ECC bytes information, then you should call
mtd_ooblayout_ecc(mtd, section++, oobecc) until it returns -ERANGE.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_free`:

mtd_ooblayout_free
==================

.. c:function:: int mtd_ooblayout_free(struct mtd_info *mtd, int section, struct mtd_oob_region *oobfree)

    Get the OOB region definition of a specific free section

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int section:
        Free section you are interested in. Depending on the layout
        you may have all the free bytes stored in a single contiguous
        section, or one section per ECC chunk plus an extra section
        for the remaining bytes (or other funky layout).

    :param struct mtd_oob_region \*oobfree:
        OOB region struct filled with the appropriate free position
        information

.. _`mtd_ooblayout_free.description`:

Description
-----------

This function returns free bytes position in the OOB area. If you want
to get all the free bytes information, then you should call
mtd_ooblayout_free(mtd, section++, oobfree) until it returns -ERANGE.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_find_region`:

mtd_ooblayout_find_region
=========================

.. c:function:: int mtd_ooblayout_find_region(struct mtd_info *mtd, int byte, int *sectionp, struct mtd_oob_region *oobregion, int (*iter)(struct mtd_info *, int section, struct mtd_oob_region *oobregion))

    Find the region attached to a specific byte

    :param struct mtd_info \*mtd:
        mtd info structure

    :param int byte:
        the byte we are searching for

    :param int \*sectionp:
        pointer where the section id will be stored

    :param struct mtd_oob_region \*oobregion:
        used to retrieve the ECC position

    :param int (\*iter)(struct mtd_info \*, int section, struct mtd_oob_region \*oobregion):
        iterator function. Should be either mtd_ooblayout_free or
        mtd_ooblayout_ecc depending on the region type you're searching for

.. _`mtd_ooblayout_find_region.description`:

Description
-----------

This function returns the section id and oobregion information of a
specific byte. For example, say you want to know where the 4th ECC byte is
stored, you'll use:

mtd_ooblayout_find_region(mtd, 3, \ :c:type:`struct section <section>`\ , \ :c:type:`struct oobregion <oobregion>`\ , mtd_ooblayout_ecc);

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_find_eccregion`:

mtd_ooblayout_find_eccregion
============================

.. c:function:: int mtd_ooblayout_find_eccregion(struct mtd_info *mtd, int eccbyte, int *section, struct mtd_oob_region *oobregion)

    Find the ECC region attached to a specific ECC byte

    :param struct mtd_info \*mtd:
        mtd info structure

    :param int eccbyte:
        the byte we are searching for

    :param int \*section:
        *undescribed*

    :param struct mtd_oob_region \*oobregion:
        OOB region information

.. _`mtd_ooblayout_find_eccregion.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_find_region`\  except it searches for a specific ECC
byte.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_get_bytes`:

mtd_ooblayout_get_bytes
=======================

.. c:function:: int mtd_ooblayout_get_bytes(struct mtd_info *mtd, u8 *buf, const u8 *oobbuf, int start, int nbytes, int (*iter)(struct mtd_info *, int section, struct mtd_oob_region *oobregion))

    Extract OOB bytes from the oob buffer

    :param struct mtd_info \*mtd:
        mtd info structure

    :param u8 \*buf:
        destination buffer to store OOB bytes

    :param const u8 \*oobbuf:
        OOB buffer

    :param int start:
        first byte to retrieve

    :param int nbytes:
        number of bytes to retrieve

    :param int (\*iter)(struct mtd_info \*, int section, struct mtd_oob_region \*oobregion):
        section iterator

.. _`mtd_ooblayout_get_bytes.description`:

Description
-----------

Extract bytes attached to a specific category (ECC or free)
from the OOB buffer and copy them into buf.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_set_bytes`:

mtd_ooblayout_set_bytes
=======================

.. c:function:: int mtd_ooblayout_set_bytes(struct mtd_info *mtd, const u8 *buf, u8 *oobbuf, int start, int nbytes, int (*iter)(struct mtd_info *, int section, struct mtd_oob_region *oobregion))

    put OOB bytes into the oob buffer

    :param struct mtd_info \*mtd:
        mtd info structure

    :param const u8 \*buf:
        source buffer to get OOB bytes from

    :param u8 \*oobbuf:
        OOB buffer

    :param int start:
        first OOB byte to set

    :param int nbytes:
        number of OOB bytes to set

    :param int (\*iter)(struct mtd_info \*, int section, struct mtd_oob_region \*oobregion):
        section iterator

.. _`mtd_ooblayout_set_bytes.description`:

Description
-----------

Fill the OOB buffer with data provided in buf. The category (ECC or free)
is selected by passing the appropriate iterator.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_count_bytes`:

mtd_ooblayout_count_bytes
=========================

.. c:function:: int mtd_ooblayout_count_bytes(struct mtd_info *mtd, int (*iter)(struct mtd_info *, int section, struct mtd_oob_region *oobregion))

    count the number of bytes in a OOB category

    :param struct mtd_info \*mtd:
        mtd info structure

    :param int (\*iter)(struct mtd_info \*, int section, struct mtd_oob_region \*oobregion):
        category iterator

.. _`mtd_ooblayout_count_bytes.description`:

Description
-----------

Count the number of bytes in a given category.

Returns a positive value on success, a negative error code otherwise.

.. _`mtd_ooblayout_get_eccbytes`:

mtd_ooblayout_get_eccbytes
==========================

.. c:function:: int mtd_ooblayout_get_eccbytes(struct mtd_info *mtd, u8 *eccbuf, const u8 *oobbuf, int start, int nbytes)

    extract ECC bytes from the oob buffer

    :param struct mtd_info \*mtd:
        mtd info structure

    :param u8 \*eccbuf:
        destination buffer to store ECC bytes

    :param const u8 \*oobbuf:
        OOB buffer

    :param int start:
        first ECC byte to retrieve

    :param int nbytes:
        number of ECC bytes to retrieve

.. _`mtd_ooblayout_get_eccbytes.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_get_bytes`\ , except it acts on ECC bytes.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_set_eccbytes`:

mtd_ooblayout_set_eccbytes
==========================

.. c:function:: int mtd_ooblayout_set_eccbytes(struct mtd_info *mtd, const u8 *eccbuf, u8 *oobbuf, int start, int nbytes)

    set ECC bytes into the oob buffer

    :param struct mtd_info \*mtd:
        mtd info structure

    :param const u8 \*eccbuf:
        source buffer to get ECC bytes from

    :param u8 \*oobbuf:
        OOB buffer

    :param int start:
        first ECC byte to set

    :param int nbytes:
        number of ECC bytes to set

.. _`mtd_ooblayout_set_eccbytes.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_set_bytes`\ , except it acts on ECC bytes.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_get_databytes`:

mtd_ooblayout_get_databytes
===========================

.. c:function:: int mtd_ooblayout_get_databytes(struct mtd_info *mtd, u8 *databuf, const u8 *oobbuf, int start, int nbytes)

    extract data bytes from the oob buffer

    :param struct mtd_info \*mtd:
        mtd info structure

    :param u8 \*databuf:
        destination buffer to store ECC bytes

    :param const u8 \*oobbuf:
        OOB buffer

    :param int start:
        first ECC byte to retrieve

    :param int nbytes:
        number of ECC bytes to retrieve

.. _`mtd_ooblayout_get_databytes.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_get_bytes`\ , except it acts on free bytes.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_set_databytes`:

mtd_ooblayout_set_databytes
===========================

.. c:function:: int mtd_ooblayout_set_databytes(struct mtd_info *mtd, const u8 *databuf, u8 *oobbuf, int start, int nbytes)

    set data bytes into the oob buffer

    :param struct mtd_info \*mtd:
        mtd info structure

    :param const u8 \*databuf:
        *undescribed*

    :param u8 \*oobbuf:
        OOB buffer

    :param int start:
        first ECC byte to set

    :param int nbytes:
        number of ECC bytes to set

.. _`mtd_ooblayout_set_databytes.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_get_bytes`\ , except it acts on free bytes.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_count_freebytes`:

mtd_ooblayout_count_freebytes
=============================

.. c:function:: int mtd_ooblayout_count_freebytes(struct mtd_info *mtd)

    count the number of free bytes in OOB

    :param struct mtd_info \*mtd:
        mtd info structure

.. _`mtd_ooblayout_count_freebytes.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_count_bytes`\ , except it count free bytes.

Returns zero on success, a negative error code otherwise.

.. _`mtd_ooblayout_count_eccbytes`:

mtd_ooblayout_count_eccbytes
============================

.. c:function:: int mtd_ooblayout_count_eccbytes(struct mtd_info *mtd)

    count the number of ECC bytes in OOB

    :param struct mtd_info \*mtd:
        mtd info structure

.. _`mtd_ooblayout_count_eccbytes.description`:

Description
-----------

Works like \ :c:func:`mtd_ooblayout_count_bytes`\ , except it count ECC bytes.

Returns zero on success, a negative error code otherwise.

.. _`mtd_kmalloc_up_to`:

mtd_kmalloc_up_to
=================

.. c:function:: void *mtd_kmalloc_up_to(const struct mtd_info *mtd, size_t *size)

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

.. This file was automatic generated / don't edit.

