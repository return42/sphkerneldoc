
.. _API-sas-remove-children:

===================
sas_remove_children
===================

*man sas_remove_children(9)*

*4.6.0-rc1*

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
