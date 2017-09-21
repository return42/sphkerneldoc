.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/glops.c

.. _`__gfs2_ail_flush`:

__gfs2_ail_flush
================

.. c:function:: void __gfs2_ail_flush(struct gfs2_glock *gl, bool fsync, unsigned int nr_revokes)

    remove all buffers for a given lock from the AIL

    :param struct gfs2_glock \*gl:
        the glock

    :param bool fsync:
        set when called from fsync (not all buffers will be clean)

    :param unsigned int nr_revokes:
        *undescribed*

.. _`__gfs2_ail_flush.description`:

Description
-----------

None of the buffers should be dirty, locked, or pinned.

.. _`rgrp_go_sync`:

rgrp_go_sync
============

.. c:function:: void rgrp_go_sync(struct gfs2_glock *gl)

    sync out the metadata for this glock

    :param struct gfs2_glock \*gl:
        the glock

.. _`rgrp_go_sync.description`:

Description
-----------

Called when demoting or unlocking an EX glock.  We must flush
to disk all dirty buffers/pages relating to this glock, and must not
return to caller to demote/unlock the glock until I/O is complete.

.. _`rgrp_go_inval`:

rgrp_go_inval
=============

.. c:function:: void rgrp_go_inval(struct gfs2_glock *gl, int flags)

    invalidate the metadata for this glock

    :param struct gfs2_glock \*gl:
        the glock

    :param int flags:
        *undescribed*

.. _`rgrp_go_inval.description`:

Description
-----------

We never used LM_ST_DEFERRED with resource groups, so that we
should always see the metadata flag set here.

.. _`inode_go_sync`:

inode_go_sync
=============

.. c:function:: void inode_go_sync(struct gfs2_glock *gl)

    Sync the dirty data and/or metadata for an inode glock

    :param struct gfs2_glock \*gl:
        the glock protecting the inode

.. _`inode_go_inval`:

inode_go_inval
==============

.. c:function:: void inode_go_inval(struct gfs2_glock *gl, int flags)

    prepare a inode glock to be released

    :param struct gfs2_glock \*gl:
        the glock

    :param int flags:
        *undescribed*

.. _`inode_go_inval.description`:

Description
-----------

Normally we invalidate everything, but if we are moving into
LM_ST_DEFERRED from LM_ST_SHARED or LM_ST_EXCLUSIVE then we
can keep hold of the metadata, since it won't have changed.

.. _`inode_go_demote_ok`:

inode_go_demote_ok
==================

.. c:function:: int inode_go_demote_ok(const struct gfs2_glock *gl)

    Check to see if it's ok to unlock an inode glock

    :param const struct gfs2_glock \*gl:
        the glock

.. _`inode_go_demote_ok.return`:

Return
------

1 if it's ok

.. _`gfs2_inode_refresh`:

gfs2_inode_refresh
==================

.. c:function:: int gfs2_inode_refresh(struct gfs2_inode *ip)

    Refresh the incore copy of the dinode

    :param struct gfs2_inode \*ip:
        The GFS2 inode

.. _`gfs2_inode_refresh.return`:

Return
------

errno

.. _`inode_go_lock`:

inode_go_lock
=============

.. c:function:: int inode_go_lock(struct gfs2_holder *gh)

    operation done after an inode lock is locked by a process

    :param struct gfs2_holder \*gh:
        *undescribed*

.. _`inode_go_lock.return`:

Return
------

errno

.. _`inode_go_dump`:

inode_go_dump
=============

.. c:function:: void inode_go_dump(struct seq_file *seq, const struct gfs2_glock *gl)

    print information about an inode

    :param struct seq_file \*seq:
        The iterator

    :param const struct gfs2_glock \*gl:
        *undescribed*

.. _`freeze_go_sync`:

freeze_go_sync
==============

.. c:function:: void freeze_go_sync(struct gfs2_glock *gl)

    promote/demote the freeze glock

    :param struct gfs2_glock \*gl:
        the glock

.. _`freeze_go_xmote_bh`:

freeze_go_xmote_bh
==================

.. c:function:: int freeze_go_xmote_bh(struct gfs2_glock *gl, struct gfs2_holder *gh)

    After promoting/demoting the freeze glock

    :param struct gfs2_glock \*gl:
        the glock

    :param struct gfs2_holder \*gh:
        *undescribed*

.. _`freeze_go_demote_ok`:

freeze_go_demote_ok
===================

.. c:function:: int freeze_go_demote_ok(const struct gfs2_glock *gl)

    :param const struct gfs2_glock \*gl:
        the glock

.. _`freeze_go_demote_ok.description`:

Description
-----------

Always returns 0

.. _`iopen_go_callback`:

iopen_go_callback
=================

.. c:function:: void iopen_go_callback(struct gfs2_glock *gl, bool remote)

    schedule the dcache entry for the inode to be deleted

    :param struct gfs2_glock \*gl:
        the glock

    :param bool remote:
        *undescribed*

.. _`iopen_go_callback.description`:

Description
-----------

gl_lockref.lock lock is held while calling this

.. This file was automatic generated / don't edit.

