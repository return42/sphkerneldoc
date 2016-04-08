
.. _API-struct-gnet-estimator:

=====================
struct gnet_estimator
=====================

*man struct gnet_estimator(9)*

*4.6.0-rc1*

rate estimator configuration


Synopsis
========

.. code-block:: c

    struct gnet_estimator {
      signed char interval;
      unsigned char ewma_log;
    };


Members
=======

interval
    sampling period

ewma_log
    the log of measurement window weight
