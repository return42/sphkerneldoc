.. -*- coding: utf-8; mode: rst -*-

.. _API-input-mt-drop-unused:

====================
input_mt_drop_unused
====================

*man input_mt_drop_unused(9)*

*4.6.0-rc5*

Inactivate slots not seen in this frame


Synopsis
========

.. c:function:: void input_mt_drop_unused( struct input_dev * dev )

Arguments
=========

``dev``
    input device with allocated MT slots


Description
===========

Lift all slots not seen since the last call to this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
