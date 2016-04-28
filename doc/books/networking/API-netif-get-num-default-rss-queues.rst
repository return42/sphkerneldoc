.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-get-num-default-rss-queues:

================================
netif_get_num_default_rss_queues
================================

*man netif_get_num_default_rss_queues(9)*

*4.6.0-rc5*

default number of RSS queues


Synopsis
========

.. c:function:: int netif_get_num_default_rss_queues( void )

Arguments
=========

``void``
    no arguments


Description
===========

This routine should set an upper limit on the number of RSS queues used
by default by multiqueue devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
