.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/label.c

.. _`ns_cmp`:

ns_cmp
======

.. c:function:: int ns_cmp(struct aa_ns *a, struct aa_ns *b)

    compare ns for label set ordering

    :param struct aa_ns \*a:
        ns to compare (NOT NULL)

    :param struct aa_ns \*b:
        ns to compare (NOT NULL)

.. _`ns_cmp.return`:

Return
------

<0 if a < b
==0 if a == b
>0  if a > b

.. _`profile_cmp`:

profile_cmp
===========

.. c:function:: int profile_cmp(struct aa_profile *a, struct aa_profile *b)

    profile comparison for set ordering

    :param struct aa_profile \*a:
        profile to compare (NOT NULL)

    :param struct aa_profile \*b:
        profile to compare (NOT NULL)

.. _`profile_cmp.return`:

Return
------

<0  if a < b
==0 if a == b
>0  if a > b

.. _`vec_cmp`:

vec_cmp
=======

.. c:function:: int vec_cmp(struct aa_profile **a, int an, struct aa_profile **b, int bn)

    label comparison for set ordering

    :param struct aa_profile \*\*a:
        label to compare (NOT NULL)

    :param int an:
        *undescribed*

    :param struct aa_profile \*\*b:
        *undescribed*

    :param int bn:
        *undescribed*

.. _`vec_cmp.return`:

Return
------

<0  if a < vec
==0 if a == vec
>0  if a > vec

.. _`aa_vec_unique`:

aa_vec_unique
=============

.. c:function:: int aa_vec_unique(struct aa_profile **vec, int n, int flags)

    canonical sort and unique a list of profiles

    :param struct aa_profile \*\*vec:
        list of profiles to sort and merge

    :param int n:
        number of refcounted profiles in the list (@n > 0)

    :param int flags:
        *undescribed*

.. _`aa_vec_unique.return`:

Return
------

the number of duplicates eliminated == references put

If \ ``flags``\  & VEC_FLAG_TERMINATE \ ``vec``\  has null terminator at vec[n], and will
null terminate vec[n - dups]

.. _`aa_label_alloc`:

aa_label_alloc
==============

.. c:function:: struct aa_label *aa_label_alloc(int size, struct aa_proxy *proxy, gfp_t gfp)

    allocate a label with a profile vector of \ ``size``\  length

    :param int size:
        size of profile vector in the label

    :param struct aa_proxy \*proxy:
        proxy to use OR null if to allocate a new one

    :param gfp_t gfp:
        memory allocation type

.. _`aa_label_alloc.return`:

Return
------

new label
else NULL if failed

.. _`label_cmp`:

label_cmp
=========

.. c:function:: int label_cmp(struct aa_label *a, struct aa_label *b)

    label comparison for set ordering

    :param struct aa_label \*a:
        label to compare (NOT NULL)

    :param struct aa_label \*b:
        label to compare (NOT NULL)

.. _`label_cmp.return`:

Return
------

<0  if a < b
==0 if a == b
>0  if a > b

.. _`__aa_label_next_not_in_set`:

\__aa_label_next_not_in_set
===========================

.. c:function:: struct aa_profile *__aa_label_next_not_in_set(struct label_it *I, struct aa_label *set, struct aa_label *sub)

    return the next profile of \ ``sub``\  not in \ ``set``\ 

    :param struct label_it \*I:
        label iterator

    :param struct aa_label \*set:
        label to test against

    :param struct aa_label \*sub:
        label to if is subset of \ ``set``\ 

.. _`__aa_label_next_not_in_set.return`:

Return
------

profile in \ ``sub``\  that is not in \ ``set``\ , with iterator set pos after
else NULL if \ ``sub``\  is a subset of \ ``set``\ 

.. _`aa_label_is_subset`:

aa_label_is_subset
==================

.. c:function:: bool aa_label_is_subset(struct aa_label *set, struct aa_label *sub)

    test if \ ``sub``\  is a subset of \ ``set``\ 

    :param struct aa_label \*set:
        label to test against

    :param struct aa_label \*sub:
        label to test if is subset of \ ``set``\ 

