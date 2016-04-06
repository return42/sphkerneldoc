
.. _API-spi-populate-tag-msg:

====================
spi_populate_tag_msg
====================

*man spi_populate_tag_msg(9)*

*4.6.0-rc1*

place a tag message in a buffer


Synopsis
========

.. c:function:: int spi_populate_tag_msg( unsigned char * msg, struct scsi_cmnd * cmd )

Arguments
=========

``msg``
    pointer to the area to place the tag

``cmd``
    pointer to the scsi command for the tag


Notes
=====

designed to create the correct type of tag message for the particular request. Returns the size of the tag message. May return 0 if TCQ is disabled for this device.
