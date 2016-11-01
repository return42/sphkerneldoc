.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/sclp_diag.h

.. _`sclp_diag_ftp`:

struct sclp_diag_ftp
====================

.. c:type:: struct sclp_diag_ftp

    Diagnostic Test FTP Service model-dependent data

.. _`sclp_diag_ftp.definition`:

Definition
----------

.. code-block:: c

    struct sclp_diag_ftp {
        u8 pcx;
        u8 ldflg;
        u8 cmd;
        u8 pgsize;
        u8 srcflg;
        u8 spare;
        u64 offset;
        u64 fsize;
        u64 length;
        u64 failaddr;
        u64 bufaddr;
        u64 asce;
        u8 fident[256];
    }

.. _`sclp_diag_ftp.members`:

Members
-------

pcx
    code for PCX communication (should be 0x80)

ldflg
    load flag (see defines above)

cmd
    FTP command

pgsize
    page size (0 = 4kB, 1 = large page size)

srcflg
    source flag

spare
    reserved (zeroes)

offset
    file offset

fsize
    file size

length
    buffer size resp. bytes transferred

failaddr
    failing address

bufaddr
    buffer address, virtual

asce
    region or segment table designation

fident
    file name (ASCII, zero-terminated)

.. _`sclp_diag_evbuf`:

struct sclp_diag_evbuf
======================

.. c:type:: struct sclp_diag_evbuf

    Diagnostic Test (ET7) Event Buffer

.. _`sclp_diag_evbuf.definition`:

Definition
----------

.. code-block:: c

    struct sclp_diag_evbuf {
        struct evbuf_header hdr;
        u16 route;
        union mdd;
    }

.. _`sclp_diag_evbuf.members`:

Members
-------

hdr
    event buffer header

route
    diagnostic route

mdd
    model-dependent data (@route dependent)

.. _`sclp_diag_sccb`:

struct sclp_diag_sccb
=====================

.. c:type:: struct sclp_diag_sccb

    Diagnostic Test (ET7) SCCB

.. _`sclp_diag_sccb.definition`:

Definition
----------

.. code-block:: c

    struct sclp_diag_sccb {
        struct sccb_header hdr;
        struct sclp_diag_evbuf evbuf;
    }

.. _`sclp_diag_sccb.members`:

Members
-------

hdr
    SCCB header

evbuf
    event buffer

.. This file was automatic generated / don't edit.

