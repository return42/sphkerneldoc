
.. _workqueue:

======================
The mac80211 workqueue
======================

mac80211 provides its own workqueue for drivers and internal mac80211 use. The workqueue is a single threaded workqueue and can only be accessed by helpers for sanity checking.
Drivers must ensure all work added onto the mac80211 workqueue should be cancelled on the driver ``stop`` callback.

mac80211 will flushed the workqueue upon interface removal and during suspend.

All work performed on the mac80211 workqueue must not acquire the RTNL lock.


.. toctree::
    :maxdepth: 1

    API-ieee80211-queue-work
    API-ieee80211-queue-delayed-work
