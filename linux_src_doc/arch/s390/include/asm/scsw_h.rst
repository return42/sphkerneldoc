.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/scsw.h

.. _`cmd_scsw`:

struct cmd_scsw
===============

.. c:type:: struct cmd_scsw

    command-mode subchannel status word

.. _`cmd_scsw.definition`:

Definition
----------

.. code-block:: c

    struct cmd_scsw {
        __u32 key : 4;
        __u32 sctl : 1;
        __u32 eswf : 1;
        __u32 cc : 2;
        __u32 fmt : 1;
        __u32 pfch : 1;
        __u32 isic : 1;
        __u32 alcc : 1;
        __u32 ssi : 1;
        __u32 zcc : 1;
        __u32 ectl : 1;
        __u32 pno : 1;
        __u32 res : 1;
        __u32 fctl : 3;
        __u32 actl : 7;
        __u32 stctl : 5;
        __u32 cpa;
        __u32 dstat : 8;
        __u32 cstat : 8;
        __u32 count : 16;
    }

.. _`cmd_scsw.members`:

Members
-------

key
    subchannel key

sctl
    suspend control

eswf
    esw format

cc
    deferred condition code

fmt
    format

pfch
    prefetch

isic
    initial-status interruption control

alcc
    address-limit checking control

ssi
    suppress-suspended interruption

zcc
    zero condition code

ectl
    extended control

pno
    path not operational

res
    reserved

fctl
    function control

actl
    activity control

stctl
    status control

cpa
    channel program address

dstat
    device status

cstat
    subchannel status

count
    residual count

.. _`tm_scsw`:

struct tm_scsw
==============

.. c:type:: struct tm_scsw

    transport-mode subchannel status word

.. _`tm_scsw.definition`:

Definition
----------

.. code-block:: c

    struct tm_scsw {
        u32 key:4;
        u32 :1;
        u32 eswf:1;
        u32 cc:2;
        u32 fmt:3;
        u32 x:1;
        u32 q:1;
        u32 :1;
        u32 ectl:1;
        u32 pno:1;
        u32 :1;
        u32 fctl:3;
        u32 actl:7;
        u32 stctl:5;
        u32 tcw;
        u32 dstat:8;
        u32 cstat:8;
        u32 fcxs:8;
        u32 ifob:1;
        u32 sesq:7;
    }

.. _`tm_scsw.members`:

Members
-------

key
    subchannel key

eswf
    esw format

cc
    deferred condition code

fmt
    format

x
    IRB-format control

q
    interrogate-complete

ectl
    extended control

pno
    path not operational

fctl
    function control

actl
    activity control

stctl
    status control

tcw
    TCW address

dstat
    device status

cstat
    subchannel status

fcxs
    FCX status

ifob
    *undescribed*

sesq
    *undescribed*

.. _`eadm_scsw`:

struct eadm_scsw
================

.. c:type:: struct eadm_scsw

    subchannel status word for eadm subchannels

.. _`eadm_scsw.definition`:

Definition
----------

.. code-block:: c

    struct eadm_scsw {
        u32 key:4;
        u32:1;
        u32 eswf:1;
        u32 cc:2;
        u32:6;
        u32 ectl:1;
        u32:2;
        u32 fctl:3;
        u32 actl:7;
        u32 stctl:5;
        u32 aob;
        u32 dstat:8;
        u32 cstat:8;
        u32:16;
    }

.. _`eadm_scsw.members`:

Members
-------

key
    subchannel key

eswf
    esw format

cc
    deferred condition code

ectl
    extended control

fctl
    function control

actl
    activity control

stctl
    status control

aob
    AOB address

dstat
    device status

cstat
    subchannel status

.. _`scsw`:

union scsw
==========

.. c:type:: struct scsw

    subchannel status word

.. _`scsw.definition`:

Definition
----------

.. code-block:: c

    union scsw {
        struct cmd_scsw cmd;
        struct tm_scsw tm;
        struct eadm_scsw eadm;
    }

.. _`scsw.members`:

Members
-------

cmd
    command-mode SCSW

tm
    transport-mode SCSW

eadm
    eadm SCSW

.. _`scsw_is_tm`:

scsw_is_tm
==========

.. c:function:: int scsw_is_tm(union scsw *scsw)

    check for transport mode scsw

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_tm.description`:

Description
-----------

Return non-zero if the specified scsw is a transport mode scsw, zero
otherwise.

.. _`scsw_key`:

scsw_key
========

.. c:function:: u32 scsw_key(union scsw *scsw)

    return scsw key field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_key.description`:

