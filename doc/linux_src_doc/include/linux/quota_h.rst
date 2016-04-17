.. -*- coding: utf-8; mode: rst -*-

=======
quota.h
=======


.. _`make_kqid`:

make_kqid
=========

.. c:function:: struct kqid make_kqid (struct user_namespace *from, enum quota_type type, qid_t qid)

    Map a user-namespace, type, qid tuple into a kqid.

    :param struct user_namespace \*from:
        User namespace that the qid is in

    :param enum quota_type type:
        The type of quota

    :param qid_t qid:
        Quota identifier



.. _`make_kqid.description`:

Description
-----------

Maps a user-namespace, type qid tuple into a kernel internal
kqid, and returns that kqid.

When there is no mapping defined for the user-namespace, type,
qid tuple an invalid kqid is returned.  Callers are expected to
test for and handle handle invalid kqids being returned.
Invalid kqids may be tested for using :c:func:`qid_valid`.



.. _`make_kqid_invalid`:

make_kqid_invalid
=================

.. c:function:: struct kqid make_kqid_invalid (enum quota_type type)

    Explicitly make an invalid kqid

    :param enum quota_type type:
        The type of quota identifier



.. _`make_kqid_invalid.description`:

Description
-----------

Returns an invalid kqid with the specified type.



.. _`make_kqid_uid`:

make_kqid_uid
=============

.. c:function:: struct kqid make_kqid_uid (kuid_t uid)

    Make a kqid from a kuid

    :param kuid_t uid:
        The kuid to make the quota identifier from



.. _`make_kqid_gid`:

make_kqid_gid
=============

.. c:function:: struct kqid make_kqid_gid (kgid_t gid)

    Make a kqid from a kgid

    :param kgid_t gid:
        The kgid to make the quota identifier from



.. _`make_kqid_projid`:

make_kqid_projid
================

.. c:function:: struct kqid make_kqid_projid (kprojid_t projid)

    Make a kqid from a projid

    :param kprojid_t projid:
        The kprojid to make the quota identifier from

