
.. _API-subsys-dev-iter-exit:

====================
subsys_dev_iter_exit
====================

*man subsys_dev_iter_exit(9)*

*4.6.0-rc1*

finish iteration


Synopsis
========

.. c:function:: void subsys_dev_iter_exit( struct subsys_dev_iter * iter )

Arguments
=========

``iter``
    subsys iterator to finish


Description
===========

Finish an iteration. Always call this function after iteration is complete whether the iteration ran till the end or not.
