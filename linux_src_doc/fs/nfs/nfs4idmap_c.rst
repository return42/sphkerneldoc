.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4idmap.c

.. _`nfs_fattr_init_names`:

nfs_fattr_init_names
====================

.. c:function:: void nfs_fattr_init_names(struct nfs_fattr *fattr, struct nfs4_string *owner_name, struct nfs4_string *group_name)

    initialise the nfs_fattr owner_name/group_name fields

    :param struct nfs_fattr \*fattr:
        fully initialised struct nfs_fattr

    :param struct nfs4_string \*owner_name:
        owner name string cache

    :param struct nfs4_string \*group_name:
        group name string cache

.. _`nfs_fattr_free_names`:

nfs_fattr_free_names
====================

.. c:function:: void nfs_fattr_free_names(struct nfs_fattr *fattr)

    free up the NFSv4 owner and group strings

    :param struct nfs_fattr \*fattr:
        a fully initialised nfs_fattr structure

.. _`nfs_fattr_map_and_free_names`:

nfs_fattr_map_and_free_names
============================

.. c:function:: void nfs_fattr_map_and_free_names(struct nfs_server *server, struct nfs_fattr *fattr)

    map owner/group strings into uid/gid and free

    :param struct nfs_server \*server:
        pointer to the filesystem nfs_server structure

    :param struct nfs_fattr \*fattr:
        a fully initialised nfs_fattr structure

.. _`nfs_fattr_map_and_free_names.description`:

Description
-----------

This helper maps the cached NFSv4 owner/group strings in fattr into
their numeric uid/gid equivalents, and then frees the cached strings.

.. This file was automatic generated / don't edit.

