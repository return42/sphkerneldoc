.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/uv/uv_bau.h

.. _`uv1_2_3_bau_msg_payload`:

struct uv1_2_3_bau_msg_payload
==============================

.. c:type:: struct uv1_2_3_bau_msg_payload

    defines payload for INTD transactions

.. _`uv1_2_3_bau_msg_payload.definition`:

Definition
----------

.. code-block:: c

    struct uv1_2_3_bau_msg_payload {
        u64 address;
        u16 sending_cpu;
        u16 acknowledge_count;
    }

.. _`uv1_2_3_bau_msg_payload.members`:

Members
-------

address
    Signifies a page or all TLB's of the cpu

sending_cpu
    CPU from which the message originates

acknowledge_count
    CPUs on the destination Hub that received the interrupt

.. _`uv4_bau_msg_payload`:

struct uv4_bau_msg_payload
==========================

.. c:type:: struct uv4_bau_msg_payload

    defines payload for INTD transactions

.. _`uv4_bau_msg_payload.definition`:

Definition
----------

.. code-block:: c

    struct uv4_bau_msg_payload {
        u64 address;
        u16 sending_cpu;
        u16 acknowledge_count;
        u32 reserved:8;
        u32 qualifier:24;
    }

.. _`uv4_bau_msg_payload.members`:

Members
-------

address
    Signifies a page or all TLB's of the cpu

sending_cpu
    CPU from which the message originates

acknowledge_count
    CPUs on the destination Hub that received the interrupt

reserved
    *undescribed*

qualifier
    Set by source to verify origin of INTD broadcast

.. _`bau_control`:

struct bau_control
==================

.. c:type:: struct bau_control


.. _`bau_control.definition`:

Definition
----------

.. code-block:: c

    struct bau_control {
        struct bau_desc *descriptor_base;
        struct bau_pq_entry *queue_first;
        struct bau_pq_entry *queue_last;
        struct bau_pq_entry *bau_msg_head;
        struct bau_control *uvhub_master;
        struct bau_control *socket_master;
        struct ptc_stats *statp;
        cpumask_t *cpumask;
        unsigned long timeout_interval;
        unsigned long set_bau_on_time;
        atomic_t active_descriptor_count;
        int plugged_tries;
        int timeout_tries;
        int ipi_attempts;
        int conseccompletes;
        u64 status_mmr;
        int status_index;
        bool nobau;
        short baudisabled;
        short cpu;
        short osnode;
        short uvhub_cpu;
        short uvhub;
        short uvhub_version;
        short cpus_in_socket;
        short cpus_in_uvhub;
        short partition_base_pnode;
        short busy;
        unsigned short message_number;
        unsigned short uvhub_quiesce;
        short socket_acknowledge_count;
        cycles_t send_message;
        cycles_t period_end;
        cycles_t period_time;
        spinlock_t uvhub_lock;
        spinlock_t queue_lock;
        spinlock_t disable_lock;
        int max_concurr;
        int max_concurr_const;
        int plugged_delay;
        int plugsb4reset;
        int timeoutsb4reset;
        int ipi_reset_limit;
        int complete_threshold;
        int cong_response_us;
        int cong_reps;
        cycles_t disabled_period;
        int period_giveups;
        int giveup_limit;
        long period_requests;
        struct hub_and_pnode *thp;
    }

.. _`bau_control.members`:

Members
-------

descriptor_base
    *undescribed*

queue_first
    *undescribed*

queue_last
    *undescribed*

bau_msg_head
    *undescribed*

uvhub_master
    *undescribed*

socket_master
    *undescribed*

statp
    *undescribed*

cpumask
    *undescribed*

timeout_interval
    *undescribed*

set_bau_on_time
    *undescribed*

active_descriptor_count
    *undescribed*

plugged_tries
    *undescribed*

timeout_tries
    *undescribed*

ipi_attempts
    *undescribed*

conseccompletes
    *undescribed*

status_mmr
    location of status mmr, determined by uvhub_cpu

status_index
    index of ERR\|BUSY bits in status mmr, determined by uvhub_cpu

nobau
    *undescribed*

baudisabled
    *undescribed*

cpu
    *undescribed*

osnode
    *undescribed*

uvhub_cpu
    *undescribed*

uvhub
    *undescribed*

uvhub_version
    *undescribed*

cpus_in_socket
    *undescribed*

cpus_in_uvhub
    *undescribed*

partition_base_pnode
    *undescribed*

busy
    *undescribed*

message_number
    *undescribed*

uvhub_quiesce
    *undescribed*

socket_acknowledge_count
    *undescribed*

send_message
    *undescribed*

period_end
    *undescribed*

period_time
    *undescribed*

uvhub_lock
    *undescribed*

queue_lock
    *undescribed*

disable_lock
    *undescribed*

max_concurr
    *undescribed*

max_concurr_const
    *undescribed*

plugged_delay
    *undescribed*

plugsb4reset
    *undescribed*

timeoutsb4reset
    *undescribed*

ipi_reset_limit
    *undescribed*

complete_threshold
    *undescribed*

cong_response_us
    *undescribed*

cong_reps
    *undescribed*

disabled_period
    *undescribed*

period_giveups
    *undescribed*

giveup_limit
    *undescribed*

period_requests
    *undescribed*

thp
    *undescribed*

.. _`bau_control.description`:

Description
-----------

Per-cpu control struct containing CPU topology information and BAU tuneables.

.. This file was automatic generated / don't edit.

