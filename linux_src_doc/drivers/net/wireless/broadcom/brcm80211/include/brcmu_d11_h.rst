.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/include/brcmu_d11.h

.. _`brcmu_chan`:

struct brcmu_chan
=================

.. c:type:: struct brcmu_chan

    stores channel formats

.. _`brcmu_chan.definition`:

Definition
----------

.. code-block:: c

    struct brcmu_chan {
        u16 chspec;
        u8 chnum;
        u8 control_ch_num;
        u8 band;
        enum brcmu_chan_bw bw;
        enum brcmu_chan_sb sb;
    }

.. _`brcmu_chan.members`:

Members
-------

chspec
    firmware specific format

chnum
    center channel number

control_ch_num
    control channel number

band
    frequency band

bw
    channel width

sb
    control sideband (location of control channel against the center one)

.. _`brcmu_chan.description`:

Description
-----------

This structure can be used with functions translating chanspec into generic
channel info and the other way.

.. _`brcmu_d11inf`:

struct brcmu_d11inf
===================

.. c:type:: struct brcmu_d11inf

    provides functions translating channel format

.. _`brcmu_d11inf.definition`:

Definition
----------

.. code-block:: c

    struct brcmu_d11inf {
        u8 io_type;
        void (*encchspec)(struct brcmu_chan *ch);
        void (*decchspec)(struct brcmu_chan *ch);
    }

.. _`brcmu_d11inf.members`:

Members
-------

io_type
    determines version of channel format used by firmware

encchspec
    encodes channel info into a chanspec, requires center channel
    number, ignores control one

decchspec
    decodes chanspec into generic info

.. This file was automatic generated / don't edit.

