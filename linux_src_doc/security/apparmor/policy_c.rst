.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/policy.c

.. _`__add_profile`:

\__add_profile
==============

.. c:function:: void __add_profile(struct list_head *list, struct aa_profile *profile)

    add a profiles to list and label tree

    :param list:
        list to add it to  (NOT NULL)
    :type list: struct list_head \*

    :param profile:
        the profile to add  (NOT NULL)
    :type profile: struct aa_profile \*

.. _`__add_profile.description`:

Description
-----------

refcount \ ``profile``\ , should be put by \__list_remove_profile

.. _`__add_profile.requires`:

Requires
--------

namespace lock be held, or list not be shared

.. _`__list_remove_profile`:

\__list_remove_profile
======================

.. c:function:: void __list_remove_profile(struct aa_profile *profile)

    remove a profile from the list it is on

    :param profile:
        the profile to remove  (NOT NULL)
    :type profile: struct aa_profile \*

.. _`__list_remove_profile.description`:

Description
-----------

remove a profile from the list, warning generally removal should
be done with \__replace_profile as most profile removals are
replacements to the unconfined profile.

put \ ``profile``\  list refcount

.. _`__list_remove_profile.requires`:

Requires
--------

namespace lock be held, or list not have been live

.. _`__remove_profile`:

\__remove_profile
=================

.. c:function:: void __remove_profile(struct aa_profile *profile)

    remove old profile, and children

    :param profile:
        profile to be replaced  (NOT NULL)
    :type profile: struct aa_profile \*

.. _`__remove_profile.requires`:

Requires
--------

namespace list lock be held, or list not be shared

.. _`__aa_profile_list_release`:

\__aa_profile_list_release
==========================

.. c:function:: void __aa_profile_list_release(struct list_head *head)

    remove all profiles on the list and put refs

    :param head:
        list of profiles  (NOT NULL)
    :type head: struct list_head \*

.. _`__aa_profile_list_release.requires`:

Requires
--------

namespace lock be held

.. _`aa_free_data`:

aa_free_data
============

.. c:function:: void aa_free_data(void *ptr, void *arg)

    free a data blob

    :param ptr:
        data to free
    :type ptr: void \*

    :param arg:
        unused
    :type arg: void \*

.. _`aa_free_profile`:

aa_free_profile
===============

.. c:function:: void aa_free_profile(struct aa_profile *profile)

    free a profile

    :param profile:
        the profile to free  (MAYBE NULL)
    :type profile: struct aa_profile \*

.. _`aa_free_profile.description`:

Description
-----------

Free a profile, its hats and null_profile. All references to the profile,
its hats and null_profile must have been put.

If the profile was referenced from a task context, \ :c:func:`free_profile`\  will
be called from an rcu callback routine, so we must not sleep here.

.. _`aa_alloc_profile`:

aa_alloc_profile
================

.. c:function:: struct aa_profile *aa_alloc_profile(const char *hname, struct aa_proxy *proxy, gfp_t gfp)

    allocate, initialize and return a new profile

    :param hname:
        name of the profile  (NOT NULL)
    :type hname: const char \*

    :param proxy:
        *undescribed*
    :type proxy: struct aa_proxy \*

    :param gfp:
        allocation type
    :type gfp: gfp_t

.. _`aa_alloc_profile.return`:

Return
------

refcount profile or NULL on failure

.. _`__strn_find_child`:

\__strn_find_child
==================

.. c:function:: struct aa_profile *__strn_find_child(struct list_head *head, const char *name, int len)

    find a profile on \ ``head``\  list using substring of \ ``name``\ 

    :param head:
        list to search  (NOT NULL)
    :type head: struct list_head \*

    :param name:
        name of profile (NOT NULL)
    :type name: const char \*

    :param len:
        length of \ ``name``\  substring to match
    :type len: int

.. _`__strn_find_child.requires`:

Requires
--------

rcu_read_lock be held

.. _`__strn_find_child.return`:

Return
------

unrefcounted profile ptr, or NULL if not found

.. _`__find_child`:

\__find_child
=============

.. c:function:: struct aa_profile *__find_child(struct list_head *head, const char *name)

    find a profile on \ ``head``\  list with a name matching \ ``name``\ 

    :param head:
        list to search  (NOT NULL)
    :type head: struct list_head \*

    :param name:
        name of profile (NOT NULL)
    :type name: const char \*

.. _`__find_child.requires`:

Requires
--------

rcu_read_lock be held

.. _`__find_child.return`:

Return
------

unrefcounted profile ptr, or NULL if not found

.. _`aa_find_child`:

aa_find_child
=============

