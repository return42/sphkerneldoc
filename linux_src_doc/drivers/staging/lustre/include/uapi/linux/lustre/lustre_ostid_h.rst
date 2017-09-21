.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/uapi/linux/lustre/lustre_ostid.h

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

.. _`ostid_to_fid`:

ostid_to_fid
============

.. c:function:: int ostid_to_fid(struct lu_fid *fid, const struct ost_id *ostid, __u32 ost_idx)

    converting all obdo, lmm, lsm, etc. 64-bit id/seq pairs into proper FIDs.  Note that if an id/seq is already in FID/IDIF format it will be passed through unchanged.  Only legacy OST objects in "group 0" will be mapped into the IDIF namespace so that they can fit into the struct lu_fid fields without loss.

    :param struct lu_fid \*fid:
        *undescribed*

    :param const struct ost_id \*ostid:
        *undescribed*

    :param __u32 ost_idx:
        *undescribed*

.. This file was automatic generated / don't edit.

