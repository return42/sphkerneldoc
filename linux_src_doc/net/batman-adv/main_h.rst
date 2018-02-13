.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/main.h

.. _`batadv_tp_max_num`:

BATADV_TP_MAX_NUM
=================

.. c:function::  BATADV_TP_MAX_NUM()

    maximum number of simultaneously active tp sessions

.. _`batadv_mesh_state`:

enum batadv_mesh_state
======================

.. c:type:: enum batadv_mesh_state

    State of a soft interface

.. _`batadv_mesh_state.definition`:

Definition
----------

.. code-block:: c

    enum batadv_mesh_state {
        BATADV_MESH_INACTIVE,
        BATADV_MESH_ACTIVE,
        BATADV_MESH_DEACTIVATING
    };

.. _`batadv_mesh_state.constants`:

Constants
---------

BATADV_MESH_INACTIVE
    soft interface is not yet running

BATADV_MESH_ACTIVE
    interface is up and running

BATADV_MESH_DEACTIVATING
    interface is getting shut down

.. _`batadv_uev_action`:

enum batadv_uev_action
======================

.. c:type:: enum batadv_uev_action

    action type of uevent

.. _`batadv_uev_action.definition`:

Definition
----------

.. code-block:: c

    enum batadv_uev_action {
        BATADV_UEV_ADD,
        BATADV_UEV_DEL,
        BATADV_UEV_CHANGE,
        BATADV_UEV_LOOPDETECT
    };

.. _`batadv_uev_action.constants`:

Constants
---------

BATADV_UEV_ADD
    gateway was selected (after none was selected)

BATADV_UEV_DEL
    selected gateway was removed and none is selectedanymore

BATADV_UEV_CHANGE
    a different gateway was selected as based gateway

BATADV_UEV_LOOPDETECT
    loop was detected which cannot be handled bybridge loop avoidance

.. _`batadv_uev_type`:

enum batadv_uev_type
====================

.. c:type:: enum batadv_uev_type

    Type of uevent

.. _`batadv_uev_type.definition`:

Definition
----------

.. code-block:: c

    enum batadv_uev_type {
        BATADV_UEV_GW,
        BATADV_UEV_BLA
    };

.. _`batadv_uev_type.constants`:

Constants
---------

BATADV_UEV_GW
    selected gateway was modified

BATADV_UEV_BLA
    bridge loop avoidance event

.. _`batadv_print_vid`:

batadv_print_vid
================

.. c:function:: int batadv_print_vid(unsigned short vid)

    return printable version of vid information

    :param unsigned short vid:
        the VLAN identifier

.. _`batadv_print_vid.return`:

Return
------

-1 when no VLAN is used, VLAN id otherwise

.. _`batadv_compare_eth`:

batadv_compare_eth
==================

.. c:function:: bool batadv_compare_eth(const void *data1, const void *data2)

    Compare two not u16 aligned Ethernet addresses

    :param const void \*data1:
        Pointer to a six-byte array containing the Ethernet address

    :param const void \*data2:
        Pointer other six-byte array containing the Ethernet address

.. _`batadv_compare_eth.note`:

note
----

can't use \ :c:func:`ether_addr_equal`\  as it requires aligned memory

.. _`batadv_compare_eth.return`:

Return
------

true if they are the same ethernet addr

.. _`batadv_has_timed_out`:

batadv_has_timed_out
====================

.. c:function:: bool batadv_has_timed_out(unsigned long timestamp, unsigned int timeout)

    compares current time (jiffies) and timestamp + timeout

    :param unsigned long timestamp:
        base value to compare with (in jiffies)

    :param unsigned int timeout:
        added to base value before comparing (in milliseconds)

.. _`batadv_has_timed_out.return`:

Return
------

true if current time is after timestamp + timeout

.. _`batadv_atomic_dec_not_zero`:

batadv_atomic_dec_not_zero
==========================

.. c:function::  batadv_atomic_dec_not_zero( v)

    Decrease unless the number is 0

    :param  v:
        pointer of type atomic_t

.. _`batadv_atomic_dec_not_zero.return`:

Return
------

non-zero if v was not 0, and zero otherwise.

.. _`batadv_smallest_signed_int`:

batadv_smallest_signed_int
==========================

.. c:function::  batadv_smallest_signed_int( x)

    Returns the smallest signed integer in two's complement with the sizeof x

    :param  x:
        type of integer

.. _`batadv_smallest_signed_int.return`:

Return
------

smallest signed integer of type

.. _`batadv_seq_before`:

batadv_seq_before
=================

.. c:function::  batadv_seq_before( x,  y)

    Checks if a sequence number x is a predecessor of y

    :param  x:
        potential predecessor of \ ``y``\ 

    :param  y:
        value to compare \ ``x``\  against

.. _`batadv_seq_before.description`:

Description
-----------

It handles overflows/underflows and can correctly check for a predecessor
unless the variable sequence number has grown by more then
2\*\*(bitwidth(x)-1)-1.

This means that for a u8 with the maximum value 255, it would think:

\* when adding nothing - it is neither a predecessor nor a successor
\* before adding more than 127 to the starting value - it is a predecessor,
\* when adding 128 - it is neither a predecessor nor a successor,
\* after adding more than 127 to the starting value - it is a successor

.. _`batadv_seq_before.return`:

Return
------

true when x is a predecessor of y, false otherwise

.. _`batadv_seq_after`:

batadv_seq_after
================

.. c:function::  batadv_seq_after( x,  y)

    Checks if a sequence number x is a successor of y

    :param  x:
        potential sucessor of \ ``y``\ 

    :param  y:
        value to compare \ ``x``\  against

.. _`batadv_seq_after.description`:

Description
-----------

It handles overflows/underflows and can correctly check for a successor
unless the variable sequence number has grown by more then
2\*\*(bitwidth(x)-1)-1.

This means that for a u8 with the maximum value 255, it would think:

\* when adding nothing - it is neither a predecessor nor a successor
\* before adding more than 127 to the starting value - it is a predecessor,
\* when adding 128 - it is neither a predecessor nor a successor,
\* after adding more than 127 to the starting value - it is a successor

.. _`batadv_seq_after.return`:

Return
------

true when x is a successor of y, false otherwise

.. _`batadv_add_counter`:

batadv_add_counter
==================

.. c:function:: void batadv_add_counter(struct batadv_priv *bat_priv, size_t idx, size_t count)

    Add to per cpu statistics counter of soft interface

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param size_t idx:
        counter index which should be modified

    :param size_t count:
        value to increase counter by

.. _`batadv_add_counter.description`:

Description
-----------

Stop preemption on local cpu while incrementing the counter

.. _`batadv_inc_counter`:

batadv_inc_counter
==================

.. c:function::  batadv_inc_counter( b,  i)

    Increase per cpu statistics counter of soft interface

    :param  b:
        the bat priv with all the soft interface information

    :param  i:
        counter index which should be modified

.. _`batadv_skb_cb`:

BATADV_SKB_CB
=============

.. c:function::  BATADV_SKB_CB( __skb)

    Get batadv_skb_cb from skb control buffer

    :param  __skb:
        skb holding the control buffer

.. _`batadv_skb_cb.description`:

Description
-----------

The members of the control buffer are defined in struct batadv_skb_cb in
types.h. The macro is inspired by the similar macro \ :c:func:`TCP_SKB_CB`\  in tcp.h.

.. _`batadv_skb_cb.return`:

Return
------

pointer to the batadv_skb_cb of the skb

.. This file was automatic generated / don't edit.

