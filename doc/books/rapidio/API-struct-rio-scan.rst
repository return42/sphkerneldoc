
.. _API-struct-rio-scan:

===============
struct rio_scan
===============

*man struct rio_scan(9)*

*4.6.0-rc1*

RIO enumeration and discovery operations


Synopsis
========

.. code-block:: c

    struct rio_scan {
      struct module * owner;
      int (* enumerate) (struct rio_mport *mport, u32 flags);
      int (* discover) (struct rio_mport *mport, u32 flags);
    };


Members
=======

owner
    The module owner of this structure

enumerate
    Callback to perform RapidIO fabric enumeration.

discover
    Callback to perform RapidIO fabric discovery.
