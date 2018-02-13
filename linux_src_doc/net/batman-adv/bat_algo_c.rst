.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_algo.c

.. _`batadv_algo_init`:

batadv_algo_init
================

.. c:function:: void batadv_algo_init( void)

    Initialize batman-adv algorithm management data structures

    :param  void:
        no arguments

.. _`batadv_algo_register`:

batadv_algo_register
====================

.. c:function:: int batadv_algo_register(struct batadv_algo_ops *bat_algo_ops)

    Register callbacks for a mesh algorithm

    :param struct batadv_algo_ops \*bat_algo_ops:
        mesh algorithm callbacks to add

.. _`batadv_algo_register.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_algo_select`:

batadv_algo_select
==================

.. c:function:: int batadv_algo_select(struct batadv_priv *bat_priv, char *name)

    Select algorithm of soft interface

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param char \*name:
        name of the algorithm to select

.. _`batadv_algo_select.description`:

Description
-----------

The algorithm callbacks for the soft interface will be set when the algorithm
with the correct name was found. Any previous selected algorithm will not be
deinitialized and the new selected algorithm will also not be initialized.
It is therefore not allowed to call batadv_algo_select outside the creation
function of the soft interface.

.. _`batadv_algo_select.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_algo_seq_print_text`:

batadv_algo_seq_print_text
==========================

.. c:function:: int batadv_algo_seq_print_text(struct seq_file *seq, void *offset)

    Print the supported algorithms in a seq file

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_algo_seq_print_text.return`:

Return
------

always 0

.. _`batadv_algo_dump_entry`:

batadv_algo_dump_entry
======================

.. c:function:: int batadv_algo_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_algo_ops *bat_algo_ops)

    fill in information about one supported routing algorithm

    :param struct sk_buff \*msg:
        netlink message to be sent back

    :param u32 portid:
        Port to reply to

    :param u32 seq:
        Sequence number of message

    :param struct batadv_algo_ops \*bat_algo_ops:
        Algorithm to be dumped

.. _`batadv_algo_dump_entry.return`:

Return
------

Error number, or 0 on success

.. _`batadv_algo_dump`:

batadv_algo_dump
================

.. c:function:: int batadv_algo_dump(struct sk_buff *msg, struct netlink_callback *cb)

    fill in information about supported routing algorithms

    :param struct sk_buff \*msg:
        netlink message to be sent back

    :param struct netlink_callback \*cb:
        Parameters to the netlink request

.. _`batadv_algo_dump.return`:

Return
------

Length of reply message.

.. This file was automatic generated / don't edit.

