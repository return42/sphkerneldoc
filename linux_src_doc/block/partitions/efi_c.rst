.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/partitions/efi.c

.. _`efi_crc32`:

efi_crc32
=========

.. c:function:: u32 efi_crc32(const void *buf, unsigned long len)

    EFI version of crc32 function

    :param const void \*buf:
        buffer to calculate crc32 of

    :param unsigned long len:
        length of buf

.. _`efi_crc32.description`:

Description
-----------

Returns EFI-style CRC32 value for \ ``buf``\ 

This function uses the little endian Ethernet polynomial
but seeds the function with ~0, and xor's with ~0 at the end.
Note, the EFI Specification, v1.02, has a reference to
Dr. Dobbs Journal, May 1994 (actually it's in May 1992).

.. _`last_lba`:

last_lba
========

.. c:function:: u64 last_lba(struct block_device *bdev)

    return number of last logical block of device

    :param struct block_device \*bdev:
        block device

.. _`last_lba.description`:

Description
-----------

Returns last LBA value on success, 0 on error.
This is stored (by sd and ide-geometry) in
the part[0] entry for this disk, and is the number of
physical sectors available on the disk.

.. _`is_pmbr_valid`:

is_pmbr_valid
=============

.. c:function:: int is_pmbr_valid(legacy_mbr *mbr, sector_t total_sectors)

    test Protective MBR for validity

    :param legacy_mbr \*mbr:
        pointer to a legacy mbr structure

    :param sector_t total_sectors:
        amount of sectors in the device

.. _`is_pmbr_valid.description`:

Description
-----------

Checks for a valid protective or hybrid
master boot record (MBR). The validity of a pMBR depends

.. _`is_pmbr_valid.on-all-of-the-following-properties`:

on all of the following properties
----------------------------------

1) MSDOS signature is in the last two bytes of the MBR
2) One partition of type 0xEE is found

In addition, a hybrid MBR will have up to three additional
primary partitions, which point to the same space that's
marked out by up to three GPT partitions.

Returns 0 upon invalid MBR, or GPT_MBR_PROTECTIVE or
GPT_MBR_HYBRID depending on the device layout.

.. _`read_lba`:

read_lba
========

.. c:function:: size_t read_lba(struct parsed_partitions *state, u64 lba, u8 *buffer, size_t count)

    Read bytes from disk, starting at given LBA

    :param struct parsed_partitions \*state:
        disk parsed partitions

    :param u64 lba:
        the Logical Block Address of the partition table

    :param u8 \*buffer:
        destination buffer

    :param size_t count:
        bytes to read

.. _`read_lba.description`:

Description
-----------

Reads \ ``count``\  bytes from \ ``state``\ ->bdev into \ ``buffer``\ .
Returns number of bytes read on success, 0 on error.

.. _`alloc_read_gpt_entries`:

alloc_read_gpt_entries
======================

.. c:function:: gpt_entry *alloc_read_gpt_entries(struct parsed_partitions *state, gpt_header *gpt)

    reads partition entries from disk

    :param struct parsed_partitions \*state:
        disk parsed partitions

    :param gpt_header \*gpt:
        GPT header

.. _`alloc_read_gpt_entries.description`:

Description
-----------

Returns ptes on success,  NULL on error.
Allocates space for PTEs based on information found in \ ``gpt``\ .

.. _`alloc_read_gpt_entries.notes`:

Notes
-----

remember to free pte when you're done!

.. _`alloc_read_gpt_header`:

alloc_read_gpt_header
=====================

.. c:function:: gpt_header *alloc_read_gpt_header(struct parsed_partitions *state, u64 lba)

    Allocates GPT header, reads into it from disk

    :param struct parsed_partitions \*state:
        disk parsed partitions

    :param u64 lba:
        the Logical Block Address of the partition table

.. _`alloc_read_gpt_header.description`:

Description
-----------

returns GPT header on success, NULL on error.   Allocates
and fills a GPT header starting at \ ````\  from \ ``state``\ ->bdev.

.. _`alloc_read_gpt_header.note`:

Note
----

remember to free gpt when finished with it.

.. _`is_gpt_valid`:

is_gpt_valid
============

.. c:function:: int is_gpt_valid(struct parsed_partitions *state, u64 lba, gpt_header **gpt, gpt_entry **ptes)

    tests one GPT header and PTEs for validity

    :param struct parsed_partitions \*state:
        disk parsed partitions

    :param u64 lba:
        logical block address of the GPT header to test

    :param gpt_header \*\*gpt:
        GPT header ptr, filled on return.

    :param gpt_entry \*\*ptes:
        PTEs ptr, filled on return.

.. _`is_gpt_valid.description`:

Description
-----------

returns 1 if valid,  0 on error.
If valid, returns pointers to newly allocated GPT header and PTEs.

.. _`is_pte_valid`:

is_pte_valid
============

.. c:function:: int is_pte_valid(const gpt_entry *pte, const u64 lastlba)

    tests one PTE for validity

    :param const gpt_entry \*pte:
        pte to check

    :param const u64 lastlba:
        last lba of the disk

.. _`is_pte_valid.description`:

Description
-----------

returns 1 if valid,  0 on error.

.. _`compare_gpts`:

compare_gpts
============

.. c:function:: void compare_gpts(gpt_header *pgpt, gpt_header *agpt, u64 lastlba)

    Search disk for valid GPT headers and PTEs

    :param gpt_header \*pgpt:
        primary GPT header

    :param gpt_header \*agpt:
        alternate GPT header

    :param u64 lastlba:
        last LBA number

.. _`compare_gpts.description`:

Description
-----------

Returns nothing.  Sanity checks pgpt and agpt fields
and prints warnings on discrepancies.

.. _`find_valid_gpt`:

find_valid_gpt
==============

.. c:function:: int find_valid_gpt(struct parsed_partitions *state, gpt_header **gpt, gpt_entry **ptes)

    Search disk for valid GPT headers and PTEs

    :param struct parsed_partitions \*state:
        disk parsed partitions

    :param gpt_header \*\*gpt:
        GPT header ptr, filled on return.

    :param gpt_entry \*\*ptes:
        PTEs ptr, filled on return.

.. _`find_valid_gpt.description`:

Description
-----------

Returns 1 if valid, 0 on error.
If valid, returns pointers to newly allocated GPT header and PTEs.
Validity depends on PMBR being valid (or being overridden by the
'gpt' kernel command line option) and finding either the Primary
GPT header and PTEs valid, or the Alternate GPT header and PTEs
valid.  If the Primary GPT header is not valid, the Alternate GPT header
is not checked unless the 'gpt' kernel command line option is passed.
This protects against devices which misreport their size, and forces
the user to decide to use the Alternate GPT.

.. _`efi_partition`:

efi_partition
=============

.. c:function:: int efi_partition(struct parsed_partitions *state)

    :param struct parsed_partitions \*state:
        disk parsed partitions

.. _`efi_partition.description`:

Description
-----------

called from check.c, if the disk contains GPT
partitions, sets up partition entries in the kernel.

If the first block on the disk is a legacy MBR,
it will get handled by \ :c:func:`msdos_partition`\ .
If it's a Protective MBR, we'll handle it here.

We do not create a Linux partition for GPT, but
only for the actual data partitions.

.. _`efi_partition.return`:

Return
------

-1 if unable to read the partition table
0 if this isn't our partition table
1 if successful

.. This file was automatic generated / don't edit.

