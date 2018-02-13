.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/policy.h

.. _`aa_get_newest_profile`:

aa_get_newest_profile
=====================

.. c:function:: struct aa_profile *aa_get_newest_profile(struct aa_profile *p)

    simple wrapper fn to wrap the label version

    :param struct aa_profile \*p:
        profile (NOT NULL)

.. _`aa_get_newest_profile.description`:

Description
-----------

Returns refcount to newest version of the profile (maybe \ ``p``\ )

.. _`aa_get_newest_profile.requires`:

Requires
--------

\ ``p``\  must be held with a valid refcount

.. _`aa_get_profile`:

aa_get_profile
==============

.. c:function:: struct aa_profile *aa_get_profile(struct aa_profile *p)

    increment refcount on profile \ ``p``\ 

    :param struct aa_profile \*p:
        profile  (MAYBE NULL)

.. _`aa_get_profile.return`:

Return
------

pointer to \ ``p``\  if \ ``p``\  is NULL will return NULL

.. _`aa_get_profile.requires`:

Requires
--------

\ ``p``\  must be held with valid refcount when called

.. _`aa_get_profile_not0`:

aa_get_profile_not0
===================

.. c:function:: struct aa_profile *aa_get_profile_not0(struct aa_profile *p)

    increment refcount on profile \ ``p``\  found via lookup

    :param struct aa_profile \*p:
        profile  (MAYBE NULL)

.. _`aa_get_profile_not0.return`:

Return
------

pointer to \ ``p``\  if \ ``p``\  is NULL will return NULL

.. _`aa_get_profile_not0.requires`:

Requires
--------

\ ``p``\  must be held with valid refcount when called

.. _`aa_get_profile_rcu`:

aa_get_profile_rcu
==================

.. c:function:: struct aa_profile *aa_get_profile_rcu(struct aa_profile __rcu **p)

    increment a refcount profile that can be replaced

    :param struct aa_profile __rcu \*\*p:
        pointer to profile that can be replaced (NOT NULL)

.. _`aa_get_profile_rcu.return`:

Return
------

pointer to a refcounted profile.
else NULL if no profile

.. _`aa_put_profile`:

aa_put_profile
==============

.. c:function:: void aa_put_profile(struct aa_profile *p)

    decrement refcount on profile \ ``p``\ 

    :param struct aa_profile \*p:
        profile  (MAYBE NULL)

.. This file was automatic generated / don't edit.

