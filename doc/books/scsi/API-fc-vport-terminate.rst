
.. _API-fc-vport-terminate:

==================
fc_vport_terminate
==================

*man fc_vport_terminate(9)*

*4.6.0-rc1*

Admin App or LLDD requests termination of a vport


Synopsis
========

.. c:function:: int fc_vport_terminate( struct fc_vport * vport )

Arguments
=========

``vport``
    fc_vport to be terminated


Description
===========

Calls the LLDD ``vport_delete`` function, then deallocates and removes the vport from the shost and object tree.


Notes
=====

This routine assumes no locks are held on entry.
