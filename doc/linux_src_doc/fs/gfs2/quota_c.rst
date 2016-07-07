.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/quota.c

.. _`gfs2_qa_alloc`:

gfs2_qa_alloc
=============

.. c:function:: int gfs2_qa_alloc(struct gfs2_inode *ip)

    make sure we have a quota allocations data structure, if necessary

    :param struct gfs2_inode \*ip:
        the inode for this reservation

.. _`gfs2_adjust_quota`:

gfs2_adjust_quota
=================

.. c:function:: int gfs2_adjust_quota(struct gfs2_inode *ip, loff_t loc, s64 change, struct gfs2_quota_data *qd, struct qc_dqblk *fdq)

    adjust record of current block usage

    :param struct gfs2_inode \*ip:
        The quota inode

    :param loff_t loc:
        Offset of the entry in the quota file

    :param s64 change:
        The amount of usage change to record

    :param struct gfs2_quota_data \*qd:
        The quota data

    :param struct qc_dqblk \*fdq:
        The updated limits to record

.. _`gfs2_adjust_quota.description`:

Description
-----------

This function was mostly borrowed from gfs2_block_truncate_page which was
in turn mostly borrowed from ext3

.. _`gfs2_adjust_quota.return`:

Return
------

0 or -ve on error

.. _`gfs2_quota_check`:

gfs2_quota_check
================

.. c:function:: int gfs2_quota_check(struct gfs2_inode *ip, kuid_t uid, kgid_t gid, struct gfs2_alloc_parms *ap)

    check if allocating new blocks will exceed quota

    :param struct gfs2_inode \*ip:
        The inode for which this check is being performed

    :param kuid_t uid:
        The uid to check against

    :param kgid_t gid:
        The gid to check against

    :param struct gfs2_alloc_parms \*ap:
        The allocation parameters. ap->target contains the requested
        blocks. ap->min_target, if set, contains the minimum blks
        requested.

.. _`gfs2_quota_check.return`:

Return
------

0 on success.
min_req = ap->min_target ? ap->min_target : ap->target;
quota must allow atleast min_req blks for success and
ap->allowed is set to the number of blocks allowed

-EDQUOT otherwise, quota violation. ap->allowed is set to number
of blocks available.

.. _`gfs2_quotad`:

gfs2_quotad
===========

.. c:function:: int gfs2_quotad(void *data)

    Write cached quota changes into the quota file

    :param void \*data:
        *undescribed*

.. This file was automatic generated / don't edit.

