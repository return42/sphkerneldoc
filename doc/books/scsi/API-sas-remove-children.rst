.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-remove-children:

===================
sas_remove_children
===================

*man sas_remove_children(9)*

*4.6.0-rc5*

tear down a devices SAS data structures


Synopsis
========

.. c:function:: void sas_remove_children( struct device * dev )

Arguments
=========

``dev``
    device belonging to the sas object


Description
===========

Removes all SAS PHYs and remote PHYs for a given object


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
