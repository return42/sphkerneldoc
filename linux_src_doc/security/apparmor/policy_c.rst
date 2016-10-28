.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/policy.c

.. _`hname_tail`:

hname_tail
==========

.. c:function:: const char *hname_tail(const char *hname)

    find the last component of an hname

    :param const char \*hname:
        *undescribed*

.. _`hname_tail.return`:

Return
------

the tail (base profile name) name component of an hname

.. _`policy_init`:

policy_init
===========

.. c:function:: bool policy_init(struct aa_policy *policy, const char *prefix, const char *name)

    initialize a policy structure

    :param struct aa_policy \*policy:
        policy to initialize  (NOT NULL)

    :param const char \*prefix:
        prefix name if any is required.  (MAYBE NULL)

    :param const char \*name:
        name of the policy, init will make a copy of it  (NOT NULL)

.. _`policy_init.note`:

Note
----

this fn creates a copy of strings passed in

.. _`policy_init.return`:

Return
------

true if policy init successful

.. _`policy_destroy`:

policy_destroy
==============

.. c:function:: void policy_destroy(struct aa_policy *policy)

    free the elements referenced by \ ``policy``\ 

    :param struct aa_policy \*policy:
        policy that is to have its elements freed  (NOT NULL)

.. _`__policy_find`:

__policy_find
=============

.. c:function:: struct aa_policy *__policy_find(struct list_head *head, const char *name)

    find a policy by \ ``name``\  on a policy list

    :param struct list_head \*head:
        list to search  (NOT NULL)

    :param const char \*name:
        name to search for  (NOT NULL)

.. _`__policy_find.requires`:

Requires
--------

rcu_read_lock be held

.. _`__policy_find.return`:

Return
------

unrefcounted policy that match \ ``name``\  or NULL if not found

.. _`__policy_strn_find`:

__policy_strn_find
==================

.. c:function:: struct aa_policy *__policy_strn_find(struct list_head *head, const char *str, int len)

    find a policy that's name matches \ ``len``\  chars of \ ``str``\ 

    :param struct list_head \*head:
        list to search  (NOT NULL)

    :param const char \*str:
        string to search for  (NOT NULL)

    :param int len:
        length of match required

.. _`__policy_strn_find.requires`:

Requires
--------

rcu_read_lock be held

.. _`__policy_strn_find.return`:

Return
------

unrefcounted policy that match \ ``str``\  or NULL if not found

if \ ``len``\  == strlen(\ ``strlen``\ ) then this is equiv to \__policy_find
other wise it allows searching for policy by a partial match of name

.. _`aa_ns_visible`:

aa_ns_visible
=============

.. c:function:: bool aa_ns_visible(struct aa_namespace *curr, struct aa_namespace *view)

    test if \ ``view``\  is visible from \ ``curr``\ 

    :param struct aa_namespace \*curr:
        namespace to treat as the parent (NOT NULL)

    :param struct aa_namespace \*view:
        namespace to test if visible from \ ``curr``\  (NOT NULL)

.. _`aa_ns_visible.return`:

Return
------

true if \ ``view``\  is visible from \ ``curr``\  else false

.. _`aa_ns_name`:

aa_ns_name
==========

.. c:function:: const char *aa_ns_name(struct aa_namespace *curr, struct aa_namespace *view)

    Find the ns name to display for \ ``view``\  from \ ``curr``\  \ ``curr``\  - current namespace (NOT NULL) \ ``view``\  - namespace attempting to view (NOT NULL)

    :param struct aa_namespace \*curr:
        *undescribed*

    :param struct aa_namespace \*view:
        *undescribed*

.. _`aa_ns_name.return`:

Return
------

name of \ ``view``\  visible from \ ``curr``\ 

.. _`alloc_namespace`:

alloc_namespace
===============

.. c:function:: struct aa_namespace *alloc_namespace(const char *prefix, const char *name)

    allocate, initialize and return a new namespace

    :param const char \*prefix:
        parent namespace name (MAYBE NULL)

    :param const char \*name:
        a preallocated name  (NOT NULL)

.. _`alloc_namespace.return`:

Return
------

refcounted namespace or NULL on failure.

.. _`free_namespace`:

free_namespace
==============

.. c:function:: void free_namespace(struct aa_namespace *ns)

    free a profile namespace

    :param struct aa_namespace \*ns:
        the namespace to free  (MAYBE NULL)

.. _`free_namespace.requires`:

Requires
--------

All references to the namespace must have been put, if the
namespace was referenced by a profile confining a task,

