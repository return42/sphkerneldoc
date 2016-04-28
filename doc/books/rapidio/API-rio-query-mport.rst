.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-query-mport:

===============
rio_query_mport
===============

*man rio_query_mport(9)*

*4.6.0-rc5*

Query mport device attributes


Synopsis
========

.. c:function:: int rio_query_mport( struct rio_mport * port, struct rio_mport_attr * mport_attr )

Arguments
=========

``port``
    mport device to query

``mport_attr``
    mport attributes data structure


Description
===========

Returns attributes of specified mport through the pointer to attributes
data structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
