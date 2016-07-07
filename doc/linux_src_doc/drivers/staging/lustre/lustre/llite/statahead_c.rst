.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/statahead.c

.. _`sa_args_init`:

sa_args_init
============

.. c:function:: int sa_args_init(struct inode *dir, struct inode *child, struct ll_sa_entry *entry, struct md_enqueue_info **pmi, struct ldlm_enqueue_info **pei)

    :param struct inode \*dir:
        *undescribed*

    :param struct inode \*child:
        *undescribed*

    :param struct ll_sa_entry \*entry:
        *undescribed*

    :param struct md_enqueue_info \*\*pmi:
        *undescribed*

    :param struct ldlm_enqueue_info \*\*pei:
        *undescribed*

.. _`do_sa_revalidate`:

do_sa_revalidate
================

.. c:function:: int do_sa_revalidate(struct inode *dir, struct ll_sa_entry *entry, struct dentry *dentry)

    \retval      1 -- dentry valid \retval      0 -- will send stat-ahead request \retval others -- prepare stat-ahead request failed

    :param struct inode \*dir:
        *undescribed*

    :param struct ll_sa_entry \*entry:
        *undescribed*

    :param struct dentry \*dentry:
        *undescribed*

.. _`ll_stop_statahead`:

ll_stop_statahead
=================

.. c:function:: void ll_stop_statahead(struct inode *dir, void *key)

    :param struct inode \*dir:
        *undescribed*

    :param void \*key:
        *undescribed*

.. _`do_statahead_enter`:

do_statahead_enter
==================

.. c:function:: int do_statahead_enter(struct inode *dir, struct dentry **dentryp, int only_unplug)

    Otherwise if a thread is started already, wait it until it is ahead of me. \retval 1       -- find entry with lock in cache, the caller needs to do nothing. \retval 0       -- find entry in cache, but without lock, the caller needs refresh from MDS. \retval others  -- the caller need to process as non-statahead.

    :param struct inode \*dir:
        *undescribed*

    :param struct dentry \*\*dentryp:
        *undescribed*

    :param int only_unplug:
        *undescribed*

.. This file was automatic generated / don't edit.

