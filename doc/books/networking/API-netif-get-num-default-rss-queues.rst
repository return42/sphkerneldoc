
.. _API-netif-get-num-default-rss-queues:

================================
netif_get_num_default_rss_queues
================================

*man netif_get_num_default_rss_queues(9)*

*4.6.0-rc1*

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

This routine should set an upper limit on the number of RSS queues used by default by multiqueue devices.
