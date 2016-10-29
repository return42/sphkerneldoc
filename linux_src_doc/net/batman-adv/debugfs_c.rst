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

.. _`batadv_debugfs_del_hardif`:

batadv_debugfs_del_hardif
=========================

.. c:function:: void batadv_debugfs_del_hardif(struct batadv_hard_iface *hard_iface)

    delete the base directory for a hard interface in debugfs.

    :param struct batadv_hard_iface \*hard_iface:
        hard interface which is deleted.

.. This file was automatic generated / don't edit.
