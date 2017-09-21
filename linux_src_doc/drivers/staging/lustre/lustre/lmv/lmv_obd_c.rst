.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lmv/lmv_obd.c

.. _`lmv_set_mdc_active`:

lmv_set_mdc_active
==================

.. c:function:: int lmv_set_mdc_active(struct lmv_obd *lmv, const struct obd_uuid *uuid, int activate)

    :param struct lmv_obd \*lmv:
        *undescribed*

    :param const struct obd_uuid \*uuid:
        *undescribed*

    :param int activate:
        *undescribed*

.. _`lmv_set_mdc_active.description`:

Description
-----------

-EINVAL  : UUID can't be found in the LMV's target list
-ENOTCONN: The UUID is found, but the target connection is bad (!)
-EBADF   : The UUID is found, but the OBD of the wrong type (!)

.. _`lmv_placement_policy`:

lmv_placement_policy
====================

.. c:function:: int lmv_placement_policy(struct obd_device *obd, struct md_op_data *op_data, u32 *mds)

    :param struct obd_device \*obd:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param u32 \*mds:
        *undescribed*

.. _`lmv_locate_target_for_name`:

lmv_locate_target_for_name
==========================

.. c:function:: struct lmv_tgt_desc *lmv_locate_target_for_name(struct lmv_obd *lmv, struct lmv_stripe_md *lsm, const char *name, int namelen, struct lu_fid *fid, u32 *mds)

    For non-striped directory, it will locate MDT by fid. For striped-directory, it will locate MDT by name. And also it will reset op_fid1 with the FID of the chosen stripe.

    :param struct lmv_obd \*lmv:
        *undescribed*

    :param struct lmv_stripe_md \*lsm:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param int namelen:
        *undescribed*

    :param struct lu_fid \*fid:
        *undescribed*

    :param u32 \*mds:
        *undescribed*

.. _`lmv_locate_mds`:

lmv_locate_mds
==============

.. c:function:: struct lmv_tgt_desc*lmv_locate_mds(struct lmv_obd *lmv, struct md_op_data *op_data, struct lu_fid *fid)

    :param struct lmv_obd \*lmv:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param struct lu_fid \*fid:
        *undescribed*

.. _`lmv_locate_mds.description`:

Description
-----------

For striped directory (lsm != NULL), it will locate the stripe
by name hash (see \ :c:func:`lsm_name_to_stripe_info`\ ). Note: if the hash_type
is unknown, it will return -EBADFD, and lmv_intent_lookup might need
walk through all of stripes to locate the entry.

For normal direcotry, it will locate MDS by FID directly.
\param[in] lmv       LMV device
\param[in] op_data   client MD stack parameters, name, namelen
mds_num etc.
\param[in] fid       object FID used to locate MDS.

retval               pointer to the lmv_tgt_desc if succeed.
ERR_PTR(errno) if failed.

.. _`lmv_get_min_striped_entry`:

lmv_get_min_striped_entry
=========================

.. c:function:: int lmv_get_min_striped_entry(struct obd_export *exp, struct md_op_data *op_data, struct md_callback *cb_op, __u64 hash_offset, int *stripe_offset, struct lu_dirent **entp, struct page **ppage)

    :param struct obd_export \*exp:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param struct md_callback \*cb_op:
        *undescribed*

    :param __u64 hash_offset:
        *undescribed*

    :param int \*stripe_offset:
        *undescribed*

    :param struct lu_dirent \*\*entp:
        *undescribed*

    :param struct page \*\*ppage:
        *undescribed*

.. _`lmv_get_min_striped_entry.description`:

Description
-----------

This function will search the dir entry, whose hash value is the
closest(>=) to \ ``hash_offset``\ , from all of sub-stripes, and it is
only being called for striped directory.

\param[in] exp               export of LMV
\param[in] op_data           parameters transferred beween client MD stack
stripe_information will be included in this
parameter
\param[in] cb_op             ldlm callback being used in enqueue in
mdc_read_page
\param[in] hash_offset       the hash value, which is used to locate
minum(closet) dir entry
\param[in\|out] stripe_offset the caller use this to indicate the stripe
index of last entry, so to avoid hash conflict
between stripes. It will also be used to
return the stripe index of current dir entry.
\param[in\|out] entp          the minum entry and it also is being used
to input the last dir entry to resolve the
hash conflict

\param[out] ppage            the page which holds the minum entry

\retval                      = 0 get the entry successfully
negative errno (< 0) does not get the entry

.. _`lmv_read_striped_page`:

lmv_read_striped_page
=====================

