.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/domain.c

.. _`aa_free_domain_entries`:

aa_free_domain_entries
======================

.. c:function:: void aa_free_domain_entries(struct aa_domain *domain)

    free entries in a domain table

    :param domain:
        the domain table to free  (MAYBE NULL)
    :type domain: struct aa_domain \*

.. _`may_change_ptraced_domain`:

may_change_ptraced_domain
=========================

.. c:function:: int may_change_ptraced_domain(struct aa_label *to_label, const char **info)

    check if can change profile on ptraced task

    :param to_label:
        profile to change to  (NOT NULL)
    :type to_label: struct aa_label \*

    :param info:
        message if there is an error
    :type info: const char \*\*

.. _`may_change_ptraced_domain.description`:

Description
-----------

Check if current is ptraced and if so if the tracing task is allowed
to trace the new domain

.. _`may_change_ptraced_domain.return`:

Return
------

\ ``0``\  or error if change not allowed

.. _`label_compound_match`:

label_compound_match
====================

.. c:function:: int label_compound_match(struct aa_profile *profile, struct aa_label *label, bool stack, unsigned int state, bool subns, u32 request, struct aa_perms *perms)

    find perms for full compound label

    :param profile:
        profile to find perms for
    :type profile: struct aa_profile \*

    :param label:
        label to check access permissions for
    :type label: struct aa_label \*

    :param stack:
        whether this is a stacking request
    :type stack: bool

    :param state:
        *undescribed*
    :type state: unsigned int

    :param subns:
        whether to do permission checks on components in a subns
    :type subns: bool

    :param request:
        permissions to request
    :type request: u32

    :param perms:
        perms struct to set
    :type perms: struct aa_perms \*

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

    :param profile:
        profile to find perms for
    :type profile: struct aa_profile \*

    :param label:
        label to check access permissions for
    :type label: struct aa_label \*

    :param stack:
        whether this is a stacking request
    :type stack: bool

    :param start:
        state to start match in
    :type start: unsigned int

    :param subns:
        whether to do permission checks on components in a subns
    :type subns: bool

    :param request:
        permissions to request
    :type request: u32

    :param perms:
        an initialized perms struct to add accumulation to
    :type perms: struct aa_perms \*

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

    :param profile:
        profile to match against (NOT NULL)
    :type profile: struct aa_profile \*

    :param label:
        label to match (NOT NULL)
    :type label: struct aa_label \*

    :param stack:
        whether this is a stacking request
    :type stack: bool

    :param state:
        state to start in
    :type state: unsigned int

    :param subns:
        whether to match subns components
    :type subns: bool

    :param request:
        permission request
    :type request: u32

    :param perms:
        Returns computed perms (NOT NULL)
    :type perms: struct aa_perms \*

.. _`label_match.return`:

Return
------

the state the match finished in, may be the none matching state

.. _`change_profile_perms`:

change_profile_perms
====================

.. c:function:: int change_profile_perms(struct aa_profile *profile, struct aa_label *target, bool stack, u32 request, unsigned int start, struct aa_perms *perms)

    find permissions for change_profile

    :param profile:
        the current profile  (NOT NULL)
    :type profile: struct aa_profile \*

    :param target:
        label to transition to (NOT NULL)
    :type target: struct aa_label \*

    :param stack:
        whether this is a stacking request
    :type stack: bool

    :param request:
        requested perms
    :type request: u32

    :param start:
        state to start matching in
    :type start: unsigned int

    :param perms:
        *undescribed*
    :type perms: struct aa_perms \*

.. _`change_profile_perms.return`:

Return
------

permission set

currently only matches full label A//&B//&C or individual components A, B, C
not arbitrary combinations. Eg. A//&B, C

.. _`aa_xattrs_match`:

aa_xattrs_match
===============

.. c:function:: int aa_xattrs_match(const struct linux_binprm *bprm, struct aa_profile *profile, unsigned int state)

    check whether a file matches the xattrs defined in profile

    :param bprm:
        binprm struct for the process to validate
    :type bprm: const struct linux_binprm \*

    :param profile:
        profile to match against (NOT NULL)
    :type profile: struct aa_profile \*

    :param state:
        state to start match in
    :type state: unsigned int

