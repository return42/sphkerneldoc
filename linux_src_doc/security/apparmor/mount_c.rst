.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/mount.c

.. _`audit_cb`:

audit_cb
========

.. c:function:: void audit_cb(struct audit_buffer *ab, void *va)

    call back for mount specific audit fields

    :param struct audit_buffer \*ab:
        audit_buffer  (NOT NULL)

    :param void \*va:
        audit struct to audit values of  (NOT NULL)

.. _`audit_mount`:

audit_mount
===========

.. c:function:: int audit_mount(struct aa_profile *profile, const char *op, const char *name, const char *src_name, const char *type, const char *trans, unsigned long flags, const void *data, u32 request, struct aa_perms *perms, const char *info, int error)

    handle the auditing of mount operations

    :param struct aa_profile \*profile:
        the profile being enforced  (NOT NULL)

    :param const char \*op:
        operation being mediated (NOT NULL)

    :param const char \*name:
        name of object being mediated (MAYBE NULL)

    :param const char \*src_name:
        src_name of object being mediated (MAYBE_NULL)

    :param const char \*type:
        type of filesystem (MAYBE_NULL)

    :param const char \*trans:
        name of trans (MAYBE NULL)

    :param unsigned long flags:
        filesystem idependent mount flags

    :param const void \*data:
        filesystem mount flags

    :param u32 request:
        permissions requested

    :param struct aa_perms \*perms:
        the permissions computed for the request (NOT NULL)

    :param const char \*info:
        extra information message (MAYBE NULL)

    :param int error:
        0 if operation allowed else failure error code

.. _`audit_mount.return`:

Return
------

\ ``0``\  or error on failure

.. _`match_mnt_flags`:

match_mnt_flags
===============

.. c:function:: unsigned int match_mnt_flags(struct aa_dfa *dfa, unsigned int state, unsigned long flags)

    Do an ordered match on mount flags

    :param struct aa_dfa \*dfa:
        dfa to match against

    :param unsigned int state:
        state to start in

    :param unsigned long flags:
        mount flags to match against

.. _`match_mnt_flags.description`:

Description
-----------

Mount flags are encoded as an ordered match. This is done instead of
checking against a simple bitmask, to allow for logical operations
on the flags.

.. _`match_mnt_flags.return`:

Return
------

next state after flags match

.. _`compute_mnt_perms`:

compute_mnt_perms
=================

.. c:function:: struct aa_perms compute_mnt_perms(struct aa_dfa *dfa, unsigned int state)

    compute mount permission associated with \ ``state``\ 

    :param struct aa_dfa \*dfa:
        dfa to match against (NOT NULL)

    :param unsigned int state:
        state match finished in

.. _`compute_mnt_perms.return`:

Return
------

mount permissions

.. _`match_mnt_path_str`:

match_mnt_path_str
==================

.. c:function:: int match_mnt_path_str(struct aa_profile *profile, const struct path *mntpath, char *buffer, const char *devname, const char *type, unsigned long flags, void *data, bool binary, const char *devinfo)

    handle path matching for mount

    :param struct aa_profile \*profile:
        the confining profile

    :param const struct path \*mntpath:
        for the mntpnt (NOT NULL)

    :param char \*buffer:
        buffer to be used to lookup mntpath

    :param const char \*devname:
        *undescribed*

    :param const char \*type:
        string for the dev type (MAYBE NULL)

    :param unsigned long flags:
        mount flags to match

    :param void \*data:
        fs mount data (MAYBE NULL)

    :param bool binary:
        whether \ ``data``\  is binary

    :param const char \*devinfo:
        error str if (IS_ERR(@devname))

.. _`match_mnt_path_str.return`:

Return
------

0 on success else error

.. _`match_mnt`:

match_mnt
=========

.. c:function:: int match_mnt(struct aa_profile *profile, const struct path *path, char *buffer, struct path *devpath, char *devbuffer, const char *type, unsigned long flags, void *data, bool binary)

    handle path matching for mount

    :param struct aa_profile \*profile:
        the confining profile

    :param const struct path \*path:
        *undescribed*

    :param char \*buffer:
        buffer to be used to lookup mntpath

    :param struct path \*devpath:
        path devname/src_name (MAYBE NULL)

    :param char \*devbuffer:
        buffer to be used to lookup devname/src_name

    :param const char \*type:
        string for the dev type (MAYBE NULL)

    :param unsigned long flags:
        mount flags to match

    :param void \*data:
        fs mount data (MAYBE NULL)

    :param bool binary:
        whether \ ``data``\  is binary

.. _`match_mnt.return`:

Return
------

0 on success else error

.. This file was automatic generated / don't edit.

