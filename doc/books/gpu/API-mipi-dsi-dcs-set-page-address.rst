.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-set-page-address:

=============================
mipi_dsi_dcs_set_page_address
=============================

*man mipi_dsi_dcs_set_page_address(9)*

*4.6.0-rc5*

define the page extent of the frame memory accessed by the host
processor


Synopsis
========

.. c:function:: int mipi_dsi_dcs_set_page_address( struct mipi_dsi_device * dsi, u16 start, u16 end )

Arguments
=========

``dsi``
    DSI peripheral device

``start``
    first page of frame memory

``end``
    last page of frame memory


Return
======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
