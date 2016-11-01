.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/dir.c

.. _`ll_dirent_type_get`:

ll_dirent_type_get
==================

.. c:function:: __u16 ll_dirent_type_get(struct lu_dirent *ent)

    IF\_\* flag shld be converted to particular OS file type in platform llite module.

    :param struct lu_dirent \*ent:
        *undescribed*

.. _`ll_dir_setdirstripe`:

ll_dir_setdirstripe
===================

.. c:function:: int ll_dir_setdirstripe(struct inode *parent, struct lmv_user_md *lump, const char *dirname, umode_t mode)

    :param struct inode \*parent:
        *undescribed*

    :param struct lmv_user_md \*lump:
        *undescribed*

    :param const char \*dirname:
        *undescribed*

    :param umode_t mode:
        *undescribed*

.. _`ll_dir_setdirstripe.description`:

Description
-----------

param[in] parent     the parent of the directory.
param[in] lump       the specified stripes.
param[in] dirname    the name of the directory.
param[in] mode       the specified mode of the directory.

retval               =0 if striped directory is being created successfully.
<0 if the creation is failed.

.. _`ll_dir_getstripe`:

ll_dir_getstripe
================

.. c:function:: int ll_dir_getstripe(struct inode *inode, void **plmm, int *plmm_size, struct ptlrpc_request **request, u64 valid)

    @valid will be used to indicate which stripe it will retrieve OBD_MD_MEA              LMV stripe EA OBD_MD_DEFAULT_MEA      Default LMV stripe EA otherwise               Default LOV EA. Each time, it can only retrieve 1 stripe EA

    :param struct inode \*inode:
        *undescribed*

    :param void \*\*plmm:
        *undescribed*

    :param int \*plmm_size:
        *undescribed*

    :param struct ptlrpc_request \*\*request:
        *undescribed*

    :param u64 valid:
        *undescribed*

.. _`ll_ioc_copy_start`:

ll_ioc_copy_start
=================

.. c:function:: int ll_ioc_copy_start(struct super_block *sb, struct hsm_copy *copy)

    copy work.

    :param struct super_block \*sb:
        *undescribed*

    :param struct hsm_copy \*copy:
        *undescribed*

.. _`ll_ioc_copy_start.description`:

Description
-----------

It sends a first hsm_progress (with extent length == 0) to coordinator as a
first information for it that real work has started.

Moreover, for a ARCHIVE request, it will sample the file data version and
store it in \a copy.

\return 0 on success.

.. _`ll_ioc_copy_end`:

ll_ioc_copy_end
===============

.. c:function:: int ll_ioc_copy_end(struct super_block *sb, struct hsm_copy *copy)

    copy work.

    :param struct super_block \*sb:
        *undescribed*

    :param struct hsm_copy \*copy:
        *undescribed*

.. _`ll_ioc_copy_end.description`:

Description
-----------

It will send the last hsm_progress update to coordinator to inform it
that copy is finished and whether it was successful or not.

Moreover,
- for ARCHIVE request, it will sample the file data version and compare it
with the version saved in \ :c:func:`ll_ioc_copy_start`\ . If they do not match, copy
will be considered as failed.
- for RESTORE request, it will sample the file data version and send it to
coordinator which is useful if the file was imported as 'released'.

\return 0 on success.

.. This file was automatic generated / don't edit.

