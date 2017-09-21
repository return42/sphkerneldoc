.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/lib.c

.. _`aa_split_fqname`:

aa_split_fqname
===============

.. c:function:: char *aa_split_fqname(char *fqname, char **ns_name)

    split a fqname into a profile and namespace name

    :param char \*fqname:
        a full qualified name in namespace profile format (NOT NULL)

    :param char \*\*ns_name:
        pointer to portion of the string containing the ns name (NOT NULL)

.. _`aa_split_fqname.return`:

Return
------

profile name or NULL if one is not specified

Split a namespace name from a profile name (see policy.c for naming
description).  If a portion of the name is missing it returns NULL for
that portion.

.. _`aa_split_fqname.note`:

NOTE
----

may modify the \ ``fqname``\  string.  The pointers returned point
into the \ ``fqname``\  string.

.. _`skipn_spaces`:

skipn_spaces
============

.. c:function:: const char *skipn_spaces(const char *str, size_t n)

    Removes leading whitespace from \ ``str``\ .

    :param const char \*str:
        The string to be stripped.

    :param size_t n:
        *undescribed*

.. _`skipn_spaces.description`:

Description
-----------

Returns a pointer to the first non-whitespace character in \ ``str``\ .
if all whitespace will return NULL

.. _`aa_info_message`:

aa_info_message
===============

.. c:function:: void aa_info_message(const char *str)

    log a none profile related status message

    :param const char \*str:
        message to log

.. _`aa_perm_mask_to_str`:

aa_perm_mask_to_str
===================

.. c:function:: void aa_perm_mask_to_str(char *str, const char *chrs, u32 mask)

    convert a perm mask to its short string

    :param char \*str:
        character buffer to store string in (at least 10 characters)

    :param const char \*chrs:
        *undescribed*

    :param u32 mask:
        permission mask to convert

.. _`aa_audit_perms_cb`:

aa_audit_perms_cb
=================

.. c:function:: void aa_audit_perms_cb(struct audit_buffer *ab, void *va)

    generic callback fn for auditing perms

    :param struct audit_buffer \*ab:
        audit buffer (NOT NULL)

    :param void \*va:
        audit struct to audit values of (NOT NULL)

.. _`aa_apply_modes_to_perms`:

aa_apply_modes_to_perms
=======================

.. c:function:: void aa_apply_modes_to_perms(struct aa_profile *profile, struct aa_perms *perms)

    apply namespace and profile flags to perms

    :param struct aa_profile \*profile:
        that perms where computed from

    :param struct aa_perms \*perms:
        perms to apply mode modifiers to

.. _`aa_apply_modes_to_perms.todo`:

TODO
----

split into profile and ns based flags for when accumulating perms

.. _`aa_perms_accum_raw`:

aa_perms_accum_raw
==================

.. c:function:: void aa_perms_accum_raw(struct aa_perms *accum, struct aa_perms *addend)

    accumulate perms with out masking off overlapping perms \ ``accum``\  - perms struct to accumulate into \ ``addend``\  - perms struct to add to \ ``accum``\ 

    :param struct aa_perms \*accum:
        *undescribed*

    :param struct aa_perms \*addend:
        *undescribed*

.. _`aa_perms_accum`:

aa_perms_accum
==============

.. c:function:: void aa_perms_accum(struct aa_perms *accum, struct aa_perms *addend)

    accumulate perms, masking off overlapping perms \ ``accum``\  - perms struct to accumulate into \ ``addend``\  - perms struct to add to \ ``accum``\ 

    :param struct aa_perms \*accum:
        *undescribed*

    :param struct aa_perms \*addend:
        *undescribed*

.. _`aa_check_perms`:

aa_check_perms
==============

.. c:function:: int aa_check_perms(struct aa_profile *profile, struct aa_perms *perms, u32 request, struct common_audit_data *sa, void (*cb)(struct audit_buffer *, void *))

    do audit mode selection based on perms set

    :param struct aa_profile \*profile:
        profile being checked

    :param struct aa_perms \*perms:
        perms computed for the request

    :param u32 request:
        requested perms

    :param struct common_audit_data \*sa:
        initialized audit structure (MAY BE NULL if not auditing)

    :param void (\*cb)(struct audit_buffer \*, void \*):
        callback fn for tpye specific fields (MAY BE NULL)

.. _`aa_check_perms.return`:

Return
------

0 if permission else error code

.. _`aa_check_perms.note`:

Note
----

profile audit modes need to be set before calling by setting the
perm masks appropriately.

If not auditing then complain mode is not enabled and the
error code will indicate whether there was an explicit deny
with a positive value.

.. _`aa_policy_init`:

aa_policy_init
==============

.. c:function:: bool aa_policy_init(struct aa_policy *policy, const char *prefix, const char *name, gfp_t gfp)

    initialize a policy structure

    :param struct aa_policy \*policy:
        policy to initialize  (NOT NULL)

    :param const char \*prefix:
        prefix name if any is required.  (MAYBE NULL)

    :param const char \*name:
        name of the policy, init will make a copy of it  (NOT NULL)

    :param gfp_t gfp:
        allocation mode

.. _`aa_policy_init.note`:

Note
----

this fn creates a copy of strings passed in

.. _`aa_policy_init.return`:

Return
------

true if policy init successful

.. _`aa_policy_destroy`:

aa_policy_destroy
=================

.. c:function:: void aa_policy_destroy(struct aa_policy *policy)

    free the elements referenced by \ ``policy``\ 

    :param struct aa_policy \*policy:
        policy that is to have its elements freed  (NOT NULL)

.. This file was automatic generated / don't edit.

