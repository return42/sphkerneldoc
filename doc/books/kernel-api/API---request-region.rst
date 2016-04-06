
.. _API---request-region:

================
__request_region
================

*man __request_region(9)*

*4.6.0-rc1*

create a new busy resource region


Synopsis
========

.. c:function:: struct resource ⋆ __request_region( struct resource * parent, resource_size_t start, resource_size_t n, const char * name, int flags )

Arguments
=========

``parent``
    parent resource descriptor

``start``
    resource start address

``n``
    resource region size

``name``
    reserving caller's ID string

``flags``
    IO resource flags
