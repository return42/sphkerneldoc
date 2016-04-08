
.. _API-rio-destid-next:

===============
rio_destid_next
===============

*man rio_destid_next(9)*

*4.6.0-rc1*

return next destID in use


Synopsis
========

.. c:function:: u16 rio_destid_next( struct rio_net * net, u16 from )

Arguments
=========

``net``
    RIO network

``from``
    destination ID from which search shall continue
