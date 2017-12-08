.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/domain.c

.. _`aa_free_domain_entries`:

aa_free_domain_entries
======================

.. c:function:: void aa_free_domain_entries(struct aa_domain *domain)

    free entries in a domain table

    :param struct aa_domain \*domain:
        the domain table to free  (MAYBE NULL)

.. _`may_change_ptraced_domain`:

may_change_ptraced_domain
=========================

.. c:function:: int may_change_ptraced_domain(struct aa_label *to_label, const char **info)

    check if can change profile on ptraced task

    :param struct aa_label \*to_label:
        profile to change to  (NOT NULL)

    :param const char \*\*info:
        message if there is an error

.. _`may_change_ptraced_domain.description`:

Description
-----------

Check if current is ptraced and if so if the tracing task is allowed
to trace the new domain

.. _`may_change_ptraced_domain.return`:

Return
------

%0 or error if change not allowed

.. _`label_compound_match`:

label_compound_match
====================

.. c:function:: int label_compound_match(struct aa_profile *profile, struct aa_label *label, bool stack, unsigned int state, bool subns, u32 request, struct aa_perms *perms)

    find perms for full compound label

    :param struct aa_profile \*profile:
        profile to find perms for

    :param struct aa_label \*label:
        label to check access permissions for

    :param bool stack:
        whether this is a stacking request

    :param unsigned int state:
        *undescribed*

    :param bool subns:
        whether to do permission checks on components in a subns

    :param u32 request:
        permissions to request

    :param struct aa_perms \*perms:
        perms struct to set

.. _`label_compound_match.return`:

Return
------

0 on success else ERROR

For the label A//&B//&C this does the perm match for A//&B//&C
\ ``perms``\  should be preinitialized with allperms OR a previous permission
check to be stacked.

.. _`label_components_match`:

label_components_match
======================

.. c:function:: int label_components_match(struct aa_profile *profile, struct aa_label *label, bool stack, unsigned int start, bool subns, u32 request, struct aa_perms *perms)

    find perms for all subcomponents of a label

    :param struct aa_profile \*profile:
        profile to find perms for

    :param struct aa_label \*label:
        label to check access permissions for

    :param bool stack:
        whether this is a stacking request

    :param unsigned int start:
        state to start match in

    :param bool subns:
        whether to do permission checks on components in a subns

    :param u32 request:
        permissions to request

    :param struct aa_perms \*perms:
        an initialized perms struct to add accumulation to

.. _`label_components_match.return`:

Return
------

0 on success else ERROR

For the label A//&B//&C this does the perm match for each of A and B and C
\ ``perms``\  should be preinitialized with allperms OR a previous permission
check to be stacked.

.. _`label_match`:

label_match
===========

.. c:function:: int label_match(struct aa_profile *profile, struct aa_label *label, bool stack, unsigned int state, bool subns, u32 request, struct aa_perms *perms)

    do a multi-component label match

    :param struct aa_profile \*profile:
        profile to match against (NOT NULL)

    :param struct aa_label \*label:
        label to match (NOT NULL)

    :param bool stack:
        whether this is a stacking request

    :param unsigned int state:
        state to start in

    :param bool subns:
        whether to match subns components

    :param u32 request:
        permission request

    :param struct aa_perms \*perms:
        Returns computed perms (NOT NULL)

.. _`label_match.return`:

Return
------

the state the match finished in, may be the none matching state

.. _`change_profile_perms`:

change_profile_perms
====================

.. c:function:: int change_profile_perms(struct aa_profile *profile, struct aa_label *target, bool stack, u32 request, unsigned int start, struct aa_perms *perms)

    find permissions for change_profile

    :param struct aa_profile \*profile:
        the current profile  (NOT NULL)

    :param struct aa_label \*target:
        label to transition to (NOT NULL)

    :param bool stack:
        whether this is a stacking request

    :param u32 request:
        requested perms

    :param unsigned int start:
        state to start matching in

    :param struct aa_perms \*perms:
        *undescribed*

.. _`change_profile_perms.return`:

Return
------

permission set

currently only matches full label A//&B//&C or individual components A, B, C
not arbitrary combinations. Eg. A//&B, C

.. _`__attach_match`:

__attach_match
==============

.. c:function:: struct aa_profile *__attach_match(const char *name, struct list_head *head, const char **info)

    find an attachment match \ ``name``\  - to match against  (NOT NULL) \ ``head``\  - profile list to walk  (NOT NULL) \ ``info``\  - info message if there was an error (NOT NULL)

    :param const char \*name:
        *undescribed*

    :param struct list_head \*head:
        *undescribed*

    :param const char \*\*info:
        *undescribed*

