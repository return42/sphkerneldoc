.. -*- coding: utf-8; mode: rst -*-

.. _API-class-dev-iter-exit:

===================
class_dev_iter_exit
===================

*man class_dev_iter_exit(9)*

*4.6.0-rc5*

finish iteration


Synopsis
========

.. c:function:: void class_dev_iter_exit( struct class_dev_iter * iter )

Arguments
=========

``iter``
    class iterator to finish


Description
===========

Finish an iteration. Always call this function after iteration is
complete whether the iteration ran till the end or not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
