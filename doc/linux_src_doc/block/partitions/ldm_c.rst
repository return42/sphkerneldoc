.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/partitions/ldm.c

.. _`ldm_debug`:

ldm_debug
=========

.. c:function::  ldm_debug( ...)

    Support for Windows Logical Disk Manager (Dynamic Disks)

    :param ... :
        variable arguments

.. _`ldm_debug.description`:

Description
-----------

Copyright (C) 2001,2002 Richard Russon <ldm\ ``flatcap``\ .org>
Copyright (c) 2001-2012 Anton Altaparmakov
Copyright (C) 2001,2002 Jakob Kemi <jakob.kemi\ ``telia``\ .com>

Documentation is available at http://www.linux-ntfs.org/doku.php?id=downloads

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
this program (in the main directory of the source in the file COPYING); if
not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330,
Boston, MA  02111-1307  USA

.. _`ldm_parse_privhead`:

ldm_parse_privhead
==================

.. c:function:: bool ldm_parse_privhead(const u8 *data, struct privhead *ph)

    Read the LDM Database PRIVHEAD structure

    :param const u8 \*data:
        Raw database PRIVHEAD structure loaded from the device

    :param struct privhead \*ph:
        In-memory privhead structure in which to return parsed information

.. _`ldm_parse_privhead.description`:

Description
-----------

This parses the LDM database PRIVHEAD structure supplied in \ ``data``\  and
sets up the in-memory privhead structure \ ``ph``\  with the obtained information.

.. _`ldm_parse_privhead.return`:

Return
------

'true'   \ ``ph``\  contains the PRIVHEAD data
'false'  \ ``ph``\  contents are undefined

.. _`ldm_parse_tocblock`:

ldm_parse_tocblock
==================

.. c:function:: bool ldm_parse_tocblock(const u8 *data, struct tocblock *toc)

    Read the LDM Database TOCBLOCK structure

    :param const u8 \*data:
        Raw database TOCBLOCK structure loaded from the device

    :param struct tocblock \*toc:
        In-memory toc structure in which to return parsed information

.. _`ldm_parse_tocblock.description`:

Description
-----------

This parses the LDM Database TOCBLOCK (table of contents) structure supplied
in \ ``data``\  and sets up the in-memory tocblock structure \ ``toc``\  with the obtained
information.

N.B.  The \*\_start and \*\_size values returned in \ ``toc``\  are not range-checked.

.. _`ldm_parse_tocblock.return`:

Return
------

'true'   \ ``toc``\  contains the TOCBLOCK data
'false'  \ ``toc``\  contents are undefined

.. _`ldm_parse_vmdb`:

ldm_parse_vmdb
==============

.. c:function:: bool ldm_parse_vmdb(const u8 *data, struct vmdb *vm)

    Read the LDM Database VMDB structure

    :param const u8 \*data:
        Raw database VMDB structure loaded from the device

    :param struct vmdb \*vm:
        In-memory vmdb structure in which to return parsed information

.. _`ldm_parse_vmdb.description`:

Description
-----------

This parses the LDM Database VMDB structure supplied in \ ``data``\  and sets up
the in-memory vmdb structure \ ``vm``\  with the obtained information.

N.B.  The \*\_start, \*\_size and \*\_seq values will be range-checked later.

.. _`ldm_parse_vmdb.return`:

Return
------

'true'   \ ``vm``\  contains VMDB info
'false'  \ ``vm``\  contents are undefined

.. _`ldm_compare_privheads`:

ldm_compare_privheads
=====================

.. c:function:: bool ldm_compare_privheads(const struct privhead *ph1, const struct privhead *ph2)

    Compare two privhead objects

    :param const struct privhead \*ph1:
        First privhead

    :param const struct privhead \*ph2:
        Second privhead

.. _`ldm_compare_privheads.description`:

Description
-----------

This compares the two privhead structures \ ``ph1``\  and \ ``ph2``\ .

.. _`ldm_compare_privheads.return`:

Return
------

