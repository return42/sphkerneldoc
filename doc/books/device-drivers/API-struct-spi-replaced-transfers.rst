
.. _API-struct-spi-replaced-transfers:

=============================
struct spi_replaced_transfers
=============================

*man struct spi_replaced_transfers(9)*

*4.6.0-rc1*

structure describing the spi_transfer replacements that have occurred so that they can get reverted


Synopsis
========

.. code-block:: c

    struct spi_replaced_transfers {
      spi_replaced_release_t release;
      void * extradata;
      struct list_head replaced_transfers;
      struct list_head * replaced_after;
      size_t inserted;
      struct spi_transfer inserted_transfers[];
    };


Members
=======

release
    some extra release code to get executed prior to relasing this structure

extradata
    pointer to some extra data if requested or NULL

replaced_transfers
    transfers that have been replaced and which need to get restored

replaced_after
    the transfer after which the ``replaced_transfers`` are to get re-inserted

inserted
    number of transfers inserted

inserted_transfers[]
    array of spi_transfers of array-size ``inserted``, that have been replacing replaced_transfers


note
====

that ``extradata`` will point to ``inserted_transfers`` [``inserted``] if some extra allocation is requested, so alignment will be the same as for spi_transfers