.. _`__aa_find_namespace`:

__aa_find_namespace
===================

.. c:function:: struct aa_namespace *__aa_find_namespace(struct list_head *head, const char *name)

    find a namespace on a list by \ ``name``\ 

    :param struct list_head \*head:
        list to search for namespace on  (NOT NULL)

    :param const char \*name:
        name of namespace to look for  (NOT NULL)

.. _`__aa_find_namespace.return`:

Return
------

unrefcounted namespace

.. _`__aa_find_namespace.requires`:

Requires
--------

rcu_read_lock be held

.. _`aa_find_namespace`:

aa_find_namespace
=================

.. c:function:: struct aa_namespace *aa_find_namespace(struct aa_namespace *root, const char *name)

    look up a profile namespace on the namespace list

    :param struct aa_namespace \*root:
        namespace to search in  (NOT NULL)

    :param const char \*name:
        name of namespace to find  (NOT NULL)

.. _`aa_find_namespace.return`:

Return
------

a refcounted namespace on the list, or NULL if no namespace
called \ ``name``\  exists.

refcount released by caller

.. _`aa_prepare_namespace`:

aa_prepare_namespace
====================

.. c:function:: struct aa_namespace *aa_prepare_namespace(const char *name)

    find an existing or create a new namespace of \ ``name``\ 

    :param const char \*name:
        the namespace to find or add  (MAYBE NULL)

.. _`aa_prepare_namespace.return`:

Return
------

refcounted namespace or NULL if failed to create one

.. _`__list_add_profile`:

__list_add_profile
==================

.. c:function:: void __list_add_profile(struct list_head *list, struct aa_profile *profile)

    add a profile to a list

    :param struct list_head \*list:
        list to add it to  (NOT NULL)

    :param struct aa_profile \*profile:
        the profile to add  (NOT NULL)

.. _`__list_add_profile.description`:

Description
-----------

refcount \ ``profile``\ , should be put by \__list_remove_profile

.. _`__list_add_profile.requires`:

Requires
--------

namespace lock be held, or list not be shared

.. _`__list_remove_profile`:

__list_remove_profile
=====================

.. c:function:: void __list_remove_profile(struct aa_profile *profile)

    remove a profile from the list it is on

    :param struct aa_profile \*profile:
        the profile to remove  (NOT NULL)

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

__remove_profile
================

.. c:function:: void __remove_profile(struct aa_profile *profile)

    remove old profile, and children

    :param struct aa_profile \*profile:
        profile to be replaced  (NOT NULL)

.. _`__remove_profile.requires`:

Requires
--------

namespace list lock be held, or list not be shared

.. _`__profile_list_release`:

__profile_list_release
======================

.. c:function:: void __profile_list_release(struct list_head *head)

    remove all profiles on the list and put refs

    :param struct list_head \*head:
        list of profiles  (NOT NULL)

.. _`__profile_list_release.requires`:

Requires
--------

namespace lock be held

.. _`destroy_namespace`:

destroy_namespace
=================

.. c:function:: void destroy_namespace(struct aa_namespace *ns)

    remove everything contained by \ ``ns``\ 

    :param struct aa_namespace \*ns:
        namespace to have it contents removed  (NOT NULL)

.. _`__remove_namespace`:

__remove_namespace
==================

.. c:function:: void __remove_namespace(struct aa_namespace *ns)

    remove a namespace and all its children

    :param struct aa_namespace \*ns:
        namespace to be removed  (NOT NULL)

.. _`__remove_namespace.requires`:

Requires
--------

ns->parent->lock be held and ns removed from parent.

.. _`__ns_list_release`:

__ns_list_release
=================

.. c:function:: void __ns_list_release(struct list_head *head)

    remove all profile namespaces on the list put refs

    :param struct list_head \*head:
        list of profile namespaces  (NOT NULL)

.. _`__ns_list_release.requires`:

Requires
--------

namespace lock be held

.. _`aa_alloc_root_ns`:

aa_alloc_root_ns
================

.. c:function:: int aa_alloc_root_ns( void)

    allocate the root profile namespace

    :param  void:
        no arguments

.. _`aa_alloc_root_ns.return`:

Return
------

\ ``0``\  on success else error

.. _`aa_free_profile`:

aa_free_profile
===============

.. c:function:: void aa_free_profile(struct aa_profile *profile)

    free a profile

    :param struct aa_profile \*profile:
        the profile to free  (MAYBE NULL)

.. _`aa_free_profile.description`:

Description
-----------

Free a profile, its hats and null_profile. All references to the profile,
its hats and null_profile must have been put.

