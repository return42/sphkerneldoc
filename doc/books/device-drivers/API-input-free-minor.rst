
.. _API-input-free-minor:

================
input_free_minor
================

*man input_free_minor(9)*

*4.6.0-rc1*

release previously allocated minor


Synopsis
========

.. c:function:: void input_free_minor( unsigned int minor )

Arguments
=========

``minor``
    minor to be released


Description
===========

This function releases previously allocated input minor so that it can be reused later.