.. c:function:: struct aa_profile *aa_find_child(struct aa_profile *parent, const char *name)

    find a profile by \ ``name``\  in \ ``parent``\ 

    :param parent:
        profile to search  (NOT NULL)
    :type parent: struct aa_profile \*

    :param name:
        profile name to search for  (NOT NULL)
    :type name: const char \*

.. _`aa_find_child.return`:

Return
------

a refcounted profile or NULL if not found

.. _`__lookup_parent`:

\__lookup_parent
================

.. c:function:: struct aa_policy *__lookup_parent(struct aa_ns *ns, const char *hname)

    lookup the parent of a profile of name \ ``hname``\ 

    :param ns:
        namespace to lookup profile in  (NOT NULL)
    :type ns: struct aa_ns \*

    :param hname:
        hierarchical profile name to find parent of  (NOT NULL)
    :type hname: const char \*

.. _`__lookup_parent.description`:

Description
-----------

Lookups up the parent of a fully qualified profile name, the profile
that matches hname does not need to exist, in general this
is used to load a new profile.

.. _`__lookup_parent.requires`:

Requires
--------

rcu_read_lock be held

.. _`__lookup_parent.return`:

Return
------

unrefcounted policy or NULL if not found

.. _`__lookupn_profile`:

\__lookupn_profile
==================

.. c:function:: struct aa_profile *__lookupn_profile(struct aa_policy *base, const char *hname, size_t n)

    lookup the profile matching \ ``hname``\ 

    :param base:
        base list to start looking up profile name from  (NOT NULL)
    :type base: struct aa_policy \*

    :param hname:
        hierarchical profile name  (NOT NULL)
    :type hname: const char \*

    :param n:
        length of \ ``hname``\ 
    :type n: size_t

.. _`__lookupn_profile.requires`:

Requires
--------

rcu_read_lock be held

.. _`__lookupn_profile.return`:

Return
------

unrefcounted profile pointer or NULL if not found

Do a relative name lookup, recursing through profile tree.

.. _`aa_lookupn_profile`:

aa_lookupn_profile
==================

.. c:function:: struct aa_profile *aa_lookupn_profile(struct aa_ns *ns, const char *hname, size_t n)

    find a profile by its full or partial name

    :param ns:
        the namespace to start from (NOT NULL)
    :type ns: struct aa_ns \*

    :param hname:
        name to do lookup on.  Does not contain namespace prefix (NOT NULL)
    :type hname: const char \*

    :param n:
        size of \ ``hname``\ 
    :type n: size_t

.. _`aa_lookupn_profile.return`:

Return
------

refcounted profile or NULL if not found

.. _`aa_new_null_profile`:

aa_new_null_profile
===================

.. c:function:: struct aa_profile *aa_new_null_profile(struct aa_profile *parent, bool hat, const char *base, gfp_t gfp)

    create or find a null-X learning profile

    :param parent:
        profile that caused this profile to be created (NOT NULL)
    :type parent: struct aa_profile \*

    :param hat:
        true if the null- learning profile is a hat
    :type hat: bool

    :param base:
        name to base the null profile off of
    :type base: const char \*

    :param gfp:
        type of allocation
    :type gfp: gfp_t

.. _`aa_new_null_profile.description`:

Description
-----------

Find/Create a null- complain mode profile used in learning mode.  The
name of the profile is unique and follows the format of parent//null-XXX.
where XXX is based on the \ ``name``\  or if that fails or is not supplied
a unique number

null profiles are added to the profile list but the list does not
hold a count on them so that they are automatically released when
not in use.

.. _`aa_new_null_profile.return`:

Return
------

new refcounted profile else NULL on failure

.. _`replacement_allowed`:

replacement_allowed
===================

.. c:function:: int replacement_allowed(struct aa_profile *profile, int noreplace, const char **info)

    test to see if replacement is allowed

    :param profile:
        profile to test if it can be replaced  (MAYBE NULL)
    :type profile: struct aa_profile \*

    :param noreplace:
        true if replacement shouldn't be allowed but addition is okay
    :type noreplace: int

    :param info:
        Returns - info about why replacement failed (NOT NULL)
    :type info: const char \*\*

.. _`replacement_allowed.return`:

Return
------

\ ``0``\  if replacement allowed else error code

.. _`audit_policy`:

audit_policy
============

.. c:function:: int audit_policy(struct aa_label *label, const char *op, const char *ns_name, const char *name, const char *info, int error)

    Do auditing of policy changes

    :param label:
        label to check if it can manage policy
    :type label: struct aa_label \*

    :param op:
        policy operation being performed
    :type op: const char \*

    :param ns_name:
        name of namespace being manipulated
    :type ns_name: const char \*

    :param name:
        name of profile being manipulated (NOT NULL)
    :type name: const char \*

    :param info:
        any extra information to be audited (MAYBE NULL)
    :type info: const char \*

    :param error:
        error code
    :type error: int

