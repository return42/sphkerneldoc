.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/user_namespace.c

.. _`make_kuid`:

make_kuid
=========

.. c:function:: kuid_t make_kuid(struct user_namespace *ns, uid_t uid)

    Map a user-namespace uid pair into a kuid.

    :param struct user_namespace \*ns:
        User namespace that the uid is in

    :param uid_t uid:
        User identifier

.. _`make_kuid.description`:

Description
-----------

Maps a user-namespace uid pair into a kernel internal kuid,
and returns that kuid.

When there is no mapping defined for the user-namespace uid
pair INVALID_UID is returned.  Callers are expected to test
for and handle INVALID_UID being returned.  INVALID_UID
may be tested for using \ :c:func:`uid_valid`\ .

.. _`from_kuid`:

from_kuid
=========

.. c:function:: uid_t from_kuid(struct user_namespace *targ, kuid_t kuid)

    Create a uid from a kuid user-namespace pair.

    :param struct user_namespace \*targ:
        The user namespace we want a uid in.

    :param kuid_t kuid:
        The kernel internal uid to start with.

.. _`from_kuid.description`:

Description
-----------

Map \ ``kuid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting uid.

There is always a mapping into the initial user_namespace.

If \ ``kuid``\  has no mapping in \ ``targ``\  (uid_t)-1 is returned.

.. _`from_kuid_munged`:

from_kuid_munged
================

.. c:function:: uid_t from_kuid_munged(struct user_namespace *targ, kuid_t kuid)

    Create a uid from a kuid user-namespace pair.

    :param struct user_namespace \*targ:
        The user namespace we want a uid in.

    :param kuid_t kuid:
        The kernel internal uid to start with.

.. _`from_kuid_munged.description`:

Description
-----------

Map \ ``kuid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting uid.

There is always a mapping into the initial user_namespace.

Unlike from_kuid from_kuid_munged never fails and always
returns a valid uid.  This makes from_kuid_munged appropriate
for use in syscalls like stat and getuid where failing the
system call and failing to provide a valid uid are not an
options.

If \ ``kuid``\  has no mapping in \ ``targ``\  overflowuid is returned.

.. _`make_kgid`:

make_kgid
=========

.. c:function:: kgid_t make_kgid(struct user_namespace *ns, gid_t gid)

    Map a user-namespace gid pair into a kgid.

    :param struct user_namespace \*ns:
        User namespace that the gid is in

    :param gid_t gid:
        group identifier

.. _`make_kgid.description`:

Description
-----------

Maps a user-namespace gid pair into a kernel internal kgid,
and returns that kgid.

When there is no mapping defined for the user-namespace gid
pair INVALID_GID is returned.  Callers are expected to test
for and handle INVALID_GID being returned.  INVALID_GID may be
tested for using \ :c:func:`gid_valid`\ .

.. _`from_kgid`:

from_kgid
=========

.. c:function:: gid_t from_kgid(struct user_namespace *targ, kgid_t kgid)

    Create a gid from a kgid user-namespace pair.

    :param struct user_namespace \*targ:
        The user namespace we want a gid in.

    :param kgid_t kgid:
        The kernel internal gid to start with.

.. _`from_kgid.description`:

Description
-----------

Map \ ``kgid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting gid.

There is always a mapping into the initial user_namespace.

If \ ``kgid``\  has no mapping in \ ``targ``\  (gid_t)-1 is returned.

.. _`from_kgid_munged`:

from_kgid_munged
================

.. c:function:: gid_t from_kgid_munged(struct user_namespace *targ, kgid_t kgid)

    Create a gid from a kgid user-namespace pair.

    :param struct user_namespace \*targ:
        The user namespace we want a gid in.

    :param kgid_t kgid:
        The kernel internal gid to start with.

.. _`from_kgid_munged.description`:

Description
-----------

Map \ ``kgid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting gid.

There is always a mapping into the initial user_namespace.

Unlike from_kgid from_kgid_munged never fails and always
returns a valid gid.  This makes from_kgid_munged appropriate
for use in syscalls like stat and getgid where failing the
system call and failing to provide a valid gid are not options.

If \ ``kgid``\  has no mapping in \ ``targ``\  overflowgid is returned.

.. _`make_kprojid`:

make_kprojid
============

.. c:function:: kprojid_t make_kprojid(struct user_namespace *ns, projid_t projid)

    Map a user-namespace projid pair into a kprojid.

    :param struct user_namespace \*ns:
        User namespace that the projid is in

    :param projid_t projid:
        Project identifier

.. _`make_kprojid.description`:

Description
-----------

Maps a user-namespace uid pair into a kernel internal kuid,
and returns that kuid.

When there is no mapping defined for the user-namespace projid
pair INVALID_PROJID is returned.  Callers are expected to test
for and handle handle INVALID_PROJID being returned.  INVALID_PROJID
may be tested for using \ :c:func:`projid_valid`\ .

.. _`from_kprojid`:

from_kprojid
============

.. c:function:: projid_t from_kprojid(struct user_namespace *targ, kprojid_t kprojid)

    Create a projid from a kprojid user-namespace pair.

    :param struct user_namespace \*targ:
        The user namespace we want a projid in.

    :param kprojid_t kprojid:
        The kernel internal project identifier to start with.

.. _`from_kprojid.description`:

Description
-----------

Map \ ``kprojid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting projid.

There is always a mapping into the initial user_namespace.

If \ ``kprojid``\  has no mapping in \ ``targ``\  (projid_t)-1 is returned.

.. _`from_kprojid_munged`:

from_kprojid_munged
===================

.. c:function:: projid_t from_kprojid_munged(struct user_namespace *targ, kprojid_t kprojid)

    Create a projiid from a kprojid user-namespace pair.

    :param struct user_namespace \*targ:
        The user namespace we want a projid in.

    :param kprojid_t kprojid:
        The kernel internal projid to start with.

.. _`from_kprojid_munged.description`:

Description
-----------

Map \ ``kprojid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting projid.

There is always a mapping into the initial user_namespace.

Unlike from_kprojid from_kprojid_munged never fails and always
returns a valid projid.  This makes from_kprojid_munged
appropriate for use in syscalls like stat and where
failing the system call and failing to provide a valid projid are
not an options.

If \ ``kprojid``\  has no mapping in \ ``targ``\  OVERFLOW_PROJID is returned.

.. This file was automatic generated / don't edit.

