.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/capi/capiutil.c

.. _`capi_cmd2par`:

capi_cmd2par
============

.. c:function:: unsigned char *capi_cmd2par(u8 cmd, u8 subcmd)

    find parameter string for CAPI 2.0 command/subcommand

    :param cmd:
        command number
    :type cmd: u8

    :param subcmd:
        subcommand number
    :type subcmd: u8

.. _`capi_cmd2par.return-value`:

Return value
------------

static string, NULL if command/subcommand unknown

.. _`capi_cmsg2message`:

capi_cmsg2message
=================

.. c:function:: unsigned capi_cmsg2message(_cmsg *cmsg, u8 *msg)

    assemble CAPI 2.0 message from \_cmsg structure

    :param cmsg:
        \_cmsg structure
    :type cmsg: _cmsg \*

    :param msg:
        buffer for assembled message
    :type msg: u8 \*

.. _`capi_cmsg2message.return-value`:

Return value
------------

0 for success

.. _`capi_message2cmsg`:

capi_message2cmsg
=================

.. c:function:: unsigned capi_message2cmsg(_cmsg *cmsg, u8 *msg)

    disassemble CAPI 2.0 message into \_cmsg structure

    :param cmsg:
        \_cmsg structure
    :type cmsg: _cmsg \*

    :param msg:
        buffer for assembled message
    :type msg: u8 \*

.. _`capi_message2cmsg.return-value`:

Return value
------------

0 for success

.. _`capi_cmsg_header`:

capi_cmsg_header
================

.. c:function:: unsigned capi_cmsg_header(_cmsg *cmsg, u16 _ApplId, u8 _Command, u8 _Subcommand, u16 _Messagenumber, u32 _Controller)

    initialize header part of \_cmsg structure

    :param cmsg:
        \_cmsg structure
    :type cmsg: _cmsg \*

    :param _ApplId:
        ApplID field value
    :type _ApplId: u16

    :param _Command:
        Command field value
    :type _Command: u8

    :param _Subcommand:
        Subcommand field value
    :type _Subcommand: u8

    :param _Messagenumber:
        Message Number field value
    :type _Messagenumber: u16

    :param _Controller:
        Controller/PLCI/NCCI field value
    :type _Controller: u32

.. _`capi_cmsg_header.return-value`:

Return value
------------

0 for success

.. _`capi_cmd2str`:

capi_cmd2str
============

.. c:function:: char *capi_cmd2str(u8 cmd, u8 subcmd)

    convert CAPI 2.0 command/subcommand number to name

    :param cmd:
        command number
    :type cmd: u8

    :param subcmd:
        subcommand number
    :type subcmd: u8

.. _`capi_cmd2str.return-value`:

Return value
------------

static string

.. _`cdebbuf_free`:

cdebbuf_free
============

.. c:function:: void cdebbuf_free(_cdebbuf *cdb)

    free CAPI debug buffer

    :param cdb:
        buffer to free
    :type cdb: _cdebbuf \*

.. _`capi_message2str`:

capi_message2str
================

.. c:function:: _cdebbuf *capi_message2str(u8 *msg)

    format CAPI 2.0 message for printing

    :param msg:
        CAPI 2.0 message
    :type msg: u8 \*

.. _`capi_message2str.description`:

Description
-----------

Allocates a CAPI debug buffer and fills it with a printable representation
of the CAPI 2.0 message in \ ``msg``\ .

.. _`capi_message2str.return-value`:

Return value
------------

allocated debug buffer, NULL on error
The returned buffer should be freed by a call to \ :c:func:`cdebbuf_free`\  after use.

.. _`capi_cmsg2str`:

capi_cmsg2str
=============

.. c:function:: _cdebbuf *capi_cmsg2str(_cmsg *cmsg)

    format \_cmsg structure for printing

    :param cmsg:
        \_cmsg structure
    :type cmsg: _cmsg \*

.. _`capi_cmsg2str.description`:

Description
-----------

Allocates a CAPI debug buffer and fills it with a printable representation
of the CAPI 2.0 message stored in \ ``cmsg``\  by a previous call to
\ :c:func:`capi_cmsg2message`\  or \ :c:func:`capi_message2cmsg`\ .

.. _`capi_cmsg2str.return-value`:

Return value
------------

allocated debug buffer, NULL on error
The returned buffer should be freed by a call to \ :c:func:`cdebbuf_free`\  after use.

.. This file was automatic generated / don't edit.

