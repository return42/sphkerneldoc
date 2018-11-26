.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/file.c

.. _`audit_file_mask`:

audit_file_mask
===============

.. c:function:: void audit_file_mask(struct audit_buffer *ab, u32 mask)

    convert mask to permission string

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param mask:
        permission mask to convert
    :type mask: u32

.. _`file_audit_cb`:

file_audit_cb
=============

.. c:function:: void file_audit_cb(struct audit_buffer *ab, void *va)

    call back for file specific audit fields

    :param ab:
        audit_buffer  (NOT NULL)
    :type ab: struct audit_buffer \*

    :param va:
        audit struct to audit values of  (NOT NULL)
    :type va: void \*

.. _`aa_audit_file`:

aa_audit_file
=============

.. c:function:: int aa_audit_file(struct aa_profile *profile, struct aa_perms *perms, const char *op, u32 request, const char *name, const char *target, struct aa_label *tlabel, kuid_t ouid, const char *info, int error)

    handle the auditing of file operations

    :param profile:
        the profile being enforced  (NOT NULL)
    :type profile: struct aa_profile \*

    :param perms:
        the permissions computed for the request (NOT NULL)
    :type perms: struct aa_perms \*

    :param op:
        operation being mediated
    :type op: const char \*

    :param request:
        permissions requested
    :type request: u32

    :param name:
        name of object being mediated (MAYBE NULL)
    :type name: const char \*

    :param target:
        name of target (MAYBE NULL)
    :type target: const char \*

    :param tlabel:
        target label (MAY BE NULL)
    :type tlabel: struct aa_label \*

    :param ouid:
        object uid
    :type ouid: kuid_t

    :param info:
        extra information message (MAYBE NULL)
    :type info: const char \*

    :param error:
        0 if operation allowed else failure error code
    :type error: int

.. _`aa_audit_file.return`:

Return
------

\ ``0``\  or error on failure

.. _`is_deleted`:

is_deleted
==========

.. c:function:: bool is_deleted(struct dentry *dentry)

    test if a file has been completely unlinked

    :param dentry:
        dentry of file to test for deletion  (NOT NULL)
    :type dentry: struct dentry \*

.. _`is_deleted.return`:

Return
------

\ ``1``\  if deleted else \ ``0``\ 

.. _`map_old_perms`:

map_old_perms
=============

.. c:function:: u32 map_old_perms(u32 old)

    map old file perms layout to the new layout

    :param old:
        permission set in old mapping
    :type old: u32

.. _`map_old_perms.return`:

Return
------

new permission mapping

.. _`aa_compute_fperms`:

aa_compute_fperms
=================

.. c:function:: struct aa_perms aa_compute_fperms(struct aa_dfa *dfa, unsigned int state, struct path_cond *cond)

    convert dfa compressed perms to internal perms

    :param dfa:
        dfa to compute perms for   (NOT NULL)
    :type dfa: struct aa_dfa \*

    :param state:
        state in dfa
    :type state: unsigned int

    :param cond:
        conditions to consider  (NOT NULL)
    :type cond: struct path_cond \*

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

    :param dfa:
        to match against  (MAYBE NULL)
    :type dfa: struct aa_dfa \*

    :param start:
        *undescribed*
    :type start: unsigned int

    :param name:
        string to match against dfa  (NOT NULL)
    :type name: const char \*

    :param cond:
        conditions to consider for permission set computation  (NOT NULL)
    :type cond: struct path_cond \*

    :param perms:
        Returns - the permissions found when matching \ ``name``\ 
    :type perms: struct aa_perms \*

.. _`aa_str_perms.return`:

Return
------

the final state in \ ``dfa``\  when beginning \ ``start``\  and walking \ ``name``\ 

.. _`aa_path_perm`:

aa_path_perm
============

.. c:function:: int aa_path_perm(const char *op, struct aa_label *label, const struct path *path, int flags, u32 request, struct path_cond *cond)

    do permissions check & audit for \ ``path``\ 

    :param op:
        operation being checked
    :type op: const char \*

    :param label:
        profile being enforced  (NOT NULL)
    :type label: struct aa_label \*

    :param path:
        path to check permissions of  (NOT NULL)
    :type path: const struct path \*

    :param flags:
        any additional path flags beyond what the profile specifies
    :type flags: int

    :param request:
        requested permissions
    :type request: u32

    :param cond:
        conditional info for this request  (NOT NULL)
    :type cond: struct path_cond \*

.. _`aa_path_perm.return`:

Return
------

\ ``0``\  else error if access denied or other error

.. _`xindex_is_subset`:

xindex_is_subset
================

.. c:function:: bool xindex_is_subset(u32 link, u32 target)

    helper for aa_path_link

    :param link:
        link permission set
    :type link: u32

    :param target:
        target permission set
    :type target: u32

.. _`xindex_is_subset.description`:

Description
-----------

test target x permissions are equal OR a subset of link x permissions
this is done as part of the subset test, where a hardlink must have
a subset of permissions that the target has.

.. _`xindex_is_subset.return`:

Return
------

\ ``1``\  if subset else \ ``0``\ 

.. _`aa_path_link`:

aa_path_link
============

.. c:function:: int aa_path_link(struct aa_label *label, struct dentry *old_dentry, const struct path *new_dir, struct dentry *new_dentry)

    Handle hard link permission check

    :param label:
        the label being enforced  (NOT NULL)
    :type label: struct aa_label \*

    :param old_dentry:
        the target dentry  (NOT NULL)
    :type old_dentry: struct dentry \*

    :param new_dir:
        directory the new link will be created in  (NOT NULL)
    :type new_dir: const struct path \*

    :param new_dentry:
        the link being created  (NOT NULL)
    :type new_dentry: struct dentry \*

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

\ ``0``\  if allowed else error

.. _`aa_file_perm`:

aa_file_perm
============

.. c:function:: int aa_file_perm(const char *op, struct aa_label *label, struct file *file, u32 request)

    do permission revalidation check & audit for \ ``file``\ 

    :param op:
        operation being checked
    :type op: const char \*

    :param label:
        label being enforced   (NOT NULL)
    :type label: struct aa_label \*

    :param file:
        file to revalidate access permissions on  (NOT NULL)
    :type file: struct file \*

    :param request:
        requested permissions
    :type request: u32

.. _`aa_file_perm.return`:

Return
------

\ ``0``\  if access allowed else error

.. This file was automatic generated / don't edit.

