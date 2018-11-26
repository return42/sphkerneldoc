.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/quota.h

.. _`make_kqid`:

make_kqid
=========

.. c:function:: struct kqid make_kqid(struct user_namespace *from, enum quota_type type, qid_t qid)

    Map a user-namespace, type, qid tuple into a kqid.

    :param from:
        User namespace that the qid is in
    :type from: struct user_namespace \*

    :param type:
        The type of quota
    :type type: enum quota_type

    :param qid:
        Quota identifier
    :type qid: qid_t

.. _`make_kqid.description`:

Description
-----------

Maps a user-namespace, type qid tuple into a kernel internal
kqid, and returns that kqid.

When there is no mapping defined for the user-namespace, type,
qid tuple an invalid kqid is returned.  Callers are expected to
test for and handle handle invalid kqids being returned.
Invalid kqids may be tested for using \ :c:func:`qid_valid`\ .

.. _`make_kqid_invalid`:

make_kqid_invalid
=================

.. c:function:: struct kqid make_kqid_invalid(enum quota_type type)

    Explicitly make an invalid kqid

    :param type:
        The type of quota identifier
    :type type: enum quota_type

.. _`make_kqid_invalid.description`:

Description
-----------

Returns an invalid kqid with the specified type.

.. _`make_kqid_uid`:

make_kqid_uid
=============

.. c:function:: struct kqid make_kqid_uid(kuid_t uid)

    Make a kqid from a kuid

    :param uid:
        The kuid to make the quota identifier from
    :type uid: kuid_t

.. _`make_kqid_gid`:

make_kqid_gid
=============

.. c:function:: struct kqid make_kqid_gid(kgid_t gid)

    Make a kqid from a kgid

    :param gid:
        The kgid to make the quota identifier from
    :type gid: kgid_t

.. _`make_kqid_projid`:

make_kqid_projid
================

.. c:function:: struct kqid make_kqid_projid(kprojid_t projid)

    Make a kqid from a projid

    :param projid:
        The kprojid to make the quota identifier from
    :type projid: kprojid_t

.. _`qid_has_mapping`:

qid_has_mapping
===============

.. c:function:: bool qid_has_mapping(struct user_namespace *ns, struct kqid qid)

    Report if a qid maps into a user namespace.

    :param ns:
        The user namespace to see if a value maps into.
    :type ns: struct user_namespace \*

    :param qid:
        The kernel internal quota identifier to test.
    :type qid: struct kqid

.. This file was automatic generated / don't edit.

