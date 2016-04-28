.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-add-dev-attr:

=====================
snd_card_add_dev_attr
=====================

*man snd_card_add_dev_attr(9)*

*4.6.0-rc5*

Append a new sysfs attribute group to card


Synopsis
========

.. c:function:: int snd_card_add_dev_attr( struct snd_card * card, const struct attribute_group * group )

Arguments
=========

``card``
    card instance

``group``
    attribute group to append


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
