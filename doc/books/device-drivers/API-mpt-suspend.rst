.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-suspend:

===========
mpt_suspend
===========

*man mpt_suspend(9)*

*4.6.0-rc5*

Fusion MPT base driver suspend routine.


Synopsis
========

.. c:function:: int mpt_suspend( struct pci_dev * pdev, pm_message_t state )

Arguments
=========

``pdev``
    Pointer to pci_dev structure

``state``
    new state to enter


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
