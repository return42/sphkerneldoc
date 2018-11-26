.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/lio_main.c

.. _`lio_sync_octeon_time`:

lio_sync_octeon_time
====================

.. c:function:: void lio_sync_octeon_time(struct work_struct *work)

    send latest localtime to octeon firmware so that firmware will correct it's time, in case there is a time skew

    :param work:
        work scheduled to send time update to octeon firmware
    :type work: struct work_struct \*

.. _`setup_sync_octeon_time_wq`:

setup_sync_octeon_time_wq
=========================

.. c:function:: int setup_sync_octeon_time_wq(struct net_device *netdev)

    Sets up the work to periodically update local time to octeon firmware

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`setup_sync_octeon_time_wq.description`:

Description
-----------

\ ``netdev``\  - network device which should send time update to firmware

.. _`cleanup_sync_octeon_time_wq`:

cleanup_sync_octeon_time_wq
===========================

.. c:function:: void cleanup_sync_octeon_time_wq(struct net_device *netdev)

    stop scheduling and destroy the work created to periodically update local time to octeon firmware

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`cleanup_sync_octeon_time_wq.description`:

Description
-----------

\ ``netdev``\  - network device which should send time update to firmware

.. This file was automatic generated / don't edit.

