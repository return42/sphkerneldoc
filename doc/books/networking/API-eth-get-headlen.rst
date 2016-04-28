.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-get-headlen:

===============
eth_get_headlen
===============

*man eth_get_headlen(9)*

*4.6.0-rc5*

determine the length of header for an ethernet frame


Synopsis
========

.. c:function:: u32 eth_get_headlen( void * data, unsigned int len )

Arguments
=========

``data``
    pointer to start of frame

``len``
    total length of frame


Description
===========

Make a best effort attempt to pull the length for all of the headers for
a given frame in a linear buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
