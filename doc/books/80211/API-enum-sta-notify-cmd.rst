
.. _API-enum-sta-notify-cmd:

===================
enum sta_notify_cmd
===================

*man enum sta_notify_cmd(9)*

*4.6.0-rc1*

sta notify command


Synopsis
========

.. code-block:: c

    enum sta_notify_cmd {
      STA_NOTIFY_SLEEP,
      STA_NOTIFY_AWAKE
    };


Constants
=========

STA_NOTIFY_SLEEP
    a station is now sleeping

STA_NOTIFY_AWAKE
    a sleeping station woke up


Description
===========

Used with the ``sta_notify`` callback in ``struct ieee80211_ops``, this indicates if an associated station made a power state transition.
