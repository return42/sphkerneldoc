.. -*- coding: utf-8; mode: rst -*-

.. _API-input-ff-create-memless:

=======================
input_ff_create_memless
=======================

*man input_ff_create_memless(9)*

*4.6.0-rc5*

create memoryless force-feedback device


Synopsis
========

.. c:function:: int input_ff_create_memless( struct input_dev * dev, void * data, int (*play_effect) struct input_dev *, void *, struct ff_effect * )

Arguments
=========

``dev``
    input device supporting force-feedback

``data``
    driver-specific data to be passed into ``play_effect``

``play_effect``
    driver-specific method for playing FF effect


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
