.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/debugfs.c

.. _`batadv_originators_hardif_open`:

batadv_originators_hardif_open
==============================

.. c:function:: int batadv_originators_hardif_open(struct inode *inode, struct file *file)

    handles debugfs output for the originator table of an hard interface

    :param struct inode \*inode:
        inode pointer to debugfs file

    :param struct file \*file:
        pointer to the seq_file

.. _`batadv_originators_hardif_open.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_dat_cache_open`:

batadv_dat_cache_open
=====================

.. c:function:: int batadv_dat_cache_open(struct inode *inode, struct file *file)

    Prepare file handler for reads from dat_chache

    :param struct inode \*inode:
        inode which was opened

    :param struct file \*file:
        file handle to be initialized

.. _`batadv_dat_cache_open.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_mcast_flags_open`:

batadv_mcast_flags_open
=======================

.. c:function:: int batadv_mcast_flags_open(struct inode *inode, struct file *file)

    prepare file handler for reads from mcast_flags

    :param struct inode \*inode:
        inode which was opened

    :param struct file \*file:
        file handle to be initialized

.. _`batadv_mcast_flags_open.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debugfs_init`:

batadv_debugfs_init
===================

.. c:function:: void batadv_debugfs_init( void)

    Initialize soft interface independent debugfs entries

    :param  void:
        no arguments

.. _`batadv_debugfs_destroy`:

batadv_debugfs_destroy
======================

.. c:function:: void batadv_debugfs_destroy( void)

    Remove all debugfs entries

    :param  void:
        no arguments

.. _`batadv_debugfs_add_hardif`:

batadv_debugfs_add_hardif
=========================

.. c:function:: int batadv_debugfs_add_hardif(struct batadv_hard_iface *hard_iface)

    creates the base directory for a hard interface in debugfs.

    :param struct batadv_hard_iface \*hard_iface:
        hard interface which should be added.

.. _`batadv_debugfs_add_hardif.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debugfs_rename_hardif`:

batadv_debugfs_rename_hardif
============================

.. c:function:: void batadv_debugfs_rename_hardif(struct batadv_hard_iface *hard_iface)

    Fix debugfs path for renamed hardif

    :param struct batadv_hard_iface \*hard_iface:
        hard interface which was renamed

.. _`batadv_debugfs_del_hardif`:

batadv_debugfs_del_hardif
=========================

.. c:function:: void batadv_debugfs_del_hardif(struct batadv_hard_iface *hard_iface)

    delete the base directory for a hard interface in debugfs.

    :param struct batadv_hard_iface \*hard_iface:
        hard interface which is deleted.

.. _`batadv_debugfs_add_meshif`:

batadv_debugfs_add_meshif
=========================

.. c:function:: int batadv_debugfs_add_meshif(struct net_device *dev)

    Initialize interface dependent debugfs entries

    :param struct net_device \*dev:
        netdev struct of the soft interface

.. _`batadv_debugfs_add_meshif.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debugfs_rename_meshif`:

batadv_debugfs_rename_meshif
============================

.. c:function:: void batadv_debugfs_rename_meshif(struct net_device *dev)

    Fix debugfs path for renamed softif

    :param struct net_device \*dev:
        net_device which was renamed

.. _`batadv_debugfs_del_meshif`:

batadv_debugfs_del_meshif
=========================

.. c:function:: void batadv_debugfs_del_meshif(struct net_device *dev)

    Remove interface dependent debugfs entries

    :param struct net_device \*dev:
        netdev struct of the soft interface

.. This file was automatic generated / don't edit.

