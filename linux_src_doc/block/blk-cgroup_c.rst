.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-cgroup.c

.. _`blkg_free`:

blkg_free
=========

.. c:function:: void blkg_free(struct blkcg_gq *blkg)

    free a blkg

    :param struct blkcg_gq \*blkg:
        blkg to free

.. _`blkg_free.description`:

Description
-----------

Free \ ``blkg``\  which may be partially allocated.

.. _`blkg_alloc`:

blkg_alloc
==========

.. c:function:: struct blkcg_gq *blkg_alloc(struct blkcg *blkcg, struct request_queue *q, gfp_t gfp_mask)

    allocate a blkg

    :param struct blkcg \*blkcg:
        block cgroup the new blkg is associated with

    :param struct request_queue \*q:
        request_queue the new blkg is associated with

    :param gfp_t gfp_mask:
        allocation mask to use

.. _`blkg_alloc.description`:

Description
-----------

Allocate a new blkg assocating \ ``blkcg``\  and \ ``q``\ .

.. _`blkg_lookup_create`:

blkg_lookup_create
==================

.. c:function:: struct blkcg_gq *blkg_lookup_create(struct blkcg *blkcg, struct request_queue *q)

    lookup blkg, try to create one if not there

    :param struct blkcg \*blkcg:
        blkcg of interest

    :param struct request_queue \*q:
        request_queue of interest

.. _`blkg_lookup_create.description`:

Description
-----------

Lookup blkg for the \ ``blkcg``\  - \ ``q``\  pair.  If it doesn't exist, try to
create one.  blkg creation is performed recursively from blkcg_root such
that all non-root blkg's have access to the parent blkg.  This function
should be called under RCU read lock and \ ``q``\ ->queue_lock.

Returns pointer to the looked up or created blkg on success, \ :c:func:`ERR_PTR`\ 
value on error.  If \ ``q``\  is dead, returns ERR_PTR(-EINVAL).  If \ ``q``\  is not
dead and bypassing, returns ERR_PTR(-EBUSY).

.. _`blkg_destroy_all`:

blkg_destroy_all
================

.. c:function:: void blkg_destroy_all(struct request_queue *q)

    destroy all blkgs associated with a request_queue

    :param struct request_queue \*q:
        request_queue of interest

.. _`blkg_destroy_all.description`:

Description
-----------

Destroy all blkgs associated with \ ``q``\ .

.. _`blkcg_print_blkgs`:

blkcg_print_blkgs
=================

.. c:function:: void blkcg_print_blkgs(struct seq_file *sf, struct blkcg *blkcg, u64 (*prfill)(struct seq_file *, struct blkg_policy_data *, int), const struct blkcg_policy *pol, int data, bool show_total)

    helper for printing per-blkg data

    :param struct seq_file \*sf:
        seq_file to print to

    :param struct blkcg \*blkcg:
        blkcg of interest

    :param u64 (\*prfill)(struct seq_file \*, struct blkg_policy_data \*, int):
        fill function to print out a blkg

    :param const struct blkcg_policy \*pol:
        policy in question

    :param int data:
        data to be passed to \ ``prfill``\ 

    :param bool show_total:
        to print out sum of prfill return values or not

.. _`blkcg_print_blkgs.description`:

Description
-----------

This function invokes \ ``prfill``\  on each blkg of \ ``blkcg``\  if pd for the
policy specified by \ ``pol``\  exists.  \ ``prfill``\  is invoked with \ ``sf``\ , the
policy data and \ ``data``\  and the matching queue lock held.  If \ ``show_total``\ 
is \ ``true``\ , the sum of the return values from \ ``prfill``\  is printed with
"Total" label at the end.

This is to be used to construct print functions for
cftype->read_seq_string method.

.. _`__blkg_prfill_u64`:

__blkg_prfill_u64
=================

.. c:function:: u64 __blkg_prfill_u64(struct seq_file *sf, struct blkg_policy_data *pd, u64 v)

    prfill helper for a single u64 value

    :param struct seq_file \*sf:
        seq_file to print to

    :param struct blkg_policy_data \*pd:
        policy private data of interest

    :param u64 v:
        value to print

