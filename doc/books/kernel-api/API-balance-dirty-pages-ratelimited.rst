
.. _API-balance-dirty-pages-ratelimited:

===============================
balance_dirty_pages_ratelimited
===============================

*man balance_dirty_pages_ratelimited(9)*

*4.6.0-rc1*

balance dirty memory state


Synopsis
========

.. c:function:: void balance_dirty_pages_ratelimited( struct address_space * mapping )

Arguments
=========

``mapping``
    address_space which was dirtied


Description
===========

Processes which are dirtying memory should call in here once for each page which was newly dirtied. The function will periodically check the system's dirty state and will initiate
writeback if needed.

On really big machines, get_writeback_state is expensive, so try to avoid calling it too often (ratelimiting). But once we're over the dirty memory limit we decrease the
ratelimiting by a lot, to prevent individual processes from overshooting the limit by (ratelimit_pages) each.