Description
-----------

Return the value of the key field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_eswf`:

scsw_eswf
=========

.. c:function:: u32 scsw_eswf(union scsw *scsw)

    return scsw eswf field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_eswf.description`:

Description
-----------

Return the value of the eswf field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_cc`:

scsw_cc
=======

.. c:function:: u32 scsw_cc(union scsw *scsw)

    return scsw cc field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cc.description`:

Description
-----------

Return the value of the cc field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_ectl`:

scsw_ectl
=========

.. c:function:: u32 scsw_ectl(union scsw *scsw)

    return scsw ectl field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_ectl.description`:

Description
-----------

Return the value of the ectl field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_pno`:

scsw_pno
========

.. c:function:: u32 scsw_pno(union scsw *scsw)

    return scsw pno field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_pno.description`:

Description
-----------

Return the value of the pno field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_fctl`:

scsw_fctl
=========

.. c:function:: u32 scsw_fctl(union scsw *scsw)

    return scsw fctl field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_fctl.description`:

Description
-----------

Return the value of the fctl field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_actl`:

scsw_actl
=========

.. c:function:: u32 scsw_actl(union scsw *scsw)

    return scsw actl field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_actl.description`:

Description
-----------

Return the value of the actl field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_stctl`:

scsw_stctl
==========

.. c:function:: u32 scsw_stctl(union scsw *scsw)

    return scsw stctl field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_stctl.description`:

Description
-----------

Return the value of the stctl field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_dstat`:

scsw_dstat
==========

.. c:function:: u32 scsw_dstat(union scsw *scsw)

    return scsw dstat field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_dstat.description`:

Description
-----------

Return the value of the dstat field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_cstat`:

scsw_cstat
==========

.. c:function:: u32 scsw_cstat(union scsw *scsw)

    return scsw cstat field

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cstat.description`:

Description
-----------

Return the value of the cstat field of the specified scsw, regardless of
whether it is a transport mode or command mode scsw.

.. _`scsw_cmd_is_valid_key`:

scsw_cmd_is_valid_key
=====================

.. c:function:: int scsw_cmd_is_valid_key(union scsw *scsw)

    check key field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_key.description`:

Description
-----------

Return non-zero if the key field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_sctl`:

scsw_cmd_is_valid_sctl
======================

.. c:function:: int scsw_cmd_is_valid_sctl(union scsw *scsw)

    check sctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_sctl.description`:

Description
-----------

Return non-zero if the sctl field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_eswf`:

scsw_cmd_is_valid_eswf
======================

.. c:function:: int scsw_cmd_is_valid_eswf(union scsw *scsw)

    check eswf field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_eswf.description`:

Description
-----------

Return non-zero if the eswf field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_cc`:

scsw_cmd_is_valid_cc
====================

.. c:function:: int scsw_cmd_is_valid_cc(union scsw *scsw)

    check cc field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_cc.description`:

Description
-----------

Return non-zero if the cc field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_fmt`:

scsw_cmd_is_valid_fmt
=====================

.. c:function:: int scsw_cmd_is_valid_fmt(union scsw *scsw)

    check fmt field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_fmt.description`:

Description
-----------

Return non-zero if the fmt field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_pfch`:

scsw_cmd_is_valid_pfch
======================

.. c:function:: int scsw_cmd_is_valid_pfch(union scsw *scsw)

    check pfch field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_pfch.description`:

Description
-----------

Return non-zero if the pfch field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_isic`:

scsw_cmd_is_valid_isic
======================

.. c:function:: int scsw_cmd_is_valid_isic(union scsw *scsw)

    check isic field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_isic.description`:

Description
-----------

Return non-zero if the isic field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_alcc`:

scsw_cmd_is_valid_alcc
======================

.. c:function:: int scsw_cmd_is_valid_alcc(union scsw *scsw)

    check alcc field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_alcc.description`:

Description
-----------

Return non-zero if the alcc field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_ssi`:

scsw_cmd_is_valid_ssi
=====================

.. c:function:: int scsw_cmd_is_valid_ssi(union scsw *scsw)

    check ssi field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_ssi.description`:

Description
-----------

Return non-zero if the ssi field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_zcc`:

scsw_cmd_is_valid_zcc
=====================

.. c:function:: int scsw_cmd_is_valid_zcc(union scsw *scsw)

    check zcc field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_zcc.description`:

Description
-----------

Return non-zero if the zcc field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_ectl`:

