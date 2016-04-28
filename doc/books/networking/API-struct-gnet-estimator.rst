.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-gnet-estimator:

=====================
struct gnet_estimator
=====================

*man struct gnet_estimator(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
