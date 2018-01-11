.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/android/binder.c

.. _`binder_work`:

struct binder_work
==================

.. c:type:: struct binder_work

    work enqueued on a worklist

.. _`binder_work.definition`:

Definition
----------

.. code-block:: c

    struct binder_work {
        struct list_head entry;
        enum {
            BINDER_WORK_TRANSACTION = 1,
            BINDER_WORK_TRANSACTION_COMPLETE,
            BINDER_WORK_RETURN_ERROR,
            BINDER_WORK_NODE,
            BINDER_WORK_DEAD_BINDER,
            BINDER_WORK_DEAD_BINDER_AND_CLEAR,
            BINDER_WORK_CLEAR_DEATH_NOTIFICATION,
        } type;
    }

.. _`binder_work.members`:

Members
-------

entry
    node enqueued on list

type
    type of work to be performed

.. _`binder_work.description`:

Description
-----------

There are separate work lists for proc, thread, and node (async).

.. _`binder_node`:

struct binder_node
==================

.. c:type:: struct binder_node

    binder node bookkeeping

.. _`binder_node.definition`:

Definition
----------

.. code-block:: c

    struct binder_node {
        int debug_id;
        spinlock_t lock;
        struct binder_work work;
        union {
            struct rb_node rb_node;
            struct hlist_node dead_node;
        } ;
        struct binder_proc *proc;
        struct hlist_head refs;
        int internal_strong_refs;
        int local_weak_refs;
        int local_strong_refs;
        int tmp_refs;
        binder_uintptr_t ptr;
        binder_uintptr_t cookie;
        struct {
            u8 has_strong_ref:1;
            u8 pending_strong_ref:1;
            u8 has_weak_ref:1;
            u8 pending_weak_ref:1;
        } ;
        struct {
            u8 accept_fds:1;
            u8 min_priority;
        } ;
        bool has_async_transaction;
        struct list_head async_todo;
    }

.. _`binder_node.members`:

Members
-------

debug_id
    unique ID for debugging
    (invariant after initialized)

lock
    lock for node fields

work
    worklist element for node work
    (protected by \ ``proc``\ ->inner_lock)

{unnamed_union}
    anonymous

rb_node
    element for proc->nodes tree
    (protected by \ ``proc``\ ->inner_lock)

dead_node
    element for binder_dead_nodes list
    (protected by binder_dead_nodes_lock)

proc
    binder_proc that owns this node
    (invariant after initialized)

refs
    list of references on this node
    (protected by \ ``lock``\ )

internal_strong_refs
    used to take strong references when
    initiating a transaction
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

local_weak_refs
    weak user refs from local process
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

local_strong_refs
    strong user refs from local process
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

tmp_refs
    temporary kernel refs
    (protected by \ ``proc``\ ->inner_lock while \ ``proc``\ 
    is valid, and by binder_dead_nodes_lock
    if \ ``proc``\  is NULL. During inc/dec and node release
    it is also protected by \ ``lock``\  to provide safety
    as the node dies and \ ``proc``\  becomes NULL)

ptr
    userspace pointer for node
    (invariant, no lock needed)

cookie
    userspace cookie for node
    (invariant, no lock needed)

{unnamed_struct}
    anonymous

has_strong_ref
    userspace notified of strong ref
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

pending_strong_ref
    userspace has acked notification of strong ref
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

has_weak_ref
    userspace notified of weak ref
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

pending_weak_ref
    userspace has acked notification of weak ref
    (protected by \ ``proc``\ ->inner_lock if \ ``proc``\ 
    and by \ ``lock``\ )

{unnamed_struct}
    anonymous

accept_fds
    file descriptor operations supported for node
    (invariant after initialized)

min_priority
    minimum scheduling priority
    (invariant after initialized)

has_async_transaction
    async transaction to node in progress
    (protected by \ ``lock``\ )

async_todo
    list of async work items
    (protected by \ ``proc``\ ->inner_lock)

.. _`binder_node.description`:

Description
-----------

Bookkeeping structure for binder nodes.

.. _`binder_ref_data`:

struct binder_ref_data
======================

.. c:type:: struct binder_ref_data

    binder_ref counts and id

.. _`binder_ref_data.definition`:

Definition
----------

.. code-block:: c

    struct binder_ref_data {
        int debug_id;
        uint32_t desc;
        int strong;
        int weak;
    }

