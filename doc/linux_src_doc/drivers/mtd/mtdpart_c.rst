.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/mtdpart.c

.. _`parse_mtd_partitions`:

parse_mtd_partitions
====================

.. c:function:: int parse_mtd_partitions(struct mtd_info *master, const char *const *types, struct mtd_partitions *pparts, struct mtd_part_parser_data *data)

    parse MTD partitions

    :param struct mtd_info \*master:
        the master partition (describes whole MTD device)

    :param const char \*const \*types:
        names of partition parsers to try or \ ``NULL``\ 

    :param struct mtd_partitions \*pparts:
        info about partitions found is returned here

    :param struct mtd_part_parser_data \*data:
        MTD partition parser-specific data

.. _`parse_mtd_partitions.description`:

Description
-----------

This function tries to find partition on MTD device \ ``master``\ . It uses MTD
partition parsers, specified in \ ``types``\ . However, if \ ``types``\  is \ ``NULL``\ , then
the default list of parsers is used. The default list contains only the
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
o zero otherwise, and \ ``pparts``\  will describe the partitions, number of
partitions, and the parser which parsed them. Caller must release
resources with \ :c:func:`mtd_part_parser_cleanup`\  when finished with the returned
data.

.. This file was automatic generated / don't edit.

