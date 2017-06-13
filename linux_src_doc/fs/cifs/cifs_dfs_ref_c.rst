.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/cifs_dfs_ref.c

.. _`cifs_build_devname`:

cifs_build_devname
==================

.. c:function:: char *cifs_build_devname(char *nodename, const char *prepath)

    build a devicename from a UNC and optional prepath

    :param char \*nodename:
        pointer to UNC string

    :param const char \*prepath:
        pointer to prefixpath (or NULL if there isn't one)

.. _`cifs_build_devname.description`:

Description
-----------

Build a new cifs devicename after chasing a DFS referral. Allocate a buffer
big enough to hold the final thing. Copy the UNC from the nodename, and
concatenate the prepath onto the end of it if there is one.

Returns pointer to the built string, or a ERR_PTR. Caller is responsible
for freeing the returned string.

.. _`cifs_compose_mount_options`:

cifs_compose_mount_options
==========================

.. c:function:: char *cifs_compose_mount_options(const char *sb_mountdata, const char *fullpath, const struct dfs_info3_param *ref, char **devname)

    creates mount options for refferral

    :param const char \*sb_mountdata:
        parent/root DFS mount options (template)

    :param const char \*fullpath:
        full path in UNC format

    :param const struct dfs_info3_param \*ref:
        server's referral

    :param char \*\*devname:
        pointer for saving device name

.. _`cifs_compose_mount_options.description`:

Description
-----------

creates mount options for submount based on template options sb_mountdata
and replacing unc,ip,prefixpath options with ones we've got form ref_unc.

.. _`cifs_compose_mount_options.return`:

Return
------

pointer to new mount options or ERR_PTR.
Caller is responcible for freeing retunrned value if it is not error.

.. _`cifs_dfs_do_refmount`:

cifs_dfs_do_refmount
====================

.. c:function:: struct vfsmount *cifs_dfs_do_refmount(struct dentry *mntpt, struct cifs_sb_info *cifs_sb, const char *fullpath, const struct dfs_info3_param *ref)

    mounts specified path using provided refferal

    :param struct dentry \*mntpt:
        *undescribed*

    :param struct cifs_sb_info \*cifs_sb:
        parent/root superblock

    :param const char \*fullpath:
        full path in UNC format

    :param const struct dfs_info3_param \*ref:
        server's referral

.. This file was automatic generated / don't edit.