scsw_cmd_is_valid_ectl
======================

.. c:function:: int scsw_cmd_is_valid_ectl(union scsw *scsw)

    check ectl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_ectl.description`:

Description
-----------

Return non-zero if the ectl field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_pno`:

scsw_cmd_is_valid_pno
=====================

.. c:function:: int scsw_cmd_is_valid_pno(union scsw *scsw)

    check pno field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_pno.description`:

Description
-----------

Return non-zero if the pno field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_fctl`:

scsw_cmd_is_valid_fctl
======================

.. c:function:: int scsw_cmd_is_valid_fctl(union scsw *scsw)

    check fctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_fctl.description`:

Description
-----------

Return non-zero if the fctl field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_actl`:

scsw_cmd_is_valid_actl
======================

.. c:function:: int scsw_cmd_is_valid_actl(union scsw *scsw)

    check actl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_actl.description`:

Description
-----------

Return non-zero if the actl field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_stctl`:

scsw_cmd_is_valid_stctl
=======================

.. c:function:: int scsw_cmd_is_valid_stctl(union scsw *scsw)

    check stctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_stctl.description`:

Description
-----------

Return non-zero if the stctl field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_dstat`:

scsw_cmd_is_valid_dstat
=======================

.. c:function:: int scsw_cmd_is_valid_dstat(union scsw *scsw)

    check dstat field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_dstat.description`:

Description
-----------

Return non-zero if the dstat field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_cmd_is_valid_cstat`:

scsw_cmd_is_valid_cstat
=======================

.. c:function:: int scsw_cmd_is_valid_cstat(union scsw *scsw)

    check cstat field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_valid_cstat.description`:

Description
-----------

Return non-zero if the cstat field of the specified command mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_key`:

scsw_tm_is_valid_key
====================

.. c:function:: int scsw_tm_is_valid_key(union scsw *scsw)

    check key field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_key.description`:

Description
-----------

Return non-zero if the key field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_eswf`:

scsw_tm_is_valid_eswf
=====================

.. c:function:: int scsw_tm_is_valid_eswf(union scsw *scsw)

    check eswf field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_eswf.description`:

Description
-----------

Return non-zero if the eswf field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_cc`:

scsw_tm_is_valid_cc
===================

.. c:function:: int scsw_tm_is_valid_cc(union scsw *scsw)

    check cc field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_cc.description`:

Description
-----------

Return non-zero if the cc field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_fmt`:

scsw_tm_is_valid_fmt
====================

.. c:function:: int scsw_tm_is_valid_fmt(union scsw *scsw)

    check fmt field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_fmt.description`:

Description
-----------

Return non-zero if the fmt field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_x`:

scsw_tm_is_valid_x
==================

.. c:function:: int scsw_tm_is_valid_x(union scsw *scsw)

    check x field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_x.description`:

Description
-----------

Return non-zero if the x field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_q`:

scsw_tm_is_valid_q
==================

.. c:function:: int scsw_tm_is_valid_q(union scsw *scsw)

    check q field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_q.description`:

Description
-----------

Return non-zero if the q field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_ectl`:

scsw_tm_is_valid_ectl
=====================

.. c:function:: int scsw_tm_is_valid_ectl(union scsw *scsw)

    check ectl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_ectl.description`:

Description
-----------

Return non-zero if the ectl field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_pno`:

scsw_tm_is_valid_pno
====================

.. c:function:: int scsw_tm_is_valid_pno(union scsw *scsw)

    check pno field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_pno.description`:

Description
-----------

Return non-zero if the pno field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_fctl`:

scsw_tm_is_valid_fctl
=====================

.. c:function:: int scsw_tm_is_valid_fctl(union scsw *scsw)

    check fctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_fctl.description`:

Description
-----------

Return non-zero if the fctl field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_actl`:

scsw_tm_is_valid_actl
=====================

.. c:function:: int scsw_tm_is_valid_actl(union scsw *scsw)

    check actl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_actl.description`:

Description
-----------

Return non-zero if the actl field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_stctl`:

scsw_tm_is_valid_stctl
======================

.. c:function:: int scsw_tm_is_valid_stctl(union scsw *scsw)

    check stctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_stctl.description`:

Description
-----------

Return non-zero if the stctl field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_dstat`:

scsw_tm_is_valid_dstat
======================

