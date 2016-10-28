.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/udf/namei.c

.. _`udf_find_entry`:

udf_find_entry
==============

.. c:function:: struct fileIdentDesc *udf_find_entry(struct inode *dir, const struct qstr *child, struct udf_fileident_bh *fibh, struct fileIdentDesc *cfi)

    find entry in given directory.

    :param struct inode \*dir:
        directory inode to search in

    :param const struct qstr \*child:
        qstr of the name

    :param struct udf_fileident_bh \*fibh:
        buffer head / inode with file identifier descriptor we found

    :param struct fileIdentDesc \*cfi:
        found file identifier descriptor with given name

.. _`udf_find_entry.description`:

Description
-----------

This function searches in the directory \ ``dir``\  for a file name \ ``child``\ . When
found, \ ``fibh``\  points to the buffer head(s) (bh is NULL for in ICB
directories) containing the file identifier descriptor (FID). In that case
the function returns pointer to the FID in the buffer or inode - but note
that FID may be split among two buffers (blocks) so accessing it via that
pointer isn't easily possible. This pointer can be used only as an iterator
for other directory manipulation functions. For inspection of the FID \ ``cfi``\ 
can be used - the found FID is copied there.

Returns pointer to FID, NULL when nothing found, or error code.

.. This file was automatic generated / don't edit.

