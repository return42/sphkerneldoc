
.. _API-enum-rc-filter-type:

===================
enum rc_filter_type
===================

*man enum rc_filter_type(9)*

*4.6.0-rc1*

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
