.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/stm.h

.. _`stp_packet_type`:

enum stp_packet_type
====================

.. c:type:: enum stp_packet_type

    STP packets that an STM driver sends

.. _`stp_packet_type.definition`:

Definition
----------

.. code-block:: c

    enum stp_packet_type {
        STP_PACKET_DATA,
        STP_PACKET_FLAG,
        STP_PACKET_USER,
        STP_PACKET_MERR,
        STP_PACKET_GERR,
        STP_PACKET_TRIG,
        STP_PACKET_XSYNC
    };

.. _`stp_packet_type.constants`:

Constants
---------

STP_PACKET_DATA
    *undescribed*

STP_PACKET_FLAG
    *undescribed*

STP_PACKET_USER
    *undescribed*

STP_PACKET_MERR
    *undescribed*

STP_PACKET_GERR
    *undescribed*

STP_PACKET_TRIG
    *undescribed*

STP_PACKET_XSYNC
    *undescribed*

.. _`stp_packet_flags`:

enum stp_packet_flags
=====================

.. c:type:: enum stp_packet_flags

    STP packet modifiers

.. _`stp_packet_flags.definition`:

Definition
----------

.. code-block:: c

    enum stp_packet_flags {
        STP_PACKET_MARKED,
        STP_PACKET_TIMESTAMPED
    };

.. _`stp_packet_flags.constants`:

Constants
---------

STP_PACKET_MARKED
    *undescribed*

STP_PACKET_TIMESTAMPED
    *undescribed*

.. _`stm_data`:

struct stm_data
===============

.. c:type:: struct stm_data

    STM device description and callbacks

.. _`stm_data.definition`:

Definition
----------

.. code-block:: c

    struct stm_data {
        const char *name;
        struct stm_device *stm;
        unsigned int sw_start;
        unsigned int sw_end;
        unsigned int sw_nchannels;
        unsigned int sw_mmiosz;
        unsigned int hw_override;
        ssize_t (* packet) (struct stm_data *, unsigned int,unsigned int, unsigned int,unsigned int, unsigned int,const unsigned char *);
        phys_addr_t (* mmio_addr) (struct stm_data *, unsigned int,unsigned int, unsigned int);
        int (* link) (struct stm_data *, unsigned int,unsigned int);
        void (* unlink) (struct stm_data *, unsigned int,unsigned int);
        long (* set_options) (struct stm_data *, unsigned int,unsigned int, unsigned int,unsigned long);
    }

.. _`stm_data.members`:

Members
-------

name
    device name

stm
    internal structure, only used by stm class code

sw_start
    first STP master available to software

sw_end
    last STP master available to software

sw_nchannels
    number of STP channels per master

sw_mmiosz
    size of one channel's IO space, for mmap, optional

hw_override
    masters in the STP stream will not match the ones
    assigned by software, but are up to the STM hardware

packet
    callback that sends an STP packet

mmio_addr
    mmap callback, optional

link
    called when a new stm_source gets linked to us, optional

unlink
    likewise for unlinking, again optional

set_options
    set device-specific options on a channel

.. _`stm_data.description`:

Description
-----------

Fill out this structure before calling \ :c:func:`stm_register_device`\  to create
an STM device and \ :c:func:`stm_unregister_device`\  to destroy it. It will also be
passed back to @\ :c:func:`packet`\ , @\ :c:func:`mmio_addr`\ , @\ :c:func:`link`\ , @\ :c:func:`unlink`\  and @\ :c:func:`set_options`\ 
callbacks.

Normally, an STM device will have a range of masters available to software
and the rest being statically assigned to various hardware trace sources.
The former is defined by the the range [\ ``sw_start``\ ..\ ``sw_end``\ ] of the device
description. That is, the lowest master that can be allocated to software
writers is \ ``sw_start``\  and data from this writer will appear is \ ``sw_start``\ 
master in the STP stream.

The \ ``packet``\  callback should adhere to the following rules:
1) it must return the number of bytes it consumed from the payload;
2) therefore, if it sent a packet that does not have payload (like FLAG),
it must return zero;
3) if it does not support the requested packet type/flag combination,
it must return -ENOTSUPP.

The \ ``unlink``\  callback is called when there are no more active writers so
that the master/channel can be quiesced.

.. _`stm_source_data`:

struct stm_source_data
======================

.. c:type:: struct stm_source_data

    STM source device description and callbacks

.. _`stm_source_data.definition`:

Definition
----------

.. code-block:: c

    struct stm_source_data {
        const char *name;
        struct stm_source_device *src;
        unsigned int percpu;
        unsigned int nr_chans;
        int (* link) (struct stm_source_data *data);
        void (* unlink) (struct stm_source_data *data);
    }

.. _`stm_source_data.members`:

Members
-------

name
    device name, will be used for policy lookup

src
    internal structure, only used by stm class code

percpu
    *undescribed*

nr_chans
    number of channels to allocate

link
    called when this source gets linked to an STM device

unlink
    called when this source is about to get unlinked from its STM

.. _`stm_source_data.description`:

Description
-----------

Fill in this structure before calling \ :c:func:`stm_source_register_device`\  to
register a source device. Also pass it to unregister and write calls.

.. This file was automatic generated / don't edit.

