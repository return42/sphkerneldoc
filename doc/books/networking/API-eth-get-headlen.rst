
.. _API-eth-get-headlen:

===============
eth_get_headlen
===============

*man eth_get_headlen(9)*

*4.6.0-rc1*

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

Make a best effort attempt to pull the length for all of the headers for a given frame in a linear buffer.
