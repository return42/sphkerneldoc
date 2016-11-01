.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lprocfs_status.h

.. _`lprocfs_stats_lock`:

lprocfs_stats_lock
==================

.. c:function:: int lprocfs_stats_lock(struct lprocfs_stats *stats, enum lprocfs_stats_lock_ops opc, unsigned long *flags)

    :param struct lprocfs_stats \*stats:
        *undescribed*

    :param enum lprocfs_stats_lock_ops opc:
        *undescribed*

    :param unsigned long \*flags:
        *undescribed*

.. _`lprocfs_stats_lock.description`:

Description
-----------

The statistics struct may be allocated with per-CPU structures for
efficient concurrent update (usually only on server-wide stats), or
as a single global struct (e.g. for per-client or per-job statistics),
so the required locking depends on the type of structure allocated.

For per-CPU statistics, pin the thread to the current cpuid so that
will only access the statistics for that CPU.  If the stats structure
for the current CPU has not been allocated (or previously freed),
allocate it now.  The per-CPU statistics do not need locking since
the thread is pinned to the CPU during update.

For global statistics, lock the stats structure to prevent concurrent update.

\param[in] stats     statistics structure to lock
\param[in] opc       type of operation:
LPROCFS_GET_SMP_ID: "lock" and return current CPU index
for incrementing statistics for that CPU
LPROCFS_GET_NUM_CPU: "lock" and return number of used
CPU indices to iterate over all indices
\param[out] flags    CPU interrupt saved state for IRQ-safe locking

\retval cpuid of current thread or number of allocated structs
\retval negative on error (only for opc LPROCFS_GET_SMP_ID + per-CPU stats)

.. _`lprocfs_stats_unlock`:

lprocfs_stats_unlock
====================

.. c:function:: void lprocfs_stats_unlock(struct lprocfs_stats *stats, enum lprocfs_stats_lock_ops opc, unsigned long *flags)

    :param struct lprocfs_stats \*stats:
        *undescribed*

    :param enum lprocfs_stats_lock_ops opc:
        *undescribed*

    :param unsigned long \*flags:
        *undescribed*

.. _`lprocfs_stats_unlock.description`:

Description
-----------

Unlock the lock acquired via \ :c:func:`lprocfs_stats_lock`\  for global statistics,
or unpin this thread from the current cpuid for per-CPU statistics.

This function must be called using the same arguments as used when calling
\ :c:func:`lprocfs_stats_lock`\  so that the correct operation can be performed.

\param[in] stats     statistics structure to unlock
\param[in] opc       type of operation (current cpuid or number of structs)
\param[in] flags     CPU interrupt saved state for IRQ-safe locking

.. This file was automatic generated / don't edit.