.. _`aa_label_is_subset.return`:

Return
------

true if \ ``sub``\  is subset of \ ``set``\ 
else false

.. _`__label_remove`:

\__label_remove
===============

.. c:function:: bool __label_remove(struct aa_label *label, struct aa_label *new)

    remove \ ``label``\  from the label set

    :param struct aa_label \*label:
        *undescribed*

    :param struct aa_label \*new:
        label to redirect to

.. _`__label_remove.requires`:

Requires
--------

labels_set(@label)->lock write_lock

.. _`__label_remove.return`:

Return
------

true if the label was in the tree and removed

.. _`__label_replace`:

\__label_replace
================

.. c:function:: bool __label_replace(struct aa_label *old, struct aa_label *new)

    replace \ ``old``\  with \ ``new``\  in label set

    :param struct aa_label \*old:
        label to remove from label set

    :param struct aa_label \*new:
        label to replace \ ``old``\  with

.. _`__label_replace.requires`:

Requires
--------

labels_set(@old)->lock write_lock
valid ref count be held on \ ``new``\ 

.. _`__label_replace.return`:

Return
------

true if \ ``old``\  was in set and replaced by \ ``new``\ 

.. _`__label_replace.note`:

Note
----

current implementation requires label set be order in such a way
that \ ``new``\  directly replaces \ ``old``\  position in the set (ie.
using pointer comparison of the label address would not work)

.. _`__label_insert`:

\__label_insert
===============

.. c:function:: struct aa_label *__label_insert(struct aa_labelset *ls, struct aa_label *label, bool replace)

    attempt to insert \ ``l``\  into a label set

    :param struct aa_labelset \*ls:
        set of labels to insert \ ``l``\  into (NOT NULL)

    :param struct aa_label \*label:
        new label to insert (NOT NULL)

    :param bool replace:
        whether insertion should replace existing entry that is not stale

.. _`__label_insert.requires`:

Requires
--------

\ ``ls``\ ->lock
caller to hold a valid ref on l
if \ ``replace``\  is true l has a preallocated proxy associated

.. _`__label_insert.return`:

Return
------

\ ``l``\  if successful in inserting \ ``l``\  - with additional refcount
else ref counted equivalent label that is already in the set,
the else condition only happens if \ ``replace``\  is false

.. _`__vec_find`:

\__vec_find
===========

.. c:function:: struct aa_label *__vec_find(struct aa_profile **vec, int n)

    find label that matches \ ``vec``\  in label set

    :param struct aa_profile \*\*vec:
        vec of profiles to find matching label for (NOT NULL)

    :param int n:
        length of \ ``vec``\ 

.. _`__vec_find.requires`:

Requires
--------

\ ``vec_labelset``\ (vec) lock held
caller to hold a valid ref on l

.. _`__vec_find.return`:

Return
------

ref counted \ ``label``\  if matching label is in tree
ref counted label that is equiv to \ ``l``\  in tree
else NULL if \ ``vec``\  equiv is not in tree

.. _`__label_find`:

\__label_find
=============

.. c:function:: struct aa_label *__label_find(struct aa_label *label)

    find label \ ``label``\  in label set

    :param struct aa_label \*label:
        label to find (NOT NULL)

.. _`__label_find.requires`:

Requires
--------

labels_set(@label)->lock held
caller to hold a valid ref on l

.. _`__label_find.return`:

Return
------

ref counted \ ``label``\  if \ ``label``\  is in tree OR
ref counted label that is equiv to \ ``label``\  in tree
else NULL if \ ``label``\  or equiv is not in tree

.. _`aa_label_remove`:

aa_label_remove
===============

.. c:function:: bool aa_label_remove(struct aa_label *label)

    remove a label from the labelset

    :param struct aa_label \*label:
        label to remove

.. _`aa_label_remove.return`:

Return
------

