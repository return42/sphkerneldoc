.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-set-key-cmd:

================
enum set_key_cmd
================

*man enum set_key_cmd(9)*

*4.6.0-rc5*

key command


Synopsis
========

.. code-block:: c

    enum set_key_cmd {
      SET_KEY,
      DISABLE_KEY
    };


Constants
=========

SET_KEY
    a key is set

DISABLE_KEY
    a key must be disabled


Description
===========

Used with the ``set_key`` callback in ``struct ieee80211_ops``, this
indicates whether a key is being removed or added.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
