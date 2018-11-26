.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/exportfs/expfs.c

.. _`get_name`:

get_name
========

.. c:function:: int get_name(const struct path *path, char *name, struct dentry *child)

    default export_operations->get_name function

    :param path:
        the directory in which to find a name
    :type path: const struct path \*

    :param name:
        a pointer to a \ ``NAME_MAX``\ +1 char buffer to store the name
    :type name: char \*

    :param child:
        the dentry for the child directory.
    :type child: struct dentry \*

.. _`get_name.description`:

Description
-----------

calls readdir on the parent until it finds an entry with
the same inode number as the child, and returns that.

.. _`export_encode_fh`:

export_encode_fh
================

.. c:function:: int export_encode_fh(struct inode *inode, struct fid *fid, int *max_len, struct inode *parent)

    default export_operations->encode_fh function

    :param inode:
        the object to encode
    :type inode: struct inode \*

    :param fid:
        where to store the file handle fragment
    :type fid: struct fid \*

    :param max_len:
        maximum length to store there
    :type max_len: int \*

    :param parent:
        parent directory inode, if wanted
    :type parent: struct inode \*

.. _`export_encode_fh.description`:

Description
-----------

This default encode_fh function assumes that the 32 inode number
is suitable for locating an inode, and that the generation number
can be used to check that it is still valid.  It places them in the
filehandle fragment where export_decode_fh expects to find them.

.. This file was automatic generated / don't edit.

