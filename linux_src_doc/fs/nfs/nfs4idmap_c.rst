.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4idmap.c

.. _`nfs_fattr_init_names`:

nfs_fattr_init_names
====================

.. c:function:: void nfs_fattr_init_names(struct nfs_fattr *fattr, struct nfs4_string *owner_name, struct nfs4_string *group_name)

    initialise the nfs_fattr owner_name/group_name fields

    :param fattr:
        fully initialised struct nfs_fattr
    :type fattr: struct nfs_fattr \*

    :param owner_name:
        owner name string cache
    :type owner_name: struct nfs4_string \*

    :param group_name:
        group name string cache
    :type group_name: struct nfs4_string \*

.. _`nfs_fattr_free_names`:

nfs_fattr_free_names
====================

.. c:function:: void nfs_fattr_free_names(struct nfs_fattr *fattr)

    free up the NFSv4 owner and group strings

    :param fattr:
        a fully initialised nfs_fattr structure
    :type fattr: struct nfs_fattr \*

.. _`nfs_fattr_map_and_free_names`:

nfs_fattr_map_and_free_names
============================

.. c:function:: void nfs_fattr_map_and_free_names(struct nfs_server *server, struct nfs_fattr *fattr)

    map owner/group strings into uid/gid and free

    :param server:
        pointer to the filesystem nfs_server structure
    :type server: struct nfs_server \*

    :param fattr:
        a fully initialised nfs_fattr structure
    :type fattr: struct nfs_fattr \*

.. _`nfs_fattr_map_and_free_names.description`:

Description
-----------

This helper maps the cached NFSv4 owner/group strings in fattr into
their numeric uid/gid equivalents, and then frees the cached strings.

.. This file was automatic generated / don't edit.

