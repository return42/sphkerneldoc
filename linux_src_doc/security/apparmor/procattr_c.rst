.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/procattr.c

.. _`aa_getprocattr`:

aa_getprocattr
==============

.. c:function:: int aa_getprocattr(struct aa_profile *profile, char **string)

    Return the profile information for \ ``profile``\ 

    :param struct aa_profile \*profile:
        the profile to print profile info about  (NOT NULL)

    :param char \*\*string:
        Returns - string containing the profile info (NOT NULL)

.. _`aa_getprocattr.return`:

Return
------

length of \ ``string``\  on success else error on failure

size of string placed in \ ``string``\  else error code on failure

.. _`aa_getprocattr.requires`:

Requires
--------

profile != NULL

Creates a string containing the namespace_name://profile_name for
\ ``profile``\ .

.. _`split_token_from_name`:

split_token_from_name
=====================

.. c:function:: char *split_token_from_name(int op, char *args, u64 *token)

    separate a string of form  <token>^<name>

    :param int op:
        operation being checked

    :param char \*args:
        string to parse  (NOT NULL)

    :param u64 \*token:
        stores returned parsed token value  (NOT NULL)

.. _`split_token_from_name.return`:

Return
------

start position of name after token else NULL on failure

.. _`aa_setprocattr_changehat`:

aa_setprocattr_changehat
========================

.. c:function:: int aa_setprocattr_changehat(char *args, size_t size, int test)

    handle procattr interface to change_hat

    :param char \*args:
        args received from writing to /proc/<pid>/attr/current (NOT NULL)

    :param size_t size:
        size of the args

    :param int test:
        true if this is a test of change_hat permissions

.. _`aa_setprocattr_changehat.return`:

Return
------

%0 or error code if change_hat fails

.. _`aa_setprocattr_changeprofile`:

aa_setprocattr_changeprofile
============================

.. c:function:: int aa_setprocattr_changeprofile(char *fqname, bool onexec, int test)

    handle procattr interface to changeprofile

    :param char \*fqname:
        args received from writting to /proc/<pid>/attr/current (NOT NULL)

    :param bool onexec:
        true if change_profile should be delayed until exec

    :param int test:
        true if this is a test of change_profile permissions

.. _`aa_setprocattr_changeprofile.return`:

Return
------

%0 or error code if change_profile fails

.. This file was automatic generated / don't edit.