.. c:function:: int lmv_read_striped_page(struct obd_export *exp, struct md_op_data *op_data, struct md_callback *cb_op, __u64 offset, struct page **ppage)

    :param struct obd_export \*exp:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param struct md_callback \*cb_op:
        *undescribed*

    :param __u64 offset:
        *undescribed*

    :param struct page \*\*ppage:
        *undescribed*

.. _`lmv_read_striped_page.description`:

Description
-----------

This function gets one entry by \ ``offset``\  from a striped directory. It will
read entries from all of stripes, and choose one closest to the required
offset(&offset). A few notes
1. skip . and .. for non-zero stripes, because there can only have one .
and .. in a directory.
2. op_data will be shared by all of stripes, instead of allocating new
one, so need to restore before reusing.
3. release the entry page if that is not being chosen.

\param[in] exp       obd export refer to LMV
\param[in] op_data   hold those MD parameters of read_entry
\param[in] cb_op     ldlm callback being used in enqueue in mdc_read_entry
\param[out] ldp      the entry being read
\param[out] ppage    the page holding the entry. Note: because the entry
will be accessed in upper layer, so we need hold the
page until the usages of entry is finished, see
ll_dir_entry_next.

retval               =0 if get entry successfully
<0 cannot get entry

.. _`lmv_unlink`:

lmv_unlink
==========

.. c:function:: int lmv_unlink(struct obd_export *exp, struct md_op_data *op_data, struct ptlrpc_request **request)

    :param struct obd_export \*exp:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param struct ptlrpc_request \*\*request:
        *undescribed*

.. _`lmv_unlink.description`:

Description
-----------

Unlink a file or directory under the parent dir. The unlink request
usually will be sent to the MDT where the child is located, but if
the client does not have the child FID then request will be sent to the
MDT where the parent is located.

If the parent is a striped directory then it also needs to locate which
stripe the name of the child is located, and replace the parent FID
(@op->op_fid1) with the stripe FID. Note: if the stripe is unknown,
it will walk through all of sub-stripes until the child is being
unlinked finally.

\param[in] exp       export refer to LMV
\param[in] op_data   different parameters transferred beween client
MD stacks, name, namelen, FIDs etc.
op_fid1 is the parent FID, op_fid2 is the child
FID.
\param[out] request point to the request of unlink.

retval               0 if succeed
negative errno if failed.

.. _`lmv_get_info`:

lmv_get_info
============

.. c:function:: int lmv_get_info(const struct lu_env *env, struct obd_export *exp, __u32 keylen, void *key, __u32 *vallen, void *val)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct obd_export \*exp:
        *undescribed*

    :param __u32 keylen:
        *undescribed*

    :param void \*key:
        *undescribed*

    :param __u32 \*vallen:
        *undescribed*

    :param void \*val:
        *undescribed*

.. _`lmv_get_info.description`:

Description
-----------

Dispatch request to lower-layer devices as needed.

\param[in]  env      execution environment for this thread
\param[in]  exp      export for the LMV device
\param[in]  keylen   length of key identifier
\param[in]  key      identifier of key to get value for
\param[in]  vallen   size of \a val
\param[out] val      pointer to storage location for value

\retval 0            on success
\retval negative     negated errno on failure

.. _`lmv_set_info_async`:

lmv_set_info_async
==================

.. c:function:: int lmv_set_info_async(const struct lu_env *env, struct obd_export *exp, u32 keylen, void *key, u32 vallen, void *val, struct ptlrpc_request_set *set)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct obd_export \*exp:
        *undescribed*

    :param u32 keylen:
        *undescribed*

    :param void \*key:
        *undescribed*

    :param u32 vallen:
        *undescribed*

    :param void \*val:
        *undescribed*

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`lmv_set_info_async.description`:

Description
-----------

Dispatch request to lower-layer devices as needed.

\param[in] env       execution environment for this thread
\param[in] exp       export for the LMV device
\param[in] keylen    length of key identifier
\param[in] key       identifier of key to store value for
\param[in] vallen    size of value to store
\param[in] val       pointer to data to be stored
\param[in] set       optional list of related ptlrpc requests

\retval 0            on success
\retval negative     negated errno on failure

.. _`lmv_quotactl`:

lmv_quotactl
============

.. c:function:: int lmv_quotactl(struct obd_device *unused, struct obd_export *exp, struct obd_quotactl *oqctl)

    process with other slave MDTs. The only exception is Q_GETOQUOTA for which we directly fetch data from the slave MDTs.

    :param struct obd_device \*unused:
        *undescribed*

    :param struct obd_export \*exp:
        *undescribed*

    :param struct obd_quotactl \*oqctl:
        *undescribed*

.. This file was automatic generated / don't edit.