.. _`binder_ref_data.members`:

Members
-------

debug_id
    unique ID for the ref

desc
    unique userspace handle for ref

strong
    strong ref count (debugging only if not locked)

weak
    weak ref count (debugging only if not locked)

.. _`binder_ref_data.description`:

Description
-----------

Structure to hold ref count and ref id information. Since
the actual ref can only be accessed with a lock, this structure
is used to return information about the ref to callers of
ref inc/dec functions.

.. _`binder_ref`:

struct binder_ref
=================

.. c:type:: struct binder_ref

    struct to track references on nodes

.. _`binder_ref.definition`:

Definition
----------

.. code-block:: c

    struct binder_ref {
        struct binder_ref_data data;
        struct rb_node rb_node_desc;
        struct rb_node rb_node_node;
        struct hlist_node node_entry;
        struct binder_proc *proc;
        struct binder_node *node;
        struct binder_ref_death *death;
    }

.. _`binder_ref.members`:

Members
-------

data
    binder_ref_data containing id, handle, and current refcounts

rb_node_desc
    node for lookup by \ ``data``\ .desc in proc's rb_tree

rb_node_node
    node for lookup by \ ``node``\  in proc's rb_tree

node_entry
    list entry for node->refs list in target node
    (protected by \ ``node``\ ->lock)

proc
    binder_proc containing ref

node
    binder_node of target node. When cleaning up a
    ref for deletion in binder_cleanup_ref, a non-NULL
    \ ``node``\  indicates the node must be freed

death
    pointer to death notification (ref_death) if requested
    (protected by \ ``node``\ ->lock)

.. _`binder_ref.description`:

Description
-----------

Structure to track references from procA to target node (on procB). This
structure is unsafe to access without holding \ ``proc``\ ->outer_lock.

.. _`binder_proc`:

struct binder_proc
==================

.. c:type:: struct binder_proc

    binder process bookkeeping

.. _`binder_proc.definition`:

Definition
----------

.. code-block:: c

    struct binder_proc {
        struct hlist_node proc_node;
        struct rb_root threads;
        struct rb_root nodes;
        struct rb_root refs_by_desc;
        struct rb_root refs_by_node;
        struct list_head waiting_threads;
        int pid;
        struct task_struct *tsk;
        struct files_struct *files;
        struct hlist_node deferred_work_node;
        int deferred_work;
        bool is_dead;
        struct list_head todo;
        wait_queue_head_t wait;
        struct binder_stats stats;
        struct list_head delivered_death;
        int max_threads;
        int requested_threads;
        int requested_threads_started;
        int tmp_ref;
        long default_priority;
        struct dentry *debugfs_entry;
        struct binder_alloc alloc;
        struct binder_context *context;
        spinlock_t inner_lock;
        spinlock_t outer_lock;
    }

.. _`binder_proc.members`:

Members
-------

proc_node
    element for binder_procs list

threads
    rbtree of binder_threads in this proc
    (protected by \ ``inner_lock``\ )

nodes
    rbtree of binder nodes associated with
    this proc ordered by node->ptr
    (protected by \ ``inner_lock``\ )

refs_by_desc
    rbtree of refs ordered by ref->desc
    (protected by \ ``outer_lock``\ )

refs_by_node
    rbtree of refs ordered by ref->node
    (protected by \ ``outer_lock``\ )

waiting_threads
    threads currently waiting for proc work
    (protected by \ ``inner_lock``\ )
    \ ``pid``\                    PID of group_leader of process
    (invariant after initialized)
    \ ``tsk``\                    task_struct for group_leader of process
    (invariant after initialized)
    \ ``files``\                  files_struct for process
    (invariant after initialized)

pid
    *undescribed*

tsk
    *undescribed*

files
    *undescribed*

deferred_work_node
    element for binder_deferred_list
    (protected by binder_deferred_lock)

deferred_work
    bitmap of deferred work to perform
    (protected by binder_deferred_lock)

is_dead
    process is dead and awaiting free
    when outstanding transactions are cleaned up
    (protected by \ ``inner_lock``\ )

todo
    list of work for this process
    (protected by \ ``inner_lock``\ )

wait
    wait queue head to wait for proc work
    (invariant after initialized)

stats
    per-process binder statistics
    (atomics, no lock needed)

