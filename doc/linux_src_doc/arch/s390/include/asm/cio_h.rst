.. -*- coding: utf-8; mode: rst -*-

=====
cio.h
=====



.. _xref_struct_ccw1:

struct ccw1
===========

.. c:type:: struct ccw1

    channel command word



Definition
----------

.. code-block:: c

  struct ccw1 {
    __u8 cmd_code;
    __u8 flags;
    __u16 count;
    __u32 cda;
  };



Members
-------

:``__u8 cmd_code``:
    command code

:``__u8 flags``:
    flags, like IDA addressing, etc.

:``__u16 count``:
    byte count

:``__u32 cda``:
    data address




Description
-----------

The ccw is the basic structure to build channel programs that perform
operations with the device or the control unit. Only Format-1 channel
command words are supported.




.. _xref_struct_erw:

struct erw
==========

.. c:type:: struct erw

    extended report word



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
  };



Members
-------

:``__u32:3 res0``:
    reserved

:``__u32:1 auth``:
    authorization check

:``__u32:1 pvrf``:
    path-verification-required flag

:``__u32:1 cpt``:
    channel-path timeout

:``__u32:1 fsavf``:
    failing storage address validity flag

:``__u32:1 cons``:
    concurrent sense

:``__u32:1 scavf``:
    secondary ccw address validity flag

:``__u32:1 fsaf``:
    failing storage address format

:``__u32:6 scnt``:
    sense count, if **cons** == ``1``

:``__u32:16 res16``:
    reserved





.. _xref_struct_erw_eadm:

struct erw_eadm
===============

.. c:type:: struct erw_eadm

    EADM Subchannel extended report word



Definition
----------

.. code-block:: c

  struct erw_eadm {
    __u32 b:1;
    __u32 r:1;
  };



Members
-------

:``__u32:1 b``:
    aob error

:``__u32:1 r``:
    arsb error





.. _xref_struct_sublog:

struct sublog
=============

.. c:type:: struct sublog

    subchannel logout area



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
  };



Members
-------

:``__u32:1 res0``:
    reserved

:``__u32:7 esf``:
    extended status flags

:``__u32:8 lpum``:
    last path used mask

:``__u32:1 arep``:
    ancillary report

:``__u32:5 fvf``:
    field-validity flags

:``__u32:2 sacc``:
    storage access code

:``__u32:2 termc``:
    termination code

:``__u32:1 devsc``:
    device-status check

:``__u32:1 serr``:
    secondary error

:``__u32:1 ioerr``:
    i/o-error alert

:``__u32:3 seqc``:
    sequence code





.. _xref_struct_esw0:

struct esw0
===========

.. c:type:: struct esw0

    Format 0 Extended Status Word (ESW)



Definition
----------

.. code-block:: c

  struct esw0 {
    struct sublog sublog;
    struct erw erw;
    __u32 faddr[2];
    __u32 saddr;
  };



Members
-------

:``struct sublog sublog``:
    subchannel logout

:``struct erw erw``:
    extended report word

:``__u32 faddr[2]``:
    failing storage address

:``__u32 saddr``:
    secondary ccw address





.. _xref_struct_esw1:

struct esw1
===========

.. c:type:: struct esw1

    Format 1 Extended Status Word (ESW)



Definition
----------

.. code-block:: c

  struct esw1 {
    __u8 zero0;
    __u8 lpum;
    __u16 zero16;
    struct erw erw;
    __u32 zeros[3];
  };



Members
-------

:``__u8 zero0``:
    reserved zeros

:``__u8 lpum``:
    last path used mask

:``__u16 zero16``:
    reserved zeros

:``struct erw erw``:
    extended report word

:``__u32 zeros[3]``:
    three fullwords of zeros





.. _xref_struct_esw2:

struct esw2
===========

.. c:type:: struct esw2

    Format 2 Extended Status Word (ESW)



Definition
----------

.. code-block:: c

  struct esw2 {
    __u8 zero0;
    __u8 lpum;
    __u16 dcti;
    struct erw erw;
    __u32 zeros[3];
  };



Members
-------

:``__u8 zero0``:
    reserved zeros

