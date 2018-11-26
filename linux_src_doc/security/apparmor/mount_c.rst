.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/mount.c

.. _`audit_cb`:

audit_cb
========

.. c:function:: void audit_cb(struct audit_buffer *ab, void *va)

    call back for mount specific audit fields

    :param ab:
        audit_buffer  (NOT NULL)
    :type ab: struct audit_buffer \*

    :param va:
        audit struct to audit values of  (NOT NULL)
    :type va: void \*

.. _`audit_mount`:

audit_mount
===========

.. c:function:: int audit_mount(struct aa_profile *profile, const char *op, const char *name, const char *src_name, const char *type, const char *trans, unsigned long flags, const void *data, u32 request, struct aa_perms *perms, const char *info, int error)

    handle the auditing of mount operations

    :param profile:
        the profile being enforced  (NOT NULL)
    :type profile: struct aa_profile \*

    :param op:
        operation being mediated (NOT NULL)
    :type op: const char \*

    :param name:
        name of object being mediated (MAYBE NULL)
    :type name: const char \*

    :param src_name:
        src_name of object being mediated (MAYBE_NULL)
    :type src_name: const char \*

    :param type:
        type of filesystem (MAYBE_NULL)
    :type type: const char \*

    :param trans:
        name of trans (MAYBE NULL)
    :type trans: const char \*

    :param flags:
        filesystem independent mount flags
    :type flags: unsigned long

    :param data:
        filesystem mount flags
    :type data: const void \*

    :param request:
        permissions requested
    :type request: u32

    :param perms:
        the permissions computed for the request (NOT NULL)
    :type perms: struct aa_perms \*

    :param info:
        extra information message (MAYBE NULL)
    :type info: const char \*

    :param error:
        0 if operation allowed else failure error code
    :type error: int

.. _`audit_mount.return`:

Return
------

\ ``0``\  or error on failure

.. _`match_mnt_flags`:

match_mnt_flags
===============

.. c:function:: unsigned int match_mnt_flags(struct aa_dfa *dfa, unsigned int state, unsigned long flags)

    Do an ordered match on mount flags

    :param dfa:
        dfa to match against
    :type dfa: struct aa_dfa \*

    :param state:
        state to start in
    :type state: unsigned int

    :param flags:
        mount flags to match against
    :type flags: unsigned long

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

    :param dfa:
        dfa to match against (NOT NULL)
    :type dfa: struct aa_dfa \*

    :param state:
        state match finished in
    :type state: unsigned int

.. _`compute_mnt_perms.return`:

Return
------

mount permissions

.. _`match_mnt_path_str`:

match_mnt_path_str
==================

.. c:function:: int match_mnt_path_str(struct aa_profile *profile, const struct path *mntpath, char *buffer, const char *devname, const char *type, unsigned long flags, void *data, bool binary, const char *devinfo)

    handle path matching for mount

    :param profile:
        the confining profile
    :type profile: struct aa_profile \*

    :param mntpath:
        for the mntpnt (NOT NULL)
    :type mntpath: const struct path \*

    :param buffer:
        buffer to be used to lookup mntpath
    :type buffer: char \*

    :param devname:
        *undescribed*
    :type devname: const char \*

    :param type:
        string for the dev type (MAYBE NULL)
    :type type: const char \*

    :param flags:
        mount flags to match
    :type flags: unsigned long

    :param data:
        fs mount data (MAYBE NULL)
    :type data: void \*

    :param binary:
        whether \ ``data``\  is binary
    :type binary: bool

    :param devinfo:
        error str if (IS_ERR(@devname))
    :type devinfo: const char \*

.. _`match_mnt_path_str.return`:

Return
------

0 on success else error

.. _`match_mnt`:

match_mnt
=========

.. c:function:: int match_mnt(struct aa_profile *profile, const struct path *path, char *buffer, struct path *devpath, char *devbuffer, const char *type, unsigned long flags, void *data, bool binary)

    handle path matching for mount

    :param profile:
        the confining profile
    :type profile: struct aa_profile \*

    :param path:
        *undescribed*
    :type path: const struct path \*

    :param buffer:
        buffer to be used to lookup mntpath
    :type buffer: char \*

    :param devpath:
        path devname/src_name (MAYBE NULL)
    :type devpath: struct path \*

    :param devbuffer:
        buffer to be used to lookup devname/src_name
    :type devbuffer: char \*

    :param type:
        string for the dev type (MAYBE NULL)
    :type type: const char \*

    :param flags:
        mount flags to match
    :type flags: unsigned long

    :param data:
        fs mount data (MAYBE NULL)
    :type data: void \*

    :param binary:
        whether \ ``data``\  is binary
    :type binary: bool

.. _`match_mnt.return`:

Return
------

0 on success else error

.. This file was automatic generated / don't edit.

