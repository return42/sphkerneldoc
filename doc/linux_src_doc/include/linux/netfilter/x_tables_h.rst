.. -*- coding: utf-8; mode: rst -*-

==========
x_tables.h
==========


.. _`xt_action_param`:

struct xt_action_param
======================

.. c:type:: xt_action_param

    parameters for matches/targets


.. _`xt_action_param.definition`:

Definition
----------

.. code-block:: c

  struct xt_action_param {
    union {unnamed_union};
    const struct net_device * in;
    const struct net_device * out;
    int fragoff;
    unsigned int thoff;
    u_int8_t family;
    bool hotdrop;
  };


.. _`xt_action_param.members`:

Members
-------

:``{unnamed_union}``:
    anonymous

:``in``:
    input netdevice

:``out``:
    output netdevice

:``fragoff``:
    packet is a fragment, this is the data offset

:``thoff``:
    position of transport header relative to skb->data

:``family``:
    Actual NFPROTO\_\* through which the function is invoked
    (helpful when match->family == NFPROTO_UNSPEC)

:``hotdrop``:
    drop packet if we had inspection problems




.. _`xt_mtchk_param`:

struct xt_mtchk_param
=====================

.. c:type:: xt_mtchk_param

    parameters for match extensions' checkentry functions


.. _`xt_mtchk_param.definition`:

Definition
----------

.. code-block:: c

  struct xt_mtchk_param {
    struct net * net;
    const char * table;
    const void * entryinfo;
    const struct xt_match * match;
    void * matchinfo;
    unsigned int hook_mask;
  };


.. _`xt_mtchk_param.members`:

Members
-------

:``net``:
    network namespace through which the check was invoked

:``table``:
    table the rule is tried to be inserted into

:``entryinfo``:
    the family-specific rule data
    (struct ipt_ip, ip6t_ip, arpt_arp or (note) ebt_entry)

:``match``:
    struct xt_match through which this function was invoked

:``matchinfo``:
    per-match data

:``hook_mask``:
    via which hooks the new rule is reachable
    Other fields as above.




.. _`xt_mtdtor_param`:

struct xt_mtdtor_param
======================

.. c:type:: xt_mtdtor_param

    match destructor parameters Fields as above.


.. _`xt_mtdtor_param.definition`:

Definition
----------

.. code-block:: c

  struct xt_mtdtor_param {
  };


.. _`xt_mtdtor_param.members`:

Members
-------




.. _`xt_tgchk_param`:

struct xt_tgchk_param
=====================

.. c:type:: xt_tgchk_param

    parameters for target extensions' checkentry functions


.. _`xt_tgchk_param.definition`:

Definition
----------

.. code-block:: c

  struct xt_tgchk_param {
    const void * entryinfo;
  };


.. _`xt_tgchk_param.members`:

Members
-------

:``entryinfo``:
    the family-specific rule data
    (struct ipt_entry, ip6t_entry, arpt_entry, ebt_entry)




.. _`xt_tgchk_param.description`:

Description
-----------

Other fields see above.



.. _`declare_per_cpu`:

DECLARE_PER_CPU
===============

.. c:function:: DECLARE_PER_CPU ( seqcount_t,  xt_recseq)

    recursive seqcount for netfilter use

    :param seqcount_t:

        *undescribed*

    :param xt_recseq:

        *undescribed*



.. _`declare_per_cpu.description`:

Description
-----------


Packet processing changes the seqcount only if no recursion happened
:c:func:`get_counters` can use :c:func:`read_seqcount_begin`/:c:func:`read_seqcount_retry`,



.. _`declare_per_cpu.because-we-use-the-normal-seqcount-convention`:

because we use the normal seqcount convention 
----------------------------------------------

Low order bit set to 1 if a writer is active.



.. _`xt_write_recseq_begin`:

xt_write_recseq_begin
=====================

.. c:function:: unsigned int xt_write_recseq_begin ( void)

    start of a write section

    :param void:
        no arguments



.. _`xt_write_recseq_begin.begin-packet-processing`:

Begin packet processing 
------------------------

all readers must wait the end
1) Must be called with preemption disabled
2) softirqs must be disabled too (or we should use :c:func:`this_cpu_add`)



.. _`xt_write_recseq_begin.returns`:

Returns 
--------

1 if no recursion on this cpu
0 if recursion detected



.. _`xt_write_recseq_end`:

xt_write_recseq_end
===================

.. c:function:: void xt_write_recseq_end (unsigned int addend)

    end of a write section

    :param unsigned int addend:
        return value from previous :c:func:`xt_write_recseq_begin`



.. _`xt_write_recseq_end.end-packet-processing`:

End packet processing 
----------------------

all readers can proceed
1) Must be called with preemption disabled
2) softirqs must be disabled too (or we should use :c:func:`this_cpu_add`)