.. _`__attach_match.description`:

Description
-----------

Do a linear search on the profiles in the list.  There is a matching
preference where an exact match is preferred over a name which uses
expressions to match, and matching expressions with the greatest
xmatch_len are preferred.

.. _`__attach_match.requires`:

Requires
--------

@head not be shared or have appropriate locks held

.. _`__attach_match.return`:

Return
------

profile or NULL if no match found

.. _`find_attach`:

find_attach
===========

.. c:function:: struct aa_label *find_attach(struct aa_ns *ns, struct list_head *list, const char *name, const char **info)

    do attachment search for unconfined processes

    :param struct aa_ns \*ns:
        the current namespace  (NOT NULL)

    :param struct list_head \*list:
        list to search  (NOT NULL)

    :param const char \*name:
        the executable name to match against  (NOT NULL)

    :param const char \*\*info:
        info message if there was an error

.. _`find_attach.return`:

Return
------

label or NULL if no match found

.. _`x_table_lookup`:

x_table_lookup
==============

.. c:function:: struct aa_label *x_table_lookup(struct aa_profile *profile, u32 xindex, const char **name)

    lookup an x transition name via transition table

    :param struct aa_profile \*profile:
        current profile (NOT NULL)

    :param u32 xindex:
        index into x transition table

    :param const char \*\*name:
        returns: name tested to find label (NOT NULL)

.. _`x_table_lookup.return`:

Return
------

refcounted label, or NULL on failure (MAYBE NULL)

.. _`x_to_label`:

x_to_label
==========

.. c:function:: struct aa_label *x_to_label(struct aa_profile *profile, const char *name, u32 xindex, const char **lookupname, const char **info)

    get target label for a given xindex

    :param struct aa_profile \*profile:
        current profile  (NOT NULL)

    :param const char \*name:
        name to lookup (NOT NULL)

    :param u32 xindex:
        index into x transition table

    :param const char \*\*lookupname:
        returns: name used in lookup if one was specified (NOT NULL)

    :param const char \*\*info:
        *undescribed*

.. _`x_to_label.description`:

Description
-----------

find label for a transition index

.. _`x_to_label.return`:

Return
------

refcounted label or NULL if not found available

.. _`apparmor_bprm_set_creds`:

apparmor_bprm_set_creds
=======================

.. c:function:: int apparmor_bprm_set_creds(struct linux_binprm *bprm)

    set the new creds on the bprm struct

    :param struct linux_binprm \*bprm:
        binprm for the exec  (NOT NULL)

.. _`apparmor_bprm_set_creds.return`:

Return
------

%0 or error on failure

.. _`apparmor_bprm_set_creds.todo`:

TODO
----

once the other paths are done see if we can't refactor into a fn

.. _`aa_change_hat`:

aa_change_hat
=============

.. c:function:: int aa_change_hat(const char  *hats, int count, u64 token, int flags)

    change hat to/from subprofile

    :param const char  \*hats:
        vector of hat names to try changing into (MAYBE NULL if \ ``count``\  == 0)

    :param int count:
        number of hat names in \ ``hats``\ 

    :param u64 token:
        magic value to validate the hat change

    :param int flags:
        flags affecting behavior of the change

.. _`aa_change_hat.description`:

Description
-----------

Returns \ ``0``\  on success, error otherwise.

Change to the first profile specified in \ ``hats``\  that exists, and store
the \ ``hat_magic``\  in the current task context.  If the count == 0 and the
\ ``token``\  matches that stored in the current task context, return to the
top level profile.

change_hat only applies to profiles in the current ns, and each profile
in the ns must make the same transition otherwise change_hat will fail.

.. _`aa_change_profile`:

aa_change_profile
=================

.. c:function:: int aa_change_profile(const char *fqname, int flags)

    perform a one-way profile transition

    :param const char \*fqname:
        name of profile may include namespace (NOT NULL)

    :param int flags:
        flags affecting change behavior

.. _`aa_change_profile.description`:

Description
-----------

Change to new profile \ ``name``\ .  Unlike with hats, there is no way
to change back.  If \ ``name``\  isn't specified the current profile name is
used.
If \ ``onexec``\  then the transition is delayed until
the next exec.

Returns \ ``0``\  on success, error otherwise.

.. This file was automatic generated / don't edit.