.. _`audit_policy.return`:

Return
------

the error to be returned after audit is done

.. _`policy_view_capable`:

policy_view_capable
===================

.. c:function:: bool policy_view_capable(struct aa_ns *ns)

    check if viewing policy in at \ ``ns``\  is allowed ns: namespace being viewed by current task (may be NULL)

    :param ns:
        *undescribed*
    :type ns: struct aa_ns \*

.. _`policy_view_capable.return`:

Return
------

true if viewing policy is allowed

If \ ``ns``\  is NULL then the namespace being viewed is assumed to be the
tasks current namespace.

.. _`aa_may_manage_policy`:

aa_may_manage_policy
====================

.. c:function:: int aa_may_manage_policy(struct aa_label *label, struct aa_ns *ns, u32 mask)

    can the current task manage policy

    :param label:
        label to check if it can manage policy
    :type label: struct aa_label \*

    :param ns:
        *undescribed*
    :type ns: struct aa_ns \*

    :param mask:
        *undescribed*
    :type mask: u32

.. _`aa_may_manage_policy.return`:

Return
------

0 if the task is allowed to manipulate policy else error

.. _`__replace_profile`:

\__replace_profile
==================

.. c:function:: void __replace_profile(struct aa_profile *old, struct aa_profile *new)

    replace \ ``old``\  with \ ``new``\  on a list

    :param old:
        profile to be replaced  (NOT NULL)
    :type old: struct aa_profile \*

    :param new:
        profile to replace \ ``old``\  with  (NOT NULL)
    :type new: struct aa_profile \*

.. _`__replace_profile.description`:

Description
-----------

Will duplicate and refcount elements that \ ``new``\  inherits from \ ``old``\ 
and will inherit \ ``old``\  children.

refcount \ ``new``\  for list, put \ ``old``\  list refcount

.. _`__replace_profile.requires`:

Requires
--------

namespace list lock be held, or list not be shared

.. _`__lookup_replace`:

\__lookup_replace
=================

.. c:function:: int __lookup_replace(struct aa_ns *ns, const char *hname, bool noreplace, struct aa_profile **p, const char **info)

    lookup replacement information for a profile \ ``ns``\  - namespace the lookup occurs in \ ``hname``\  - name of profile to lookup \ ``noreplace``\  - true if not replacing an existing profile

    :param ns:
        *undescribed*
    :type ns: struct aa_ns \*

    :param hname:
        *undescribed*
    :type hname: const char \*

    :param noreplace:
        *undescribed*
    :type noreplace: bool

    :param p:
        profile to be replaced
    :type p: struct aa_profile \*\*

    :param info:
        info string on why lookup failed
    :type info: const char \*\*

.. _`__lookup_replace.return`:

Return
------

profile to replace (no ref) on success else ptr error

.. _`aa_replace_profiles`:

aa_replace_profiles
===================

.. c:function:: ssize_t aa_replace_profiles(struct aa_ns *policy_ns, struct aa_label *label, u32 mask, struct aa_loaddata *udata)

    replace profile(s) on the profile list

    :param policy_ns:
        namespace load is occurring on
    :type policy_ns: struct aa_ns \*

    :param label:
        label that is attempting to load/replace policy
    :type label: struct aa_label \*

    :param mask:
        permission mask
    :type mask: u32

    :param udata:
        serialized data stream  (NOT NULL)
    :type udata: struct aa_loaddata \*

.. _`aa_replace_profiles.description`:

Description
-----------

unpack and replace a profile on the profile list and uses of that profile
by any task creds via invalidating the old version of the profile, which
tasks will notice to update their own cred.  If the profile does not exist
on the profile list it is added.

.. _`aa_replace_profiles.return`:

Return
------

size of data consumed else error code on failure.

.. _`aa_remove_profiles`:

aa_remove_profiles
==================

.. c:function:: ssize_t aa_remove_profiles(struct aa_ns *policy_ns, struct aa_label *subj, char *fqname, size_t size)

    remove profile(s) from the system

    :param policy_ns:
        namespace the remove is being done from
    :type policy_ns: struct aa_ns \*

    :param subj:
        label attempting to remove policy
    :type subj: struct aa_label \*

    :param fqname:
        name of the profile or namespace to remove  (NOT NULL)
    :type fqname: char \*

    :param size:
        size of the name
    :type size: size_t

.. _`aa_remove_profiles.description`:

Description
-----------

Remove a profile or sub namespace from the current namespace, so that
they can not be found anymore and mark them as replaced by unconfined

.. _`aa_remove_profiles.note`:

NOTE
----

removing confinement does not restore rlimits to preconfinement values

.. _`aa_remove_profiles.return`:

Return
------

size of data consume else error code if fails

.. This file was automatic generated / don't edit.

