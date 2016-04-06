
.. _API-snd-card-add-dev-attr:

=====================
snd_card_add_dev_attr
=====================

*man snd_card_add_dev_attr(9)*

*4.6.0-rc1*

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