'true'   Identical
'false'  Different

.. _`ldm_compare_tocblocks`:

ldm_compare_tocblocks
=====================

.. c:function:: bool ldm_compare_tocblocks(const struct tocblock *toc1, const struct tocblock *toc2)

    Compare two tocblock objects

    :param const struct tocblock \*toc1:
        First toc

    :param const struct tocblock \*toc2:
        Second toc

.. _`ldm_compare_tocblocks.description`:

Description
-----------

This compares the two tocblock structures \ ``toc1``\  and \ ``toc2``\ .

.. _`ldm_compare_tocblocks.return`:

Return
------

'true'   Identical
'false'  Different

.. _`ldm_validate_privheads`:

ldm_validate_privheads
======================

.. c:function:: bool ldm_validate_privheads(struct parsed_partitions *state, struct privhead *ph1)

    Compare the primary privhead with its backups

    :param struct parsed_partitions \*state:
        Partition check state including device holding the LDM Database

    :param struct privhead \*ph1:
        Memory struct to fill with ph contents

.. _`ldm_validate_privheads.description`:

Description
-----------

Read and compare all three privheads from disk.

The privheads on disk show the size and location of the main disk area and
the configuration area (the database).  The values are range-checked against
\ ``hd``\ , which contains the real size of the disk.

.. _`ldm_validate_privheads.return`:

Return
------

'true'   Success
'false'  Error

.. _`ldm_validate_tocblocks`:

ldm_validate_tocblocks
======================

.. c:function:: bool ldm_validate_tocblocks(struct parsed_partitions *state, unsigned long base, struct ldmdb *ldb)

    Validate the table of contents and its backups

    :param struct parsed_partitions \*state:
        Partition check state including device holding the LDM Database

    :param unsigned long base:
        Offset, into \ ``state``\ ->bdev, of the database

    :param struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_validate_tocblocks.description`:

Description
-----------

Find and compare the four tables of contents of the LDM Database stored on
\ ``state``\ ->bdev and return the parsed information into \ ``toc1``\ .

The offsets and sizes of the configs are range-checked against a privhead.

.. _`ldm_validate_tocblocks.return`:

Return
------

'true'   \ ``toc1``\  contains validated TOCBLOCK info
'false'  \ ``toc1``\  contents are undefined

.. _`ldm_validate_vmdb`:

ldm_validate_vmdb
=================

.. c:function:: bool ldm_validate_vmdb(struct parsed_partitions *state, unsigned long base, struct ldmdb *ldb)

    Read the VMDB and validate it

    :param struct parsed_partitions \*state:
        Partition check state including device holding the LDM Database

    :param unsigned long base:
        Offset, into \ ``bdev``\ , of the database

    :param struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_validate_vmdb.description`:

Description
-----------

Find the vmdb of the LDM Database stored on \ ``bdev``\  and return the parsed
information in \ ``ldb``\ .

.. _`ldm_validate_vmdb.return`:

Return
------

'true'   \ ``ldb``\  contains validated VBDB info
'false'  \ ``ldb``\  contents are undefined

.. _`ldm_validate_partition_table`:

ldm_validate_partition_table
============================

.. c:function:: bool ldm_validate_partition_table(struct parsed_partitions *state)

    Determine whether bdev might be a dynamic disk

    :param struct parsed_partitions \*state:
        Partition check state including device holding the LDM Database

.. _`ldm_validate_partition_table.description`:

Description
-----------

This function provides a weak test to decide whether the device is a dynamic
disk or not.  It looks for an MS-DOS-style partition table containing at
least one partition of type 0x42 (formerly SFS, now used by Windows for
dynamic disks).

N.B.  The only possible error can come from the read_part_sector and that is
only likely to happen if the underlying device is strange.  If that IS
the case we should return zero to let someone else try.

.. _`ldm_validate_partition_table.return`:

Return
------

'true'   \ ``state``\ ->bdev is a dynamic disk
'false'  \ ``state``\ ->bdev is not a dynamic disk, or an error occurred