.. c:function:: int scsw_tm_is_valid_dstat(union scsw *scsw)

    check dstat field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_dstat.description`:

Description
-----------

Return non-zero if the dstat field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_cstat`:

scsw_tm_is_valid_cstat
======================

.. c:function:: int scsw_tm_is_valid_cstat(union scsw *scsw)

    check cstat field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_cstat.description`:

Description
-----------

Return non-zero if the cstat field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_fcxs`:

scsw_tm_is_valid_fcxs
=====================

.. c:function:: int scsw_tm_is_valid_fcxs(union scsw *scsw)

    check fcxs field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_fcxs.description`:

Description
-----------

Return non-zero if the fcxs field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_tm_is_valid_schxs`:

scsw_tm_is_valid_schxs
======================

.. c:function:: int scsw_tm_is_valid_schxs(union scsw *scsw)

    check schxs field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_valid_schxs.description`:

Description
-----------

Return non-zero if the schxs field of the specified transport mode scsw is
valid, zero otherwise.

.. _`scsw_is_valid_actl`:

scsw_is_valid_actl
==================

.. c:function:: int scsw_is_valid_actl(union scsw *scsw)

    check actl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_actl.description`:

Description
-----------

Return non-zero if the actl field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_cc`:

scsw_is_valid_cc
================

.. c:function:: int scsw_is_valid_cc(union scsw *scsw)

    check cc field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_cc.description`:

Description
-----------

Return non-zero if the cc field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_cstat`:

scsw_is_valid_cstat
===================

.. c:function:: int scsw_is_valid_cstat(union scsw *scsw)

    check cstat field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_cstat.description`:

Description
-----------

Return non-zero if the cstat field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_dstat`:

scsw_is_valid_dstat
===================

.. c:function:: int scsw_is_valid_dstat(union scsw *scsw)

    check dstat field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_dstat.description`:

Description
-----------

Return non-zero if the dstat field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_ectl`:

scsw_is_valid_ectl
==================

.. c:function:: int scsw_is_valid_ectl(union scsw *scsw)

    check ectl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_ectl.description`:

Description
-----------

Return non-zero if the ectl field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_eswf`:

scsw_is_valid_eswf
==================

.. c:function:: int scsw_is_valid_eswf(union scsw *scsw)

    check eswf field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_eswf.description`:

Description
-----------

Return non-zero if the eswf field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_fctl`:

scsw_is_valid_fctl
==================

.. c:function:: int scsw_is_valid_fctl(union scsw *scsw)

    check fctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_fctl.description`:

Description
-----------

Return non-zero if the fctl field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_key`:

scsw_is_valid_key
=================

.. c:function:: int scsw_is_valid_key(union scsw *scsw)

    check key field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_key.description`:

Description
-----------

Return non-zero if the key field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_pno`:

scsw_is_valid_pno
=================

.. c:function:: int scsw_is_valid_pno(union scsw *scsw)

    check pno field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_pno.description`:

Description
-----------

Return non-zero if the pno field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_is_valid_stctl`:

scsw_is_valid_stctl
===================

.. c:function:: int scsw_is_valid_stctl(union scsw *scsw)

    check stctl field validity

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_valid_stctl.description`:

Description
-----------

Return non-zero if the stctl field of the specified scsw is valid,
regardless of whether it is a transport mode or command mode scsw.
Return zero if the field does not contain a valid value.

.. _`scsw_cmd_is_solicited`:

scsw_cmd_is_solicited
=====================

.. c:function:: int scsw_cmd_is_solicited(union scsw *scsw)

    check for solicited scsw

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_cmd_is_solicited.description`:

Description
-----------

Return non-zero if the command mode scsw indicates that the associated
status condition is solicited, zero if it is unsolicited.

.. _`scsw_tm_is_solicited`:

scsw_tm_is_solicited
====================

.. c:function:: int scsw_tm_is_solicited(union scsw *scsw)

    check for solicited scsw

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_tm_is_solicited.description`:

Description
-----------

Return non-zero if the transport mode scsw indicates that the associated
status condition is solicited, zero if it is unsolicited.

.. _`scsw_is_solicited`:

scsw_is_solicited
=================

.. c:function:: int scsw_is_solicited(union scsw *scsw)

    check for solicited scsw

    :param union scsw \*scsw:
        pointer to scsw

.. _`scsw_is_solicited.description`:

Description
-----------

Return non-zero if the transport or command mode scsw indicates that the
associated status condition is solicited, zero if it is unsolicited.

.. This file was automatic generated / don't edit.

