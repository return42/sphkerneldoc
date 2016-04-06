
.. _API-mipi-dsi-dcs-set-column-address:

===============================
mipi_dsi_dcs_set_column_address
===============================

*man mipi_dsi_dcs_set_column_address(9)*

*4.6.0-rc1*

define the column extent of the frame memory accessed by the host processor


Synopsis
========

.. c:function:: int mipi_dsi_dcs_set_column_address( struct mipi_dsi_device * dsi, u16 start, u16 end )

Arguments
=========

``dsi``
    DSI peripheral device

``start``
    first column of frame memory

``end``
    last column of frame memory


Return
======

0 on success or a negative error code on failure.
