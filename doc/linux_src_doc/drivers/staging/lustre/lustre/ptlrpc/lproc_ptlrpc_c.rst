.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/lproc_ptlrpc.c

.. _`nrs_state2str`:

nrs_state2str
=============

.. c:function:: const char *nrs_state2str(enum ptlrpc_nrs_pol_state state)

    readable strings.

    :param enum ptlrpc_nrs_pol_state state:
        *undescribed*

.. _`nrs_state2str.description`:

Description
-----------

\param[in] state The policy state

.. _`nrs_policy_get_info_locked`:

nrs_policy_get_info_locked
==========================

.. c:function:: void nrs_policy_get_info_locked(struct ptlrpc_nrs_policy *policy, struct ptlrpc_nrs_pol_info *info)

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param struct ptlrpc_nrs_pol_info \*info:
        *undescribed*

.. _`nrs_policy_get_info_locked.description`:

Description
-----------

Information is copied in \a info.

\param[in] policy The policy
\param[out] info  Holds returned status information

.. _`ptlrpc_lprocfs_nrs_seq_show`:

ptlrpc_lprocfs_nrs_seq_show
===========================

.. c:function:: int ptlrpc_lprocfs_nrs_seq_show(struct seq_file *m, void *n)

    service.

    :param struct seq_file \*m:
        *undescribed*

    :param void \*n:
        *undescribed*

.. _`lprocfs_nrs_wr_max_cmd`:

LPROCFS_NRS_WR_MAX_CMD
======================

.. c:function::  LPROCFS_NRS_WR_MAX_CMD()

    length of the " reg" substring

.. _`ptlrpc_lprocfs_nrs_seq_write`:

ptlrpc_lprocfs_nrs_seq_write
============================

.. c:function:: ssize_t ptlrpc_lprocfs_nrs_seq_write(struct file *file, const char __user *buffer, size_t count, loff_t *off)

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*off:
        *undescribed*

.. _`ptlrpc_lprocfs_nrs_seq_write.description`:

Description
-----------

Commands consist of the policy name, followed by an optional [reg\|hp] token;
if the optional token is omitted, the operation is performed on both the
regular and high-priority (if the service has one) NRS head.

.. This file was automatic generated / don't edit.

