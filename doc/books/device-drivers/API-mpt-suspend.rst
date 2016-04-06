
.. _API-mpt-suspend:

===========
mpt_suspend
===========

*man mpt_suspend(9)*

*4.6.0-rc1*

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
