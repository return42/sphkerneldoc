.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/secid.c

.. _`aa_secid_update`:

aa_secid_update
===============

.. c:function:: void aa_secid_update(u32 secid, struct aa_label *label)

    update a secid mapping to a new label

    :param u32 secid:
        secid to update

    :param struct aa_label \*label:
        label the secid will now map to

.. _`aa_alloc_secid`:

aa_alloc_secid
==============

.. c:function:: int aa_alloc_secid(struct aa_label *label, gfp_t gfp)

    allocate a new secid for a profile

    :param struct aa_label \*label:
        the label to allocate a secid for

    :param gfp_t gfp:
        memory allocation flags

.. _`aa_alloc_secid.return`:

Return
------

0 with \ ``label``\ ->secid initialized
<0 returns error with \ ``label``\ ->secid set to AA_SECID_INVALID

.. _`aa_free_secid`:

aa_free_secid
=============

.. c:function:: void aa_free_secid(u32 secid)

    free a secid

    :param u32 secid:
        secid to free

.. This file was automatic generated / don't edit.

