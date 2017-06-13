.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/cio.h

.. _`ccw1`:

struct ccw1
===========

.. c:type:: struct ccw1

    channel command word

.. _`ccw1.definition`:

Definition
----------

.. code-block:: c

    struct ccw1 {
        __u8 cmd_code;
        __u8 flags;
        __u16 count;
        __u32 cda;
    }

.. _`ccw1.members`:

Members
-------

cmd_code
    command code

flags
    flags, like IDA addressing, etc.

count
    byte count

cda
    data address

.. _`ccw1.description`:

Description
-----------

The ccw is the basic structure to build channel programs that perform
operations with the device or the control unit. Only Format-1 channel
command words are supported.

.. _`ccw0`:

struct ccw0
===========

.. c:type:: struct ccw0

    channel command word

.. _`ccw0.definition`:

Definition
----------

.. code-block:: c

    struct ccw0 {
        __u8 cmd_code;
        __u32 cda:24;
        __u8 flags;
        __u8 reserved;
        __u16 count;
    }

.. _`ccw0.members`:

Members
-------

cmd_code
    command code

cda
    data address

flags
    flags, like IDA addressing, etc.

reserved
    will be ignored

count
    byte count

.. _`ccw0.description`:

Description
-----------

The format-0 ccw structure.

.. _`erw`:

struct erw
==========

.. c:type:: struct erw

    extended report word

.. _`erw.definition`:

Definition
----------

.. code-block:: c

    struct erw {
        __u32 res0:3;
        __u32 auth:1;
        __u32 pvrf:1;
        __u32 cpt:1;
        __u32 fsavf:1;
        __u32 cons:1;
        __u32 scavf:1;
        __u32 fsaf:1;
        __u32 scnt:6;
        __u32 res16:16;
    }

.. _`erw.members`:

Members
-------

res0
    reserved

auth
    authorization check

pvrf
    path-verification-required flag

cpt
    channel-path timeout

fsavf
    failing storage address validity flag

cons
    concurrent sense

scavf
    secondary ccw address validity flag

fsaf
    failing storage address format

scnt
    sense count, if \ ``cons``\  == \ ``1``\ 

res16
    reserved

.. _`erw_eadm`:

struct erw_eadm
===============

.. c:type:: struct erw_eadm

    EADM Subchannel extended report word

.. _`erw_eadm.definition`:

Definition
----------

.. code-block:: c

    struct erw_eadm {
        __u32 b:1;
        __u32 r:1;
    }

.. _`erw_eadm.members`:

Members
-------

b
    aob error

r
    arsb error

.. _`sublog`:

struct sublog
=============

.. c:type:: struct sublog

    subchannel logout area

.. _`sublog.definition`:

Definition
----------

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
    }

.. _`sublog.members`:

Members
-------

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

.. _`esw0`:

struct esw0
===========

.. c:type:: struct esw0

    Format 0 Extended Status Word (ESW)

.. _`esw0.definition`:

Definition
----------

.. code-block:: c

    struct esw0 {
        struct sublog sublog;
        struct erw erw;
        __u32 faddr;
        __u32 saddr;
    }

.. _`esw0.members`:

Members
-------

sublog
    subchannel logout

erw
    extended report word

faddr
    failing storage address

saddr
    secondary ccw address

.. _`esw1`:

struct esw1
===========

.. c:type:: struct esw1

    Format 1 Extended Status Word (ESW)

.. _`esw1.definition`:

Definition
----------

.. code-block:: c

    struct esw1 {
        __u8 zero0;
        __u8 lpum;
        __u16 zero16;
        struct erw erw;
        __u32 zeros;
    }

.. _`esw1.members`:

Members
-------

zero0
    reserved zeros

lpum
    last path used mask

zero16
    reserved zeros

erw
    extended report word

zeros
    three fullwords of zeros

.. _`esw2`:

struct esw2
===========

.. c:type:: struct esw2

    Format 2 Extended Status Word (ESW)

.. _`esw2.definition`:

Definition
----------

.. code-block:: c

    struct esw2 {
        __u8 zero0;
        __u8 lpum;
        __u16 dcti;
        struct erw erw;
        __u32 zeros;
    }

.. _`esw2.members`:

Members
-------