delivered_death
    list of delivered death notification
    (protected by \ ``inner_lock``\ )

max_threads
    cap on number of binder threads
    (protected by \ ``inner_lock``\ )

requested_threads
    number of binder threads requested but not
    yet started. In current implementation, can
    only be 0 or 1.
    (protected by \ ``inner_lock``\ )

requested_threads_started
    number binder threads started
    (protected by \ ``inner_lock``\ )

tmp_ref
    temporary reference to indicate proc is in use
    (protected by \ ``inner_lock``\ )

default_priority
    default scheduler priority
    (invariant after initialized)

debugfs_entry
    debugfs node

alloc
    binder allocator bookkeeping

context
    binder_context for this proc
    (invariant after initialized)

inner_lock
    can nest under outer_lock and/or node lock

outer_lock
    no nesting under innor or node lock
    Lock order: 1) outer, 2) node, 3) inner

.. _`binder_proc.description`:

Description
-----------

Bookkeeping structure for binder processes

.. _`binder_thread`:

struct binder_thread
====================

.. c:type:: struct binder_thread

    binder thread bookkeeping

.. _`binder_thread.definition`:

Definition
----------

.. code-block:: c

    struct binder_thread {
        struct binder_proc *proc;
        struct rb_node rb_node;
        struct list_head waiting_thread_node;
        int pid;
        int looper;
        bool looper_need_return;
        struct binder_transaction *transaction_stack;
        struct list_head todo;
        struct binder_error return_error;
        struct binder_error reply_error;
        wait_queue_head_t wait;
        struct binder_stats stats;
        atomic_t tmp_ref;
        bool is_dead;
    }

.. _`binder_thread.members`:

Members
-------

proc
    binder process for this thread
    (invariant after initialization)

rb_node
    element for proc->threads rbtree
    (protected by \ ``proc``\ ->inner_lock)

waiting_thread_node
    element for \ ``proc``\ ->waiting_threads list
    (protected by \ ``proc``\ ->inner_lock)

pid
    PID for this thread
    (invariant after initialization)

looper
    bitmap of looping state
    (only accessed by this thread)

looper_need_return
    *undescribed*

transaction_stack
    stack of in-progress transactions for this thread
    (protected by \ ``proc``\ ->inner_lock)

todo
    list of work to do for this thread
    (protected by \ ``proc``\ ->inner_lock)

return_error
    transaction errors reported by this thread
    (only accessed by this thread)

reply_error
    transaction errors reported by target thread
    (protected by \ ``proc``\ ->inner_lock)

wait
    wait queue for thread work

stats
    per-thread statistics
    (atomics, no lock needed)

tmp_ref
    temporary reference to indicate thread is in use
    (atomic since \ ``proc``\ ->inner_lock cannot
    always be acquired)

is_dead
    thread is dead and awaiting free
    when outstanding transactions are cleaned up
    (protected by \ ``proc``\ ->inner_lock)

.. _`binder_thread.description`:

Description
-----------

Bookkeeping structure for binder threads.

.. _`binder_proc_lock`:

binder_proc_lock
================

.. c:function::  binder_proc_lock( proc)

    Acquire outer lock for given binder_proc

    :param  proc:
        struct binder_proc to acquire

.. _`binder_proc_lock.description`:

Description
-----------

Acquires proc->outer_lock. Used to protect binder_ref
structures associated with the given proc.

.. _`binder_proc_unlock`:

binder_proc_unlock
==================

.. c:function::  binder_proc_unlock( _proc)

    Release spinlock for given binder_proc

    :param  _proc:
        *undescribed*

.. _`binder_proc_unlock.description`:

Description
-----------

Release lock acquired via \ :c:func:`binder_proc_lock`\ 

.. _`binder_inner_proc_lock`:

binder_inner_proc_lock
======================

.. c:function::  binder_inner_proc_lock( proc)

    Acquire inner lock for given binder_proc

    :param  proc:
        struct binder_proc to acquire

.. _`binder_inner_proc_lock.description`:

Description
-----------

Acquires proc->inner_lock. Used to protect todo lists

.. _`binder_inner_proc_unlock`:

binder_inner_proc_unlock
========================

.. c:function::  binder_inner_proc_unlock( proc)

    Release inner lock for given binder_proc

    :param  proc:
        struct binder_proc to acquire

