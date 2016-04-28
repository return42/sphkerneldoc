.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-sublog:

=============
struct sublog
=============

*man struct sublog(9)*

*4.6.0-rc5*

subchannel logout area


Synopsis
========

.. code-block:: c

    struct sublog {
      __u32 res0:1;
      __u32 esf:7;
      __u32 lpum:8;
      __u32 arep:1;
      __u32 fvf:5;
      __u32 sacc:2;
      __u32 termc:2;
      __u32 devsc:1;
      __u32 serr:1;
      __u32 ioerr:1;
      __u32 seqc:3;
    };


Members
=======

res0
    reserved

esf
    extended status flags

lpum
    last path used mask

arep
    ancillary report

fvf
    field-validity flags

sacc
    storage access code

termc
    termination code

devsc
    device-status check

serr
    secondary error

ioerr
    i/o-error alert

seqc
    sequence code


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
