.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/policy_ns.h

.. _`aa_get_ns`:

aa_get_ns
=========

.. c:function:: struct aa_ns *aa_get_ns(struct aa_ns *ns)

    increment references count on \ ``ns``\ 

    :param struct aa_ns \*ns:
        namespace to increment reference count of (MAYBE NULL)

.. _`aa_get_ns.return`:

Return
------

pointer to \ ``ns``\ , if \ ``ns``\  is NULL returns NULL

.. _`aa_get_ns.requires`:

Requires
--------

@ns must be held with valid refcount when called

.. _`aa_put_ns`:

aa_put_ns
=========

.. c:function:: void aa_put_ns(struct aa_ns *ns)

    decrement refcount on \ ``ns``\ 

    :param struct aa_ns \*ns:
        namespace to put reference of

.. _`aa_put_ns.description`:

Description
-----------

Decrement reference count of \ ``ns``\  and if no longer in use free it

.. _`__aa_findn_ns`:

__aa_findn_ns
=============

.. c:function:: struct aa_ns *__aa_findn_ns(struct list_head *head, const char *name, size_t n)

    find a namespace on a list by \ ``name``\ 

    :param struct list_head \*head:
        list to search for namespace on  (NOT NULL)

    :param const char \*name:
        name of namespace to look for  (NOT NULL)

    :param size_t n:
        length of \ ``name``\ 

.. _`__aa_findn_ns.return`:

Return
------

unrefcounted namespace

.. _`__aa_findn_ns.requires`:

Requires
--------

rcu_read_lock be held

.. This file was automatic generated / don't edit.

