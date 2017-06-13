.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/dgnc/digi.h

.. _`digi_t`:

struct digi_t
=============

.. c:type:: struct digi_t

    Ioctl commands for DIGI parameters.

.. _`digi_t.definition`:

Definition
----------

.. code-block:: c

    struct digi_t {
        unsigned short digi_flags;
        unsigned short digi_maxcps;
        unsigned short digi_maxchar;
        unsigned short digi_bufsize;
        unsigned char digi_onlen;
        unsigned char digi_offlen;
        char digi_onstr[DIGI_PLEN];
        char digi_offstr[DIGI_PLEN];
        char digi_term[DIGI_TSIZ];
    }

.. _`digi_t.members`:

Members
-------

digi_flags
    Flags.

digi_maxcps
    Maximum printer CPS.

digi_maxchar
    Maximum characters in the print queue.

digi_bufsize
    Buffer size.

digi_onlen
    Length of ON string.

digi_offlen
    Length of OFF string.

digi_onstr
    Printer ON string.

digi_offstr
    Printer OFF string.

digi_term
    Terminal string.

.. _`digi_dinfo`:

struct digi_dinfo
=================

.. c:type:: struct digi_dinfo

    Driver status information.

.. _`digi_dinfo.definition`:

Definition
----------

.. code-block:: c

    struct digi_dinfo {
        unsigned int dinfo_nboards;
        char dinfo_reserved[12];
        char dinfo_version[16];
    }

.. _`digi_dinfo.members`:

Members
-------

dinfo_nboards
    Number of boards configured.

dinfo_reserved
    Not used, for future expansion.

.. _`digi_info`:

struct digi_info
================

.. c:type:: struct digi_info

    Ioctl commands for per board information.

.. _`digi_info.definition`:

Definition
----------

.. code-block:: c

    struct digi_info {
        unsigned int info_bdnum;
        unsigned int info_ioport;
        unsigned int info_physaddr;
        unsigned int info_physsize;
        unsigned int info_memsize;
        unsigned short info_bdtype;
        unsigned short info_nports;
        char info_bdstate;
        char info_reserved[7];
    }

.. _`digi_info.members`:

Members
-------

info_bdnum
    Board number (0 based).

info_ioport
    IO port address.

info_physaddr
    *undescribed*

info_physsize
    *undescribed*

info_memsize
    Amount of dual-port memory on board.

info_bdtype
    Board type.

info_nports
    Number of ports.

info_bdstate
    Board state.

info_reserved
    Not used, for future expansion.

.. _`digi_info.description`:

Description
-----------

Physsize and memsize differ when board has "windowed" memory.

.. _`digi_getbuffer`:

struct digi_getbuffer
=====================

.. c:type:: struct digi_getbuffer

    Holds buffer use counts.

.. _`digi_getbuffer.definition`:

Definition
----------

.. code-block:: c

    struct digi_getbuffer {
        unsigned long tx_in;
        unsigned long tx_out;
        unsigned long rxbuf;
        unsigned long txbuf;
        unsigned long txdone;
    }

.. _`digi_getbuffer.members`:

Members
-------

tx_in
    *undescribed*

tx_out
    *undescribed*

rxbuf
    *undescribed*

txbuf
    *undescribed*

txdone
    *undescribed*

.. _`digi_getcounter`:

struct digi_getcounter
======================

.. c:type:: struct digi_getcounter


.. _`digi_getcounter.definition`:

Definition
----------

.. code-block:: c

    struct digi_getcounter {
        unsigned long norun;
        unsigned long noflow;
        unsigned long nframe;
        unsigned long nparity;
        unsigned long nbreak;
        unsigned long rbytes;
        unsigned long tbytes;
    }

.. _`digi_getcounter.members`:

Members
-------

norun
    Number of UART overrun errors.

noflow
    Number of buffer overflow errors.

nframe
    Number of framing errors.

nparity
    Number of parity errors.

nbreak
    Number of breaks received.

rbytes
    Number of received bytes.

tbytes
    Number of transmitted bytes.

.. _`ni_info`:

struct ni_info
==============

.. c:type:: struct ni_info

    intelligent <--> non-intelligent DPA translation.

.. _`ni_info.definition`:

Definition
----------

.. code-block:: c

    struct ni_info {
        int board;
        int channel;
        int dtr;
        int rts;
        int cts;
        int dsr;
        int ri;
        int dcd;
        int curtx;
        int currx;
        unsigned short iflag;
        unsigned short oflag;
        unsigned short cflag;
        unsigned short lflag;
        unsigned int mstat;
        unsigned char hflow;
        unsigned char xmit_stopped;
        unsigned char recv_stopped;
        unsigned int baud;
    }

.. _`ni_info.members`:

Members
-------

board
    *undescribed*

channel
    *undescribed*

dtr
    *undescribed*

rts
    *undescribed*

cts
    *undescribed*

dsr
    *undescribed*

ri
    *undescribed*

dcd
    *undescribed*

curtx
    *undescribed*

currx
    *undescribed*

iflag
    *undescribed*

oflag
    *undescribed*

cflag
    *undescribed*

lflag
    *undescribed*

mstat
    *undescribed*

hflow
    *undescribed*

xmit_stopped
    *undescribed*

recv_stopped
    *undescribed*

baud
    *undescribed*

.. This file was automatic generated / don't edit.

