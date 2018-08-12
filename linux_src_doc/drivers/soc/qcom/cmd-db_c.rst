.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/cmd-db.c

.. _`entry_header`:

struct entry_header
===================

.. c:type:: struct entry_header

    header for each entry in cmddb

.. _`entry_header.definition`:

Definition
----------

.. code-block:: c

    struct entry_header {
        u8 id[8];
        __le32 priority[NUM_PRIORITY];
        __le32 addr;
        __le16 len;
        __le16 offset;
    }

.. _`entry_header.members`:

Members
-------

id
    resource's identifier

priority
    unused

addr
    the address of the resource

len
    length of the data

offset
    offset from :@data_offset, start of the data

.. _`rsc_hdr`:

struct rsc_hdr
==============

.. c:type:: struct rsc_hdr

    resource header information

.. _`rsc_hdr.definition`:

Definition
----------

.. code-block:: c

    struct rsc_hdr {
        __le16 slv_id;
        __le16 header_offset;
        __le16 data_offset;
        __le16 cnt;
        __le16 version;
        __le16 reserved[3];
    }

.. _`rsc_hdr.members`:

Members
-------

slv_id
    id for the resource

header_offset
    entry's header at offset from the end of the cmd_db_header

data_offset
    entry's data at offset from the end of the cmd_db_header

cnt
    number of entries for HW type

version
    MSB is major, LSB is minor

reserved
    reserved for future use.

.. _`cmd_db_header`:

struct cmd_db_header
====================

.. c:type:: struct cmd_db_header

    The DB header information

.. _`cmd_db_header.definition`:

Definition
----------

.. code-block:: c

    struct cmd_db_header {
        __le32 version;
        u8 magic[4];
        struct rsc_hdr header[MAX_SLV_ID];
        __le32 checksum;
        __le32 reserved;
        u8 data[];
    }

.. _`cmd_db_header.members`:

Members
-------

version
    The cmd db version

magic
    constant expected in the database

header
    array of resources

checksum
    checksum for the header. Unused.

reserved
    reserved memory

data
    driver specific data

.. _`description-of-the-command-db-database.`:

Description of the Command DB database.
=======================================

At the start of the command DB memory is the cmd_db_header structure.
The cmd_db_header holds the version, checksum, magic key as well as an
array for header for each slave (depicted by the rsc_header). Each h/w
based accelerator is a 'slave' (shared resource) and has slave id indicating
the type of accelerator. The rsc_header is the header for such individual
slaves of a given type. The entries for each of these slaves begin at the
rsc_hdr.header_offset. In addition each slave could have auxiliary data
that may be needed by the driver. The data for the slave starts at the
entry_header.offset to the location pointed to by the rsc_hdr.data_offset.

Drivers have a stringified key to a slave/resource. They can query the slave
information and get the slave id and the auxiliary data and the length of the
data. Using this information, they can format the request to be sent to the
h/w accelerator and request a resource state.

.. _`cmd_db_ready`:

cmd_db_ready
============

.. c:function:: int cmd_db_ready( void)

    Indicates if command DB is available

    :param  void:
        no arguments

.. _`cmd_db_ready.return`:

Return
------

0 on success, errno otherwise

.. _`cmd_db_read_addr`:

cmd_db_read_addr
================

.. c:function:: u32 cmd_db_read_addr(const char *id)

    Query command db for resource id address.

    :param const char \*id:
        resource id to query for address

.. _`cmd_db_read_addr.return`:

Return
------

resource address on success, 0 on error

This is used to retrieve resource address based on resource
id.

.. _`cmd_db_read_aux_data`:

cmd_db_read_aux_data
====================

.. c:function:: int cmd_db_read_aux_data(const char *id, u8 *data, size_t len)

    Query command db for aux data.

    :param const char \*id:
        Resource to retrieve AUX Data on.

    :param u8 \*data:
        Data buffer to copy returned aux data to. Returns size on NULL

    :param size_t len:
        Caller provides size of data buffer passed in.

.. _`cmd_db_read_aux_data.return`:

Return
------

size of data on success, errno otherwise

.. _`cmd_db_read_aux_data_len`:

cmd_db_read_aux_data_len
========================

.. c:function:: size_t cmd_db_read_aux_data_len(const char *id)

    Get the length of the auxiliary data stored in DB.

    :param const char \*id:
        Resource to retrieve AUX Data.

.. _`cmd_db_read_aux_data_len.return`:

Return
------

size on success, 0 on error

.. _`cmd_db_read_slave_id`:

cmd_db_read_slave_id
====================

.. c:function:: enum cmd_db_hw_type cmd_db_read_slave_id(const char *id)

    Get the slave ID for a given resource address

    :param const char \*id:
        Resource id to query the DB for version

.. _`cmd_db_read_slave_id.return`:

Return
------

cmd_db_hw_type enum on success, CMD_DB_HW_INVALID on error

.. This file was automatic generated / don't edit.

