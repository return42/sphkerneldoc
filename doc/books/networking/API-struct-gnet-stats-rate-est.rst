
.. _API-struct-gnet-stats-rate-est:

==========================
struct gnet_stats_rate_est
==========================

*man struct gnet_stats_rate_est(9)*

*4.6.0-rc1*

rate estimator


Synopsis
========

.. code-block:: c

    struct gnet_stats_rate_est {
      __u32 bps;
      __u32 pps;
    };


Members
=======

bps
    current byte rate

pps
    current packet rate
