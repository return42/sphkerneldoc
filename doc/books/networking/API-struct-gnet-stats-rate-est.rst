.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-gnet-stats-rate-est:

==========================
struct gnet_stats_rate_est
==========================

*man struct gnet_stats_rate_est(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
