.. -*- coding: utf-8; mode: rst -*-

.. _API-input-ff-erase:

==============
input_ff_erase
==============

*man input_ff_erase(9)*

*4.6.0-rc5*

erase a force-feedback effect from device


Synopsis
========

.. c:function:: int input_ff_erase( struct input_dev * dev, int effect_id, struct file * file )

Arguments
=========

``dev``
    input device to erase effect from

``effect_id``
    id of the effect to be erased

``file``
    purported owner of the request


Description
===========

This function erases a force-feedback effect from specified device. The
effect will only be erased if it was uploaded through the same file
handle that is requesting erase.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
