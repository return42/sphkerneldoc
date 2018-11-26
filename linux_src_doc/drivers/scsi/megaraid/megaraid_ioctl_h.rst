.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_ioctl.h

.. _`con_log`:

con_log
=======

.. c:function::  con_log( level,  fmt)

    console log routine

    :param level:
        indicates the severity of the message.
    :type level: 

    :param fmt:
        format string
    :type fmt: 

.. _`con_log.description`:

Description
-----------

con_log displays the error messages on the console based on the current
debug level. Also it attaches the appropriate kernel severity level with
the message.

.. _`uioc_t`:

typedef uioc_t
==============

.. c:type:: typedef uioc_t

    the common ioctl packet structure

.. _`uioc_t.description`:

Description
-----------

Note         : All LSI drivers understand only this packet. Any other
: format sent by applications would be converted to this.

.. _`mraid_hba_info_t`:

typedef mraid_hba_info_t
========================

.. c:type:: typedef mraid_hba_info_t

    information about the controller

.. _`mraid_hba_info_t.description`:

Description
-----------

Extended information of 256 bytes about the controller. Align on the single
byte boundary so that 32-bit applications can be run on 64-bit platform
drivers withoug re-compilation.

.. _`mraid_hba_info_t.note`:

NOTE
----

reduce the number of reserved bytes whenever new field are added, so
that total size of the structure remains 256 bytes.

.. _`mcontroller_t`:

typedef mcontroller_t
=====================

.. c:type:: typedef mcontroller_t

    adapter info structure for old mimd_t apps

.. _`mm_dmapool_t`:

typedef mm_dmapool_t
====================

.. c:type:: typedef mm_dmapool_t

    Represents one dma pool with just one buffer

.. This file was automatic generated / don't edit.

