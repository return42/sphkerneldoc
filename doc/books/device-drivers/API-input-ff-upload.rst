.. -*- coding: utf-8; mode: rst -*-

.. _API-input-ff-upload:

===============
input_ff_upload
===============

*man input_ff_upload(9)*

*4.6.0-rc5*

upload effect into force-feedback device


Synopsis
========

.. c:function:: int input_ff_upload( struct input_dev * dev, struct ff_effect * effect, struct file * file )

Arguments
=========

``dev``
    input device

``effect``
    effect to be uploaded

``file``
    owner of the effect


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
