.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_v.c

.. _`batadv_v_iface_update_mac`:

batadv_v_iface_update_mac
=========================

.. c:function:: void batadv_v_iface_update_mac(struct batadv_hard_iface *hard_iface)

    react to hard-interface MAC address change

    :param struct batadv_hard_iface \*hard_iface:
        the modified interface

.. _`batadv_v_iface_update_mac.description`:

Description
-----------

If the modified interface is the primary one, update the originator
address in the ELP and OGM messages to reflect the new MAC address.

.. _`batadv_v_orig_print_neigh`:

batadv_v_orig_print_neigh
=========================

.. c:function:: void batadv_v_orig_print_neigh(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing, struct seq_file *seq)

    print neighbors for the originator table

    :param struct batadv_orig_node \*orig_node:
        the orig_node for which the neighbors are printed

    :param struct batadv_hard_iface \*if_outgoing:
        outgoing interface for these entries

    :param struct seq_file \*seq:
        debugfs table seq_file struct

.. _`batadv_v_orig_print_neigh.description`:

Description
-----------

Must be called while holding an rcu lock.

.. _`batadv_v_hardif_neigh_print`:

batadv_v_hardif_neigh_print
===========================

.. c:function:: void batadv_v_hardif_neigh_print(struct seq_file *seq, struct batadv_hardif_neigh_node *hardif_neigh)

    print a single ELP neighbour node

    :param struct seq_file \*seq:
        neighbour table seq_file struct

    :param struct batadv_hardif_neigh_node \*hardif_neigh:
        hardif neighbour information

.. _`batadv_v_neigh_print`:

batadv_v_neigh_print
====================

.. c:function:: void batadv_v_neigh_print(struct batadv_priv *bat_priv, struct seq_file *seq)

    print the single hop neighbour list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct seq_file \*seq:
        neighbour table seq_file struct

.. _`batadv_v_orig_print`:

batadv_v_orig_print
===================

.. c:function:: void batadv_v_orig_print(struct batadv_priv *bat_priv, struct seq_file *seq, struct batadv_hard_iface *if_outgoing)

    print the originator table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct seq_file \*seq:
        debugfs table seq_file struct

    :param struct batadv_hard_iface \*if_outgoing:
        the outgoing interface for which this should be printed

.. _`batadv_v_mesh_init`:

batadv_v_mesh_init
==================

.. c:function:: int batadv_v_mesh_init(struct batadv_priv *bat_priv)

    initialize the B.A.T.M.A.N. V private resources for a mesh

    :param struct batadv_priv \*bat_priv:
        the object representing the mesh interface to initialise

.. _`batadv_v_mesh_init.return`:

Return
------

0 on success or a negative error code otherwise

.. _`batadv_v_mesh_free`:

batadv_v_mesh_free
==================

.. c:function:: void batadv_v_mesh_free(struct batadv_priv *bat_priv)

    free the B.A.T.M.A.N. V private resources for a mesh

    :param struct batadv_priv \*bat_priv:
        the object representing the mesh interface to free

.. _`batadv_v_init`:

batadv_v_init
=============

.. c:function:: int batadv_v_init( void)

    B.A.T.M.A.N. V initialization function

    :param  void:
        no arguments

.. _`batadv_v_init.description`:

Description
-----------

Takes care of initializing all the subcomponents.
It is invoked upon module load only.

.. _`batadv_v_init.return`:

Return
------

0 on success or a negative error code otherwise

.. This file was automatic generated / don't edit.

