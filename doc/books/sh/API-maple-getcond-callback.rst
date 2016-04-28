.. -*- coding: utf-8; mode: rst -*-

.. _API-maple-getcond-callback:

======================
maple_getcond_callback
======================

*man maple_getcond_callback(9)*

*4.6.0-rc5*

setup handling MAPLE_COMMAND_GETCOND


Synopsis
========

.. c:function:: void maple_getcond_callback( struct maple_device * dev, void (*callback) struct mapleq *mq, unsigned long interval, unsigned long function )

Arguments
=========

``dev``
    device responding

``callback``
    handler callback

``interval``
    interval in jiffies between callbacks

``function``
    the function code for the device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
