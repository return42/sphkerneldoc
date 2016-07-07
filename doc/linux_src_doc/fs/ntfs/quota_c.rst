.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/quota.c

.. _`ntfs_mark_quotas_out_of_date`:

ntfs_mark_quotas_out_of_date
============================

.. c:function:: bool ntfs_mark_quotas_out_of_date(ntfs_volume *vol)

    mark the quotas out of date on an ntfs volume

    :param ntfs_volume \*vol:
        ntfs volume on which to mark the quotas out of date

.. _`ntfs_mark_quotas_out_of_date.description`:

Description
-----------

Mark the quotas out of date on the ntfs volume \ ``vol``\  and return 'true' on
success and 'false' on error.

.. This file was automatic generated / don't edit.