If the profile was referenced from a task context, \ :c:func:`free_profile`\  will
be called from an rcu callback routine, so we must not sleep here.

.. _`aa_free_profile_rcu`:

aa_free_profile_rcu
===================

.. c:function:: void aa_free_profile_rcu(struct rcu_head *head)

    free aa_profile by rcu (called by aa_free_profile_kref)

    :param struct rcu_head \*head:
        rcu_head callback for freeing of a profile  (NOT NULL)

.. _`aa_free_profile_kref`:

aa_free_profile_kref
====================

.. c:function:: void aa_free_profile_kref(struct kref *kref)

    free aa_profile by kref (called by aa_put_profile)

    :param struct kref \*kref:
        *undescribed*

.. _`aa_alloc_profile`:

aa_alloc_profile
================

.. c:function:: struct aa_profile *aa_alloc_profile(const char *hname)

    allocate, initialize and return a new profile

    :param const char \*hname:
        name of the profile  (NOT NULL)

.. _`aa_alloc_profile.return`:

Return
------

refcount profile or NULL on failure

.. _`aa_new_null_profile`:

aa_new_null_profile
===================

.. c:function:: struct aa_profile *aa_new_null_profile(struct aa_profile *parent, int hat)

    create a new null-X learning profile

    :param struct aa_profile \*parent:
        profile that caused this profile to be created (NOT NULL)

    :param int hat:
        true if the null- learning profile is a hat

.. _`aa_new_null_profile.description`:

Description
-----------

Create a null- complain mode profile used in learning mode.  The name of
the profile is unique and follows the format of parent//null-<uniq>.

null profiles are added to the profile list but the list does not
hold a count on them so that they are automatically released when
not in use.

.. _`aa_new_null_profile.return`:

Return
------

new refcounted profile else NULL on failure

.. _`__find_child`:

__find_child
============

.. c:function:: struct aa_profile *__find_child(struct list_head *head, const char *name)

    find a profile on \ ``head``\  list with a name matching \ ``name``\ 

    :param struct list_head \*head:
        list to search  (NOT NULL)

    :param const char \*name:
        name of profile (NOT NULL)

.. _`__find_child.requires`:

Requires
--------

rcu_read_lock be held

.. _`__find_child.return`:

Return
------

unrefcounted profile ptr, or NULL if not found

.. _`__strn_find_child`:

__strn_find_child
=================

.. c:function:: struct aa_profile *__strn_find_child(struct list_head *head, const char *name, int len)

    find a profile on \ ``head``\  list using substring of \ ``name``\ 

    :param struct list_head \*head:
        list to search  (NOT NULL)

    :param const char \*name:
        name of profile (NOT NULL)

    :param int len:
        length of \ ``name``\  substring to match

.. _`__strn_find_child.requires`:

Requires
--------

rcu_read_lock be held

.. _`__strn_find_child.return`:

Return
------

unrefcounted profile ptr, or NULL if not found

.. _`aa_find_child`:

aa_find_child
=============

.. c:function:: struct aa_profile *aa_find_child(struct aa_profile *parent, const char *name)

    find a profile by \ ``name``\  in \ ``parent``\ 

    :param struct aa_profile \*parent:
        profile to search  (NOT NULL)

    :param const char \*name:
        profile name to search for  (NOT NULL)

.. _`aa_find_child.return`:

Return
------

a refcounted profile or NULL if not found

.. _`__lookup_parent`:

__lookup_parent
===============

.. c:function:: struct aa_policy *__lookup_parent(struct aa_namespace *ns, const char *hname)

    lookup the parent of a profile of name \ ``hname``\ 

    :param struct aa_namespace \*ns:
        namespace to lookup profile in  (NOT NULL)

    :param const char \*hname:
        hierarchical profile name to find parent of  (NOT NULL)

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

.. _`__lookup_profile`:

__lookup_profile
================

.. c:function:: struct aa_profile *__lookup_profile(struct aa_policy *base, const char *hname)

    lookup the profile matching \ ``hname``\ 

    :param struct aa_policy \*base:
        base list to start looking up profile name from  (NOT NULL)

    :param const char \*hname:
        hierarchical profile name  (NOT NULL)

.. _`__lookup_profile.requires`:

Requires
--------

rcu_read_lock be held

.. _`__lookup_profile.return`:

Return
------

unrefcounted profile pointer or NULL if not found

Do a relative name lookup, recursing through profile tree.

.. _`aa_lookup_profile`:

aa_lookup_profile
=================