.. _`aa_xattrs_match.return`:

Return
------

number of extended attributes that matched, or < 0 on error

.. _`__attach_match`:

\__attach_match
===============

.. c:function:: struct aa_profile *__attach_match(const struct linux_binprm *bprm, const char *name, struct list_head *head, const char **info)

    find an attachment match \ ``bprm``\  - binprm structure of transitioning task \ ``name``\  - to match against  (NOT NULL) \ ``head``\  - profile list to walk  (NOT NULL) \ ``info``\  - info message if there was an error (NOT NULL)

    :param bprm:
        *undescribed*
    :type bprm: const struct linux_binprm \*

    :param name:
        *undescribed*
    :type name: const char \*

    :param head:
        *undescribed*
    :type head: struct list_head \*

    :param info:
        *undescribed*
    :type info: const char \*\*

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

\ ``head``\  not be shared or have appropriate locks held

.. _`__attach_match.return`:

Return
------

profile or NULL if no match found

.. _`find_attach`:

find_attach
===========

.. c:function:: struct aa_label *find_attach(const struct linux_binprm *bprm, struct aa_ns *ns, struct list_head *list, const char *name, const char **info)

    do attachment search for unconfined processes \ ``bprm``\  - binprm structure of transitioning task

    :param bprm:
        *undescribed*
    :type bprm: const struct linux_binprm \*

    :param ns:
        the current namespace  (NOT NULL)
    :type ns: struct aa_ns \*

    :param list:
        list to search  (NOT NULL)
    :type list: struct list_head \*

    :param name:
        the executable name to match against  (NOT NULL)
    :type name: const char \*

    :param info:
        info message if there was an error
    :type info: const char \*\*

.. _`find_attach.return`:

Return
------

label or NULL if no match found

.. _`x_table_lookup`:

x_table_lookup
==============

.. c:function:: struct aa_label *x_table_lookup(struct aa_profile *profile, u32 xindex, const char **name)

    lookup an x transition name via transition table

    :param profile:
        current profile (NOT NULL)
    :type profile: struct aa_profile \*

    :param xindex:
        index into x transition table
    :type xindex: u32

    :param name:
        returns: name tested to find label (NOT NULL)
    :type name: const char \*\*

.. _`x_table_lookup.return`:

Return
------

refcounted label, or NULL on failure (MAYBE NULL)

.. _`x_to_label`:

x_to_label
==========

.. c:function:: struct aa_label *x_to_label(struct aa_profile *profile, const struct linux_binprm *bprm, const char *name, u32 xindex, const char **lookupname, const char **info)

    get target label for a given xindex

    :param profile:
        current profile  (NOT NULL)
    :type profile: struct aa_profile \*

    :param bprm:
        binprm structure of transitioning task
    :type bprm: const struct linux_binprm \*

    :param name:
        name to lookup (NOT NULL)
    :type name: const char \*

    :param xindex:
        index into x transition table
    :type xindex: u32

    :param lookupname:
        returns: name used in lookup if one was specified (NOT NULL)
    :type lookupname: const char \*\*

    :param info:
        *undescribed*
    :type info: const char \*\*

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

    :param bprm:
        binprm for the exec  (NOT NULL)
    :type bprm: struct linux_binprm \*

.. _`apparmor_bprm_set_creds.return`:

Return
------

\ ``0``\  or error on failure

.. _`apparmor_bprm_set_creds.todo`:

TODO
----

once the other paths are done see if we can't refactor into a fn

.. _`aa_change_hat`:

aa_change_hat
=============

.. c:function:: int aa_change_hat(const char  *hats, int count, u64 token, int flags)

    change hat to/from subprofile

    :param hats:
        vector of hat names to try changing into (MAYBE NULL if \ ``count``\  == 0)
    :type hats: const char  \*

    :param count:
        number of hat names in \ ``hats``\ 
    :type count: int

    :param token:
        magic value to validate the hat change
    :type token: u64

    :param flags:
        flags affecting behavior of the change
    :type flags: int

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

    :param fqname:
        name of profile may include namespace (NOT NULL)
    :type fqname: const char \*

    :param flags:
        flags affecting change behavior
    :type flags: int

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

