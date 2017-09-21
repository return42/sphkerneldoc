.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_ftide010.c

.. _`ftide010`:

struct ftide010
===============

.. c:type:: struct ftide010

    state container for the Faraday FTIDE010

.. _`ftide010.definition`:

Definition
----------

.. code-block:: c

    struct ftide010 {
        struct device *dev;
        void __iomem *base;
        struct clk *pclk;
        struct ata_host *host;
        unsigned int master_cbl;
        unsigned int slave_cbl;
        struct sata_gemini *sg;
        bool master_to_sata0;
        bool slave_to_sata0;
        bool master_to_sata1;
        bool slave_to_sata1;
    }

.. _`ftide010.members`:

Members
-------

dev
    pointer back to the device representing this controller

base
    remapped I/O space address

pclk
    peripheral clock for the IDE block

host
    pointer to the ATA host for this device

master_cbl
    master cable type

slave_cbl
    slave cable type

sg
    Gemini SATA bridge pointer, if running on the Gemini

master_to_sata0
    Gemini SATA bridge: the ATA master is connected
    to the SATA0 bridge

slave_to_sata0
    Gemini SATA bridge: the ATA slave is connected
    to the SATA0 bridge

master_to_sata1
    Gemini SATA bridge: the ATA master is connected
    to the SATA1 bridge

slave_to_sata1
    Gemini SATA bridge: the ATA slave is connected
    to the SATA1 bridge

.. This file was automatic generated / don't edit.

