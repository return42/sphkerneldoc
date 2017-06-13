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

.. c:function:: int may_change_ptraced_domain(struct aa_profile *to_profile)

    check if can change profile on ptraced task

    :param struct aa_profile \*to_profile:
        profile to change to  (NOT NULL)

.. _`may_change_ptraced_domain.description`:

Description
-----------

Check if current is ptraced and if so if the tracing task is allowed
to trace the new domain

.. _`may_change_ptraced_domain.return`:

Return
------

%0 or error if change not allowed

.. _`change_profile_perms`:

change_profile_perms
====================

.. c:function:: struct file_perms change_profile_perms(struct aa_profile *profile, struct aa_ns *ns, const char *name, u32 request, unsigned int start)

    find permissions for change_profile

    :param struct aa_profile \*profile:
        the current profile  (NOT NULL)

    :param struct aa_ns \*ns:
        the namespace being switched to  (NOT NULL)

    :param const char \*name:
        the name of the profile to change to  (NOT NULL)

    :param u32 request:
        requested perms

    :param unsigned int start:
        state to start matching in

.. _`change_profile_perms.return`:

Return
------

permission set

.. _`__attach_match`:

__attach_match
==============

.. c:function:: struct aa_profile *__attach_match(const char *name, struct list_head *head)

    find an attachment match \ ``name``\  - to match against  (NOT NULL) \ ``head``\  - profile list to walk  (NOT NULL)

    :param const char \*name:
        *undescribed*

    :param struct list_head \*head:
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

.. c:function:: struct aa_profile *find_attach(struct aa_ns *ns, struct list_head *list, const char *name)

    do attachment search for unconfined processes

    :param struct aa_ns \*ns:
        the current namespace  (NOT NULL)

    :param struct list_head \*list:
        list to search  (NOT NULL)

    :param const char \*name:
        the executable name to match against  (NOT NULL)

.. _`find_attach.return`:

Return
------

profile or NULL if no match found

.. _`separate_fqname`:

separate_fqname
===============

.. c:function:: const char *separate_fqname(const char *fqname, const char **ns_name)

    separate the namespace and profile names

    :param const char \*fqname:
        the fqname name to split  (NOT NULL)

    :param const char \*\*ns_name:
        the namespace name if it exists  (NOT NULL)

.. _`separate_fqname.description`:

Description
-----------

This is the xtable equivalent routine of aa_split_fqname.  It finds the
split in an xtable fqname which contains an embedded \0 instead of a :
if a namespace is specified.  This is done so the xtable is constant and
isn't re-split on every lookup.

Either the profile or namespace name may be optional but if the namespace
is specified the profile name termination must be present.  This results

.. _`separate_fqname.in-the-following-possible-encodings`:

in the following possible encodings
-----------------------------------

profile_name\0
:ns_name\0profile_name\0
:ns_name\0\0

.. _`separate_fqname.note`:

NOTE
----

the xtable fqname is pre-validated at load time in unpack_trans_table

.. _`separate_fqname.return`:

Return
------

profile name if it is specified else NULL

.. _`x_table_lookup`:

x_table_lookup
==============

.. c:function:: struct aa_profile *x_table_lookup(struct aa_profile *profile, u32 xindex)

    lookup an x transition name via transition table

    :param struct aa_profile \*profile:
        current profile (NOT NULL)

    :param u32 xindex:
        index into x transition table

.. _`x_table_lookup.return`:

Return
------

refcounted profile, or NULL on failure (MAYBE NULL)

.. _`x_to_profile`:

x_to_profile
============

.. c:function:: struct aa_profile *x_to_profile(struct aa_profile *profile, const char *name, u32 xindex)

    get target profile for a given xindex

    :param struct aa_profile \*profile:
        current profile  (NOT NULL)

    :param const char \*name:
        name to lookup (NOT NULL)

    :param u32 xindex:
        index into x transition table

.. _`x_to_profile.description`:

Description
-----------

find profile for a transition index

.. _`x_to_profile.return`:

Return
------

refcounted profile or NULL if not found available

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

.. _`apparmor_bprm_secureexec`:

apparmor_bprm_secureexec
========================

.. c:function:: int apparmor_bprm_secureexec(struct linux_binprm *bprm)

    determine if secureexec is needed

    :param struct linux_binprm \*bprm:
        binprm for exec  (NOT NULL)

.. _`apparmor_bprm_secureexec.return`:

Return
------

%1 if secureexec is needed else \ ``0``\ 

.. _`apparmor_bprm_committing_creds`:

apparmor_bprm_committing_creds
==============================

.. c:function:: void apparmor_bprm_committing_creds(struct linux_binprm *bprm)

    do task cleanup on committing new creds

    :param struct linux_binprm \*bprm:
        binprm for the exec  (NOT NULL)

.. _`apparmor_bprm_committed_creds`:

apparmor_bprm_committed_creds
=============================

.. c:function:: void apparmor_bprm_committed_creds(struct linux_binprm *bprm)

    do cleanup after new creds committed

    :param struct linux_binprm \*bprm:
        binprm for the exec  (NOT NULL)

.. _`new_compound_name`:

new_compound_name
=================

.. c:function:: char *new_compound_name(const char *n1, const char *n2)

    create an hname with \ ``n2``\  appended to \ ``n1``\ 

    :param const char \*n1:
        base of hname  (NOT NULL)

    :param const char \*n2:
        name to append (NOT NULL)

.. _`new_compound_name.return`:

Return
------

new name or NULL on error

.. _`aa_change_hat`:

aa_change_hat
=============

.. c:function:: int aa_change_hat(const char  *hats[], int count, u64 token, bool permtest)

    change hat to/from subprofile

    :param const char  \*hats:
        vector of hat names to try changing into (MAYBE NULL if \ ``count``\  == 0)

    :param int count:
        number of hat names in \ ``hats``\ 

    :param u64 token:
        magic value to validate the hat change

    :param bool permtest:
        true if this is just a permission test

.. _`aa_change_hat.description`:

Description
-----------

Change to the first profile specified in \ ``hats``\  that exists, and store
the \ ``hat_magic``\  in the current task context.  If the count == 0 and the
\ ``token``\  matches that stored in the current task context, return to the
top level profile.

Returns \ ``0``\  on success, error otherwise.

.. _`aa_change_profile`:

aa_change_profile
=================

.. c:function:: int aa_change_profile(const char *fqname, bool onexec, bool permtest, bool stack)

    perform a one-way profile transition

    :param const char \*fqname:
        name of profile may include namespace (NOT NULL)

    :param bool onexec:
        whether this transition is to take place immediately or at exec

    :param bool permtest:
        true if this is just a permission test

    :param bool stack:
        *undescribed*

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

