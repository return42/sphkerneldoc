.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/quota/kqid.c

.. _`qid_eq`:

qid_eq
======

.. c:function:: bool qid_eq(struct kqid left, struct kqid right)

    Test to see if to kquid values are the same

    :param left:
        A qid value
    :type left: struct kqid

    :param right:
        Another quid value
    :type right: struct kqid

.. _`qid_eq.description`:

Description
-----------

Return true if the two qid values are equal and false otherwise.

.. _`qid_lt`:

qid_lt
======

.. c:function:: bool qid_lt(struct kqid left, struct kqid right)

    Test to see if one qid value is less than another

    :param left:
        The possibly lesser qid value
    :type left: struct kqid

    :param right:
        The possibly greater qid value
    :type right: struct kqid

.. _`qid_lt.description`:

Description
-----------

Return true if left is less than right and false otherwise.

.. _`from_kqid`:

from_kqid
=========

.. c:function:: qid_t from_kqid(struct user_namespace *targ, struct kqid kqid)

    Create a qid from a kqid user-namespace pair.

    :param targ:
        The user namespace we want a qid in.
    :type targ: struct user_namespace \*

    :param kqid:
        The kernel internal quota identifier to start with.
    :type kqid: struct kqid

.. _`from_kqid.description`:

Description
-----------

Map \ ``kqid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting qid.

There is always a mapping into the initial user_namespace.

If \ ``kqid``\  has no mapping in \ ``targ``\  (qid_t)-1 is returned.

.. _`from_kqid_munged`:

from_kqid_munged
================

.. c:function:: qid_t from_kqid_munged(struct user_namespace *targ, struct kqid kqid)

    Create a qid from a kqid user-namespace pair.

    :param targ:
        The user namespace we want a qid in.
    :type targ: struct user_namespace \*

    :param kqid:
        The kernel internal quota identifier to start with.
    :type kqid: struct kqid

.. _`from_kqid_munged.description`:

Description
-----------

Map \ ``kqid``\  into the user-namespace specified by \ ``targ``\  and
return the resulting qid.

There is always a mapping into the initial user_namespace.

Unlike from_kqid from_kqid_munged never fails and always
returns a valid projid.  This makes from_kqid_munged
appropriate for use in places where failing to provide
a qid_t is not a good option.

If \ ``kqid``\  has no mapping in \ ``targ``\  the kqid.type specific
overflow identifier is returned.

.. _`qid_valid`:

qid_valid
=========

.. c:function:: bool qid_valid(struct kqid qid)

    Report if a valid value is stored in a kqid.

    :param qid:
        The kernel internal quota identifier to test.
    :type qid: struct kqid

.. This file was automatic generated / don't edit.

