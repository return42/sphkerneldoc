.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre/lustre_idl.h

.. _`fid_seq_is_igif`:

fid_seq_is_igif
===============

.. c:function:: bool fid_seq_is_igif(__u64 seq)

    \param fid the fid to be tested. \return true if the fid is a igif; otherwise false.

    :param __u64 seq:
        *undescribed*

.. _`fid_seq_is_idif`:

fid_seq_is_idif
===============

.. c:function:: bool fid_seq_is_idif(__u64 seq)

    \param fid the fid to be tested. \return true if the fid is a idif; otherwise false.

    :param __u64 seq:
        *undescribed*

.. _`ostid_set_id`:

ostid_set_id
============

.. c:function:: void ostid_set_id(struct ost_id *oi, __u64 oid)

    we need check oi_seq to decide where to set oi_id, so oi_seq should always be set ahead of oi_id.

    :param struct ost_id \*oi:
        *undescribed*

    :param __u64 oid:
        *undescribed*

.. _`ostid_to_fid`:

ostid_to_fid
============

.. c:function:: int ostid_to_fid(struct lu_fid *fid, struct ost_id *ostid, __u32 ost_idx)

    converting all obdo, lmm, lsm, etc. 64-bit id/seq pairs into proper FIDs.  Note that if an id/seq is already in FID/IDIF format it will be passed through unchanged.  Only legacy OST objects in "group 0" will be mapped into the IDIF namespace so that they can fit into the struct lu_fid fields without loss.  For reference see: http://wiki.old.lustre.org/index.php/Architecture_-_Interoperability_fids_zfs

    :param struct lu_fid \*fid:
        *undescribed*

    :param struct ost_id \*ostid:
        *undescribed*

    :param __u32 ost_idx:
        *undescribed*

.. _`lu_igif_ino`:

lu_igif_ino
===========

.. c:function:: ino_t lu_igif_ino(const struct lu_fid *fid)

    \param fid a igif to get inode number from. \return inode number for the igif.

    :param const struct lu_fid \*fid:
        *undescribed*

.. _`lu_igif_gen`:

lu_igif_gen
===========

.. c:function:: __u32 lu_igif_gen(const struct lu_fid *fid)

    \param fid a igif to get inode generation from. \return inode generation for the igif.

    :param const struct lu_fid \*fid:
        *undescribed*

.. _`lu_igif_build`:

lu_igif_build
=============

.. c:function:: void lu_igif_build(struct lu_fid *fid, __u32 ino, __u32 gen)

    :param struct lu_fid \*fid:
        *undescribed*

    :param __u32 ino:
        *undescribed*

    :param __u32 gen:
        *undescribed*

.. _`lu_page_shift`:

LU_PAGE_SHIFT
=============

.. c:function::  LU_PAGE_SHIFT()

.. _`lu_page_shift.description`:

Description
-----------

This is the directory page size packed in MDS_READPAGE RPC.
It's different than PAGE_SIZE because the client needs to
access the struct lu_dirpage header packed at the beginning of
the "page" and without this there isn't any way to know find the
lu_dirpage header is if client and server PAGE_SIZE differ.

.. _`fid_to_lmm_oi`:

fid_to_lmm_oi
=============

.. c:function:: void fid_to_lmm_oi(const struct lu_fid *fid, struct ost_id *oi)

    2.4 uses struct lov_mds_md_v1 { ........ \__u64 lmm_object_id; \__u64 lmm_object_seq; ...... } to identify the LOV(MDT) object, and lmm_object_seq will be normal_fid, which make it hard to combine these conversion to ostid_to FID. so we will do lmm_oi/fid conversion separately

    :param const struct lu_fid \*fid:
        *undescribed*

    :param struct ost_id \*oi:
        *undescribed*

.. _`fid_to_lmm_oi.description`:

Description
-----------

We can tell the lmm_oi by this way,
1.8: lmm_object_id = {inode}, lmm_object_gr = 0
2.1: lmm_object_id = {oid < 128k}, lmm_object_seq = FID_SEQ_NORMAL
2.4: lmm_oi.f_seq = FID_SEQ_NORMAL, lmm_oi.f_oid = {oid < 128k},
lmm_oi.f_ver = 0

But currently lmm_oi/lsm_oi does not have any "real" usages,
except for printing some information, and the user can always
get the real FID from LMA, besides this multiple case check might
make swab more complicate. So we will keep using id/seq for lmm_oi.

.. _`lustre_fnv_1a_64_prime`:

LUSTRE_FNV_1A_64_PRIME
======================

.. c:function::  LUSTRE_FNV_1A_64_PRIME()

    1a hash algorithm is as follows: hash = FNV_offset_basis for each octet_of_data to be hashed hash = hash XOR octet_of_data hash = hash × FNV_prime return hash http://en.wikipedia.org/wiki/Fowler–Noll–Vo_hash_function#FNV-1a_hash

.. _`lustre_fnv_1a_64_prime.description`:

Description
-----------

http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-reference-source
FNV_prime is 2^40 + 2^8 + 0xb3 = 0x100000001b3ULL

.. This file was automatic generated / don't edit.

