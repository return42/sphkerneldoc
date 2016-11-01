.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/statahead.c

.. _`sa_prep_data`:

sa_prep_data
============

.. c:function:: int sa_prep_data(struct inode *dir, struct inode *child, struct sa_entry *entry, struct md_enqueue_info **pmi, struct ldlm_enqueue_info **pei)

    :param struct inode \*dir:
        *undescribed*

    :param struct inode \*child:
        *undescribed*

    :param struct sa_entry \*entry:
        *undescribed*

    :param struct md_enqueue_info \*\*pmi:
        *undescribed*

    :param struct ldlm_enqueue_info \*\*pei:
        *undescribed*

.. _`sa_revalidate`:

sa_revalidate
=============

.. c:function:: int sa_revalidate(struct inode *dir, struct sa_entry *entry, struct dentry *dentry)

    :param struct inode \*dir:
        *undescribed*

    :param struct sa_entry \*entry:
        *undescribed*

    :param struct dentry \*dentry:
        *undescribed*

.. _`sa_revalidate.description`:

Description
-----------

\retval      1 dentry valid, no RPC sent
\retval      0 dentry invalid, will send async stat RPC
\retval      negative number upon error

.. _`revalidate_statahead_dentry`:

revalidate_statahead_dentry
===========================

.. c:function:: int revalidate_statahead_dentry(struct inode *dir, struct ll_statahead_info *sai, struct dentry **dentryp, bool unplug)

    :param struct inode \*dir:
        *undescribed*

    :param struct ll_statahead_info \*sai:
        *undescribed*

    :param struct dentry \*\*dentryp:
        *undescribed*

    :param bool unplug:
        *undescribed*

.. _`revalidate_statahead_dentry.description`:

Description
-----------

\param[in]  dir      parent directory
\param[in]  sai      sai structure
\param[out] dentryp  pointer to dentry which will be revalidated
\param[in]  unplug   unplug statahead window only (normally for negative
dentry)
\retval              1 on success, dentry is saved in \ ``dentryp``\ 
\retval              0 if revalidation failed (no proper lock on client)
\retval              negative number upon error

.. _`start_statahead_thread`:

start_statahead_thread
======================

.. c:function:: int start_statahead_thread(struct inode *dir, struct dentry *dentry)

    :param struct inode \*dir:
        *undescribed*

    :param struct dentry \*dentry:
        *undescribed*

.. _`start_statahead_thread.description`:

Description
-----------

\param[in] dir       parent directory
\param[in] dentry    dentry that triggers statahead, normally the first
dirent under \ ``dir``\ 
\retval              -EAGAIN on success, because when this function is
called, it's already in lookup call, so client should
do it itself instead of waiting for statahead thread
to do it asynchronously.
\retval              negative number upon error

.. _`ll_statahead`:

ll_statahead
============

.. c:function:: int ll_statahead(struct inode *dir, struct dentry **dentryp, bool unplug)

    will start statahead thread if this is the first dir entry, else revalidate dentry from statahead cache.

    :param struct inode \*dir:
        *undescribed*

    :param struct dentry \*\*dentryp:
        *undescribed*

    :param bool unplug:
        *undescribed*

.. _`ll_statahead.description`:

Description
-----------

\param[in]  dir      parent directory
\param[out] dentryp  dentry to getattr
\param[in]  unplug   unplug statahead window only (normally for negative
dentry)
\retval              1 on success
\retval              0 revalidation from statahead cache failed, caller needs
to getattr from server directly
\retval              negative number on error, caller often ignores this and
then getattr from server

.. This file was automatic generated / don't edit.

