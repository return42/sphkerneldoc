
.. _API-maple-getcond-callback:

======================
maple_getcond_callback
======================

*man maple_getcond_callback(9)*

*4.6.0-rc1*

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
