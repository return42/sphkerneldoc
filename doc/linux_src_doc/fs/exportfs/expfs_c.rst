.. -*- coding: utf-8; mode: rst -*-

=======
expfs.c
=======


.. _`get_name`:

get_name
========

.. c:function:: int get_name (const struct path *path, char *name, struct dentry *child)

    default export_operations->get_name function

    :param const struct path \*path:
        the directory in which to find a name

    :param char \*name:
        a pointer to a ``NAME_MAX``\ +1 char buffer to store the name

    :param struct dentry \*child:
        the dentry for the child directory.



.. _`get_name.description`:

Description
-----------

calls readdir on the parent until it finds an entry with
the same inode number as the child, and returns that.



.. _`export_encode_fh`:

export_encode_fh
================

.. c:function:: int export_encode_fh (struct inode *inode, struct fid *fid, int *max_len, struct inode *parent)

    default export_operations->encode_fh function

    :param struct inode \*inode:
        the object to encode

    :param struct fid \*fid:
        where to store the file handle fragment

    :param int \*max_len:
        maximum length to store there

    :param struct inode \*parent:
        parent directory inode, if wanted



.. _`export_encode_fh.description`:

Description
-----------

This default encode_fh function assumes that the 32 inode number
is suitable for locating an inode, and that the generation number
can be used to check that it is still valid.  It places them in the
filehandle fragment where export_decode_fh expects to find them.

