.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/attrib.c

.. _`ntfs_map_runlist_nolock`:

ntfs_map_runlist_nolock
=======================

.. c:function:: int ntfs_map_runlist_nolock(ntfs_inode *ni, VCN vcn, ntfs_attr_search_ctx *ctx)

    NTFS attribute operations.  Part of the Linux-NTFS project.

    :param ntfs_inode \*ni:
        *undescribed*

    :param VCN vcn:
        *undescribed*

    :param ntfs_attr_search_ctx \*ctx:
        *undescribed*

.. _`ntfs_map_runlist_nolock.description`:

Description
-----------

Copyright (c) 2001-2012 Anton Altaparmakov and Tuxera Inc.
Copyright (c) 2002 Richard Russon

This program/include file is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program/include file is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (in the main directory of the Linux-NTFS
distribution in the file COPYING); if not, write to the Free Software
Foundation,Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

.. _`ntfs_map_runlist`:

ntfs_map_runlist
================

.. c:function:: int ntfs_map_runlist(ntfs_inode *ni, VCN vcn)

    map (a part of) a runlist of an ntfs inode

    :param ntfs_inode \*ni:
        ntfs inode for which to map (part of) a runlist

    :param VCN vcn:
        map runlist part containing this vcn

.. _`ntfs_map_runlist.description`:

Description
-----------

Map the part of a runlist containing the \ ``vcn``\  of the ntfs inode \ ``ni``\ .

Return 0 on success and -errno on error.  There is one special error code
which is not an error as such.  This is -ENOENT.  It means that \ ``vcn``\  is out
of bounds of the runlist.

.. _`ntfs_map_runlist.locking`:

Locking
-------

- The runlist must be unlocked on entry and is unlocked on return.
- This function takes the runlist lock for writing and may modify
the runlist.

.. _`ntfs_attr_vcn_to_lcn_nolock`:

ntfs_attr_vcn_to_lcn_nolock
===========================

.. c:function:: LCN ntfs_attr_vcn_to_lcn_nolock(ntfs_inode *ni, const VCN vcn, const bool write_locked)

    convert a vcn into a lcn given an ntfs inode

    :param ntfs_inode \*ni:
        ntfs inode of the attribute whose runlist to search

    :param const VCN vcn:
        vcn to convert

    :param const bool write_locked:
        true if the runlist is locked for writing

.. _`ntfs_attr_vcn_to_lcn_nolock.description`:

Description
-----------

Find the virtual cluster number \ ``vcn``\  in the runlist of the ntfs attribute
described by the ntfs inode \ ``ni``\  and return the corresponding logical cluster
number (lcn).

If the \ ``vcn``\  is not mapped yet, the attempt is made to map the attribute
extent containing the \ ``vcn``\  and the vcn to lcn conversion is retried.

If \ ``write_locked``\  is true the caller has locked the runlist for writing and
if false for reading.

Since lcns must be >= 0, we use negative return codes with special meaning:

Return code  Meaning / Description
==========================================
LCN_HOLE    Hole / not allocated on disk.
LCN_ENOENT  There is no such vcn in the runlist, i.e. \ ``vcn``\  is out of bounds.
LCN_ENOMEM  Not enough memory to map runlist.
LCN_EIO     Critical error (runlist/file is corrupt, i/o error, etc).

.. _`ntfs_attr_vcn_to_lcn_nolock.locking`:

Locking
-------

- The runlist must be locked on entry and is left locked on return.
- If \ ``write_locked``\  is 'false', i.e. the runlist is locked for reading,
the lock may be dropped inside the function so you cannot rely on
the runlist still being the same when this function returns.

.. _`ntfs_attr_find_vcn_nolock`:

ntfs_attr_find_vcn_nolock
=========================

.. c:function:: runlist_element *ntfs_attr_find_vcn_nolock(ntfs_inode *ni, const VCN vcn, ntfs_attr_search_ctx *ctx)

    find a vcn in the runlist of an ntfs inode

    :param ntfs_inode \*ni:
        ntfs inode describing the runlist to search

    :param const VCN vcn:
        vcn to find

    :param ntfs_attr_search_ctx \*ctx:
        active attribute search context if present or NULL if not

.. _`ntfs_attr_find_vcn_nolock.description`:

Description
-----------

