.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-sta-notify-cmd:

===================
enum sta_notify_cmd
===================

*man enum sta_notify_cmd(9)*

*4.6.0-rc5*

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

Used with the ``sta_notify`` callback in ``struct ieee80211_ops``, this
indicates if an associated station made a power state transition.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
