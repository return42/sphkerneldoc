.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/quota.c

.. _`gfs2_qa_alloc`:

gfs2_qa_alloc
=============

.. c:function:: int gfs2_qa_alloc(struct gfs2_inode *ip)

    make sure we have a quota allocations data structure, if necessary

    :param ip:
        the inode for this reservation
    :type ip: struct gfs2_inode \*

.. _`gfs2_adjust_quota`:

gfs2_adjust_quota
=================

.. c:function:: int gfs2_adjust_quota(struct gfs2_inode *ip, loff_t loc, s64 change, struct gfs2_quota_data *qd, struct qc_dqblk *fdq)

    adjust record of current block usage

    :param ip:
        The quota inode
    :type ip: struct gfs2_inode \*

    :param loc:
        Offset of the entry in the quota file
    :type loc: loff_t

    :param change:
        The amount of usage change to record
    :type change: s64

    :param qd:
        The quota data
    :type qd: struct gfs2_quota_data \*

    :param fdq:
        The updated limits to record
    :type fdq: struct qc_dqblk \*

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

    :param ip:
        The inode for which this check is being performed
    :type ip: struct gfs2_inode \*

    :param uid:
        The uid to check against
    :type uid: kuid_t

    :param gid:
        The gid to check against
    :type gid: kgid_t

    :param ap:
        The allocation parameters. ap->target contains the requested
        blocks. ap->min_target, if set, contains the minimum blks
        requested.
    :type ap: struct gfs2_alloc_parms \*

.. _`gfs2_quota_check.return`:

Return
------

0 on success.
min_req = ap->min_target ? ap->min_target : ap->target;
quota must allow at least min_req blks for success and
ap->allowed is set to the number of blocks allowed

-EDQUOT otherwise, quota violation. ap->allowed is set to number
of blocks available.

.. _`gfs2_quotad`:

gfs2_quotad
===========

.. c:function:: int gfs2_quotad(void *data)

    Write cached quota changes into the quota file

    :param data:
        *undescribed*
    :type data: void \*

.. This file was automatic generated / don't edit.

