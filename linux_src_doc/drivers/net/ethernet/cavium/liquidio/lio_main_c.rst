.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/lio_main.c

.. _`lio_sync_octeon_time_cb`:

lio_sync_octeon_time_cb
=======================

.. c:function:: void lio_sync_octeon_time_cb(struct octeon_device *oct, u32 status, void *buf)

    callback that is invoked when soft command sent by \ :c:func:`lio_sync_octeon_time`\  has completed successfully or failed

    :param struct octeon_device \*oct:
        *undescribed*

    :param u32 status:
        *undescribed*

    :param void \*buf:
        *undescribed*

.. _`lio_sync_octeon_time_cb.description`:

Description
-----------

\ ``oct``\  - octeon device structure
\ ``status``\  - indicates success or failure
\ ``buf``\  - pointer to the command that was sent to firmware

.. _`lio_sync_octeon_time`:

lio_sync_octeon_time
====================

.. c:function:: void lio_sync_octeon_time(struct work_struct *work)

    send latest localtime to octeon firmware so that firmware will correct it's time, in case there is a time skew

    :param struct work_struct \*work:
        work scheduled to send time update to octeon firmware

.. _`setup_sync_octeon_time_wq`:

setup_sync_octeon_time_wq
=========================

.. c:function:: int setup_sync_octeon_time_wq(struct net_device *netdev)

    Sets up the work to periodically update local time to octeon firmware

    :param struct net_device \*netdev:
        *undescribed*

.. _`setup_sync_octeon_time_wq.description`:

Description
-----------

\ ``netdev``\  - network device which should send time update to firmware

.. _`cleanup_sync_octeon_time_wq`:

cleanup_sync_octeon_time_wq
===========================

.. c:function:: void cleanup_sync_octeon_time_wq(struct net_device *netdev)

    stop scheduling and destroy the work created to periodically update local time to octeon firmware

    :param struct net_device \*netdev:
        *undescribed*

.. _`cleanup_sync_octeon_time_wq.description`:

Description
-----------

\ ``netdev``\  - network device which should send time update to firmware

.. This file was automatic generated / don't edit.

