
.. _API-rio-find-mport:

==============
rio_find_mport
==============

*man rio_find_mport(9)*

*4.6.0-rc1*

find RIO mport by its ID


Synopsis
========

.. c:function:: struct rio_mport ⋆ rio_find_mport( int mport_id )

Arguments
=========

``mport_id``
    number (ID) of mport device


Description
===========

Given a RIO mport number, the desired mport is located in the global list of mports. If the mport is found, a pointer to its data structure is returned. If no mport is found,
``NULL`` is returned.
