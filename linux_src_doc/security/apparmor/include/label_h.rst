.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/label.h

.. _`__aa_get_label`:

\__aa_get_label
===============

.. c:function:: struct aa_label *__aa_get_label(struct aa_label *l)

    get a reference count to uncounted label reference

    :param struct aa_label \*l:
        reference to get a count on

.. _`__aa_get_label.return`:

Return
------

pointer to reference OR NULL if race is lost and reference is
being repeated.

.. _`__aa_get_label.requires`:

Requires
--------

lock held, and the return code MUST be checked

.. _`aa_get_label_rcu`:

aa_get_label_rcu
================

.. c:function:: struct aa_label *aa_get_label_rcu(struct aa_label __rcu **l)

    increment refcount on a label that can be replaced

    :param struct aa_label __rcu \*\*l:
        pointer to label that can be replaced (NOT NULL)

.. _`aa_get_label_rcu.return`:

Return
------

pointer to a refcounted label.
else NULL if no label

.. _`aa_get_newest_label`:

aa_get_newest_label
===================

.. c:function:: struct aa_label *aa_get_newest_label(struct aa_label *l)

    find the newest version of \ ``l``\ 

    :param struct aa_label \*l:
        the label to check for newer versions of

.. _`aa_get_newest_label.return`:

Return
------

refcounted newest version of \ ``l``\  taking into account
replacement, renames and removals
return \ ``l``\ .

.. This file was automatic generated / don't edit.