.. _`__blkg_prfill_u64.description`:

Description
-----------

Print \ ``v``\  to \ ``sf``\  for the device assocaited with \ ``pd``\ .

.. _`__blkg_prfill_rwstat`:

__blkg_prfill_rwstat
====================

.. c:function:: u64 __blkg_prfill_rwstat(struct seq_file *sf, struct blkg_policy_data *pd, const struct blkg_rwstat *rwstat)

    prfill helper for a blkg_rwstat

    :param struct seq_file \*sf:
        seq_file to print to

    :param struct blkg_policy_data \*pd:
        policy private data of interest

    :param const struct blkg_rwstat \*rwstat:
        rwstat to print

.. _`__blkg_prfill_rwstat.description`:

Description
-----------

Print \ ``rwstat``\  to \ ``sf``\  for the device assocaited with \ ``pd``\ .

.. _`blkg_prfill_stat`:

blkg_prfill_stat
================

.. c:function:: u64 blkg_prfill_stat(struct seq_file *sf, struct blkg_policy_data *pd, int off)

    prfill callback for blkg_stat

    :param struct seq_file \*sf:
        seq_file to print to

    :param struct blkg_policy_data \*pd:
        policy private data of interest

    :param int off:
        offset to the blkg_stat in \ ``pd``\ 

.. _`blkg_prfill_stat.description`:

Description
-----------

prfill callback for printing a blkg_stat.

.. _`blkg_prfill_rwstat`:

blkg_prfill_rwstat
==================

.. c:function:: u64 blkg_prfill_rwstat(struct seq_file *sf, struct blkg_policy_data *pd, int off)

    prfill callback for blkg_rwstat

    :param struct seq_file \*sf:
        seq_file to print to

    :param struct blkg_policy_data \*pd:
        policy private data of interest

    :param int off:
        offset to the blkg_rwstat in \ ``pd``\ 

.. _`blkg_prfill_rwstat.description`:

Description
-----------

prfill callback for printing a blkg_rwstat.

.. _`blkg_print_stat_bytes`:

blkg_print_stat_bytes
=====================

.. c:function:: int blkg_print_stat_bytes(struct seq_file *sf, void *v)

    seq_show callback for blkg->stat_bytes

    :param struct seq_file \*sf:
        seq_file to print to

    :param void \*v:
        unused

.. _`blkg_print_stat_bytes.description`:

Description
-----------

To be used as cftype->seq_show to print blkg->stat_bytes.
cftype->private must be set to the blkcg_policy.

.. _`blkg_print_stat_ios`:

blkg_print_stat_ios
===================

.. c:function:: int blkg_print_stat_ios(struct seq_file *sf, void *v)

    seq_show callback for blkg->stat_ios

    :param struct seq_file \*sf:
        seq_file to print to

    :param void \*v:
        unused

.. _`blkg_print_stat_ios.description`:

Description
-----------

To be used as cftype->seq_show to print blkg->stat_ios.  cftype->private
must be set to the blkcg_policy.

.. _`blkg_print_stat_bytes_recursive`:

blkg_print_stat_bytes_recursive
===============================

.. c:function:: int blkg_print_stat_bytes_recursive(struct seq_file *sf, void *v)

    recursive version of blkg_print_stat_bytes

    :param struct seq_file \*sf:
        seq_file to print to

    :param void \*v:
        unused

.. _`blkg_print_stat_ios_recursive`:

blkg_print_stat_ios_recursive
=============================

.. c:function:: int blkg_print_stat_ios_recursive(struct seq_file *sf, void *v)

    recursive version of blkg_print_stat_ios

    :param struct seq_file \*sf:
        seq_file to print to

    :param void \*v:
        unused

.. _`blkg_stat_recursive_sum`:

blkg_stat_recursive_sum
=======================