zero0
    reserved zeros

lpum
    last path used mask

dcti
    device-connect-time interval

erw
    extended report word

zeros
    three fullwords of zeros

.. _`esw3`:

struct esw3
===========

.. c:type:: struct esw3

    Format 3 Extended Status Word (ESW)

.. _`esw3.definition`:

Definition
----------

.. code-block:: c

    struct esw3 {
        __u8 zero0;
        __u8 lpum;
        __u16 res;
        struct erw erw;
        __u32 zeros;
    }

.. _`esw3.members`:

Members
-------

zero0
    reserved zeros

lpum
    last path used mask

res
    reserved

erw
    extended report word

zeros
    three fullwords of zeros

.. _`esw_eadm`:

struct esw_eadm
===============

.. c:type:: struct esw_eadm

    EADM Subchannel Extended Status Word (ESW)

.. _`esw_eadm.definition`:

Definition
----------

.. code-block:: c

    struct esw_eadm {
        __u32 sublog;
        struct erw_eadm erw;
    }

.. _`esw_eadm.members`:

Members
-------

sublog
    subchannel logout

erw
    extended report word

.. _`irb`:

struct irb
==========

.. c:type:: struct irb

    interruption response block

.. _`irb.definition`:

Definition
----------

.. code-block:: c

    struct irb {
        union scsw scsw;
        union esw;
        __u8 ecw;
    }

.. _`irb.members`:

Members
-------

scsw
    subchannel status word

esw
    extended status word

ecw
    extended control word

.. _`irb.description`:

Description
-----------

The irb that is handed to the device driver when an interrupt occurs. For
solicited interrupts, the common I/O layer already performs checks whether
a field is valid; a field not being valid is always passed as \ ``0``\ .
If a unit check occurred, \ ``ecw``\  may contain sense data; this is retrieved
by the common I/O layer itself if the device doesn't support concurrent
sense (so that the device driver never needs to perform basic sene itself).
For unsolicited interrupts, the irb is passed as-is (expect for sense data,
if applicable).

.. _`ciw`:

struct ciw
==========

.. c:type:: struct ciw

    command information word  (CIW) layout

.. _`ciw.definition`:

Definition
----------

.. code-block:: c

    struct ciw {
        __u32 et:2;
        __u32 reserved:2;
        __u32 ct:4;
        __u32 cmd:8;
        __u32 count:16;
    }

.. _`ciw.members`:

Members
-------

et
    entry type

reserved
    reserved bits

ct
    command type

cmd
    command code

count
    command count

.. _`ccw_dev_id`:

struct ccw_dev_id
=================

.. c:type:: struct ccw_dev_id

    unique identifier for ccw devices

.. _`ccw_dev_id.definition`:

Definition
----------

.. code-block:: c

    struct ccw_dev_id {
        u8 ssid;
        u16 devno;
    }

.. _`ccw_dev_id.members`:

Members
-------

ssid
    subchannel set id

devno
    device number

.. _`ccw_dev_id.description`:

Description
-----------

This structure is not directly based on any hardware structure. The
hardware identifies a device by its device number and its subchannel,
which is in turn identified by its id. In order to get a unique identifier
for ccw devices across subchannel sets, \ ``struct``\  ccw_dev_id has been
introduced.

.. _`ccw_dev_id_is_equal`:

ccw_dev_id_is_equal
===================

.. c:function:: int ccw_dev_id_is_equal(struct ccw_dev_id *dev_id1, struct ccw_dev_id *dev_id2)

    compare two ccw_dev_ids

    :param struct ccw_dev_id \*dev_id1:
        a ccw_dev_id

    :param struct ccw_dev_id \*dev_id2:
        another ccw_dev_id

.. _`ccw_dev_id_is_equal.return`:

Return
------

 \ ``1``\  if the two structures are equal field-by-field,
 \ ``0``\  if not.

.. _`ccw_dev_id_is_equal.context`:

Context
-------

 any

.. _`pathmask_to_pos`:

pathmask_to_pos
===============

.. c:function:: u8 pathmask_to_pos(u8 mask)

    find the position of the left-most bit in a pathmask

    :param u8 mask:
        pathmask with at least one bit set

.. This file was automatic generated / don't edit.