true if \ ``label``\  was removed from the tree
else \ ``label``\  was not in tree so it could not be removed

.. _`aa_label_replace`:

aa_label_replace
================

.. c:function:: bool aa_label_replace(struct aa_label *old, struct aa_label *new)

    replace a label \ ``old``\  with a new version \ ``new``\ 

    :param struct aa_label \*old:
        label to replace

    :param struct aa_label \*new:
        label replacing \ ``old``\ 

.. _`aa_label_replace.return`:

Return
------

true if \ ``old``\  was in tree and replaced
else \ ``old``\  was not in tree, and \ ``new``\  was not inserted

.. _`vec_find`:

vec_find
========

.. c:function:: struct aa_label *vec_find(struct aa_profile **vec, int n)

    find label \ ``l``\  in label set

    :param struct aa_profile \*\*vec:
        array of profiles to find equiv label for (NOT NULL)

    :param int n:
        length of \ ``vec``\ 

.. _`vec_find.return`:

Return
------

refcounted label if \ ``vec``\  equiv is in tree
else NULL if \ ``vec``\  equiv is not in tree

.. _`aa_label_find`:

aa_label_find
=============

.. c:function:: struct aa_label *aa_label_find(struct aa_label *label)

    find label \ ``label``\  in label set

    :param struct aa_label \*label:
        label to find (NOT NULL)

.. _`aa_label_find.requires`:

Requires
--------

caller to hold a valid ref on l

.. _`aa_label_find.return`:

Return
------

refcounted \ ``label``\  if \ ``label``\  is in tree
refcounted label that is equiv to \ ``label``\  in tree
else NULL if \ ``label``\  or equiv is not in tree

.. _`aa_label_insert`:

aa_label_insert
===============

.. c:function:: struct aa_label *aa_label_insert(struct aa_labelset *ls, struct aa_label *label)

    insert label \ ``label``\  into \ ``ls``\  or return existing label \ ``ls``\  - labelset to insert \ ``label``\  into \ ``label``\  - label to insert

    :param struct aa_labelset \*ls:
        *undescribed*

    :param struct aa_label \*label:
        *undescribed*

.. _`aa_label_insert.requires`:

Requires
--------

caller to hold a valid ref on \ ``label``\ 

.. _`aa_label_insert.return`:

Return
------

ref counted \ ``label``\  if successful in inserting \ ``label``\ 
else ref counted equivalent label that is already in the set

.. _`aa_label_next_in_merge`:

aa_label_next_in_merge
======================

.. c:function:: struct aa_profile *aa_label_next_in_merge(struct label_it *I, struct aa_label *a, struct aa_label *b)

    find the next profile when merging \ ``a``\  and \ ``b``\ 

    :param struct label_it \*I:
        label iterator

    :param struct aa_label \*a:
        label to merge

    :param struct aa_label \*b:
        label to merge

.. _`aa_label_next_in_merge.return`:

Return
------

next profile
else null if no more profiles

.. _`label_merge_cmp`:

label_merge_cmp
===============

.. c:function:: int label_merge_cmp(struct aa_label *a, struct aa_label *b, struct aa_label *z)

    cmp of \ ``a``\  merging with \ ``b``\  against \ ``z``\  for set ordering

    :param struct aa_label \*a:
        label to merge then compare (NOT NULL)

    :param struct aa_label \*b:
        label to merge then compare (NOT NULL)

    :param struct aa_label \*z:
        label to compare merge against (NOT NULL)

.. _`label_merge_cmp.assumes`:

Assumes
-------

using the most recent versions of \ ``a``\ , \ ``b``\ , and \ ``z``\ 

.. _`label_merge_cmp.return`:

Return
------

<0  if a < b
==0 if a == b
>0  if a > b

.. _`label_merge_insert`:

label_merge_insert
==================

