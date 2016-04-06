
.. _API-reciprocal-scale:

================
reciprocal_scale
================

*man reciprocal_scale(9)*

*4.6.0-rc1*

"scale" a value into range [0, ep_ro)


Synopsis
========

.. c:function:: u32 reciprocal_scale( u32 val, u32 ep_ro )

Arguments
=========

``val``
    value

``ep_ro``
    right open interval endpoint


Description
===========

Perform a “reciprocal multiplication” in order to “scale” a value into range [0, ep_ro), where the upper interval endpoint is right-open. This is useful, e.g. for accessing a
index of an array containing ep_ro elements, for example. Think of it as sort of modulus, only that the result isn't that of modulo. ;) Note that if initial input is a small
value, then result will return 0.


Return
======

a result based on val in interval [0, ep_ro).
