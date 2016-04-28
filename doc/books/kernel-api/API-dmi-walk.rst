.. -*- coding: utf-8; mode: rst -*-

.. _API-dmi-walk:

========
dmi_walk
========

*man dmi_walk(9)*

*4.6.0-rc5*

Walk the DMI table and get called back for every record


Synopsis
========

.. c:function:: int dmi_walk( void (*decode) const struct dmi_header *, void *, void * private_data )

Arguments
=========

``decode``
    Callback function

``private_data``
    Private data to be passed to the callback function


Description
===========

Returns -1 when the DMI table can't be reached, 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