Find the virtual cluster number \ ``vcn``\  in the runlist described by the ntfs
inode \ ``ni``\  and return the address of the runlist element containing the \ ``vcn``\ .

If the \ ``vcn``\  is not mapped yet, the attempt is made to map the attribute
extent containing the \ ``vcn``\  and the vcn to lcn conversion is retried.

If \ ``ctx``\  is specified, it is an active search context of \ ``ni``\  and its base mft
record.  This is needed when \ :c:func:`ntfs_attr_find_vcn_nolock`\  encounters unmapped
runlist fragments and allows their mapping.  If you do not have the mft
record mapped, you can specify \ ``ctx``\  as NULL and \ :c:func:`ntfs_attr_find_vcn_nolock`\ 
will perform the necessary mapping and unmapping.

Note, \ :c:func:`ntfs_attr_find_vcn_nolock`\  saves the state of \ ``ctx``\  on entry and
restores it before returning.  Thus, \ ``ctx``\  will be left pointing to the same
attribute on return as on entry.  However, the actual pointers in \ ``ctx``\  may
point to different memory locations on return, so you must remember to reset
any cached pointers from the \ ``ctx``\ , i.e. after the call to
\ :c:func:`ntfs_attr_find_vcn_nolock`\ , you will probably want to do:
m = ctx->mrec;
a = ctx->attr;
Assuming you cache ctx->attr in a variable \ ``a``\  of type ATTR_RECORD \* and that
you cache ctx->mrec in a variable \ ``m``\  of type MFT_RECORD \*.
Note you need to distinguish between the lcn of the returned runlist element
being >= 0 and LCN_HOLE.  In the later case you have to return zeroes on
read and allocate clusters on write.

Return the runlist element containing the \ ``vcn``\  on success and
ERR_PTR(-errno) on error.  You need to test the return value with \ :c:func:`IS_ERR`\ 
to decide if the return is success or failure and \ :c:func:`PTR_ERR`\  to get to the
error code if \ :c:func:`IS_ERR`\  is true.

.. _`ntfs_attr_find_vcn_nolock.the-possible-error-return-codes-are`:

The possible error return codes are
-----------------------------------

-ENOENT - No such vcn in the runlist, i.e. \ ``vcn``\  is out of bounds.
-ENOMEM - Not enough memory to map runlist.
-EIO    - Critical error (runlist/file is corrupt, i/o error, etc).

.. _`ntfs_attr_find_vcn_nolock.warning`:

WARNING
-------

If \ ``ctx``\  is supplied, regardless of whether success or failure is
returned, you need to check IS_ERR(@ctx->mrec) and if 'true' the \ ``ctx``\ 
is no longer valid, i.e. you need to either call
\ :c:func:`ntfs_attr_reinit_search_ctx`\  or \ :c:func:`ntfs_attr_put_search_ctx`\  on it.
In that case PTR_ERR(@ctx->mrec) will give you the error code for
why the mapping of the old inode failed.

.. _`ntfs_attr_find_vcn_nolock.locking`:

Locking
-------

- The runlist described by \ ``ni``\  must be locked for writing on entry
and is locked on return.  Note the runlist may be modified when
needed runlist fragments need to be mapped.
- If \ ``ctx``\  is NULL, the base mft record of \ ``ni``\  must not be mapped on
entry and it will be left unmapped on return.
- If \ ``ctx``\  is not NULL, the base mft record must be mapped on entry
and it will be left mapped on return.

.. _`ntfs_attr_find`:

ntfs_attr_find
==============

