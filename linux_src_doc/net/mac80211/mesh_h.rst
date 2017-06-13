.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/mesh.h

.. _`mesh_path_flags`:

enum mesh_path_flags
====================

.. c:type:: enum mesh_path_flags

    mac80211 mesh path flags

.. _`mesh_path_flags.definition`:

Definition
----------

.. code-block:: c

    enum mesh_path_flags {
        MESH_PATH_ACTIVE,
        MESH_PATH_RESOLVING,
        MESH_PATH_SN_VALID,
        MESH_PATH_FIXED,
        MESH_PATH_RESOLVED,
        MESH_PATH_REQ_QUEUED,
        MESH_PATH_DELETED
    };

.. _`mesh_path_flags.constants`:

Constants
---------

MESH_PATH_ACTIVE
    the mesh path can be used for forwarding

MESH_PATH_RESOLVING
    the discovery process is running for this mesh path

MESH_PATH_SN_VALID
    the mesh path contains a valid destination sequence
    number

MESH_PATH_FIXED
    the mesh path has been manually set and should not be
    modified

MESH_PATH_RESOLVED
    the mesh path can has been resolved

MESH_PATH_REQ_QUEUED
    there is an unsent path request for this destination
    already queued up, waiting for the discovery process to start.

MESH_PATH_DELETED
    the mesh path has been deleted and should no longer
    be used

.. _`mesh_path_flags.description`:

Description
-----------

MESH_PATH_RESOLVED is used by the mesh path timer to
decide when to stop or cancel the mesh path discovery.

.. _`mesh_deferred_task_flags`:

enum mesh_deferred_task_flags
=============================

.. c:type:: enum mesh_deferred_task_flags

    mac80211 mesh deferred tasks

.. _`mesh_deferred_task_flags.definition`:

Definition
----------

.. code-block:: c

    enum mesh_deferred_task_flags {
        MESH_WORK_HOUSEKEEPING,
        MESH_WORK_ROOT,
        MESH_WORK_DRIFT_ADJUST,
        MESH_WORK_MBSS_CHANGED
    };

.. _`mesh_deferred_task_flags.constants`:

Constants
---------

MESH_WORK_HOUSEKEEPING
    run the periodic mesh housekeeping tasks

MESH_WORK_ROOT
    the mesh root station needs to send a frame

MESH_WORK_DRIFT_ADJUST
    time to compensate for clock drift relative to other
    mesh nodes

MESH_WORK_MBSS_CHANGED
    rebuild beacon and notify driver of BSS changes

.. _`mesh_path`:

struct mesh_path
================

.. c:type:: struct mesh_path

    mac80211 mesh path structure

.. _`mesh_path.definition`:

Definition
----------

.. code-block:: c

    struct mesh_path {
        u8 dst;
        u8 mpp;
        struct rhash_head rhash;
        struct hlist_node gate_list;
        struct ieee80211_sub_if_data *sdata;
        struct sta_info __rcu *next_hop;
        struct timer_list timer;
        struct sk_buff_head frame_queue;
        struct rcu_head rcu;
        u32 sn;
        u32 metric;
        u8 hop_count;
        unsigned long exp_time;
        u32 discovery_timeout;
        u8 discovery_retries;
        enum mesh_path_flags flags;
        spinlock_t state_lock;
        u8 rann_snd_addr;
        u32 rann_metric;
        unsigned long last_preq_to_root;
        bool is_root;
        bool is_gate;
    }

.. _`mesh_path.members`:

Members
-------

dst
    mesh path destination mac address

mpp
    mesh proxy mac address

rhash
    rhashtable list pointer

gate_list
    list pointer for known gates list

sdata
    mesh subif

next_hop
    mesh neighbor to which frames for this destination will be
    forwarded

timer
    mesh path discovery timer

frame_queue
    pending queue for frames sent to this destination while the
    path is unresolved

rcu
    rcu head for freeing mesh path

sn
    target sequence number

metric
    current metric to this destination

hop_count
    hops to destination

exp_time
    in jiffies, when the path will expire or when it expired

discovery_timeout
    timeout (lapse in jiffies) used for the last discovery
    retry

discovery_retries
    number of discovery retries

flags
    mesh path flags, as specified on \ :c:type:`enum mesh_path_flags <mesh_path_flags>`\ 

state_lock
    mesh path state lock used to protect changes to the
    mpath itself.  No need to take this lock when adding or removing
    an mpath to a hash bucket on a path table.

rann_snd_addr
    the RANN sender address

rann_metric
    the aggregated path metric towards the root node

last_preq_to_root
    Timestamp of last PREQ sent to root

is_root
    the destination station of this path is a root node

is_gate
    the destination station of this path is a mesh gate

.. _`mesh_path.description`:

Description
-----------


The dst address is unique in the mesh path table. Since the mesh_path is
protected by RCU, deleting the next_hop STA must remove / substitute the
mesh_path structure and wait until that is no longer reachable before
destroying the STA completely.

.. _`mesh_table`:

struct mesh_table
=================

.. c:type:: struct mesh_table


.. _`mesh_table.definition`:

Definition
----------

.. code-block:: c

    struct mesh_table {
        struct hlist_head known_gates;
        spinlock_t gates_lock;
        struct rhashtable rhead;
        atomic_t entries;
    }

.. _`mesh_table.members`:

Members
-------

known_gates
    list of known mesh gates and their mpaths by the station. The
    gate's mpath may or may not be resolved and active.

gates_lock
    protects updates to known_gates

rhead
    the rhashtable containing struct mesh_paths, keyed by dest addr

entries
    number of entries in the table

.. _`rmc_entry`:

struct rmc_entry
================

.. c:type:: struct rmc_entry

    entry in the Recent Multicast Cache

.. _`rmc_entry.definition`:

Definition
----------

.. code-block:: c

    struct rmc_entry {
        struct hlist_node list;
        unsigned long exp_time;
        u32 seqnum;
        u8 sa;
    }

.. _`rmc_entry.members`:

Members
-------

list
    hashtable list pointer

exp_time
    expiration time of the entry, in jiffies

seqnum
    mesh sequence number of the frame

sa
    source address of the frame

.. _`rmc_entry.description`:

Description
-----------

The Recent Multicast Cache keeps track of the latest multicast frames that
have been received by a mesh interface and discards received multicast frames
that are found in the cache.

.. This file was automatic generated / don't edit.

