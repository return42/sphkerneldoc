
.. _API-drm-prime-gem-destroy:

=====================
drm_prime_gem_destroy
=====================

*man drm_prime_gem_destroy(9)*

*4.6.0-rc1*

helper to clean up a PRIME-imported GEM object


Synopsis
========

.. c:function:: void drm_prime_gem_destroy( struct drm_gem_object * obj, struct sg_table * sg )

Arguments
=========

``obj``
    GEM object which was created from a dma-buf

``sg``
    the sg-table which was pinned at import time


Description
===========

This is the cleanup functions which GEM drivers need to call when they use ``drm_gem_prime_import`` to import dma-bufs.
