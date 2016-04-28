.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-rc-filter-type:

===================
enum rc_filter_type
===================

*man enum rc_filter_type(9)*

*4.6.0-rc5*

Filter type constants.


Synopsis
========

.. code-block:: c

    enum rc_filter_type {
      RC_FILTER_NORMAL,
      RC_FILTER_WAKEUP,
      RC_FILTER_MAX
    };


Constants
=========

RC_FILTER_NORMAL
    Filter for normal operation.

RC_FILTER_WAKEUP
    Filter for waking from suspend.

RC_FILTER_MAX
    Number of filter types.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