.. c:function:: u64 blkg_stat_recursive_sum(struct blkcg_gq *blkg, struct blkcg_policy *pol, int off)

    collect hierarchical blkg_stat

    :param struct blkcg_gq \*blkg:
        blkg of interest

    :param struct blkcg_policy \*pol:
        blkcg_policy which contains the blkg_stat

    :param int off:
        offset to the blkg_stat in blkg_policy_data or \ ``blkg``\ 

.. _`blkg_stat_recursive_sum.description`:

Description
-----------

Collect the blkg_stat specified by \ ``blkg``\ , \ ``pol``\  and \ ``off``\  and all its
online descendants and their aux counts.  The caller must be holding the
queue lock for online tests.

If \ ``pol``\  is NULL, blkg_stat is at \ ``off``\  bytes into \ ``blkg``\ ; otherwise, it is
at \ ``off``\  bytes into \ ``blkg``\ 's blkg_policy_data of the policy.

.. _`blkg_rwstat_recursive_sum`:

blkg_rwstat_recursive_sum
=========================

.. c:function:: struct blkg_rwstat blkg_rwstat_recursive_sum(struct blkcg_gq *blkg, struct blkcg_policy *pol, int off)

    collect hierarchical blkg_rwstat

    :param struct blkcg_gq \*blkg:
        blkg of interest

    :param struct blkcg_policy \*pol:
        blkcg_policy which contains the blkg_rwstat

    :param int off:
        offset to the blkg_rwstat in blkg_policy_data or \ ``blkg``\ 

.. _`blkg_rwstat_recursive_sum.description`:

Description
-----------

Collect the blkg_rwstat specified by \ ``blkg``\ , \ ``pol``\  and \ ``off``\  and all its
online descendants and their aux counts.  The caller must be holding the
queue lock for online tests.

If \ ``pol``\  is NULL, blkg_rwstat is at \ ``off``\  bytes into \ ``blkg``\ ; otherwise, it
is at \ ``off``\  bytes into \ ``blkg``\ 's blkg_policy_data of the policy.

.. _`blkg_conf_prep`:

blkg_conf_prep
==============

.. c:function:: int blkg_conf_prep(struct blkcg *blkcg, const struct blkcg_policy *pol, char *input, struct blkg_conf_ctx *ctx)

    parse and prepare for per-blkg config update

    :param struct blkcg \*blkcg:
        target block cgroup

    :param const struct blkcg_policy \*pol:
        target policy

    :param char \*input:
        input string

    :param struct blkg_conf_ctx \*ctx:
        blkg_conf_ctx to be filled

.. _`blkg_conf_prep.description`:

Description
-----------

Parse per-blkg config update from \ ``input``\  and initialize \ ``ctx``\  with the
result.  \ ``ctx``\ ->blkg points to the blkg to be updated and \ ``ctx``\ ->body the
part of \ ``input``\  following MAJ:MIN.  This function returns with RCU read
lock and queue lock held and must be paired with \ :c:func:`blkg_conf_finish`\ .

.. _`blkg_conf_finish`:

blkg_conf_finish
================

.. c:function:: void blkg_conf_finish(struct blkg_conf_ctx *ctx)

    finish up per-blkg config update

    :param struct blkg_conf_ctx \*ctx:
        blkg_conf_ctx intiailized by \ :c:func:`blkg_conf_prep`\ 

.. _`blkg_conf_finish.description`:

Description
-----------

Finish up after per-blkg config update.  This function must be paired
with \ :c:func:`blkg_conf_prep`\ .

.. _`blkcg_css_offline`:

blkcg_css_offline
=================

.. c:function:: void blkcg_css_offline(struct cgroup_subsys_state *css)

    cgroup css_offline callback

    :param struct cgroup_subsys_state \*css:
        css of interest

.. _`blkcg_css_offline.description`:

Description
-----------

This function is called when \ ``css``\  is about to go away and responsible
for shooting down all blkgs associated with \ ``css``\ .  blkgs should be
removed while holding both q and blkcg locks.  As blkcg lock is nested
inside q lock, this function performs reverse double lock dancing.