.. c:function:: struct aa_label *label_merge_insert(struct aa_label *new, struct aa_label *a, struct aa_label *b)

    create a new label by merging \ ``a``\  and \ ``b``\ 

    :param struct aa_label \*new:
        preallocated label to merge into (NOT NULL)

    :param struct aa_label \*a:
        label to merge with \ ``b``\   (NOT NULL)

    :param struct aa_label \*b:
        label to merge with \ ``a``\   (NOT NULL)

.. _`label_merge_insert.requires`:

Requires
--------

preallocated proxy

.. _`label_merge_insert.return`:

Return
------

ref counted label either \ ``new``\  if merge is unique
\ ``a``\  if \ ``b``\  is a subset of \ ``a``\ 
\ ``b``\  if \ ``a``\  is a subset of \ ``b``\ 

.. _`label_merge_insert.note`:

NOTE
----

will not use \ ``new``\  if the merge results in \ ``new``\  == \ ``a``\  or \ ``b``\ 

Must be used within labelset write lock to avoid racing with
setting labels stale.

.. _`labelset_of_merge`:

labelset_of_merge
=================

.. c:function:: struct aa_labelset *labelset_of_merge(struct aa_label *a, struct aa_label *b)

    find which labelset a merged label should be inserted

    :param struct aa_label \*a:
        label to merge and insert

    :param struct aa_label \*b:
        label to merge and insert

.. _`labelset_of_merge.return`:

Return
------

labelset that the merged label should be inserted into

.. _`__label_find_merge`:

\__label_find_merge
===================

.. c:function:: struct aa_label *__label_find_merge(struct aa_labelset *ls, struct aa_label *a, struct aa_label *b)

    find label that is equiv to merge of \ ``a``\  and \ ``b``\ 

    :param struct aa_labelset \*ls:
        set of labels to search (NOT NULL)

    :param struct aa_label \*a:
        label to merge with \ ``b``\   (NOT NULL)

    :param struct aa_label \*b:
        label to merge with \ ``a``\   (NOT NULL)

.. _`__label_find_merge.requires`:

Requires
--------

ls->lock read_lock held

.. _`__label_find_merge.return`:

Return
------

ref counted label that is equiv to merge of \ ``a``\  and \ ``b``\ 
else NULL if merge of \ ``a``\  and \ ``b``\  is not in set

.. _`aa_label_find_merge`:

aa_label_find_merge
===================

.. c:function:: struct aa_label *aa_label_find_merge(struct aa_label *a, struct aa_label *b)

    find label that is equiv to merge of \ ``a``\  and \ ``b``\ 

    :param struct aa_label \*a:
        label to merge with \ ``b``\   (NOT NULL)

    :param struct aa_label \*b:
        label to merge with \ ``a``\   (NOT NULL)

.. _`aa_label_find_merge.requires`:

Requires
--------

labels be fully constructed with a valid ns

.. _`aa_label_find_merge.return`:

Return
------

ref counted label that is equiv to merge of \ ``a``\  and \ ``b``\ 
else NULL if merge of \ ``a``\  and \ ``b``\  is not in set

.. _`aa_label_merge`:

aa_label_merge
==============

.. c:function:: struct aa_label *aa_label_merge(struct aa_label *a, struct aa_label *b, gfp_t gfp)

    attempt to insert new merged label of \ ``a``\  and \ ``b``\ 

    :param struct aa_label \*a:
        label to merge with \ ``b``\   (NOT NULL)

    :param struct aa_label \*b:
        label to merge with \ ``a``\   (NOT NULL)

    :param gfp_t gfp:
        memory allocation type

.. _`aa_label_merge.requires`:

Requires
--------

caller to hold valid refs on \ ``a``\  and \ ``b``\ 
labels be fully constructed with a valid ns

.. _`aa_label_merge.return`:

Return
------

ref counted new label if successful in inserting merge of a & b
else ref counted equivalent label that is already in the set.
else NULL if could not create label (-ENOMEM)

.. _`label_compound_match`:

label_compound_match
====================

.. c:function:: int label_compound_match(struct aa_profile *profile, struct aa_label *label, unsigned int state, bool subns, u32 request, struct aa_perms *perms)

    find perms for full compound label

    :param struct aa_profile \*profile:
        profile to find perms for

    :param struct aa_label \*label:
        label to check access permissions for

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

