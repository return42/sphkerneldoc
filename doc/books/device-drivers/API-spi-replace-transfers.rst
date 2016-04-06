
.. _API-spi-replace-transfers:

=====================
spi_replace_transfers
=====================

*man spi_replace_transfers(9)*

*4.6.0-rc1*

replace transfers with several transfers and register change with spi_message.resources


Synopsis
========

.. c:function:: struct spi_replaced_transfers ⋆ spi_replace_transfers( struct spi_message * msg, struct spi_transfer * xfer_first, size_t remove, size_t insert, spi_replaced_release_t release, size_t extradatasize, gfp_t gfp )

Arguments
=========

``msg``
    the spi_message we work upon

``xfer_first``
    the first spi_transfer we want to replace

``remove``
    number of transfers to remove

``insert``
    the number of transfers we want to insert instead

``release``
    extra release code necessary in some circumstances

``extradatasize``
    extra data to allocate (with alignment guarantees of struct ``spi_transfer``)

``gfp``
    gfp flags


Returns
=======

pointer to ``spi_replaced_transfers``, PTR_ERR(...) in case of errors.
