
.. _API-drm-atomic-async-commit:

=======================
drm_atomic_async_commit
=======================

*man drm_atomic_async_commit(9)*

*4.6.0-rc1*

atomic\ ``async`` configuration commit


Synopsis
========

.. c:function:: int drm_atomic_async_commit( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic configuration to check


Description
===========

Note that this function can return -EDEADLK if the driver needed to acquire more locks but encountered a deadlock. The caller must then do the usual w/w backoff dance and restart.
All other errors are fatal.

Also note that on successful execution ownership of ``state`` is transferred from the caller of this function to the function itself. The caller must not free or in any other way
access ``state``. If the function fails then the caller must clean up ``state`` itself.


Returns
=======

0 on success, negative error code on failure.
