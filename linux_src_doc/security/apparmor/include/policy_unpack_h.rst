.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/policy_unpack.h

.. _`__aa_get_loaddata`:

\__aa_get_loaddata
==================

.. c:function:: struct aa_loaddata *__aa_get_loaddata(struct aa_loaddata *data)

    get a reference count to uncounted data reference

    :param struct aa_loaddata \*data:
        reference to get a count on

.. _`__aa_get_loaddata.return`:

Return
------

pointer to reference OR NULL if race is lost and reference is
being repeated.

.. _`__aa_get_loaddata.requires`:

Requires
--------

\ ``data``\ ->ns->lock held, and the return code MUST be checked

Use only from inode->i_private and \ ``data``\ ->list found references

.. _`aa_get_loaddata`:

aa_get_loaddata
===============

.. c:function:: struct aa_loaddata *aa_get_loaddata(struct aa_loaddata *data)

    get a reference count from a counted data reference

    :param struct aa_loaddata \*data:
        reference to get a count on

.. _`aa_get_loaddata.return`:

Return
------

point to reference

.. _`aa_get_loaddata.requires`:

Requires
--------

\ ``data``\  to have a valid reference count on it. It is a bug
if the race to reap can be encountered when it is used.

.. This file was automatic generated / don't edit.

