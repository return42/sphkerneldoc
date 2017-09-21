.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/file.c

.. _`audit_file_mask`:

audit_file_mask
===============

.. c:function:: void audit_file_mask(struct audit_buffer *ab, u32 mask)

    convert mask to permission string

    :param struct audit_buffer \*ab:
        *undescribed*

    :param u32 mask:
        permission mask to convert

.. _`file_audit_cb`:

file_audit_cb
=============

.. c:function:: void file_audit_cb(struct audit_buffer *ab, void *va)

    call back for file specific audit fields

    :param struct audit_buffer \*ab:
        audit_buffer  (NOT NULL)

    :param void \*va:
        audit struct to audit values of  (NOT NULL)

.. _`aa_audit_file`:

aa_audit_file
=============

.. c:function:: int aa_audit_file(struct aa_profile *profile, struct aa_perms *perms, const char *op, u32 request, const char *name, const char *target, struct aa_label *tlabel, kuid_t ouid, const char *info, int error)

    handle the auditing of file operations

    :param struct aa_profile \*profile:
        the profile being enforced  (NOT NULL)

    :param struct aa_perms \*perms:
        the permissions computed for the request (NOT NULL)

    :param const char \*op:
        operation being mediated

    :param u32 request:
        permissions requested

    :param const char \*name:
        name of object being mediated (MAYBE NULL)

    :param const char \*target:
        name of target (MAYBE NULL)

    :param struct aa_label \*tlabel:
        target label (MAY BE NULL)

    :param kuid_t ouid:
        object uid

    :param const char \*info:
        extra information message (MAYBE NULL)

    :param int error:
        0 if operation allowed else failure error code

.. _`aa_audit_file.return`:

Return
------

%0 or error on failure

.. _`is_deleted`:

is_deleted
==========

.. c:function:: bool is_deleted(struct dentry *dentry)

    test if a file has been completely unlinked

    :param struct dentry \*dentry:
        dentry of file to test for deletion  (NOT NULL)

.. _`is_deleted.return`:

Return
------

%1 if deleted else \ ``0``\ 

.. _`map_old_perms`:

map_old_perms
=============

.. c:function:: u32 map_old_perms(u32 old)

    map old file perms layout to the new layout

    :param u32 old:
        permission set in old mapping

.. _`map_old_perms.return`:

Return
------

new permission mapping

.. _`aa_compute_fperms`:

aa_compute_fperms
=================

.. c:function:: struct aa_perms aa_compute_fperms(struct aa_dfa *dfa, unsigned int state, struct path_cond *cond)

    convert dfa compressed perms to internal perms

    :param struct aa_dfa \*dfa:
        dfa to compute perms for   (NOT NULL)

    :param unsigned int state:
        state in dfa

    :param struct path_cond \*cond:
        conditions to consider  (NOT NULL)

.. _`aa_compute_fperms.todo`:

TODO
----

convert from dfa + state to permission entry, do computation conversion
at load time.

.. _`aa_compute_fperms.return`:

Return
------

computed permission set

.. _`aa_str_perms`:

aa_str_perms
============

.. c:function:: unsigned int aa_str_perms(struct aa_dfa *dfa, unsigned int start, const char *name, struct path_cond *cond, struct aa_perms *perms)

    find permission that match \ ``name``\ 

    :param struct aa_dfa \*dfa:
        to match against  (MAYBE NULL)

    :param unsigned int start:
        *undescribed*

    :param const char \*name:
        string to match against dfa  (NOT NULL)

    :param struct path_cond \*cond:
        conditions to consider for permission set computation  (NOT NULL)

    :param struct aa_perms \*perms:
        Returns - the permissions found when matching \ ``name``\ 

.. _`aa_str_perms.return`:

Return
------

the final state in \ ``dfa``\  when beginning \ ``start``\  and walking \ ``name``\ 

.. _`aa_path_perm`:

aa_path_perm
============

.. c:function:: int aa_path_perm(const char *op, struct aa_label *label, const struct path *path, int flags, u32 request, struct path_cond *cond)

    do permissions check & audit for \ ``path``\ 

    :param const char \*op:
        operation being checked

    :param struct aa_label \*label:
        profile being enforced  (NOT NULL)

    :param const struct path \*path:
        path to check permissions of  (NOT NULL)

    :param int flags:
        any additional path flags beyond what the profile specifies

    :param u32 request:
        requested permissions

    :param struct path_cond \*cond:
        conditional info for this request  (NOT NULL)

.. _`aa_path_perm.return`:

Return
------

%0 else error if access denied or other error

.. _`xindex_is_subset`:

xindex_is_subset
================

.. c:function:: bool xindex_is_subset(u32 link, u32 target)

    helper for aa_path_link

    :param u32 link:
        link permission set

    :param u32 target:
        target permission set

.. _`xindex_is_subset.description`:

Description
-----------

test target x permissions are equal OR a subset of link x permissions
this is done as part of the subset test, where a hardlink must have
a subset of permissions that the target has.

.. _`xindex_is_subset.return`:

Return
------

%1 if subset else \ ``0``\ 

.. _`aa_path_link`:

aa_path_link
============

.. c:function:: int aa_path_link(struct aa_label *label, struct dentry *old_dentry, const struct path *new_dir, struct dentry *new_dentry)

    Handle hard link permission check

    :param struct aa_label \*label:
        the label being enforced  (NOT NULL)

    :param struct dentry \*old_dentry:
        the target dentry  (NOT NULL)

    :param const struct path \*new_dir:
        directory the new link will be created in  (NOT NULL)

    :param struct dentry \*new_dentry:
        the link being created  (NOT NULL)

.. _`aa_path_link.description`:

Description
-----------

Handle the permission test for a link & target pair.  Permission
is encoded as a pair where the link permission is determined
first, and if allowed, the target is tested.  The target test
is done from the point of the link match (not start of DFA)
making the target permission dependent on the link permission match.

The subset test if required forces that permissions granted
on link are a subset of the permission granted to target.

.. _`aa_path_link.return`:

Return
------

%0 if allowed else error

.. _`aa_file_perm`:

aa_file_perm
============

.. c:function:: int aa_file_perm(const char *op, struct aa_label *label, struct file *file, u32 request)

    do permission revalidation check & audit for \ ``file``\ 

    :param const char \*op:
        operation being checked

    :param struct aa_label \*label:
        label being enforced   (NOT NULL)

    :param struct file \*file:
        file to revalidate access permissions on  (NOT NULL)

    :param u32 request:
        requested permissions

.. _`aa_file_perm.return`:

Return
------

%0 if access allowed else error

.. This file was automatic generated / don't edit.

