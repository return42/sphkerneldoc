.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/dir.c

.. _`ll_dirent_type_get`:

ll_dirent_type_get
==================

.. c:function:: __u16 ll_dirent_type_get(struct lu_dirent *ent)

    IF\_\* flag shld be converted to particular OS file type in platform llite module.

    :param struct lu_dirent \*ent:
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