This is the blkcg counterpart of \ :c:func:`ioc_release_fn`\ .

.. _`blkcg_init_queue`:

blkcg_init_queue
================

.. c:function:: int blkcg_init_queue(struct request_queue *q)

    initialize blkcg part of request queue

    :param struct request_queue \*q:
        request_queue to initialize

.. _`blkcg_init_queue.description`:

Description
-----------

Called from \ :c:func:`blk_alloc_queue_node`\ . Responsible for initializing blkcg
part of new request_queue \ ``q``\ .

.. _`blkcg_init_queue.return`:

Return
------

0 on success, -errno on failure.

.. _`blkcg_drain_queue`:

blkcg_drain_queue
=================

.. c:function:: void blkcg_drain_queue(struct request_queue *q)

    drain blkcg part of request_queue

    :param struct request_queue \*q:
        request_queue to drain

.. _`blkcg_drain_queue.description`:

Description
-----------

Called from \ :c:func:`blk_drain_queue`\ .  Responsible for draining blkcg part.

.. _`blkcg_exit_queue`:

blkcg_exit_queue
================

.. c:function:: void blkcg_exit_queue(struct request_queue *q)

    exit and release blkcg part of request_queue

    :param struct request_queue \*q:
        request_queue being released

.. _`blkcg_exit_queue.description`:

Description
-----------

Called from \ :c:func:`blk_release_queue`\ .  Responsible for exiting blkcg part.

.. _`blkcg_activate_policy`:

blkcg_activate_policy
=====================

.. c:function:: int blkcg_activate_policy(struct request_queue *q, const struct blkcg_policy *pol)

    activate a blkcg policy on a request_queue

    :param struct request_queue \*q:
        request_queue of interest

    :param const struct blkcg_policy \*pol:
        blkcg policy to activate

.. _`blkcg_activate_policy.description`:

Description
-----------

Activate \ ``pol``\  on \ ``q``\ .  Requires \ ``GFP_KERNEL``\  context.  \ ``q``\  goes through
bypass mode to populate its blkgs with policy_data for \ ``pol``\ .

Activation happens with \ ``q``\  bypassed, so nobody would be accessing blkgs
from IO path.  Update of each blkg is protected by both queue and blkcg
locks so that holding either lock and testing \ :c:func:`blkcg_policy_enabled`\  is
always enough for dereferencing policy data.

The caller is responsible for synchronizing [de]activations and policy
[un]registerations.  Returns 0 on success, -errno on failure.

.. _`blkcg_deactivate_policy`:

blkcg_deactivate_policy
=======================

.. c:function:: void blkcg_deactivate_policy(struct request_queue *q, const struct blkcg_policy *pol)

    deactivate a blkcg policy on a request_queue

    :param struct request_queue \*q:
        request_queue of interest

    :param const struct blkcg_policy \*pol:
        blkcg policy to deactivate

.. _`blkcg_deactivate_policy.description`:

Description
-----------

Deactivate \ ``pol``\  on \ ``q``\ .  Follows the same synchronization rules as
\ :c:func:`blkcg_activate_policy`\ .

.. _`blkcg_policy_register`:

blkcg_policy_register
=====================

.. c:function:: int blkcg_policy_register(struct blkcg_policy *pol)

    register a blkcg policy

    :param struct blkcg_policy \*pol:
        blkcg policy to register

.. _`blkcg_policy_register.description`:

Description
-----------

Register \ ``pol``\  with blkcg core.  Might sleep and \ ``pol``\  may be modified on
successful registration.  Returns 0 on success and -errno on failure.

.. _`blkcg_policy_unregister`:

blkcg_policy_unregister
=======================

.. c:function:: void blkcg_policy_unregister(struct blkcg_policy *pol)

    unregister a blkcg policy

    :param struct blkcg_policy \*pol:
        blkcg policy to unregister

.. _`blkcg_policy_unregister.description`:

Description
-----------

Undo blkcg_policy_register(\ ``pol``\ ).  Might sleep.

.. This file was automatic generated / don't edit.

