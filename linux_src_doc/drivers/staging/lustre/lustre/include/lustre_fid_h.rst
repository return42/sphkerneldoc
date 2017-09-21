.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre_fid.h

.. _`ostid_build_res_name`:

ostid_build_res_name
====================

.. c:function:: void ostid_build_res_name(const struct ost_id *oi, struct ldlm_res_id *name)

    finally, when we replace ost_id with FID in data stack.

    :param const struct ost_id \*oi:
        *undescribed*

    :param struct ldlm_res_id \*name:
        *undescribed*

.. _`ostid_build_res_name.description`:

Description
-----------

Currently, resid from the old client, whose res[0] = object_id,
res[1] = object_seq, is just opposite with Metatdata
resid, where, res[0] = fid->f_seq, res[1] = fid->f_oid.
To unify the resid identification, we will reverse the data
resid to keep it same with Metadata resid, i.e.

For resid from the old client,
res[0] = objid,  res[1] = 0, still keep the original order,
for compatibility.

For new resid
res will be built from normal FID directly, i.e. res[0] = f_seq,
res[1] = f_oid + f_ver.

.. _`ostid_res_name_eq`:

ostid_res_name_eq
=================

.. c:function:: int ostid_res_name_eq(const struct ost_id *oi, const struct ldlm_res_id *name)

    :param const struct ost_id \*oi:
        *undescribed*

    :param const struct ldlm_res_id \*name:
        *undescribed*

.. _`ostid_set_id`:

ostid_set_id
============

.. c:function:: int ostid_set_id(struct ost_id *oi, __u64 oid)

    we need check oi_seq to decide where to set oi_id, so oi_seq should always be set ahead of oi_id.

    :param struct ost_id \*oi:
        *undescribed*

    :param __u64 oid:
        *undescribed*

.. _`fid_flatten`:

fid_flatten
===========

.. c:function:: __u64 fid_flatten(const struct lu_fid *fid)

    bit FID values into a 64-bit value for use as an inode number. For non-IGIF FIDs this starts just over 2^32, and continues without conflict until 2^64, at which point we wrap the high 24 bits of the SEQ into the range where there may not be many OID values in use, to minimize the risk of conflict.

    :param const struct lu_fid \*fid:
        *undescribed*

.. _`fid_flatten.description`:

Description
-----------

Suppose LUSTRE_SEQ_MAX_WIDTH less than (1 << 24) which is currently true,
the time between re-used inode numbers is very long - 2^40 SEQ numbers,
or about 2^40 client mounts, if clients create less than 2^24 files/mount.

.. _`fid_flatten32`:

fid_flatten32
=============

.. c:function:: __u32 fid_flatten32(const struct lu_fid *fid)

    :param const struct lu_fid \*fid:
        *undescribed*

.. This file was automatic generated / don't edit.

