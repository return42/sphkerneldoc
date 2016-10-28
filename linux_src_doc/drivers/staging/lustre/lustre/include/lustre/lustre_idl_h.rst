.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre/lustre_idl.h

.. _`fld_range_is_any`:

fld_range_is_any
================

.. c:function:: unsigned fld_range_is_any(const struct lu_seq_range *range)

    but it does not know whether the seq is MDT or OST, so it will send req with ALL type, which means either seq type gotten from lookup can be expected.

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`range_space`:

range_space
===========

.. c:function:: __u64 range_space(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`range_init`:

range_init
==========

.. c:function:: void range_init(struct lu_seq_range *range)

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`range_within`:

range_within
============

.. c:function:: int range_within(const struct lu_seq_range *range, __u64 s)

    :param const struct lu_seq_range \*range:
        *undescribed*

    :param __u64 s:
        *undescribed*

.. _`fid_seq_is_igif`:

fid_seq_is_igif
===============

.. c:function:: int fid_seq_is_igif(const __u64 seq)

    \param fid the fid to be tested. \return true if the fid is a igif; otherwise false.

    :param const __u64 seq:
        *undescribed*

.. _`fid_seq_is_idif`:

fid_seq_is_idif
===============

.. c:function:: int fid_seq_is_idif(const __u64 seq)

    \param fid the fid to be tested. \return true if the fid is a idif; otherwise false.

    :param const __u64 seq:
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

    converting all obdo, lmm, lsm, etc. 64-bit id/seq pairs into proper FIDs.  Note that if an id/seq is already in FID/IDIF format it will be passed through unchanged.  Only legacy OST objects in "group 0" will be mapped into the IDIF namespace so that they can fit into the struct lu_fid fields without loss.  For reference see: http://arch.lustre.org/index.php?title=Interoperability_fids_zfs

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

.. This file was automatic generated / don't edit.