.. c:function:: struct aa_profile *aa_lookup_profile(struct aa_namespace *ns, const char *hname)

    find a profile by its full or partial name

    :param struct aa_namespace \*ns:
        the namespace to start from (NOT NULL)

    :param const char \*hname:
        name to do lookup on.  Does not contain namespace prefix (NOT NULL)

.. _`aa_lookup_profile.return`:

Return
------

refcounted profile or NULL if not found

.. _`replacement_allowed`:

replacement_allowed
===================

.. c:function:: int replacement_allowed(struct aa_profile *profile, int noreplace, const char **info)

    test to see if replacement is allowed

    :param struct aa_profile \*profile:
        profile to test if it can be replaced  (MAYBE NULL)

    :param int noreplace:
        true if replacement shouldn't be allowed but addition is okay

    :param const char \*\*info:
        Returns - info about why replacement failed (NOT NULL)

.. _`replacement_allowed.return`:

Return
------

\ ``0``\  if replacement allowed else error code

.. _`audit_policy`:

audit_policy
============

.. c:function:: int audit_policy(int op, gfp_t gfp, const char *name, const char *info, int error)

    Do auditing of policy changes

    :param int op:
        policy operation being performed

    :param gfp_t gfp:
        memory allocation flags

    :param const char \*name:
        name of profile being manipulated (NOT NULL)

    :param const char \*info:
        any extra information to be audited (MAYBE NULL)

    :param int error:
        error code

.. _`audit_policy.return`:

Return
------

the error to be returned after audit is done

.. _`aa_may_manage_policy`:

aa_may_manage_policy
====================

.. c:function:: bool aa_may_manage_policy(int op)

    can the current task manage policy

    :param int op:
        the policy manipulation operation being done

.. _`aa_may_manage_policy.return`:

Return
------

true if the task is allowed to manipulate policy

.. _`__replace_profile`:

__replace_profile
=================

.. c:function:: void __replace_profile(struct aa_profile *old, struct aa_profile *new, bool share_replacedby)

    replace \ ``old``\  with \ ``new``\  on a list

    :param struct aa_profile \*old:
        profile to be replaced  (NOT NULL)

    :param struct aa_profile \*new:
        profile to replace \ ``old``\  with  (NOT NULL)

    :param bool share_replacedby:
        transfer \ ``old``\ ->replacedby to \ ``new``\ 

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

__lookup_replace
================

.. c:function:: int __lookup_replace(struct aa_namespace *ns, const char *hname, bool noreplace, struct aa_profile **p, const char **info)

    lookup replacement information for a profile \ ``ns``\  - namespace the lookup occurs in \ ``hname``\  - name of profile to lookup \ ``noreplace``\  - true if not replacing an existing profile

    :param struct aa_namespace \*ns:
        *undescribed*

    :param const char \*hname:
        *undescribed*

    :param bool noreplace:
        *undescribed*

    :param struct aa_profile \*\*p:
        profile to be replaced

    :param const char \*\*info:
        info string on why lookup failed

.. _`__lookup_replace.return`:

Return
------

profile to replace (no ref) on success else ptr error

.. _`aa_replace_profiles`:

aa_replace_profiles
===================

.. c:function:: ssize_t aa_replace_profiles(void *udata, size_t size, bool noreplace)

    replace profile(s) on the profile list

    :param void \*udata:
        serialized data stream  (NOT NULL)

    :param size_t size:
        size of the serialized data stream

    :param bool noreplace:
        true if only doing addition, no replacement allowed

.. _`aa_replace_profiles.description`:

Description
-----------

unpack and replace a profile on the profile list and uses of that profile
by any aa_task_cxt.  If the profile does not exist on the profile list
it is added.

.. _`aa_replace_profiles.return`:

Return
------

size of data consumed else error code on failure.

.. _`aa_remove_profiles`:

aa_remove_profiles
==================

.. c:function:: ssize_t aa_remove_profiles(char *fqname, size_t size)

    remove profile(s) from the system

    :param char \*fqname:
        name of the profile or namespace to remove  (NOT NULL)

    :param size_t size:
        size of the name

.. _`aa_remove_profiles.description`:

Description
-----------

Remove a profile or sub namespace from the current namespace, so that
they can not be found anymore and mark them as replaced by unconfined

.. _`aa_remove_profiles.note`:

NOTE
----

removing confinement does not restore rlimits to preconfinemnet values

.. _`aa_remove_profiles.return`:

Return
------

size of data consume else error code if fails

.. This file was automatic generated / don't edit.