.. c:function:: int label_components_match(struct aa_profile *profile, struct aa_label *label, unsigned int start, bool subns, u32 request, struct aa_perms *perms)

    find perms for all subcomponents of a label

    :param struct aa_profile \*profile:
        profile to find perms for

    :param struct aa_label \*label:
        label to check access permissions for

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

.. _`aa_label_match`:

aa_label_match
==============

.. c:function:: int aa_label_match(struct aa_profile *profile, struct aa_label *label, unsigned int state, bool subns, u32 request, struct aa_perms *perms)

    do a multi-component label match

    :param struct aa_profile \*profile:
        profile to match against (NOT NULL)

    :param struct aa_label \*label:
        label to match (NOT NULL)

    :param unsigned int state:
        state to start in

    :param bool subns:
        whether to match subns components

    :param u32 request:
        permission request

    :param struct aa_perms \*perms:
        Returns computed perms (NOT NULL)

.. _`aa_label_match.return`:

Return
------

the state the match finished in, may be the none matching state

.. _`aa_update_label_name`:

aa_update_label_name
====================

.. c:function:: bool aa_update_label_name(struct aa_ns *ns, struct aa_label *label, gfp_t gfp)

    update a label to have a stored name

    :param struct aa_ns \*ns:
        ns being viewed from (NOT NULL)

    :param struct aa_label \*label:
        label to update (NOT NULL)

    :param gfp_t gfp:
        type of memory allocation

.. _`aa_update_label_name.requires`:

Requires
--------

labels_set(label) not locked in caller

.. _`aa_update_label_name.note`:

note
----

only updates the label name if it does not have a name already
and if it is in the labelset

.. _`aa_profile_snxprint`:

aa_profile_snxprint
===================

.. c:function:: int aa_profile_snxprint(char *str, size_t size, struct aa_ns *view, struct aa_profile *profile, int flags, struct aa_ns **prev_ns)

    print a profile name to a buffer

    :param char \*str:
        buffer to write to. (MAY BE NULL if \ ``size``\  == 0)

    :param size_t size:
        size of buffer

    :param struct aa_ns \*view:
        namespace profile is being viewed from

    :param struct aa_profile \*profile:
        profile to view (NOT NULL)

    :param int flags:
        whether to include the mode string

    :param struct aa_ns \*\*prev_ns:
        last ns printed when used in compound print

.. _`aa_profile_snxprint.return`:

Return
------

size of name written or would be written if larger than
available buffer

.. _`aa_profile_snxprint.note`:

Note
----

will not print anything if the profile is not visible

.. _`aa_label_snxprint`:

aa_label_snxprint
=================

.. c:function:: int aa_label_snxprint(char *str, size_t size, struct aa_ns *ns, struct aa_label *label, int flags)

    print a label name to a string buffer

    :param char \*str:
        buffer to write to. (MAY BE NULL if \ ``size``\  == 0)

    :param size_t size:
        size of buffer

    :param struct aa_ns \*ns:
        namespace profile is being viewed from

    :param struct aa_label \*label:
        label to view (NOT NULL)

    :param int flags:
        whether to include the mode string

.. _`aa_label_snxprint.return`:

Return
------

size of name written or would be written if larger than
available buffer

.. _`aa_label_snxprint.note`:

Note
----

labels do not have to be strictly hierarchical to the ns as
objects may be shared across different namespaces and thus
pickup labeling from each ns.  If a particular part of the
label is not visible it will just be excluded.  And if none
of the label is visible "---" will be used.

.. _`aa_label_asxprint`:

aa_label_asxprint
=================

.. c:function:: int aa_label_asxprint(char **strp, struct aa_ns *ns, struct aa_label *label, int flags, gfp_t gfp)

    allocate a string buffer and print label into it

    :param char \*\*strp:
        Returns - the allocated buffer with the label name. (NOT NULL)

    :param struct aa_ns \*ns:
        namespace profile is being viewed from

    :param struct aa_label \*label:
        label to view (NOT NULL)

    :param int flags:
        flags controlling what label info is printed

    :param gfp_t gfp:
        kernel memory allocation type

