
.. _API-reinit-completion:

=================
reinit_completion
=================

*man reinit_completion(9)*

*4.6.0-rc1*

reinitialize a completion structure


Synopsis
========

.. c:function:: void reinit_completion( struct completion * x )

Arguments
=========

``x``
    pointer to completion structure that is to be reinitialized


Description
===========

This inline function should be used to reinitialize a completion structure so it can be reused. This is especially important after ``complete_all`` is used.
