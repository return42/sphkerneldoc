.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/policy.h

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

.. _`aa_get_newest_profile`:

aa_get_newest_profile
=====================

.. c:function:: struct aa_profile *aa_get_newest_profile(struct aa_profile *p)

    find the newest version of \ ``profile``\ 

    :param struct aa_profile \*p:
        *undescribed*

.. _`aa_get_newest_profile.return`:

Return
------

refcounted newest version of \ ``profile``\  taking into account
replacement, renames and removals
return \ ``profile``\ .

.. _`aa_put_profile`:

aa_put_profile
==============

.. c:function:: void aa_put_profile(struct aa_profile *p)

    decrement refcount on profile \ ``p``\ 

    :param struct aa_profile \*p:
        profile  (MAYBE NULL)

.. _`aa_get_namespace`:

aa_get_namespace
================

.. c:function:: struct aa_namespace *aa_get_namespace(struct aa_namespace *ns)

    increment references count on \ ``ns``\ 

    :param struct aa_namespace \*ns:
        namespace to increment reference count of (MAYBE NULL)

.. _`aa_get_namespace.return`:

Return
------

pointer to \ ``ns``\ , if \ ``ns``\  is NULL returns NULL

.. _`aa_get_namespace.requires`:

Requires
--------

\ ``ns``\  must be held with valid refcount when called

.. _`aa_put_namespace`:

aa_put_namespace
================

.. c:function:: void aa_put_namespace(struct aa_namespace *ns)

    decrement refcount on \ ``ns``\ 

    :param struct aa_namespace \*ns:
        namespace to put reference of

.. _`aa_put_namespace.description`:

Description
-----------

Decrement reference count of \ ``ns``\  and if no longer in use free it

.. This file was automatic generated / don't edit.