.. _`ldm_get_disk_objid`:

ldm_get_disk_objid
==================

.. c:function:: struct vblk *ldm_get_disk_objid(const struct ldmdb *ldb)

    Search a linked list of vblk's for a given Disk Id

    :param const struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_get_disk_objid.description`:

Description
-----------

The LDM Database contains a list of all partitions on all dynamic disks.
The primary PRIVHEAD, at the beginning of the physical disk, tells us
the GUID of this disk.  This function searches for the GUID in a linked
list of vblk's.

.. _`ldm_get_disk_objid.return`:

Return
------

Pointer, A matching vblk was found
NULL,    No match, or an error

.. _`ldm_create_data_partitions`:

ldm_create_data_partitions
==========================

.. c:function:: bool ldm_create_data_partitions(struct parsed_partitions *pp, const struct ldmdb *ldb)

    Create data partitions for this device

    :param struct parsed_partitions \*pp:
        List of the partitions parsed so far

    :param const struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_create_data_partitions.description`:

Description
-----------

The database contains ALL the partitions for ALL disk groups, so we need to
filter out this specific disk. Using the disk's object id, we can find all
the partitions in the database that belong to this disk.

Add each partition in our database, to the parsed_partitions structure.

N.B.  This function creates the partitions in the order it finds partition
objects in the linked list.

.. _`ldm_create_data_partitions.return`:

Return
------

'true'   Partition created
'false'  Error, probably a range checking problem

.. _`ldm_relative`:

ldm_relative
============

.. c:function:: int ldm_relative(const u8 *buffer, int buflen, int base, int offset)

    Calculate the next relative offset

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param int base:
        Size of the previous fixed width fields

    :param int offset:
        Cumulative size of the previous variable-width fields

.. _`ldm_relative.description`:

Description
-----------

Because many of the VBLK fields are variable-width, it's necessary
to calculate each offset based on the previous one and the length
of the field it pointed to.

.. _`ldm_relative.return`:

Return
------

-1 Error, the calculated offset exceeded the size of the buffer
n OK, a range-checked offset into buffer

.. _`ldm_get_vnum`:

ldm_get_vnum
============

.. c:function:: u64 ldm_get_vnum(const u8 *block)

    Convert a variable-width, big endian number, into cpu order

    :param const u8 \*block:
        Pointer to the variable-width number to convert

.. _`ldm_get_vnum.description`:

Description
-----------

Large numbers in the LDM Database are often stored in a packed format.  Each
number is prefixed by a one byte width marker.  All numbers in the database
are stored in big-endian byte order.  This function reads one of these
numbers and returns the result

N.B.  This function DOES NOT perform any range checking, though the most
it will read is eight bytes.

.. _`ldm_get_vnum.return`:

Return
------

n A number
0 Zero, or an error occurred

.. _`ldm_get_vstr`:

ldm_get_vstr
============

.. c:function:: int ldm_get_vstr(const u8 *block, u8 *buffer, int buflen)

    Read a length-prefixed string into a buffer

    :param const u8 \*block:
        Pointer to the length marker

    :param u8 \*buffer:
        Location to copy string to

    :param int buflen:
        Size of the output buffer

.. _`ldm_get_vstr.description`:

Description
-----------

Many of the strings in the LDM Database are not NULL terminated.  Instead
they are prefixed by a one byte length marker.  This function copies one of
these strings into a buffer.

N.B.  This function DOES NOT perform any range checking on the input.
If the buffer is too small, the output will be truncated.

.. _`ldm_get_vstr.return`:

Return
------

0, Error and \ ``buffer``\  contents are undefined
n, String length in characters (excluding NULL)
buflen-1, String was truncated.

.. _`ldm_parse_cmp3`:

ldm_parse_cmp3
==============