:``__u8 lpum``:
    last path used mask

:``__u16 dcti``:
    device-connect-time interval

:``struct erw erw``:
    extended report word

:``__u32 zeros[3]``:
    three fullwords of zeros





.. _xref_struct_esw3:

struct esw3
===========

.. c:type:: struct esw3

    Format 3 Extended Status Word (ESW)



Definition
----------

.. code-block:: c

  struct esw3 {
    __u8 zero0;
    __u8 lpum;
    __u16 res;
    struct erw erw;
    __u32 zeros[3];
  };



Members
-------

:``__u8 zero0``:
    reserved zeros

:``__u8 lpum``:
    last path used mask

:``__u16 res``:
    reserved

:``struct erw erw``:
    extended report word

:``__u32 zeros[3]``:
    three fullwords of zeros





.. _xref_struct_esw_eadm:

struct esw_eadm
===============

.. c:type:: struct esw_eadm

    EADM Subchannel Extended Status Word (ESW)



Definition
----------

.. code-block:: c

  struct esw_eadm {
    __u32 sublog;
    struct erw_eadm erw;
  };



Members
-------

:``__u32 sublog``:
    subchannel logout

:``struct erw_eadm erw``:
    extended report word





.. _xref_struct_irb:

struct irb
==========

.. c:type:: struct irb

    interruption response block



Definition
----------

.. code-block:: c

  struct irb {
    union scsw scsw;
    union esw;
    __u8 ecw[32];
  };



Members
-------

:``union scsw scsw``:
    subchannel status word

:``union esw``:
    extended status word

:``__u8 ecw[32]``:
    extended control word




Description
-----------

The irb that is handed to the device driver when an interrupt occurs. For
solicited interrupts, the common I/O layer already performs checks whether
a field is valid; a field not being valid is always passed as ``0``.
If a unit check occurred, **ecw** may contain sense data; this is retrieved
by the common I/O layer itself if the device doesn't support concurrent
sense (so that the device driver never needs to perform basic sene itself).
For unsolicited interrupts, the irb is passed as-is (expect for sense data,
if applicable).




.. _xref_struct_ciw:

struct ciw
==========

.. c:type:: struct ciw

    command information word (CIW) layout



Definition
----------

.. code-block:: c

  struct ciw {
    __u32 et:2;
    __u32 reserved:2;
    __u32 ct:4;
    __u32 cmd:8;
    __u32 count:16;
  };



Members
-------

:``__u32:2 et``:
    entry type

:``__u32:2 reserved``:
    reserved bits

:``__u32:4 ct``:
    command type

:``__u32:8 cmd``:
    command code

:``__u32:16 count``:
    command count





.. _xref_struct_ccw_dev_id:

struct ccw_dev_id
=================

.. c:type:: struct ccw_dev_id

    unique identifier for ccw devices



Definition
----------

.. code-block:: c

  struct ccw_dev_id {
    u8 ssid;
    u16 devno;
  };



Members
-------

:``u8 ssid``:
    subchannel set id

:``u16 devno``:
    device number




Description
-----------

This structure is not directly based on any hardware structure. The
hardware identifies a device by its device number and its subchannel,
which is in turn identified by its id. In order to get a unique identifier
for ccw devices across subchannel sets, **struct** ccw_dev_id has been
introduced.




.. _xref_ccw_dev_id_is_equal:

ccw_dev_id_is_equal
===================

.. c:function:: int ccw_dev_id_is_equal (struct ccw_dev_id * dev_id1, struct ccw_dev_id * dev_id2)

    compare two ccw_dev_ids

    :param struct ccw_dev_id * dev_id1:
        a ccw_dev_id

    :param struct ccw_dev_id * dev_id2:
        another ccw_dev_id



Returns
-------

 ``1`` if the two structures are equal field-by-field,
 ``0`` if not.



Context
-------

 any




.. _xref_pathmask_to_pos:

pathmask_to_pos
===============

.. c:function:: u8 pathmask_to_pos (u8 mask)

    find the position of the left-most bit in a pathmask

    :param u8 mask:
        pathmask with at least one bit set


