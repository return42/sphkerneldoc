
.. _API-struct-gnet-stats-rate-est64:

============================
struct gnet_stats_rate_est64
============================

*man struct gnet_stats_rate_est64(9)*

*4.6.0-rc1*

rate estimator


Synopsis
========

.. code-block:: c

    struct gnet_stats_rate_est64 {
      __u64 bps;
      __u64 pps;
    };


Members
=======

bps
    current byte rate

pps
    current packet rate
