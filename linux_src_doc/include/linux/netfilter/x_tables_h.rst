.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/netfilter/x_tables.h

.. _`xt_action_param`:

struct xt_action_param
======================

.. c:type:: struct xt_action_param

    parameters for matches/targets

.. _`xt_action_param.definition`:

Definition
----------

.. code-block:: c

    struct xt_action_param {
        union {unnamed_union};
        union {unnamed_union};
        const struct nf_hook_state *state;
        int fragoff;
        unsigned int thoff;
        bool hotdrop;
    }

.. _`xt_action_param.members`:

Members
-------

{unnamed_union}
    anonymous


{unnamed_union}
    anonymous


state
    pointer to hook state this packet came from

fragoff
    packet is a fragment, this is the data offset

thoff
    position of transport header relative to skb->data

hotdrop
    drop packet if we had inspection problems

.. _`xt_mtchk_param`:

struct xt_mtchk_param
=====================

.. c:type:: struct xt_mtchk_param

    parameters for match extensions' checkentry functions

.. _`xt_mtchk_param.definition`:

Definition
----------

.. code-block:: c

    struct xt_mtchk_param {
        struct net *net;
        const char *table;
        const void *entryinfo;
        const struct xt_match *match;
        void *matchinfo;
        unsigned int hook_mask;
        u_int8_t family;
        bool nft_compat;
    }

.. _`xt_mtchk_param.members`:

Members
-------

net
    network namespace through which the check was invoked

table
    table the rule is tried to be inserted into

entryinfo
    the family-specific rule data
    (struct ipt_ip, ip6t_ip, arpt_arp or (note) ebt_entry)

match
    struct xt_match through which this function was invoked

matchinfo
    per-match data

hook_mask
    via which hooks the new rule is reachable
    Other fields as above.

family
    *undescribed*

nft_compat
    *undescribed*

.. _`xt_mtdtor_param`:

struct xt_mtdtor_param
======================

.. c:type:: struct xt_mtdtor_param

    match destructor parameters Fields as above.

.. _`xt_mtdtor_param.definition`:

Definition
----------

.. code-block:: c

    struct xt_mtdtor_param {
        struct net *net;
        const struct xt_match *match;
        void *matchinfo;
        u_int8_t family;
    }

.. _`xt_mtdtor_param.members`:

Members
-------

net
    *undescribed*

match
    *undescribed*

matchinfo
    *undescribed*

family
    *undescribed*

.. _`xt_tgchk_param`:

struct xt_tgchk_param
=====================

.. c:type:: struct xt_tgchk_param

    parameters for target extensions' checkentry functions

.. _`xt_tgchk_param.definition`:

Definition
----------

.. code-block:: c

    struct xt_tgchk_param {
        struct net *net;
        const char *table;
        const void *entryinfo;
        const struct xt_target *target;
        void *targinfo;
        unsigned int hook_mask;
        u_int8_t family;
        bool nft_compat;
    }

.. _`xt_tgchk_param.members`:

Members
-------

net
    *undescribed*

table
    *undescribed*

entryinfo
    the family-specific rule data
    (struct ipt_entry, ip6t_entry, arpt_entry, ebt_entry)

target
    *undescribed*

targinfo
    *undescribed*

hook_mask
    *undescribed*

family
    *undescribed*

nft_compat
    *undescribed*

.. _`xt_tgchk_param.description`:

Description
-----------

Other fields see above.

.. _`declare_per_cpu`:

DECLARE_PER_CPU
===============

.. c:function::  DECLARE_PER_CPU( seqcount_t,  xt_recseq)

    recursive seqcount for netfilter use

    :param  seqcount_t:
        *undescribed*

    :param  xt_recseq:
        *undescribed*

.. _`declare_per_cpu.description`:

Description
-----------

Packet processing changes the seqcount only if no recursion happened
\ :c:func:`get_counters`\  can use \ :c:func:`read_seqcount_begin`\ /read_seqcount_retry(),
because we use the normal seqcount convention :
Low order bit set to 1 if a writer is active.

.. _`xt_write_recseq_begin`:

xt_write_recseq_begin
=====================

.. c:function:: unsigned int xt_write_recseq_begin( void)

    start of a write section

    :param  void:
        no arguments

.. _`xt_write_recseq_begin.description`:

Description
-----------

Begin packet processing : all readers must wait the end
1) Must be called with preemption disabled
2) softirqs must be disabled too (or we should use \ :c:func:`this_cpu_add`\ )
Returns :
1 if no recursion on this cpu
0 if recursion detected

.. _`xt_write_recseq_end`:

xt_write_recseq_end
===================

.. c:function:: void xt_write_recseq_end(unsigned int addend)

    end of a write section

    :param unsigned int addend:
        return value from previous \ :c:func:`xt_write_recseq_begin`\ 

.. _`xt_write_recseq_end.description`:

Description
-----------

End packet processing : all readers can proceed
1) Must be called with preemption disabled
2) softirqs must be disabled too (or we should use \ :c:func:`this_cpu_add`\ )

.. This file was automatic generated / don't edit.