.. _`binder_inner_proc_unlock.description`:

Description
-----------

Release lock acquired via \ :c:func:`binder_inner_proc_lock`\ 

.. _`binder_node_lock`:

binder_node_lock
================

.. c:function::  binder_node_lock( node)

    Acquire spinlock for given binder_node

    :param  node:
        struct binder_node to acquire

.. _`binder_node_lock.description`:

Description
-----------

Acquires node->lock. Used to protect binder_node fields

.. _`binder_node_unlock`:

binder_node_unlock
==================

.. c:function::  binder_node_unlock( node)

    Release spinlock for given binder_proc

    :param  node:
        struct binder_node to acquire

.. _`binder_node_unlock.description`:

Description
-----------

Release lock acquired via \ :c:func:`binder_node_lock`\ 

.. _`binder_node_inner_lock`:

binder_node_inner_lock
======================

.. c:function::  binder_node_inner_lock( node)

    Acquire node and inner locks

    :param  node:
        struct binder_node to acquire

.. _`binder_node_inner_lock.description`:

Description
-----------

Acquires node->lock. If node->proc also acquires
proc->inner_lock. Used to protect binder_node fields

.. _`binder_node_inner_unlock`:

binder_node_inner_unlock
========================

.. c:function::  binder_node_inner_unlock( node)

    Release node and inner locks

    :param  node:
        struct binder_node to acquire

.. _`binder_node_inner_unlock.description`:

Description
-----------

Release lock acquired via \ :c:func:`binder_node_lock`\ 

.. _`binder_worklist_empty`:

binder_worklist_empty
=====================

.. c:function:: bool binder_worklist_empty(struct binder_proc *proc, struct list_head *list)

    Check if no items on the work list

    :param struct binder_proc \*proc:
        binder_proc associated with list

    :param struct list_head \*list:
        list to check

.. _`binder_worklist_empty.return`:

Return
------

true if there are no items on list, else false

.. _`binder_enqueue_work`:

binder_enqueue_work
===================

.. c:function:: void binder_enqueue_work(struct binder_proc *proc, struct binder_work *work, struct list_head *target_list)

    Add an item to the work list

    :param struct binder_proc \*proc:
        binder_proc associated with list

    :param struct binder_work \*work:
        struct binder_work to add to list

    :param struct list_head \*target_list:
        list to add work to

.. _`binder_enqueue_work.description`:

Description
-----------

Adds the work to the specified list. Asserts that work
is not already on a list.

.. _`binder_dequeue_work`:

binder_dequeue_work
===================

.. c:function:: void binder_dequeue_work(struct binder_proc *proc, struct binder_work *work)

    Removes an item from the work list

    :param struct binder_proc \*proc:
        binder_proc associated with list

    :param struct binder_work \*work:
        struct binder_work to remove from list

.. _`binder_dequeue_work.description`:

Description
-----------

Removes the specified work item from whatever list it is on.
Can safely be called if work is not on any list.

.. _`binder_dequeue_work_head`:

binder_dequeue_work_head
========================

.. c:function:: struct binder_work *binder_dequeue_work_head(struct binder_proc *proc, struct list_head *list)

    Dequeues the item at head of list

    :param struct binder_proc \*proc:
        binder_proc associated with list

    :param struct list_head \*list:
        list to dequeue head

.. _`binder_dequeue_work_head.description`:

Description
-----------

Removes the head of the list if there are items on the list

.. _`binder_dequeue_work_head.return`:

Return
------

pointer dequeued binder_work, NULL if list was empty

.. _`binder_select_thread_ilocked`:

binder_select_thread_ilocked
============================

.. c:function:: struct binder_thread *binder_select_thread_ilocked(struct binder_proc *proc)

    selects a thread for doing proc work.

    :param struct binder_proc \*proc:
        process to select a thread from

.. _`binder_select_thread_ilocked.description`:

Description
-----------

Note that calling this function moves the thread off the waiting_threads
list, so it can only be woken up by the caller of this function, or a
signal. Therefore, callers \*should\* always wake up the thread this function
returns.

.. _`binder_select_thread_ilocked.return`:

Return
------

If there's a thread currently waiting for process work,
returns that thread. Otherwise returns NULL.

.. _`binder_wakeup_thread_ilocked`:

