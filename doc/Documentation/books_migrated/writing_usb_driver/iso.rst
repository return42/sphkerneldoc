.. -*- coding: utf-8; mode: rst -*-

.. _iso:

****************
Isochronous Data
****************

This usb-skeleton driver does not have any examples of interrupt or
isochronous data being sent to or from the device. Interrupt data is
sent almost exactly as bulk data is, with a few minor exceptions.
Isochronous data works differently with continuous streams of data being
sent to or from the device. The audio and video camera drivers are very
good examples of drivers that handle isochronous data and will be useful
if you also need to do this.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
