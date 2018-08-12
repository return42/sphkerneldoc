.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/cadence_master.h

.. _`sdw_cdns_pdi`:

struct sdw_cdns_pdi
===================

.. c:type:: struct sdw_cdns_pdi

    PDI (Physical Data Interface) instance

.. _`sdw_cdns_pdi.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns_pdi {
        bool assigned;
        int num;
        int intel_alh_id;
        int l_ch_num;
        int h_ch_num;
        int ch_count;
        enum sdw_data_direction dir;
        enum sdw_stream_type type;
    }

.. _`sdw_cdns_pdi.members`:

Members
-------

assigned
    pdi assigned

num
    pdi number

intel_alh_id
    link identifier

l_ch_num
    low channel for PDI

h_ch_num
    high channel for PDI

ch_count
    total channel count for PDI

dir
    data direction

type
    stream type, PDM or PCM

.. _`sdw_cdns_port`:

struct sdw_cdns_port
====================

.. c:type:: struct sdw_cdns_port

    Cadence port structure

.. _`sdw_cdns_port.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns_port {
        unsigned int num;
        bool assigned;
        unsigned int ch;
        enum sdw_data_direction direction;
        struct sdw_cdns_pdi *pdi;
    }

.. _`sdw_cdns_port.members`:

Members
-------

num
    port number

assigned
    port assigned

ch
    channel count

direction
    data port direction

pdi
    pdi for this port

.. _`sdw_cdns_streams`:

struct sdw_cdns_streams
=======================

.. c:type:: struct sdw_cdns_streams

    Cadence stream data structure

.. _`sdw_cdns_streams.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns_streams {
        unsigned int num_bd;
        unsigned int num_in;
        unsigned int num_out;
        unsigned int num_ch_bd;
        unsigned int num_ch_in;
        unsigned int num_ch_out;
        unsigned int num_pdi;
        struct sdw_cdns_pdi *bd;
        struct sdw_cdns_pdi *in;
        struct sdw_cdns_pdi *out;
    }

.. _`sdw_cdns_streams.members`:

Members
-------

num_bd
    number of bidirectional streams

num_in
    number of input streams

num_out
    number of output streams

num_ch_bd
    number of output stream channels

num_ch_in
    *undescribed*

num_ch_out
    *undescribed*

num_pdi
    total number of PDIs

bd
    bidirectional streams

in
    input streams

out
    output streams

.. _`sdw_cdns_stream_config`:

struct sdw_cdns_stream_config
=============================

.. c:type:: struct sdw_cdns_stream_config

    stream configuration

.. _`sdw_cdns_stream_config.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns_stream_config {
        unsigned int pcm_bd;
        unsigned int pcm_in;
        unsigned int pcm_out;
        unsigned int pdm_bd;
        unsigned int pdm_in;
        unsigned int pdm_out;
    }

.. _`sdw_cdns_stream_config.members`:

Members
-------

pcm_bd
    number of bidirectional PCM streams supported

pcm_in
    number of input PCM streams supported

pcm_out
    number of output PCM streams supported

pdm_bd
    number of bidirectional PDM streams supported

pdm_in
    number of input PDM streams supported

pdm_out
    number of output PDM streams supported

.. _`sdw_cdns_dma_data`:

struct sdw_cdns_dma_data
========================

.. c:type:: struct sdw_cdns_dma_data

    Cadence DMA data

.. _`sdw_cdns_dma_data.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns_dma_data {
        char *name;
        struct sdw_stream_runtime *stream;
        int nr_ports;
        struct sdw_cdns_port **port;
        struct sdw_bus *bus;
        enum sdw_stream_type stream_type;
        int link_id;
    }

.. _`sdw_cdns_dma_data.members`:

Members
-------

name
    SoundWire stream name

stream
    *undescribed*

nr_ports
    Number of ports

port
    Ports

bus
    Bus handle

stream_type
    Stream type

link_id
    Master link id

.. _`sdw_cdns`:

struct sdw_cdns
===============

.. c:type:: struct sdw_cdns

    Cadence driver context

.. _`sdw_cdns.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns {
        struct device *dev;
        struct sdw_bus bus;
        unsigned int instance;
        u32 response_buf[0x80];
        struct completion tx_complete;
        struct sdw_defer *defer;
        struct sdw_cdns_port *ports;
        int num_ports;
        struct sdw_cdns_streams pcm;
        struct sdw_cdns_streams pdm;
        void __iomem *registers;
        bool link_up;
        unsigned int msg_count;
    }

.. _`sdw_cdns.members`:

Members
-------

dev
    Linux device

bus
    Bus handle

instance
    instance number

response_buf
    SoundWire response buffer

tx_complete
    Tx completion

defer
    Defer pointer

ports
    Data ports

num_ports
    Total number of data ports

pcm
    PCM streams

pdm
    PDM streams

registers
    Cadence registers

link_up
    Link status

msg_count
    Messages sent on bus

.. This file was automatic generated / don't edit.

