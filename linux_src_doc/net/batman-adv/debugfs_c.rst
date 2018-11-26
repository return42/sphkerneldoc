.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/debugfs.c

.. _`batadv_debugfs_deprecated`:

batadv_debugfs_deprecated
=========================

.. c:function:: void batadv_debugfs_deprecated(struct file *file, const char *alt)

    Log use of deprecated batadv debugfs access

    :param file:
        file which was accessed
    :type file: struct file \*

    :param alt:
        explanation what can be used as alternative
    :type alt: const char \*

.. _`batadv_originators_hardif_open`:

batadv_originators_hardif_open
==============================

.. c:function:: int batadv_originators_hardif_open(struct inode *inode, struct file *file)

    handles debugfs output for the originator table of an hard interface

    :param inode:
        inode pointer to debugfs file
    :type inode: struct inode \*

    :param file:
        pointer to the seq_file
    :type file: struct file \*

.. _`batadv_originators_hardif_open.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_dat_cache_open`:

batadv_dat_cache_open
=====================

.. c:function:: int batadv_dat_cache_open(struct inode *inode, struct file *file)

    Prepare file handler for reads from dat_cache

    :param inode:
        inode which was opened
    :type inode: struct inode \*

    :param file:
        file handle to be initialized
    :type file: struct file \*

.. _`batadv_dat_cache_open.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_mcast_flags_open`:

batadv_mcast_flags_open
=======================

.. c:function:: int batadv_mcast_flags_open(struct inode *inode, struct file *file)

    prepare file handler for reads from mcast_flags

    :param inode:
        inode which was opened
    :type inode: struct inode \*

    :param file:
        file handle to be initialized
    :type file: struct file \*

.. _`batadv_mcast_flags_open.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debugfs_init`:

batadv_debugfs_init
===================

.. c:function:: void batadv_debugfs_init( void)

    Initialize soft interface independent debugfs entries

    :param void:
        no arguments
    :type void: 

.. _`batadv_debugfs_destroy`:

batadv_debugfs_destroy
======================

.. c:function:: void batadv_debugfs_destroy( void)

    Remove all debugfs entries

    :param void:
        no arguments
    :type void: 

.. _`batadv_debugfs_add_hardif`:

batadv_debugfs_add_hardif
=========================

.. c:function:: int batadv_debugfs_add_hardif(struct batadv_hard_iface *hard_iface)

    creates the base directory for a hard interface in debugfs.

    :param hard_iface:
        hard interface which should be added.
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_debugfs_add_hardif.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debugfs_rename_hardif`:

batadv_debugfs_rename_hardif
============================

.. c:function:: void batadv_debugfs_rename_hardif(struct batadv_hard_iface *hard_iface)

    Fix debugfs path for renamed hardif

    :param hard_iface:
        hard interface which was renamed
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_debugfs_del_hardif`:

batadv_debugfs_del_hardif
=========================

.. c:function:: void batadv_debugfs_del_hardif(struct batadv_hard_iface *hard_iface)

    delete the base directory for a hard interface in debugfs.

    :param hard_iface:
        hard interface which is deleted.
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_debugfs_add_meshif`:

batadv_debugfs_add_meshif
=========================

.. c:function:: int batadv_debugfs_add_meshif(struct net_device *dev)

    Initialize interface dependent debugfs entries

    :param dev:
        netdev struct of the soft interface
    :type dev: struct net_device \*

.. _`batadv_debugfs_add_meshif.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debugfs_rename_meshif`:

batadv_debugfs_rename_meshif
============================

.. c:function:: void batadv_debugfs_rename_meshif(struct net_device *dev)

    Fix debugfs path for renamed softif

    :param dev:
        net_device which was renamed
    :type dev: struct net_device \*

.. _`batadv_debugfs_del_meshif`:

batadv_debugfs_del_meshif
=========================

.. c:function:: void batadv_debugfs_del_meshif(struct net_device *dev)

    Remove interface dependent debugfs entries

    :param dev:
        netdev struct of the soft interface
    :type dev: struct net_device \*

.. This file was automatic generated / don't edit.