.. c:function:: bool ldm_parse_cmp3(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Component object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_cmp3.description`:

Description
-----------

Read a raw VBLK Component object (version 3) into a vblk structure.

.. _`ldm_parse_cmp3.return`:

Return
------

'true'   \ ``vb``\  contains a Component VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_dgr3`:

ldm_parse_dgr3
==============

.. c:function:: int ldm_parse_dgr3(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Disk Group object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_dgr3.description`:

Description
-----------

Read a raw VBLK Disk Group object (version 3) into a vblk structure.

.. _`ldm_parse_dgr3.return`:

Return
------

'true'   \ ``vb``\  contains a Disk Group VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_dgr4`:

ldm_parse_dgr4
==============

.. c:function:: bool ldm_parse_dgr4(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Disk Group object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_dgr4.description`:

Description
-----------

Read a raw VBLK Disk Group object (version 4) into a vblk structure.

.. _`ldm_parse_dgr4.return`:

Return
------

'true'   \ ``vb``\  contains a Disk Group VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_dsk3`:

ldm_parse_dsk3
==============

.. c:function:: bool ldm_parse_dsk3(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Disk object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_dsk3.description`:

Description
-----------

Read a raw VBLK Disk object (version 3) into a vblk structure.

.. _`ldm_parse_dsk3.return`:

Return
------

'true'   \ ``vb``\  contains a Disk VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_dsk4`:

ldm_parse_dsk4
==============

.. c:function:: bool ldm_parse_dsk4(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Disk object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_dsk4.description`:

Description
-----------

Read a raw VBLK Disk object (version 4) into a vblk structure.

.. _`ldm_parse_dsk4.return`:

Return
------

'true'   \ ``vb``\  contains a Disk VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_prt3`:

ldm_parse_prt3
==============

.. c:function:: bool ldm_parse_prt3(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Partition object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_prt3.description`:

Description
-----------

Read a raw VBLK Partition object (version 3) into a vblk structure.

.. _`ldm_parse_prt3.return`:

Return
------

'true'   \ ``vb``\  contains a Partition VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_vol5`:

ldm_parse_vol5
==============

.. c:function:: bool ldm_parse_vol5(const u8 *buffer, int buflen, struct vblk *vb)

    Read a raw VBLK Volume object into a vblk structure

    :param const u8 \*buffer:
        Block of data being worked on

    :param int buflen:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_vol5.description`:

Description
-----------

Read a raw VBLK Volume object (version 5) into a vblk structure.

.. _`ldm_parse_vol5.return`:

Return
------

'true'   \ ``vb``\  contains a Volume VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_parse_vblk`:

ldm_parse_vblk
==============

.. c:function:: bool ldm_parse_vblk(const u8 *buf, int len, struct vblk *vb)

    Read a raw VBLK object into a vblk structure

    :param const u8 \*buf:
        Block of data being worked on

    :param int len:
        Size of the block of data

    :param struct vblk \*vb:
        In-memory vblk in which to return information

.. _`ldm_parse_vblk.description`:

Description
-----------

Read a raw VBLK object into a vblk structure.  This function just reads the
information common to all VBLK types, then delegates the rest of the work to

.. _`ldm_parse_vblk.helper-functions`:

helper functions
----------------

ldm_parse\_\*.

.. _`ldm_parse_vblk.return`:

Return
------

'true'   \ ``vb``\  contains a VBLK
'false'  \ ``vb``\  contents are not defined

.. _`ldm_ldmdb_add`:

ldm_ldmdb_add
=============

.. c:function:: bool ldm_ldmdb_add(u8 *data, int len, struct ldmdb *ldb)

    Adds a raw VBLK entry to the ldmdb database

    :param u8 \*data:
        Raw VBLK to add to the database

    :param int len:
        Size of the raw VBLK

    :param struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_ldmdb_add.description`:

Description
-----------

The VBLKs are sorted into categories.  Partitions are also sorted by offset.

N.B.  This function does not check the validity of the VBLKs.

.. _`ldm_ldmdb_add.return`:

Return
------

'true'   The VBLK was added
'false'  An error occurred

.. _`ldm_frag_add`:

ldm_frag_add
============

.. c:function:: bool ldm_frag_add(const u8 *data, int size, struct list_head *frags)

    Add a VBLK fragment to a list

    :param const u8 \*data:
        Raw fragment to be added to the list

    :param int size:
        Size of the raw fragment

    :param struct list_head \*frags:
        Linked list of VBLK fragments

.. _`ldm_frag_add.description`:

Description
-----------

Fragmented VBLKs may not be consecutive in the database, so they are placed
in a list so they can be pieced together later.

.. _`ldm_frag_add.return`:

Return
------

'true'   Success, the VBLK was added to the list
'false'  Error, a problem occurred

.. _`ldm_frag_free`:

ldm_frag_free
=============

.. c:function:: void ldm_frag_free(struct list_head *list)

    Free a linked list of VBLK fragments

    :param struct list_head \*list:
        Linked list of fragments

.. _`ldm_frag_free.description`:

Description
-----------

Free a linked list of VBLK fragments

.. _`ldm_frag_free.return`:

Return
------

none

.. _`ldm_frag_commit`:

ldm_frag_commit
===============

.. c:function:: bool ldm_frag_commit(struct list_head *frags, struct ldmdb *ldb)

    Validate fragmented VBLKs and add them to the database

    :param struct list_head \*frags:
        Linked list of VBLK fragments

    :param struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_frag_commit.description`:

Description
-----------

Now that all the fragmented VBLKs have been collected, they must be added to
the database for later use.

.. _`ldm_frag_commit.return`:

Return
------

'true'   All the fragments we added successfully
'false'  One or more of the fragments we invalid

.. _`ldm_get_vblks`:

ldm_get_vblks
=============

.. c:function:: bool ldm_get_vblks(struct parsed_partitions *state, unsigned long base, struct ldmdb *ldb)

    Read the on-disk database of VBLKs into memory

    :param struct parsed_partitions \*state:
        Partition check state including device holding the LDM Database

    :param unsigned long base:
        Offset, into \ ``state``\ ->bdev, of the database

    :param struct ldmdb \*ldb:
        Cache of the database structures

.. _`ldm_get_vblks.description`:

Description
-----------

To use the information from the VBLKs, they need to be read from the disk,
unpacked and validated.  We cache them in \ ``ldb``\  according to their type.

.. _`ldm_get_vblks.return`:

Return
------

'true'   All the VBLKs were read successfully
'false'  An error occurred

.. _`ldm_free_vblks`:

ldm_free_vblks
==============

.. c:function:: void ldm_free_vblks(struct list_head *lh)

    Free a linked list of vblk's

    :param struct list_head \*lh:
        Head of a linked list of struct vblk

.. _`ldm_free_vblks.description`:

Description
-----------

Free a list of vblk's and free the memory used to maintain the list.

.. _`ldm_free_vblks.return`:

Return
------

none

.. _`ldm_partition`:

ldm_partition
=============

.. c:function:: int ldm_partition(struct parsed_partitions *state)

    Find out whether a device is a dynamic disk and handle it

    :param struct parsed_partitions \*state:
        Partition check state including device holding the LDM Database

.. _`ldm_partition.description`:

Description
-----------

This determines whether the device \ ``bdev``\  is a dynamic disk and if so creates
the partitions necessary in the gendisk structure pointed to by \ ``hd``\ .

We create a dummy device 1, which contains the LDM database, and then create
each partition described by the LDM database in sequence as devices 2+. For
example, if the device is hda, we would have: hda1: LDM database, hda2, hda3,

.. _`ldm_partition.and-so-on`:

and so on
---------

the actual data containing partitions.

.. _`ldm_partition.return`:

Return
------

1 Success, \ ``state``\ ->bdev is a dynamic disk and we handled it
0 Success, \ ``state``\ ->bdev is not a dynamic disk
-1 An error occurred before enough information had been read
Or \ ``state``\ ->bdev is a dynamic disk, but it may be corrupted

.. This file was automatic generated / don't edit.

