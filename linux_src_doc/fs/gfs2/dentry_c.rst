.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/dentry.c

.. _`gfs2_drevalidate`:

gfs2_drevalidate
================

.. c:function:: int gfs2_drevalidate(struct dentry *dentry, unsigned int flags)

    Check directory lookup consistency

    :param struct dentry \*dentry:
        the mapping to check

    :param unsigned int flags:
        lookup flags

.. _`gfs2_drevalidate.description`:

Description
-----------

Check to make sure the lookup necessary to arrive at this inode from its
parent is still good.

.. _`gfs2_drevalidate.return`:

Return
------

1 if the dentry is ok, 0 if it isn't

.. This file was automatic generated / don't edit.

