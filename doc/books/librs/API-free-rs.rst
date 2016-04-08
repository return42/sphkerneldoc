
.. _API-free-rs:

=======
free_rs
=======

*man free_rs(9)*

*4.6.0-rc1*

Free the rs control structure, if it is no longer used


Synopsis
========

.. c:function:: void free_rs( struct rs_control * rs )

Arguments
=========

``rs``
    the control structure which is not longer used by the caller