.. _`aa_label_asxprint.return`:

Return
------

size of name written or would be written if larger than
available buffer

.. _`aa_label_acntsxprint`:

aa_label_acntsxprint
====================

.. c:function:: int aa_label_acntsxprint(char __counted **strp, struct aa_ns *ns, struct aa_label *label, int flags, gfp_t gfp)

    allocate a \__counted string buffer and print label

    :param char __counted \*\*strp:
        buffer to write to. (MAY BE NULL if \ ``size``\  == 0)

    :param struct aa_ns \*ns:
        namespace profile is being viewed from

    :param struct aa_label \*label:
        label to view (NOT NULL)

    :param int flags:
        flags controlling what label info is printed

    :param gfp_t gfp:
        kernel memory allocation type

.. _`aa_label_acntsxprint.return`:

Return
------

size of name written or would be written if larger than
available buffer

.. _`aa_label_strn_parse`:

aa_label_strn_parse
===================

.. c:function:: struct aa_label *aa_label_strn_parse(struct aa_label *base, const char *str, size_t n, gfp_t gfp, bool create, bool force_stack)

    parse, validate and convert a text string to a label

    :param struct aa_label \*base:
        base label to use for lookups (NOT NULL)

    :param const char \*str:
        null terminated text string (NOT NULL)

    :param size_t n:
        length of str to parse, will stop at \0 if encountered before n

    :param gfp_t gfp:
        allocation type

    :param bool create:
        true if should create compound labels if they don't exist

    :param bool force_stack:
        true if should stack even if no leading &

.. _`aa_label_strn_parse.return`:

Return
------

the matching refcounted label if present
else ERRPTR

.. _`aa_labelset_destroy`:

aa_labelset_destroy
===================

.. c:function:: void aa_labelset_destroy(struct aa_labelset *ls)

    remove all labels from the label set

    :param struct aa_labelset \*ls:
        label set to cleanup (NOT NULL)

.. _`aa_labelset_destroy.description`:

Description
-----------

Labels that are removed from the set may still exist beyond the set
being destroyed depending on their reference counting

.. _`__label_update`:

\__label_update
===============

.. c:function:: struct aa_label *__label_update(struct aa_label *label)

    insert updated version of \ ``label``\  into labelset \ ``label``\  - the label to update/replace

    :param struct aa_label \*label:
        *undescribed*

.. _`__label_update.return`:

Return
------

new label that is up to date
else NULL on failure

.. _`__label_update.requires`:

Requires
--------

\ ``ns``\  lock be held

.. _`__label_update.note`:

Note
----

worst case is the stale \ ``label``\  does not get updated and has
to be updated at a later time.

.. _`__labelset_update`:

\__labelset_update
==================

.. c:function:: void __labelset_update(struct aa_ns *ns)

    update labels in \ ``ns``\ 

    :param struct aa_ns \*ns:
        namespace to update labels in  (NOT NULL)

.. _`__labelset_update.requires`:

Requires
--------

\ ``ns``\  lock be held

Walk the labelset ensuring that all labels are up to date and valid
Any label that has a stale component is marked stale and replaced and
by an updated version.

If failures happen due to memory pressures then stale labels will
be left in place until the next pass.

.. _`__aa_labelset_update_subtree`:

\__aa_labelset_update_subtree
=============================

.. c:function:: void __aa_labelset_update_subtree(struct aa_ns *ns)

    update all labels with a stale component

    :param struct aa_ns \*ns:
        ns to start update at (NOT NULL)

.. _`__aa_labelset_update_subtree.requires`:

Requires
--------

\ ``ns``\  lock be held

Invalidates labels based on \ ``p``\  in \ ``ns``\  and any children namespaces.

.. This file was automatic generated / don't edit.