.. c:function:: int ntfs_attr_find(const ATTR_TYPE type, const ntfschar *name, const u32 name_len, const IGNORE_CASE_BOOL ic, const u8 *val, const u32 val_len, ntfs_attr_search_ctx *ctx)

    find (next) attribute in mft record

    :param const ATTR_TYPE type:
        attribute type to find

    :param const ntfschar \*name:
        attribute name to find (optional, i.e. NULL means don't care)

    :param const u32 name_len:
        attribute name length (only needed if \ ``name``\  present)

    :param const IGNORE_CASE_BOOL ic:
        IGNORE_CASE or CASE_SENSITIVE (ignored if \ ``name``\  not present)

    :param const u8 \*val:
        attribute value to find (optional, resident attributes only)

    :param const u32 val_len:
        attribute value length

    :param ntfs_attr_search_ctx \*ctx:
        search context with mft record and attribute to search from

.. _`ntfs_attr_find.description`:

Description
-----------

You should not need to call this function directly.  Use \ :c:func:`ntfs_attr_lookup`\ 
instead.

\ :c:func:`ntfs_attr_find`\  takes a search context \ ``ctx``\  as parameter and searches the
mft record specified by \ ``ctx``\ ->mrec, beginning at \ ``ctx``\ ->attr, for an
attribute of \ ``type``\ , optionally \ ``name``\  and \ ``val``\ .

If the attribute is found, \ :c:func:`ntfs_attr_find`\  returns 0 and \ ``ctx``\ ->attr will
point to the found attribute.

If the attribute is not found, \ :c:func:`ntfs_attr_find`\  returns -ENOENT and
\ ``ctx``\ ->attr will point to the attribute before which the attribute being
searched for would need to be inserted if such an action were to be desired.

On actual error, \ :c:func:`ntfs_attr_find`\  returns -EIO.  In this case \ ``ctx``\ ->attr is
undefined and in particular do not rely on it not changing.

If \ ``ctx``\ ->is_first is 'true', the search begins with \ ``ctx``\ ->attr itself.  If it
is 'false', the search begins after \ ``ctx``\ ->attr.

If \ ``ic``\  is IGNORE_CASE, the \ ``name``\  comparisson is not case sensitive and
\ ``ctx``\ ->ntfs_ino must be set to the ntfs inode to which the mft record
\ ``ctx``\ ->mrec belongs.  This is so we can get at the ntfs volume and hence at
the upcase table.  If \ ``ic``\  is CASE_SENSITIVE, the comparison is case
sensitive.  When \ ``name``\  is present, \ ``name_len``\  is the \ ``name``\  length in Unicode
characters.

If \ ``name``\  is not present (NULL), we assume that the unnamed attribute is
being searched for.

Finally, the resident attribute value \ ``val``\  is looked for, if present.  If
\ ``val``\  is not present (NULL), \ ``val_len``\  is ignored.

\ :c:func:`ntfs_attr_find`\  only searches the specified mft record and it ignores the
presence of an attribute list attribute (unless it is the one being searched
for, obviously).  If you need to take attribute lists into consideration,
use \ :c:func:`ntfs_attr_lookup`\  instead (see below).  This also means that you cannot
use \ :c:func:`ntfs_attr_find`\  to search for extent records of non-resident
attributes, as extents with lowest_vcn != 0 are usually described by the
attribute list attribute only. - Note that it is possible that the first
extent is only in the attribute list while the last extent is in the base
mft record, so do not rely on being able to find the first extent in the
base mft record.

.. _`ntfs_attr_find.warning`:

Warning
-------

Never use \ ``val``\  when looking for attribute types which can be
non-resident as this most likely will result in a crash!

.. _`load_attribute_list`:

load_attribute_list
===================

.. c:function:: int load_attribute_list(ntfs_volume *vol, runlist *runlist, u8 *al_start, const s64 size, const s64 initialized_size)

    load an attribute list into memory

    :param ntfs_volume \*vol:
        ntfs volume from which to read

    :param runlist \*runlist:
        runlist of the attribute list

    :param u8 \*al_start:
        destination buffer

    :param const s64 size:
        size of the destination buffer in bytes

    :param const s64 initialized_size:
        initialized size of the attribute list

.. _`load_attribute_list.description`:

Description
-----------

Walk the runlist \ ``runlist``\  and load all clusters from it copying them into
the linear buffer \ ``al``\ . The maximum number of bytes copied to \ ``al``\  is \ ``size``\ 
bytes. Note, \ ``size``\  does not need to be a multiple of the cluster size. If
\ ``initialized_size``\  is less than \ ``size``\ , the region in \ ``al``\  between
\ ``initialized_size``\  and \ ``size``\  will be zeroed and not read from disk.

Return 0 on success or -errno on error.

.. _`ntfs_external_attr_find`:

ntfs_external_attr_find
=======================

.. c:function:: int ntfs_external_attr_find(const ATTR_TYPE type, const ntfschar *name, const u32 name_len, const IGNORE_CASE_BOOL ic, const VCN lowest_vcn, const u8 *val, const u32 val_len, ntfs_attr_search_ctx *ctx)

    find an attribute in the attribute list of an inode

    :param const ATTR_TYPE type:
        attribute type to find

    :param const ntfschar \*name:
        attribute name to find (optional, i.e. NULL means don't care)

    :param const u32 name_len:
        attribute name length (only needed if \ ``name``\  present)

    :param const IGNORE_CASE_BOOL ic:
        IGNORE_CASE or CASE_SENSITIVE (ignored if \ ``name``\  not present)

    :param const VCN lowest_vcn:
        lowest vcn to find (optional, non-resident attributes only)

    :param const u8 \*val:
        attribute value to find (optional, resident attributes only)

    :param const u32 val_len:
        attribute value length

    :param ntfs_attr_search_ctx \*ctx:
        search context with mft record and attribute to search from

.. _`ntfs_external_attr_find.description`:

Description
-----------

You should not need to call this function directly.  Use \ :c:func:`ntfs_attr_lookup`\ 
instead.

Find an attribute by searching the attribute list for the corresponding
attribute list entry.  Having found the entry, map the mft record if the
attribute is in a different mft record/inode, \ :c:func:`ntfs_attr_find`\  the attribute
in there and return it.

On first search \ ``ctx``\ ->ntfs_ino must be the base mft record and \ ``ctx``\  must
have been obtained from a call to \ :c:func:`ntfs_attr_get_search_ctx`\ .  On subsequent
calls \ ``ctx``\ ->ntfs_ino can be any extent inode, too (@ctx->base_ntfs_ino is
then the base inode).

After finishing with the attribute/mft record you need to call
\ :c:func:`ntfs_attr_put_search_ctx`\  to cleanup the search context (unmapping any
mapped inodes, etc).

If the attribute is found, \ :c:func:`ntfs_external_attr_find`\  returns 0 and
\ ``ctx``\ ->attr will point to the found attribute.  \ ``ctx``\ ->mrec will point to the
mft record in which \ ``ctx``\ ->attr is located and \ ``ctx``\ ->al_entry will point to
the attribute list entry for the attribute.

If the attribute is not found, \ :c:func:`ntfs_external_attr_find`\  returns -ENOENT and
\ ``ctx``\ ->attr will point to the attribute in the base mft record before which
the attribute being searched for would need to be inserted if such an action
were to be desired.  \ ``ctx``\ ->mrec will point to the mft record in which
\ ``ctx``\ ->attr is located and \ ``ctx``\ ->al_entry will point to the attribute list
entry of the attribute before which the attribute being searched for would
need to be inserted if such an action were to be desired.

Thus to insert the not found attribute, one wants to add the attribute to
\ ``ctx``\ ->mrec (the base mft record) and if there is not enough space, the
attribute should be placed in a newly allocated extent mft record.  The
attribute list entry for the inserted attribute should be inserted in the
attribute list attribute at \ ``ctx``\ ->al_entry.

On actual error, \ :c:func:`ntfs_external_attr_find`\  returns -EIO.  In this case
\ ``ctx``\ ->attr is undefined and in particular do not rely on it not changing.

.. _`ntfs_attr_lookup`:

ntfs_attr_lookup
================

.. c:function:: int ntfs_attr_lookup(const ATTR_TYPE type, const ntfschar *name, const u32 name_len, const IGNORE_CASE_BOOL ic, const VCN lowest_vcn, const u8 *val, const u32 val_len, ntfs_attr_search_ctx *ctx)

    find an attribute in an ntfs inode

    :param const ATTR_TYPE type:
        attribute type to find

    :param const ntfschar \*name:
        attribute name to find (optional, i.e. NULL means don't care)

    :param const u32 name_len:
        attribute name length (only needed if \ ``name``\  present)

    :param const IGNORE_CASE_BOOL ic:
        IGNORE_CASE or CASE_SENSITIVE (ignored if \ ``name``\  not present)

    :param const VCN lowest_vcn:
        lowest vcn to find (optional, non-resident attributes only)

    :param const u8 \*val:
        attribute value to find (optional, resident attributes only)

    :param const u32 val_len:
        attribute value length

    :param ntfs_attr_search_ctx \*ctx:
        search context with mft record and attribute to search from

.. _`ntfs_attr_lookup.description`:

Description
-----------

Find an attribute in an ntfs inode.  On first search \ ``ctx``\ ->ntfs_ino must
be the base mft record and \ ``ctx``\  must have been obtained from a call to
\ :c:func:`ntfs_attr_get_search_ctx`\ .

This function transparently handles attribute lists and \ ``ctx``\  is used to
continue searches where they were left off at.

After finishing with the attribute/mft record you need to call
\ :c:func:`ntfs_attr_put_search_ctx`\  to cleanup the search context (unmapping any
mapped inodes, etc).

Return 0 if the search was successful and -errno if not.

When 0, \ ``ctx``\ ->attr is the found attribute and it is in mft record
\ ``ctx``\ ->mrec.  If an attribute list attribute is present, \ ``ctx``\ ->al_entry is
the attribute list entry of the found attribute.

When -ENOENT, \ ``ctx``\ ->attr is the attribute which collates just after the
attribute being searched for, i.e. if one wants to add the attribute to the
mft record this is the correct place to insert it into.  If an attribute
list attribute is present, \ ``ctx``\ ->al_entry is the attribute list entry which
collates just after the attribute list entry of the attribute being searched
for, i.e. if one wants to add the attribute to the mft record this is the
correct place to insert its attribute list entry into.

When -errno != -ENOENT, an error occurred during the lookup.  \ ``ctx``\ ->attr is
then undefined and in particular you should not rely on it not changing.

.. _`ntfs_attr_init_search_ctx`:

ntfs_attr_init_search_ctx
=========================

.. c:function:: void ntfs_attr_init_search_ctx(ntfs_attr_search_ctx *ctx, ntfs_inode *ni, MFT_RECORD *mrec)

    initialize an attribute search context

    :param ntfs_attr_search_ctx \*ctx:
        attribute search context to initialize

    :param ntfs_inode \*ni:
        ntfs inode with which to initialize the search context

    :param MFT_RECORD \*mrec:
        mft record with which to initialize the search context

.. _`ntfs_attr_init_search_ctx.description`:

Description
-----------

Initialize the attribute search context \ ``ctx``\  with \ ``ni``\  and \ ``mrec``\ .

.. _`ntfs_attr_reinit_search_ctx`:

ntfs_attr_reinit_search_ctx
===========================

.. c:function:: void ntfs_attr_reinit_search_ctx(ntfs_attr_search_ctx *ctx)

    reinitialize an attribute search context

    :param ntfs_attr_search_ctx \*ctx:
        attribute search context to reinitialize

.. _`ntfs_attr_reinit_search_ctx.description`:

Description
-----------

Reinitialize the attribute search context \ ``ctx``\ , unmapping an associated
extent mft record if present, and initialize the search context again.

This is used when a search for a new attribute is being started to reset
the search context to the beginning.

.. _`ntfs_attr_get_search_ctx`:

ntfs_attr_get_search_ctx
========================

.. c:function:: ntfs_attr_search_ctx *ntfs_attr_get_search_ctx(ntfs_inode *ni, MFT_RECORD *mrec)

    allocate/initialize a new attribute search context

    :param ntfs_inode \*ni:
        ntfs inode with which to initialize the search context

    :param MFT_RECORD \*mrec:
        mft record with which to initialize the search context

.. _`ntfs_attr_get_search_ctx.description`:

Description
-----------

Allocate a new attribute search context, initialize it with \ ``ni``\  and \ ``mrec``\ ,
and return it. Return NULL if allocation failed.

.. _`ntfs_attr_put_search_ctx`:

ntfs_attr_put_search_ctx
========================

.. c:function:: void ntfs_attr_put_search_ctx(ntfs_attr_search_ctx *ctx)

    release an attribute search context

    :param ntfs_attr_search_ctx \*ctx:
        attribute search context to free

.. _`ntfs_attr_put_search_ctx.description`:

Description
-----------

Release the attribute search context \ ``ctx``\ , unmapping an associated extent
mft record if present.

.. _`ntfs_attr_find_in_attrdef`:

ntfs_attr_find_in_attrdef
=========================

.. c:function:: ATTR_DEF *ntfs_attr_find_in_attrdef(const ntfs_volume *vol, const ATTR_TYPE type)

    find an attribute in the \ ``$AttrDef``\  system file

    :param const ntfs_volume \*vol:
        ntfs volume to which the attribute belongs

    :param const ATTR_TYPE type:
        attribute type which to find

.. _`ntfs_attr_find_in_attrdef.description`:

Description
-----------

Search for the attribute definition record corresponding to the attribute
\ ``type``\  in the \ ``$AttrDef``\  system file.

Return the attribute type definition record if found and NULL if not found.

.. _`ntfs_attr_size_bounds_check`:

ntfs_attr_size_bounds_check
===========================

.. c:function:: int ntfs_attr_size_bounds_check(const ntfs_volume *vol, const ATTR_TYPE type, const s64 size)

    check a size of an attribute type for validity

    :param const ntfs_volume \*vol:
        ntfs volume to which the attribute belongs

    :param const ATTR_TYPE type:
        attribute type which to check

    :param const s64 size:
        size which to check

.. _`ntfs_attr_size_bounds_check.description`:

Description
-----------

Check whether the \ ``size``\  in bytes is valid for an attribute of \ ``type``\  on the
ntfs volume \ ``vol``\ .  This information is obtained from \ ``$AttrDef``\  system file.

Return 0 if valid, -ERANGE if not valid, or -ENOENT if the attribute is not
listed in \ ``$AttrDef``\ .

.. _`ntfs_attr_can_be_non_resident`:

ntfs_attr_can_be_non_resident
=============================

.. c:function:: int ntfs_attr_can_be_non_resident(const ntfs_volume *vol, const ATTR_TYPE type)

    check if an attribute can be non-resident

    :param const ntfs_volume \*vol:
        ntfs volume to which the attribute belongs

    :param const ATTR_TYPE type:
        attribute type which to check

.. _`ntfs_attr_can_be_non_resident.description`:

Description
-----------

Check whether the attribute of \ ``type``\  on the ntfs volume \ ``vol``\  is allowed to
be non-resident.  This information is obtained from \ ``$AttrDef``\  system file.

Return 0 if the attribute is allowed to be non-resident, -EPERM if not, and
-ENOENT if the attribute is not listed in \ ``$AttrDef``\ .

.. _`ntfs_attr_can_be_resident`:

ntfs_attr_can_be_resident
=========================

.. c:function:: int ntfs_attr_can_be_resident(const ntfs_volume *vol, const ATTR_TYPE type)

    check if an attribute can be resident

    :param const ntfs_volume \*vol:
        ntfs volume to which the attribute belongs

    :param const ATTR_TYPE type:
        attribute type which to check

.. _`ntfs_attr_can_be_resident.description`:

Description
-----------

Check whether the attribute of \ ``type``\  on the ntfs volume \ ``vol``\  is allowed to
be resident.  This information is derived from our ntfs knowledge and may
not be completely accurate, especially when user defined attributes are
present.  Basically we allow everything to be resident except for index
allocation and \ ``$EA``\  attributes.

Return 0 if the attribute is allowed to be non-resident and -EPERM if not.

.. _`ntfs_attr_can_be_resident.warning`:

Warning
-------

In the system file \ ``$MFT``\  the attribute \ ``$Bitmap``\  must be non-resident
otherwise windows will not boot (blue screen of death)!  We cannot
check for this here as we do not know which inode's \ ``$Bitmap``\  is
being asked about so the caller needs to special case this.

.. _`ntfs_attr_record_resize`:

ntfs_attr_record_resize
=======================

.. c:function:: int ntfs_attr_record_resize(MFT_RECORD *m, ATTR_RECORD *a, u32 new_size)

    resize an attribute record

    :param MFT_RECORD \*m:
        mft record containing attribute record

    :param ATTR_RECORD \*a:
        attribute record to resize

    :param u32 new_size:
        new size in bytes to which to resize the attribute record \ ``a``\ 

.. _`ntfs_attr_record_resize.description`:

Description
-----------

Resize the attribute record \ ``a``\ , i.e. the resident part of the attribute, in
the mft record \ ``m``\  to \ ``new_size``\  bytes.

Return 0 on success and -errno on error.  The following error codes are

.. _`ntfs_attr_record_resize.defined`:

defined
-------

-ENOSPC - Not enough space in the mft record \ ``m``\  to perform the resize.

.. _`ntfs_attr_record_resize.note`:

Note
----

On error, no modifications have been performed whatsoever.

.. _`ntfs_attr_record_resize.warning`:

Warning
-------

If you make a record smaller without having copied all the data you
are interested in the data may be overwritten.

.. _`ntfs_resident_attr_value_resize`:

ntfs_resident_attr_value_resize
===============================

.. c:function:: int ntfs_resident_attr_value_resize(MFT_RECORD *m, ATTR_RECORD *a, const u32 new_size)

    resize the value of a resident attribute

    :param MFT_RECORD \*m:
        mft record containing attribute record

    :param ATTR_RECORD \*a:
        attribute record whose value to resize

    :param const u32 new_size:
        new size in bytes to which to resize the attribute value of \ ``a``\ 

.. _`ntfs_resident_attr_value_resize.description`:

Description
-----------

Resize the value of the attribute \ ``a``\  in the mft record \ ``m``\  to \ ``new_size``\  bytes.
If the value is made bigger, the newly allocated space is cleared.

Return 0 on success and -errno on error.  The following error codes are

.. _`ntfs_resident_attr_value_resize.defined`:

defined
-------

-ENOSPC - Not enough space in the mft record \ ``m``\  to perform the resize.

.. _`ntfs_resident_attr_value_resize.note`:

Note
----

On error, no modifications have been performed whatsoever.

.. _`ntfs_resident_attr_value_resize.warning`:

Warning
-------

If you make a record smaller without having copied all the data you
are interested in the data may be overwritten.

.. _`ntfs_attr_make_non_resident`:

ntfs_attr_make_non_resident
===========================

.. c:function:: int ntfs_attr_make_non_resident(ntfs_inode *ni, const u32 data_size)

    convert a resident to a non-resident attribute

    :param ntfs_inode \*ni:
        ntfs inode describing the attribute to convert

    :param const u32 data_size:
        size of the resident data to copy to the non-resident attribute

.. _`ntfs_attr_make_non_resident.description`:

Description
-----------

Convert the resident ntfs attribute described by the ntfs inode \ ``ni``\  to a
non-resident one.

\ ``data_size``\  must be equal to the attribute value size.  This is needed since
we need to know the size before we can map the mft record and our callers
always know it.  The reason we cannot simply read the size from the vfs
inode i_size is that this is not necessarily uptodate.  This happens when
\ :c:func:`ntfs_attr_make_non_resident`\  is called in the ->truncate call path(s).

Return 0 on success and -errno on error.  The following error return codes

.. _`ntfs_attr_make_non_resident.are-defined`:

are defined
-----------

-EPERM  - The attribute is not allowed to be non-resident.
-ENOMEM - Not enough memory.
-ENOSPC - Not enough disk space.
-EINVAL - Attribute not defined on the volume.
-EIO    - I/o error or other error.
Note that -ENOSPC is also returned in the case that there is not enough
space in the mft record to do the conversion.  This can happen when the mft
record is already very full.  The caller is responsible for trying to make
space in the mft record and trying again.  FIXME: Do we need a separate
error return code for this kind of -ENOSPC or is it always worth trying
again in case the attribute may then fit in a resident state so no need to
make it non-resident at all?  Ho-hum...  (AIA)

.. _`ntfs_attr_make_non_resident.note-to-self`:

NOTE to self
------------

No changes in the attribute list are required to move from
a resident to a non-resident attribute.

.. _`ntfs_attr_make_non_resident.locking`:

Locking
-------

- The caller must hold i_mutex on the inode.

.. _`ntfs_attr_extend_allocation`:

ntfs_attr_extend_allocation
===========================

.. c:function:: s64 ntfs_attr_extend_allocation(ntfs_inode *ni, s64 new_alloc_size, const s64 new_data_size, const s64 data_start)

    extend the allocated space of an attribute

    :param ntfs_inode \*ni:
        ntfs inode of the attribute whose allocation to extend

    :param s64 new_alloc_size:
        new size in bytes to which to extend the allocation to

    :param const s64 new_data_size:
        new size in bytes to which to extend the data to

    :param const s64 data_start:
        beginning of region which is required to be non-sparse

.. _`ntfs_attr_extend_allocation.description`:

Description
-----------

Extend the allocated space of an attribute described by the ntfs inode \ ``ni``\ 
to \ ``new_alloc_size``\  bytes.  If \ ``data_start``\  is -1, the whole extension may be
implemented as a hole in the file (as long as both the volume and the ntfs
inode \ ``ni``\  have sparse support enabled).  If \ ``data_start``\  is >= 0, then the
region between the old allocated size and \ ``data_start``\  - 1 may be made sparse
but the regions between \ ``data_start``\  and \ ``new_alloc_size``\  must be backed by
actual clusters.

If \ ``new_data_size``\  is -1, it is ignored.  If it is >= 0, then the data size
of the attribute is extended to \ ``new_data_size``\ .  Note that the i_size of the
vfs inode is not updated.  Only the data size in the base attribute record
is updated.  The caller has to update i_size separately if this is required.

.. _`ntfs_attr_extend_allocation.warning`:

WARNING
-------

It is a \ :c:func:`BUG`\  for \ ``new_data_size``\  to be smaller than the old data
size as well as for \ ``new_data_size``\  to be greater than \ ``new_alloc_size``\ .

For resident attributes this involves resizing the attribute record and if
necessary moving it and/or other attributes into extent mft records and/or
converting the attribute to a non-resident attribute which in turn involves
extending the allocation of a non-resident attribute as described below.

For non-resident attributes this involves allocating clusters in the data
zone on the volume (except for regions that are being made sparse) and
extending the run list to describe the allocated clusters as well as
updating the mapping pairs array of the attribute.  This in turn involves
resizing the attribute record and if necessary moving it and/or other
attributes into extent mft records and/or splitting the attribute record
into multiple extent attribute records.

Also, the attribute list attribute is updated if present and in some of the
above cases (the ones where extent mft records/attributes come into play),
an attribute list attribute is created if not already present.

Return the new allocated size on success and -errno on error.  In the case
that an error is encountered but a partial extension at least up to
\ ``data_start``\  (if present) is possible, the allocation is partially extended
and this is returned.  This means the caller must check the returned size to
determine if the extension was partial.  If \ ``data_start``\  is -1 then partial
allocations are not performed.

Do not call \ :c:func:`ntfs_attr_extend_allocation`\  for \ ``$MFT``\ /$DATA.

.. _`ntfs_attr_extend_allocation.locking`:

Locking
-------

This function takes the runlist lock of \ ``ni``\  for writing as well as
locking the mft record of the base ntfs inode.  These locks are maintained
throughout execution of the function.  These locks are required so that the
attribute can be resized safely and so that it can for example be converted
from resident to non-resident safely.

.. _`ntfs_attr_extend_allocation.todo`:

TODO
----

At present attribute list attribute handling is not implemented.

At present it is not safe to call this function for anything other
than the \ ``$DATA``\  attribute(s) of an uncompressed and unencrypted file.

.. _`ntfs_attr_set`:

ntfs_attr_set
=============

.. c:function:: int ntfs_attr_set(ntfs_inode *ni, const s64 ofs, const s64 cnt, const u8 val)

    fill (a part of) an attribute with a byte

    :param ntfs_inode \*ni:
        ntfs inode describing the attribute to fill

    :param const s64 ofs:
        offset inside the attribute at which to start to fill

    :param const s64 cnt:
        number of bytes to fill

    :param const u8 val:
        the unsigned 8-bit value with which to fill the attribute

.. _`ntfs_attr_set.description`:

Description
-----------

Fill \ ``cnt``\  bytes of the attribute described by the ntfs inode \ ``ni``\  starting at
byte offset \ ``ofs``\  inside the attribute with the constant byte \ ``val``\ .

This function is effectively like \ :c:func:`memset`\  applied to an ntfs attribute.
Note thie function actually only operates on the page cache pages belonging
to the ntfs attribute and it marks them dirty after doing the \ :c:func:`memset`\ .
Thus it relies on the vm dirty page write code paths to cause the modified
pages to be written to the mft record/disk.

Return 0 on success and -errno on error.  An error code of -ESPIPE means
that \ ``ofs``\  + \ ``cnt``\  were outside the end of the attribute and no write was
performed.

.. This file was automatic generated / don't edit.

