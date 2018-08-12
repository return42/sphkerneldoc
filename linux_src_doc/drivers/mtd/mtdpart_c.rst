.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/mtdpart.c

.. _`mtd_part`:

struct mtd_part
===============

.. c:type:: struct mtd_part

    our partition node structure

.. _`mtd_part.definition`:

Definition
----------

.. code-block:: c

    struct mtd_part {
        struct mtd_info mtd;
        struct mtd_info *parent;
        uint64_t offset;
        struct list_head list;
    }

.. _`mtd_part.members`:

Members
-------

mtd
    struct holding partition details

parent
    parent mtd - flash device or another partition

offset
    partition offset relative to the \*flash device\*

list
    *undescribed*

.. _`mtd_parse_part`:

mtd_parse_part
==============

.. c:function:: int mtd_parse_part(struct mtd_part *slave, const char *const *types)

    parse MTD partition looking for subpartitions

    :param struct mtd_part \*slave:
        part that is supposed to be a container and should be parsed

    :param const char \*const \*types:
        NULL-terminated array with names of partition parsers to try

.. _`mtd_parse_part.description`:

Description
-----------

Some partitions are kind of containers with extra subpartitions (volumes).
There can be various formats of such containers. This function tries to use
specified parsers to analyze given partition and registers found
subpartitions on success.

.. _`__mtd_del_partition`:

\__mtd_del_partition
====================

.. c:function:: int __mtd_del_partition(struct mtd_part *priv)

    delete MTD partition

    :param struct mtd_part \*priv:
        internal MTD struct for partition to be deleted

.. _`__mtd_del_partition.description`:

Description
-----------

This function must be called with the partitions mutex locked.

.. _`mtd_part_get_compatible_parser`:

mtd_part_get_compatible_parser
==============================

.. c:function:: struct mtd_part_parser *mtd_part_get_compatible_parser(const char *compat)

    find MTD parser by a compatible string

    :param const char \*compat:
        compatible string describing partitions in a device tree

.. _`mtd_part_get_compatible_parser.description`:

Description
-----------

MTD parsers can specify supported partitions by providing a table of
compatibility strings. This function finds a parser that advertises support
for a passed value of "compatible".

.. _`parse_mtd_partitions`:

parse_mtd_partitions
====================

.. c:function:: int parse_mtd_partitions(struct mtd_info *master, const char *const *types, struct mtd_part_parser_data *data)

    parse and register MTD partitions

    :param struct mtd_info \*master:
        the master partition (describes whole MTD device)

    :param const char \*const \*types:
        names of partition parsers to try or \ ``NULL``\ 

    :param struct mtd_part_parser_data \*data:
        MTD partition parser-specific data

.. _`parse_mtd_partitions.description`:

Description
-----------

This function tries to find & register partitions on MTD device \ ``master``\ . It
uses MTD partition parsers, specified in \ ``types``\ . However, if \ ``types``\  is \ ``NULL``\ ,
then the default list of parsers is used. The default list contains only the
"cmdlinepart" and "ofpart" parsers ATM.

.. _`parse_mtd_partitions.note`:

Note
----

If there are more then one parser in \ ``types``\ , the kernel only takes the
partitions parsed out by the first parser.

.. _`parse_mtd_partitions.this-function-may-return`:

This function may return
------------------------

o a negative error code in case of failure
o number of found partitions otherwise

.. This file was automatic generated / don't edit.

