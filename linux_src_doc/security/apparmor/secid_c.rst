.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/secid.c

.. _`aa_secid_update`:

aa_secid_update
===============

.. c:function:: void aa_secid_update(u32 secid, struct aa_label *label)

    update a secid mapping to a new label

    :param secid:
        secid to update
    :type secid: u32

    :param label:
        label the secid will now map to
    :type label: struct aa_label \*

.. _`aa_alloc_secid`:

aa_alloc_secid
==============

.. c:function:: int aa_alloc_secid(struct aa_label *label, gfp_t gfp)

    allocate a new secid for a profile

    :param label:
        the label to allocate a secid for
    :type label: struct aa_label \*

    :param gfp:
        memory allocation flags
    :type gfp: gfp_t

.. _`aa_alloc_secid.return`:

Return
------

0 with \ ``label->secid``\  initialized
<0 returns error with \ ``label->secid``\  set to AA_SECID_INVALID

.. _`aa_free_secid`:

aa_free_secid
=============

.. c:function:: void aa_free_secid(u32 secid)

    free a secid

    :param secid:
        secid to free
    :type secid: u32

.. This file was automatic generated / don't edit.