binder_wakeup_thread_ilocked
============================

.. c:function:: void binder_wakeup_thread_ilocked(struct binder_proc *proc, struct binder_thread *thread, bool sync)

    wakes up a thread for doing proc work.

    :param struct binder_proc \*proc:
        process to wake up a thread in

    :param struct binder_thread \*thread:
        specific thread to wake-up (may be NULL)

    :param bool sync:
        whether to do a synchronous wake-up

.. _`binder_wakeup_thread_ilocked.description`:

Description
-----------

This function wakes up a thread in the \ ``proc``\  process.
The caller may provide a specific thread to wake-up in
the \ ``thread``\  parameter. If \ ``thread``\  is NULL, this function
will wake up threads that have called \ :c:func:`poll`\ .

Note that for this function to work as expected, callers
should first call \ :c:func:`binder_select_thread`\  to find a thread
to handle the work (if they don't have a thread already),
and pass the result into the \ ``thread``\  parameter.

.. _`binder_inc_node_tmpref`:

binder_inc_node_tmpref
======================

.. c:function:: void binder_inc_node_tmpref(struct binder_node *node)

    take a temporary reference on node

    :param struct binder_node \*node:
        node to reference

.. _`binder_inc_node_tmpref.description`:

Description
-----------

Take reference on node to prevent the node from being freed
while referenced only by a local variable. The inner lock is
needed to serialize with the node work on the queue (which
isn't needed after the node is dead). If the node is dead
(node->proc is NULL), use binder_dead_nodes_lock to protect
node->tmp_refs against dead-node-only cases where the node
lock cannot be acquired (eg traversing the dead node list to
print nodes)

.. _`binder_dec_node_tmpref`:

binder_dec_node_tmpref
======================

.. c:function:: void binder_dec_node_tmpref(struct binder_node *node)

    remove a temporary reference on node

    :param struct binder_node \*node:
        node to reference

.. _`binder_dec_node_tmpref.description`:

Description
-----------

Release temporary reference on node taken via \ :c:func:`binder_inc_node_tmpref`\ 

.. _`binder_get_ref_for_node_olocked`:

binder_get_ref_for_node_olocked
===============================

.. c:function:: struct binder_ref *binder_get_ref_for_node_olocked(struct binder_proc *proc, struct binder_node *node, struct binder_ref *new_ref)

    get the ref associated with given node

    :param struct binder_proc \*proc:
        binder_proc that owns the ref

    :param struct binder_node \*node:
        binder_node of target

    :param struct binder_ref \*new_ref:
        newly allocated binder_ref to be initialized or \ ``NULL``\ 

.. _`binder_get_ref_for_node_olocked.description`:

Description
-----------

Look up the ref for the given node and return it if it exists

If it doesn't exist and the caller provides a newly allocated
ref, initialize the fields of the newly allocated ref and insert
into the given proc rb_trees and node refs list.

.. _`binder_get_ref_for_node_olocked.return`:

Return
------

the ref for node. It is possible that another thread
allocated/initialized the ref first in which case the
returned ref would be different than the passed-in
new_ref. new_ref must be kfree'd by the caller in
this case.

.. _`binder_inc_ref_olocked`:

binder_inc_ref_olocked
======================

.. c:function:: int binder_inc_ref_olocked(struct binder_ref *ref, int strong, struct list_head *target_list)

    increment the ref for given handle

    :param struct binder_ref \*ref:
        ref to be incremented

    :param int strong:
        if true, strong increment, else weak

    :param struct list_head \*target_list:
        list to queue node work on

.. _`binder_inc_ref_olocked.description`:

Description
-----------

Increment the ref. \ ``ref``\ ->proc->outer_lock must be held on entry

.. _`binder_inc_ref_olocked.return`:

Return
------

0, if successful, else errno

.. _`binder_dec_ref_olocked`:

binder_dec_ref_olocked
======================

.. c:function:: bool binder_dec_ref_olocked(struct binder_ref *ref, int strong)

    dec the ref for given handle

    :param struct binder_ref \*ref:
        ref to be decremented

    :param int strong:
        if true, strong decrement, else weak

.. _`binder_dec_ref_olocked.description`:

Description
-----------

Decrement the ref.

.. _`binder_dec_ref_olocked.return`:

Return
------

true if ref is cleaned up and ready to be freed

.. _`binder_get_node_from_ref`:

binder_get_node_from_ref
========================

.. c:function:: struct binder_node *binder_get_node_from_ref(struct binder_proc *proc, u32 desc, bool need_strong_ref, struct binder_ref_data *rdata)

    get the node from the given proc/desc

    :param struct binder_proc \*proc:
        proc containing the ref

    :param u32 desc:
        the handle associated with the ref

    :param bool need_strong_ref:
        if true, only return node if ref is strong

    :param struct binder_ref_data \*rdata:
        the id/refcount data for the ref

.. _`binder_get_node_from_ref.description`:

Description
-----------

Given a proc and ref handle, return the associated binder_node

.. _`binder_get_node_from_ref.return`:

Return
------

a binder_node or NULL if not found or not strong when strong required

.. _`binder_free_ref`:

binder_free_ref
===============

.. c:function:: void binder_free_ref(struct binder_ref *ref)

    free the binder_ref

    :param struct binder_ref \*ref:
        ref to free

.. _`binder_free_ref.description`:

Description
-----------

Free the binder_ref. Free the binder_node indicated by ref->node
(if non-NULL) and the binder_ref_death indicated by ref->death.

.. _`binder_update_ref_for_handle`:

binder_update_ref_for_handle
============================

.. c:function:: int binder_update_ref_for_handle(struct binder_proc *proc, uint32_t desc, bool increment, bool strong, struct binder_ref_data *rdata)

    inc/dec the ref for given handle

    :param struct binder_proc \*proc:
        proc containing the ref

    :param uint32_t desc:
        the handle associated with the ref

    :param bool increment:
        true=inc reference, false=dec reference

    :param bool strong:
        true=strong reference, false=weak reference

    :param struct binder_ref_data \*rdata:
        the id/refcount data for the ref

.. _`binder_update_ref_for_handle.description`:

Description
-----------

Given a proc and ref handle, increment or decrement the ref
according to "increment" arg.

.. _`binder_update_ref_for_handle.return`:

Return
------

0 if successful, else errno

.. _`binder_dec_ref_for_handle`:

binder_dec_ref_for_handle
=========================

.. c:function:: int binder_dec_ref_for_handle(struct binder_proc *proc, uint32_t desc, bool strong, struct binder_ref_data *rdata)

    dec the ref for given handle

    :param struct binder_proc \*proc:
        proc containing the ref

    :param uint32_t desc:
        the handle associated with the ref

    :param bool strong:
        true=strong reference, false=weak reference

    :param struct binder_ref_data \*rdata:
        the id/refcount data for the ref

.. _`binder_dec_ref_for_handle.description`:

Description
-----------

Just calls \ :c:func:`binder_update_ref_for_handle`\  to decrement the ref.

.. _`binder_dec_ref_for_handle.return`:

Return
------

0 if successful, else errno

.. _`binder_inc_ref_for_node`:

binder_inc_ref_for_node
=======================

.. c:function:: int binder_inc_ref_for_node(struct binder_proc *proc, struct binder_node *node, bool strong, struct list_head *target_list, struct binder_ref_data *rdata)

    increment the ref for given proc/node

    :param struct binder_proc \*proc:
        proc containing the ref

    :param struct binder_node \*node:
        target node

    :param bool strong:
        true=strong reference, false=weak reference

    :param struct list_head \*target_list:
        worklist to use if node is incremented

    :param struct binder_ref_data \*rdata:
        the id/refcount data for the ref

.. _`binder_inc_ref_for_node.description`:

Description
-----------

Given a proc and node, increment the ref. Create the ref if it
doesn't already exist

.. _`binder_inc_ref_for_node.return`:

Return
------

0 if successful, else errno

.. _`binder_thread_dec_tmpref`:

binder_thread_dec_tmpref
========================

.. c:function:: void binder_thread_dec_tmpref(struct binder_thread *thread)

    decrement thread->tmp_ref

    :param struct binder_thread \*thread:
        thread to decrement

.. _`binder_thread_dec_tmpref.description`:

Description
-----------

A thread needs to be kept alive while being used to create or
handle a transaction. \ :c:func:`binder_get_txn_from`\  is used to safely
extract t->from from a binder_transaction and keep the thread
indicated by t->from from being freed. When done with that
binder_thread, this function is called to decrement the
tmp_ref and free if appropriate (thread has been released
and no transaction being processed by the driver)

.. _`binder_proc_dec_tmpref`:

binder_proc_dec_tmpref
======================

.. c:function:: void binder_proc_dec_tmpref(struct binder_proc *proc)

    decrement proc->tmp_ref

    :param struct binder_proc \*proc:
        proc to decrement

.. _`binder_proc_dec_tmpref.description`:

Description
-----------

A binder_proc needs to be kept alive while being used to create or
handle a transaction. proc->tmp_ref is incremented when
creating a new transaction or the binder_proc is currently in-use
by threads that are being released. When done with the binder_proc,
this function is called to decrement the counter and free the
proc if appropriate (proc has been released, all threads have
been released and not currenly in-use to process a transaction).

.. _`binder_get_txn_from`:

binder_get_txn_from
===================

.. c:function:: struct binder_thread *binder_get_txn_from(struct binder_transaction *t)

    safely extract the "from" thread in transaction

    :param struct binder_transaction \*t:
        binder transaction for t->from

.. _`binder_get_txn_from.description`:

Description
-----------

Atomically return the "from" thread and increment the tmp_ref
count for the thread to ensure it stays alive until
\ :c:func:`binder_thread_dec_tmpref`\  is called.

.. _`binder_get_txn_from.return`:

Return
------

the value of t->from

.. _`binder_get_txn_from_and_acq_inner`:

binder_get_txn_from_and_acq_inner
=================================

.. c:function:: struct binder_thread *binder_get_txn_from_and_acq_inner(struct binder_transaction *t)

    get t->from and acquire inner lock

    :param struct binder_transaction \*t:
        binder transaction for t->from

.. _`binder_get_txn_from_and_acq_inner.description`:

Description
-----------

Same as \ :c:func:`binder_get_txn_from`\  except it also acquires the proc->inner_lock
to guarantee that the thread cannot be released while operating on it.
The caller must call \ :c:func:`binder_inner_proc_unlock`\  to release the inner lock
as well as call \ :c:func:`binder_dec_thread_txn`\  to release the reference.

.. _`binder_get_txn_from_and_acq_inner.return`:

Return
------

the value of t->from

.. _`binder_cleanup_transaction`:

binder_cleanup_transaction
==========================

.. c:function:: void binder_cleanup_transaction(struct binder_transaction *t, const char *reason, uint32_t error_code)

    cleans up undelivered transaction

    :param struct binder_transaction \*t:
        transaction that needs to be cleaned up

    :param const char \*reason:
        reason the transaction wasn't delivered

    :param uint32_t error_code:
        error to return to caller (if synchronous call)

.. _`binder_validate_object`:

binder_validate_object
======================

.. c:function:: size_t binder_validate_object(struct binder_buffer *buffer, u64 offset)

    checks for a valid metadata object in a buffer.

    :param struct binder_buffer \*buffer:
        binder_buffer that we're parsing.

    :param u64 offset:
        offset in the buffer at which to validate an object.

.. _`binder_validate_object.return`:

Return
------

If there's a valid metadata object at \ ``offset``\  in \ ``buffer``\ , the
size of that object. Otherwise, it returns zero.

.. _`binder_validate_ptr`:

binder_validate_ptr
===================

.. c:function:: struct binder_buffer_object *binder_validate_ptr(struct binder_buffer *b, binder_size_t index, binder_size_t *start, binder_size_t num_valid)

    validates binder_buffer_object in a binder_buffer.

    :param struct binder_buffer \*b:
        binder_buffer containing the object

    :param binder_size_t index:
        index in offset array at which the binder_buffer_object is
        located

    :param binder_size_t \*start:
        points to the start of the offset array

    :param binder_size_t num_valid:
        the number of valid offsets in the offset array

.. _`binder_validate_ptr.return`:

Return
------

If \ ``index``\  is within the valid range of the offset array
described by \ ``start``\  and \ ``num_valid``\ , and if there's a valid
binder_buffer_object at the offset found in index \ ``index``\ 
of the offset array, that object is returned. Otherwise,
\ ``NULL``\  is returned.
Note that the offset found in index \ ``index``\  itself is not
verified; this function assumes that \ ``num_valid``\  elements
from \ ``start``\  were previously verified to have valid offsets.

.. _`binder_validate_fixup`:

binder_validate_fixup
=====================

.. c:function:: bool binder_validate_fixup(struct binder_buffer *b, binder_size_t *objects_start, struct binder_buffer_object *buffer, binder_size_t fixup_offset, struct binder_buffer_object *last_obj, binder_size_t last_min_offset)

    validates pointer/fd fixups happen in order.

    :param struct binder_buffer \*b:
        transaction buffer
        \ ``objects_start``\        start of objects buffer

    :param binder_size_t \*objects_start:
        *undescribed*

    :param struct binder_buffer_object \*buffer:
        binder_buffer_object in which to fix up

    :param binder_size_t fixup_offset:
        *undescribed*

    :param struct binder_buffer_object \*last_obj:
        last binder_buffer_object that we fixed up in

    :param binder_size_t last_min_offset:
        minimum fixup offset in \ ``last_obj``\ 

.. _`binder_validate_fixup.return`:

Return
------

%true if a fixup in buffer \ ``buffer``\  at offset \ ``offset``\  is
allowed.

For safety reasons, we only allow fixups inside a buffer to happen
at increasing offsets; additionally, we only allow fixup on the last
buffer object that was verified, or one of its parents.

.. _`binder_validate_fixup.example-of-what-is-allowed`:

Example of what is allowed
--------------------------


A
B (parent = A, offset = 0)
C (parent = A, offset = 16)
D (parent = C, offset = 0)
E (parent = A, offset = 32) // min_offset is 16 (C.parent_offset)

.. _`binder_validate_fixup.decreasing-offsets-within-the-same-parent`:

Decreasing offsets within the same parent
-----------------------------------------


A
C (parent = A, offset = 16)
B (parent = A, offset = 0) // decreasing offset within A

Referring to a parent that wasn't the last object or any of its parents:
A
B (parent = A, offset = 0)
C (parent = A, offset = 0)
C (parent = A, offset = 16)
D (parent = B, offset = 0) // B is not A or any of A's parents

.. _`binder_proc_transaction`:

binder_proc_transaction
=======================

.. c:function:: bool binder_proc_transaction(struct binder_transaction *t, struct binder_proc *proc, struct binder_thread *thread)

    sends a transaction to a process and wakes it up

    :param struct binder_transaction \*t:
        transaction to send

    :param struct binder_proc \*proc:
        process to send the transaction to

    :param struct binder_thread \*thread:
        thread in \ ``proc``\  to send the transaction to (may be NULL)

.. _`binder_proc_transaction.description`:

Description
-----------

This function queues a transaction to the specified process. It will try
to find a thread in the target process to handle the transaction and
wake it up. If no thread is found, the work is queued to the proc
waitqueue.

If the \ ``thread``\  parameter is not NULL, the transaction is always queued
to the waitlist of that specific thread.

.. _`binder_proc_transaction.return`:

Return
------

true if the transactions was successfully queued
false if the target process or thread is dead

.. _`binder_get_node_refs_for_txn`:

binder_get_node_refs_for_txn
============================

.. c:function:: struct binder_node *binder_get_node_refs_for_txn(struct binder_node *node, struct binder_proc **procp, uint32_t *error)

    Get required refs on node for txn

    :param struct binder_node \*node:
        struct binder_node for which to get refs

    :param struct binder_proc \*\*procp:
        *undescribed*

    :param uint32_t \*error:
        if no \ ``proc``\  then returns BR_DEAD_REPLY

.. _`binder_get_node_refs_for_txn.description`:

Description
-----------

User-space normally keeps the node alive when creating a transaction
since it has a reference to the target. The local strong ref keeps it
alive if the sending process dies before the target process processes
the transaction. If the source process is malicious or has a reference
counting bug, relying on the local strong ref can fail.

Since user-space can cause the local strong ref to go away, we also take
a tmpref on the node to ensure it survives while we are constructing
the transaction. We also need a tmpref on the proc while we are
constructing the transaction, so we take that here as well.

.. _`binder_get_node_refs_for_txn.return`:

Return
------

The target_node with refs taken or NULL if no \ ``node``\ ->proc is NULL.
Also sets \ ``proc``\  if valid. If the \ ``node``\ ->proc is NULL indicating that the
target proc has died, \ ``error``\  is set to BR_DEAD_REPLY

.. This file was automatic generated / don't edit.

